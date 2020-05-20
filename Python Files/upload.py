# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'upload.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pyrebase
import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDir
global fileName

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


firebase=pyrebase.initialize_app(config)
storage=firebase.storage()



from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_upload(object):
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

    def details(self):
        from details import Ui_details
        self.Window = QtWidgets.QMainWindow()
        self.ui = Ui_details()
        self.ui.setupUi(self.Window)
        self.Window.show()

    def upload(self):
        from upload import Ui_upload
        self.Window = QtWidgets.QMainWindow()
        self.ui = Ui_upload()
        self.ui.setupUi(self.Window)
        self.Window.show()

    def uplaylist(self):
        from yourplaylist import Ui_userplaylist
        self.Window = QtWidgets.QMainWindow()
        self.ui = Ui_userplaylist()
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
        self.label_3.setGeometry(QtCore.QRect(0, 0, 801, 591))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(r"C:\Users\Anuradha\Desktop\College\DBMS Project\Project Files\pictures\background.jpeg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(0, 140, 151, 81))
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
        self.pushButton_5.setGeometry(QtCore.QRect(0, 370, 151, 111))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(11)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_5.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(r"C:\Users\Anuradha\Desktop\College\DBMS Project\Project Files\pictures\yourplaylist.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon1)
        self.pushButton_5.setIconSize(QtCore.QSize(200, 106))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, -1, 151, 581))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 260, 151, 121))
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
        self.pushButton_6.setGeometry(QtCore.QRect(0, 460, 151, 121))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(11)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_6.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(r"C:\Users\Anuradha\Desktop\College\DBMS Project\Project Files\pictures\createplaylist.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon3)
        self.pushButton_6.setIconSize(QtCore.QSize(220, 113))
        self.pushButton_6.setObjectName("pushButton_6")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(132, 0, 41, 581))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 151, 71))
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
        self.label.setGeometry(QtCore.QRect(0, 210, 151, 61))
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
        self.pushButton_2.setGeometry(QtCore.QRect(0, 70, 151, 71))
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
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(230, 190, 171, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(13)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(380, 340, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(18)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(490, 190, 191, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(13)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_3.raise_()
        self.label_5.raise_()
        self.pushButton_8.raise_()
        self.pushButton_3.raise_()
        self.line.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        self.pushButton_2.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_4.raise_()
        self.pushButton_7.raise_()
        self.pushButton_10.raise_()
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
        self.pushButton.clicked.connect(self.home)
        self.pushButton_2.clicked.connect(self.search)
        self.pushButton_8.clicked.connect(self.settings)
        self.pushButton_6.clicked.connect(self.cplaylist)
        self.pushButton_3.clicked.connect(self.upload)
        self.pushButton_10.clicked.connect(self.details)
        self.pushButton_7.clicked.connect(self.home)
        self.pushButton_5.clicked.connect(self.uplaylist)

        self.pushButton_4.clicked.connect(self.__init__)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_4.setText(_translate("MainWindow", "Choose File"))
        self.pushButton_7.setText(_translate("MainWindow", "Done"))
        self.pushButton_10.setText(_translate("MainWindow", "Add details"))

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 file dialogs - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.openFileNameDialog()
        # self.openFileNamesDialog()
        # self.saveFileDialog()
        # self.show()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        global fileName
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            fileName = fileName.replace('/', '\\')
            print(fileName)
            path_on_cloud = os.path.basename(fileName)
            storage.child(path_on_cloud).put(fileName)
            links = storage.child(path_on_cloud).get_url(None)
            print(links)


class MyMainWindow(QtWidgets.QMainWindow, Ui_upload):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MyMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
