import threading
import requests
import argparse

import sys
<<<<<<< HEAD
sys.path.append('C:\\dev\\dev\\q_app')
=======
sys.path.append('/home/krechetov/dev/q_app')
>>>>>>> 6975834373a499a0b8934f235ded6403aeba11e9

from flask import Flask, request, jsonify, abort
from utils import config_parser
from app.db.exceptions import UserNotFoundException
from app.db.interaction.interaction import DbInteraction

class Server:

<<<<<<< HEAD
    def __init__(self, host, port, rebuild_db=False):
=======
    def __init__(self, host, port, ebuild_db=False):
>>>>>>> 6975834373a499a0b8934f235ded6403aeba11e9
        self.host = host
        self.port = port

        self.app = Flask(__name__)
        self.app.add_url_rule("/shutdown", view_func=self.shutdown)
        self.app.add_url_rule("/", view_func=self.get_home)
        self.app.add_url_rule("/home", view_func=self.shutdown)

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


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, dest='config')

    args = parser.parse_args()

    config = config_parser(args.config)

    server_host = config['SERVER_HOST']
    server_port = config['SERVER_PORT']


    server = Server(
        host = server_host,
<<<<<<< HEAD
        port = server_port      
=======
        port = server_port     
>>>>>>> 6975834373a499a0b8934f235ded6403aeba11e9
    )

    server.run_server()