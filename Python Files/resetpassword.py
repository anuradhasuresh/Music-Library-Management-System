# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resetpassword.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import pyrebase
import os
import webbrowser
import vlc
from PyQt5 import QtCore, QtGui, QtWidgets
path=""
i=0

config = {
    "apiKey": "AIzaSyBpZrD02XUMgqAI4g9m4JE2FfLdYUMk7ZU",
    "authDomain": "fir-69239.firebaseapp.com",
    "databaseURL": "https://fir-69239.firebaseio.com",
    "projectId": "fir-69239",
    "storageBucket": "fir-69239.appspot.com",
    "messagingSenderId": "359676708097",
    "appId": "1:359676708097:web:37d080280938eb10208700",
    "measurementId": "G-2QGGF2SVVF"
  }

firebase=pyrebase.initialize_app(config)
auth = firebase.auth()
storage=firebase.storage()
db = firebase.database()

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_reset(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 513)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 80, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(280, 180, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 180, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 280, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(-10, -50, 811, 601))
        self.label_3.setStyleSheet("background-color: rgb(52, 105, 157);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_3.raise_()
        self.label.raise_()
        self.lineEdit.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(self.reset)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def reset(self):

        email = self.lineEdit.text()
        try:
            auth.send_password_reset_email(email)
        except Exception as e:
            self.showMessageBox('Warning', 'Invalid Email')
            global i
            i = 1
        if (i == 1):
            i += 1
        else:
            self.showMessageBox('Warning', 'Link for password reset has been sent to your email.')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "RESET PASSWORD"))
        self.label_2.setText(_translate("MainWindow", "EMAIL"))
        self.pushButton.setText(_translate("MainWindow", "RESET PASSWORD"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_reset()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
