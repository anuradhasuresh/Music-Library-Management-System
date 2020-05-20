# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import datetime
import json
i=0

from PyQt5 import QtCore, QtGui, QtWidgets
from signup3 import Ui_SigningUpWindow
from login2 import Ui_LoginWindow

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

    def OpenWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SigningUpWindow()
        self.ui.setupUi(self.window)
        #MainWindow.hide()
        self.window.show()

    def OpenWindow1(self):
        self.window1 = QtWidgets.QMainWindow()
        self.ui1 = Ui_LoginWindow()
        self.ui1.setupUi(self.window1)
        #MainWindow.hide()
        self.window1.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(796, 575)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 150, 541, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.signupbutton = QtWidgets.QPushButton(self.centralwidget)
        self.signupbutton.setGeometry(QtCore.QRect(170, 270, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.signupbutton.setFont(font)
        self.signupbutton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.signupbutton.setObjectName("signupbutton")
        self.loginbutton = QtWidgets.QPushButton(self.centralwidget)
        self.loginbutton.setGeometry(QtCore.QRect(490, 270, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.loginbutton.setFont(font)
        self.loginbutton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.loginbutton.setObjectName("loginbutton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 801, 541))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../background.jpeg"))
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.label.raise_()
        self.signupbutton.raise_()
        self.loginbutton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 796, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.loginbutton.clicked.connect(self.OpenWindow1)
        self.signupbutton.clicked.connect(self.OpenWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "WELCOME"))
        self.signupbutton.setText(_translate("MainWindow", "SIGN UP"))
        self.loginbutton.setText(_translate("MainWindow", "LOGIN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
