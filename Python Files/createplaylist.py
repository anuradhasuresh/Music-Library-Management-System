# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createplaylist.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


import vlc
from PyQt5 import QtCore, QtGui, QtWidgets
import pyrebase
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import datetime
import json

i = 0

signin_status = False
enter = 0

userEmail = ""
userPass = ""
msg = ""
x = ""

config = {
  "apiKey": "AIzaSyDNJvIvenCv0EKbzy_McKRii6Cnl4WRyDk",
  "authDomain": "music-library-project.firebaseapp.com",
  "databaseURL": "https://music-library-project.firebaseio.com",
  "projectId": "music-library-project",
  "storageBucket": "music-library-project.appspot.com",
  "messagingSenderId": "896225086586",
  "appId": "1:896225086586:web:5d36dadf4463f414ecbfc3",
  "measurementId": "G-J71DQLEFNH"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()
storage = firebase.storage()
links = ""
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_cplaylist(object):
    def home(self):
        from home import Ui_home
        self.Window = QtWidgets.QMainWindow()
        self.ui = Ui_home()
        self.ui.setupUi(self.Window)
        self.Window.show()

    def search(self):
        from searchbysong import Ui_search
        self.Window = QtWidgets.QMainWindow()
        self.ui = Ui_search()
        self.ui.setupUi(self.Window)
        self.Window.show()

    def settings(self):
        from settings import Ui_settings
        self.Window = QtWidgets.QMainWindow()
        self.ui = Ui_settings()
        self.ui.setupUi(self.Window)
        self.Window.show()

    def upload(self):
        from upload import MyMainWindow
        self.Window = QtWidgets.QMainWindow()
        self.ui = MyMainWindow()
        self.ui.setupUi(self.Window)
        self.Window.show()

    def cplaylist(self):
        from createplaylist import Ui_cplaylist
        from settings import Ui_settings
        self.Window = QtWidgets.QMainWindow()
        self.ui = Ui_cplaylist()
        self.ui.setupUi(self.Window)
        self.Window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, -19, 801, 611))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(r"C:\Users\Anuradha\Desktop\College\DBMS Project\Project Files\pictures\background.jpeg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(0, 141, 151, 81))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"C:\Users\Anuradha\Desktop\College\DBMS Project\Project Files\pictures\settings.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon)
        self.pushButton_8.setIconSize(QtCore.QSize(150, 78))
        self.pushButton_8.setAutoDefault(True)
        self.pushButton_8.setDefault(True)
        self.pushButton_8.setFlat(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 371, 151, 111))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(11)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_5.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(r"C:\Users\Anuradha\Desktop\College\DBMS Project\Project Files\pictures\yourplaylist.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon1)
        self.pushButton_5.setIconSize(QtCore.QSize(200, 106))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 151, 581))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 261, 151, 121))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(r"C:\Users\Anuradha\Desktop\College\DBMS Project\Project Files\pictures\upload.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(215, 106))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 461, 151, 121))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(11)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("")
        self.pushButton_6.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(r"C:\Users\Anuradha\Desktop\College\DBMS Project\Project Files\pictures\createplaylist.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon3)
        self.pushButton_6.setIconSize(QtCore.QSize(220, 113))
        self.pushButton_6.setObjectName("pushButton_6")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(132, 1, 41, 581))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 1, 151, 71))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(r"C:\Users\Anuradha\Desktop\College\DBMS Project\Project Files\pictures\home.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon4)
        self.pushButton.setIconSize(QtCore.QSize(150, 78))
        self.pushButton.setAutoDefault(True)
        self.pushButton.setDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 211, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(216, 216, 216);")
        self.label.setPixmap(QtGui.QPixmap(r"C:\Users\Anuradha\Desktop\College\DBMS Project\Project Files\pictures\library.jpeg"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 71, 151, 71))
        self.pushButton_2.setMouseTracking(False)
        self.pushButton_2.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.pushButton_2.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(r"C:\Users\Anuradha\Desktop\College\DBMS Project\Project Files\pictures\search.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon5)
        self.pushButton_2.setIconSize(QtCore.QSize(150, 78))
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setAutoDefault(True)
        self.pushButton_2.setDefault(True)
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 110, 261, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("alternate-background-color: rgb(85, 170, 255);")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(440, 130, 341, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(270, 210, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(11)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(550, 210, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(11)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(195, 320, 561, 192))
        self.listWidget.setObjectName("listWidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 40, 261, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("alternate-background-color: rgb(85, 170, 255);")
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(440, 60, 341, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(190, 260, 361, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("alternate-background-color: rgb(85, 170, 255);")
        self.label_6.setObjectName("label_6")
        self.label_3.raise_()
        self.label_5.raise_()
        self.pushButton_8.raise_()
        self.pushButton_5.raise_()
        self.pushButton_3.raise_()
        self.pushButton_6.raise_()
        self.line.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        self.pushButton_2.raise_()
        self.label_2.raise_()
        self.lineEdit.raise_()
        self.pushButton_7.raise_()
        self.pushButton_4.raise_()
        self.listWidget.raise_()
        self.label_4.raise_()
        self.lineEdit_2.raise_()
        self.label_6.raise_()
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

        self.pushButton_7.clicked.connect(self.udplaylist)
        self.pushButton.clicked.connect(self.home)
        self.pushButton_2.clicked.connect(self.search)
        self.pushButton_8.clicked.connect(self.settings)
        self.pushButton_6.clicked.connect(self.cplaylist)
        self.pushButton_3.clicked.connect(self.upload)
        self.pushButton_4.clicked.connect(self.home)

        # self.listWidget_2.itemDoubleClicked.connect(self.)

    def udplaylist(self):
        global i
        song = self.lineEdit.text()
        self.listWidget.addItem(song)
        # path_on_cloud=self.lineEdit.text()
        path_on_cloud1 = song + ".mp3"
        global links
        links = storage.child(path_on_cloud1).get_url(None)
        plname = self.lineEdit_2.text()
        print(links)
        data = {"Song Name": song,
                "url": links}
        db.child("PLAYLIST").child(plname).child(i).set(data)
        # users_by_name = db.child(plname).child(i).child("Song Name").get()
        i += 1
        # s1=users_by_name.val()
        # self.listWidget_2.addItem(s1)
        # albumn=db.child("user").get()
        # print(users_by_name.val())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Enter the song "))
        self.pushButton_7.setText(_translate("MainWindow", "Add more"))
        self.pushButton_4.setText(_translate("MainWindow", "Done"))
        self.label_4.setText(_translate("MainWindow", "Enter playlist name"))
        self.label_6.setText(_translate("MainWindow", "The songs added are : "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_cplaylist()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
