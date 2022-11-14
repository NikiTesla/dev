import threading
import requests
import argparse

import sys
sys.path.append('/home/krechetov/dev/q_app')

from flask import Flask, request, jsonify, abort
from utils import config_parser
from app.db.exceptions import UserNotFoundException
from app.db.interaction.interaction import DbInteraction

class Server:

    def __init__(self, host, port, db_host, db_port, user, password, db_name, rebuild_db=False):
        self.host = host
        self.port = port

        self.db_interaction = DbInteraction(
            host=db_host,
            port=db_port,
            user=user,
            password=password,
            db_name=db_name,
            rebuild_db=True
        )

        self.app = Flask(__name__)
        self.app.add_url_rule("/shutdown", view_func=self.shutdown)
        self.app.add_url_rule("/", view_func=self.get_home)
        self.app.add_url_rule("/home", view_func=self.shutdown)
        self.app.add_url_rule("/add_user_info", view_func=self.add_user_info, methods=['POST'])
        self.app.add_url_rule("/get_user_info/<username>", view_func=self.get_user_info)
        self.app.add_url_rule("/edit_user_info/<username>", view_func=self.edit_user_info, methods=['PUT'])

        self.app.register_error_handler(404, self.page_not_found)


    def page_not_found(self, err_description):
        return jsonify(error=str(err_description)), 404


    def run_server(self):
        self.server = threading.Thread(target=self.app.run, kwargs={'host' : self.host, 'port' : self.port})
        self.server.start()
        return self.server

    def shutdown_server(self):
        request.get(f'http://{self.host}:{self.port}/shutdown')

    def shutdown(self):
        terminate_func = request.environ.get('werkzeug.server.shutdown')
        if terminate_func:
            terminate_func()

    def get_home(self):
        return "Hello, api server"

    
    def add_user_info(self):
        request_body = dict(request.json)
        username = request_body['username']
        password = request_body['password']
        email = request_body['email']

        self.db_interaction.add_user_info(
            username=username,
            password=password,
            email=email
        )

        return f'Success added {username}', 201

    
    def get_user_info(self, username):
        try:
            user_info = self.db_interaction.get_user_info(username)
            return user_info
        except UserNotFoundException:
            abort(404, description='User not found')

    
    def edit_user_info(self, username):
        request_body = dict(request.json)
        new_username = request_body['username']
        new_password = request_body['password']
        new_email = request_body['email']

        self.db_interaction.edit_user_info(
            username=username,
            new_username=new_username,
            new_password=new_password,
            new_email=new_email
        )

        return 'Success', 200


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, dest='config')

    args = parser.parse_args()

    config = config_parser(args.config)

    server_host = config['SERVER_HOST']
    server_port = config['SERVER_PORT']

    db_host = config['DB_HOST']
    db_port = config['DB_PORT']
    db_user = config['DB_USER']
    db_password = config['DB_PASSWORD']
    db_name = config['DB_NAME']


    server = Server(
        host = server_host,
        port = server_port,
        db_host=db_host,
        db_port=db_port,
        user=db_user,
        password=db_password,
        db_name=db_name        
    )

    server.run_server()