from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Регистрация")
        MainWindow.resize(800, 200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        font = QtGui.QFont()

        self.button_login = QtWidgets.QPushButton(self.centralwidget)
        self.button_login.setGeometry(QtCore.QRect(50, 100, 300, 40))
        font.setFamily("OpenSymbol")
        font.setPointSize(14)
        self.button_login.setObjectName("log_in")

        self.button_signup = QtWidgets.QPushButton(self.centralwidget)
        self.button_signup.setGeometry(QtCore.QRect(450, 100, 300, 40))
        font.setFamily("OpenSymbol")
        font.setPointSize(14)
        self.button_signup.setFont(font)
        self.button_signup.setObjectName("sign_up")


        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(50, 50, 300, 40))
        self.lineEdit.setObjectName("login")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(450, 50, 300, 40))
        self.lineEdit.setObjectName("password")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Регистрация"))
        self.button_login.setText(_translate("MainWindow", "Войти"))
        self.button_signup.setText(_translate("MainWindow", "Зарегестрироваться"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())