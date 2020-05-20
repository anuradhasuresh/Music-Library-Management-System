# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login2.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pyrebase
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import datetime
import json
i=0


signin_status = False
enter = 0

userEmail=""
userPass=""
msg=""
x=""

import pyrebase
config = {
  "apiKey": "AIzaSyDNJvIvenCv0EKbzy_McKRii6Cnl4WRyDk",
  "authDomain": "music-library-project.firebaseapp.com",
  "databaseURL": "https://music-library-project.firebaseio.com",
  "projectId": "music-library-project",
  "storageBucket": "music-library-project.appspot.com",
  "messagingSenderId": "896225086586",
  "appId": "1:896225086586:web:5d36dadf4463f414ecbfc3",
  "measurementId": "G-J71DQLEFNH"
};
firebase=pyrebase.initialize_app(config)
storage=firebase.storage()
auth = firebase.auth()
db = firebase.database()

class Ui_MainWindow(object):
    def __init__(self, parent = None):
        super(Ui_MainWindow, self).__init__()

class Ui_LoginWindow(object):
    def home(self):
        from home import Ui_home
        self.window = QtWidgets.QMainWindow()
        self.ui=Ui_home()
        self.ui.setupUi(self.window)
        self.window.show()
        #MainWindow.hide()
        self.window.show()

    def welcome(self):
        from welcome import Ui_MainWindow
        self.Window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.Window)
        self.Window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 540)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.login = QtWidgets.QLabel(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(320, 90, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.login.setFont(font)
        self.login.setObjectName("login")
        self.email = QtWidgets.QLabel(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(160, 200, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.email.setFont(font)
        self.email.setObjectName("email")
        self.enteremail = QtWidgets.QLineEdit(self.centralwidget)
        self.enteremail.setGeometry(QtCore.QRect(320, 190, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.enteremail.setFont(font)
        self.enteremail.setObjectName("enteremail")
        self.password = QtWidgets.QLabel(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(160, 260, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.password.setFont(font)
        self.password.setObjectName("password")
        self.entrpassword = QtWidgets.QLineEdit(self.centralwidget)
        self.entrpassword.setGeometry(QtCore.QRect(320, 250, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.entrpassword.setFont(font)
        self.entrpassword.setObjectName("entrpassword")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.entrpassword.setEchoMode(QtWidgets.QLineEdit.Password)  # password
        self.pushButton.setGeometry(QtCore.QRect(480, 340, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 340, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 811, 601))
        self.label_3.setStyleSheet("background-color: rgb(52, 105, 157);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_3.raise_()
        self.login.raise_()
        self.email.raise_()
        self.enteremail.raise_()
        self.password.raise_()
        self.entrpassword.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_2.clicked.connect(self.welcome)
        self.pushButton.clicked.connect(self.signin)

    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def signin(self):

        userEmail = self.enteremail.text()
        userPass = self.entrpassword.text()
        try:
            user = auth.sign_in_with_email_and_password(userEmail, userPass)
        except Exception as e:
            self.showMessageBox('Warning', 'Invalid Email and Password')
            global i
            i = 1
        if (i == 1):
            i += 1
        else:
            self.home()
            # auth.signout()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.login.setText(_translate("MainWindow", "LOGIN"))
        self.email.setText(_translate("MainWindow", "EMAIL"))
        self.password.setText(_translate("MainWindow", "PASSWORD"))
        self.pushButton.setText(_translate("MainWindow", "LOGIN"))
        self.pushButton_2.setText(_translate("MainWindow", "BACK"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
