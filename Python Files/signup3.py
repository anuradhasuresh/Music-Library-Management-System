# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup3.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import datetime
import json
i=0

userEmail=""
userPass=""

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

class Ui_SigningUpWindow(object):

    def loginwindow(self):
        from login2 import Ui_LoginWindow
        self.window = QtWidgets.QMainWindow()
        self.ui=Ui_LoginWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        #MainWindow.hide()
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 70, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 160, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 240, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(370, 150, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(370, 230, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 390, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 390, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(-10, 0, 811, 601))
        self.label_4.setStyleSheet("background-color: rgb(52, 105, 157);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(370, 310, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(100, 320, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_4.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.lineEdit_3.raise_()
        self.label_5.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.create)
        self.pushButton_2.clicked.connect(self.loginwindow)

    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def create(self):
        new_userEmail = self.lineEdit.text()
        new_userPass = self.lineEdit_2.text()
        p2 = self.lineEdit_3.text()
        if (new_userPass == p2):
            try:
                auth.create_user_with_email_and_password(new_userEmail, new_userPass)
            except Exception as e:
                self.showMessageBox('Warning', 'Email Already Exists. Please try again.')
                global i
                i = 1
            if (i == 1):
                i += 1
            else:
                self.showMessageBox('Successful', 'Successfully Signed Up! ')
        else:
            self.showMessageBox('Warning', 'Passwords do not match. Please try again. ')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "SIGN UP"))
        self.label_2.setText(_translate("MainWindow", "EMAIL"))
        self.label_3.setText(_translate("MainWindow", "PASSWORD"))
        self.pushButton.setText(_translate("MainWindow", "SIGN UP"))
        self.pushButton_2.setText(_translate("MainWindow", "LOGIN"))
        self.label_5.setText(_translate("MainWindow", "RE-ENTER PASSWORD"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_SigningUpWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
