import sqlite3
import sys
import getpass


class AuthException(Exception):
    pass


class NotExist(AuthException):
    pass


class AlreadyExist(AuthException):
    pass

class AgeIsIncorrect(AuthException):
    pass


class User:
    
    def __init__(self, name, age, country, field, password):
        print('Hello, ', name)
        self.name = name
        self.age = age
        self.country = country
        self.field = field
        self._password = password

    def __str__(self):
        return f"\nName\t: {self.name}\nAge\t: {self.age}\nCountry\t: {self.country}\nField\t: {self.field}\n"

    @staticmethod
    def sign_up():
        db = sqlite3.connect("people.db")
        cur = db.cursor()
        try:
            name = input("Enter name: ")
            names = cur.executemany("SELECT name FROM info WHERE name=?", name).fetchall()
            if names: print("Name already exists"); raise AlreadyExist()

            age = int(input("Enter age: "))
            if age < 0 or age > 150: raise AgeIsIncorrect()
            
            country = input("Enter country: ")
            field = input("Enter field: ")
            password = getpass.getpass()

        except sqlite3.OperationalError:
            print("Problems occured!")
            print(sys.exc_info)
        except AuthException:
            print(sys.exc_info())
            print('Enter correct information')
            User.sign_up()
        else:
            print("Authorization - ok! Welcome!")
            cur.executemany("INSERT INTO info VALUES(?, ?, ?, ?, ?)",
                                    [(name, age, country, field, password)])
            db.commit()

    @staticmethod
    def log_in():
        db = sqlite3.connect("people.db")
        cur = db.cursor()
        print("Hello, let's log in")

        try:
            name = input("Enter name: ")
            names = cur.execute(f"SELECT name FROM info WHERE name='{name}'").fetchall()
            if not names: print("Name doesn't exist"); raise NotExist()
        except AuthException:
            print(sys.exc_info())
        else:
            info = cur.execute(f"SELECT * FROM info WHERE name='{name}'").fetchone()
            if getpass.getpass('Password: ') == info[-1]: return User(*info)
            print("Not logged in")

        return 0


if __name__ == "__main__":
    print('testing authorization . . .\n')

    db = sqlite3.connect('people.db')
    cur = db.cursor()

    cur.execute(f"CREATE TABLE info(name, INT age, country, field, password)")

    db.commit()