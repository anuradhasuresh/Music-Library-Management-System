# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'romantic.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
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

class Ui_romantic(object):
    def play(self,Happier, Gorgeous, Know, Sorry, Needy, Shape, Perfect):
        global player

        if Happier:
            import vlc
            path_on_cloud = "Happier" + ".mp3"
            links = storage.child(path_on_cloud).get_url(None)
            player = vlc.MediaPlayer(links)
            player.play()

        elif Gorgeous:
            import vlc
            path_on_cloud = "Gorgeous" + ".mp3"
            links = storage.child(path_on_cloud).get_url(None)
            player = vlc.MediaPlayer(links)
            player.play()

        elif Know:
            import vlc
            path_on_cloud = "What Do I Know" + ".mp3"
            links = storage.child(path_on_cloud).get_url(None)
            player = vlc.MediaPlayer(links)
            player.play()

        elif Sorry:
            import vlc
            path_on_cloud = "Sorry" + ".mp3"
            links = storage.child(path_on_cloud).get_url(None)
            player = vlc.MediaPlayer(links)
            player.play()

        elif Needy:
            import vlc
            path_on_cloud = "Needy"+ ".mp3"
            links = storage.child(path_on_cloud).get_url(None)
            player = vlc.MediaPlayer(links)
            player.play()

        elif Shape:
            import vlc
            path_on_cloud = "Shape Of You"+ ".mp3"
            links = storage.child(path_on_cloud).get_url(None)
            player = vlc.MediaPlayer(links)
            player.play()

        elif Perfect:
            import vlc
            path_on_cloud = "Perfect" + ".mp3"
            links = storage.child(path_on_cloud).get_url(None)
            player = vlc.MediaPlayer(links)
            player.play()


    def pause(self):
        player.pause()

    def stop(self):
        player.stop()


    def home(self):
        from home import Ui_home
        self.Window = QtWidgets.QMainWindow()
        self.ui = Ui_home()
        self.ui.setupUi(self.Window)
        self.Window.show()

    def romantic(self):
        from romantic import Ui_romantic
        self.Window = QtWidgets.QMainWindow()
        self.ui = Ui_romantic()
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 211, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(216, 216, 216);")
        self.label.setPixmap(QtGui.QPixmap("../../library.jpeg"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, -9, 801, 601))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../../background.jpeg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 151, 581))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 371, 151, 111))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(11)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_5.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../yourplaylist"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QtCore.QSize(200, 106))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 71, 151, 71))
        self.pushButton_2.setMouseTracking(False)
        self.pushButton_2.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../search.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(150, 78))
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setAutoDefault(True)
        self.pushButton_2.setDefault(True)
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(132, 1, 41, 591))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 461, 151, 131))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(11)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_6.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../createplaylist.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon2)
        self.pushButton_6.setIconSize(QtCore.QSize(220, 113))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(0, 141, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../settings.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon3)
        self.pushButton_8.setIconSize(QtCore.QSize(150, 78))
        self.pushButton_8.setAutoDefault(True)
        self.pushButton_8.setDefault(True)
        self.pushButton_8.setFlat(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 1, 151, 71))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../../home.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon4)
        self.pushButton.setIconSize(QtCore.QSize(150, 78))
        self.pushButton.setAutoDefault(True)
        self.pushButton.setDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 261, 151, 121))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_3.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../../upload.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon5)
        self.pushButton_3.setIconSize(QtCore.QSize(215, 106))
        self.pushButton_3.setObjectName("pushButton_3")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(230, 220, 361, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_10 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_10.setGeometry(QtCore.QRect(230, 190, 361, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.radioButton_10.setFont(font)
        self.radioButton_10.setObjectName("radioButton_10")
        self.radioButton_6 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_6.setGeometry(QtCore.QRect(228, 250, 361, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.radioButton_6.setFont(font)
        self.radioButton_6.setObjectName("radioButton_6")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(400, 20, 101, 91))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(16)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_14.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../../rom.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_14.setIcon(icon6)
        self.pushButton_14.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(380, 510, 61, 51))
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_4.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../../play.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon7)
        self.pushButton_4.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_4.setObjectName("pushButton_4")
        self.radioButton_7 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_7.setGeometry(QtCore.QRect(228, 280, 361, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.radioButton_7.setFont(font)
        self.radioButton_7.setObjectName("radioButton_7")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(570, 510, 61, 51))
        self.pushButton_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_9.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../../stop.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon8)
        self.pushButton_9.setIconSize(QtCore.QSize(50, 60))
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 120, 591, 371))
        self.label_2.setStyleSheet("background-color: rgb(43, 86, 129);\n"
"background-color: rgb(255, 255, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(470, 510, 61, 51))
        self.pushButton_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_7.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../../pause.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon9)
        self.pushButton_7.setIconSize(QtCore.QSize(50, 60))
        self.pushButton_7.setObjectName("pushButton_7")
        self.radioButton_11 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_11.setGeometry(QtCore.QRect(230, 160, 361, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.radioButton_11.setFont(font)
        self.radioButton_11.setObjectName("radioButton_11")
        self.radioButton_8 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_8.setGeometry(QtCore.QRect(230, 310, 361, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.radioButton_8.setFont(font)
        self.radioButton_8.setObjectName("radioButton_8")
        self.radioButton_12 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_12.setGeometry(QtCore.QRect(230, 130, 361, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.radioButton_12.setFont(font)
        self.radioButton_12.setObjectName("radioButton_12")
        self.label_3.raise_()
        self.label_5.raise_()
        self.label_2.raise_()
        self.pushButton_5.raise_()
        self.pushButton_2.raise_()
        self.line.raise_()
        self.pushButton_6.raise_()
        self.pushButton_8.raise_()
        self.pushButton.raise_()
        self.pushButton_3.raise_()
        self.radioButton.raise_()
        self.radioButton_10.raise_()
        self.radioButton_6.raise_()
        self.pushButton_14.raise_()
        self.pushButton_4.raise_()
        self.radioButton_7.raise_()
        self.pushButton_9.raise_()
        self.pushButton_7.raise_()
        self.radioButton_11.raise_()
        self.radioButton_8.raise_()
        self.radioButton_12.raise_()
        self.label.raise_()
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

        self.pushButton_4.clicked.connect(lambda: self.play(self.radioButton.isChecked(),
                                                            self.radioButton_6.isChecked(),
                                                            self.radioButton_7.isChecked(),
                                                            self.radioButton_8.isChecked(),
                                                            self.radioButton_10.isChecked(),
                                                            self.radioButton_11.isChecked(),
                                                            self.radioButton_12.isChecked()))

        self.pushButton_7.clicked.connect(self.pause)
        self.pushButton_9.clicked.connect(self.stop)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton.setText(_translate("MainWindow", "  Happier"))
        self.radioButton_6.setText(_translate("MainWindow", "  Gorgeous"))
        self.radioButton_7.setText(_translate("MainWindow", "  What Do I Know"))
        self.radioButton_8.setText(_translate("MainWindow", "  Sorry"))
        self.radioButton_10.setText(_translate("MainWindow", "  Needy"))
        self.radioButton_11.setText(_translate("MainWindow", "  Shape Of You"))
        self.radioButton_12.setText(_translate("MainWindow", "  Perfect"))
        self.pushButton.clicked.connect(self.home)
        self.pushButton_2.clicked.connect(self.search)
        self.pushButton_8.clicked.connect(self.settings)
        self.pushButton_6.clicked.connect(self.cplaylist)
        self.pushButton_3.clicked.connect(self.upload)
        self.pushButton_5.clicked.connect(self.uplaylist)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_romantic()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
