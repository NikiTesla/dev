import sys
sys.path.append('/home/krechetov/dev/app')
print(sys.path)


from db.models.models import Base, User
from db.client.client import MySQLConnection
from db.exception import UserNotFoundException


class DbInteraction():
    def __init__(self, host, port, user, password, db_name, rebuild_db=False):
        self.mysql_connection = MySQLConnection(
            host=host,
            port=port,
            user=user,
            password=password,
            db_name=db_name,
            rebuild_db=rebuild_db
        )

        self.engine = self.mysql_connection.connection.engine

        if rebuild_db:
            self.create_table_users()
            self.create_table_musical_compositions()


    def create_table_users(self):
        if not self.engine.dialect.has_table(self.engine, 'users'):
            Base.metadata.tables['users'].create(self.engine)
        else:
            self.mysql_connection.execute_query("DROP TABLE IF EXISTS users")
            Base.metadata.tables['users'].create(self.engine)


    def create_table_musical_compositions(self):
        if not self.engine.dialect.has_table(self.engine, 'musical_compositions'):
            Base.metadata.tables['musical_compositions'].create(self.engine)
        else:
            self.mysql_connection.execute_query("DROP TABLE IF EXISTS musical_compositions")
            Base.metadata.tables['musical_compositions'].create(self.engine)


    def add_user_info(self, username, email, password):
        user = User(
            username=username,
            password=password,
            email=email
        )

        self.mysql_connection.session.add(user)
        return self.get_user_info(username)
    

    def get_user_info(self, username):
        user = self.mysql_connection.session.query(User).filter_by(username=username).first()
        if user:
            self.mysql_connection.session.expire_all()
            return {'username': user.username, 'email': user.email, 'password': user.password}
        else:
            raise UserNotFoundException('User not found')

    
    def edit_user_info(self, username, new_username=None, new_email=None, new_password=None):
        user = self.mysql_connection.session.query(User).filter_by(username=username).first()
        if user:
            if new_username is not None:
                user.username = new_username
            if new_email is not None:
                user.email = new_email
            if new_password is not None:
                user.password = new_password
            return self.get_user_info(username if new_username is None else new_username)
        else:
            raise UserNotFoundException("User not found")



if __name__ == "__main__":
    db = DbInteraction(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='pass',
        db_name='some_db',
        rebuild_db=True
    )
    
    db.add_user_info('test', 'test', 'test')