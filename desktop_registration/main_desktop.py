import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import authorization as auth
from ui import Ui_MainWindow

class Registration(QMainWindow):
    def __init__(self):
        super(Registration, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.login = auth.User.log_in
        self.signup = auth.User.sign_up

        self.init_UI()

    def init_UI(self):
        self.ui.button_login.clicked.connect(self.login)
        self.ui.button_signup.clicked.connect(self.signup)

        self.update()

app = QApplication([])
application = Registration()
application.show()
sys.exit(app.exec())