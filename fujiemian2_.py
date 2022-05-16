# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test6.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow2):
        MainWindow2.setObjectName("MainWindow2")
        MainWindow2.resize(1000, 700)
        MainWindow2.setMinimumSize(QtCore.QSize(1000, 700))
        MainWindow2.setMaximumSize(QtCore.QSize(1000, 700))
        MainWindow2.setStyleSheet("background-color:rgb(103, 116, 166);")
        self.centralwidget = QtWidgets.QWidget(MainWindow2)
        self.centralwidget.setObjectName("centralwidget")
        self.label_bottom = QtWidgets.QLabel(self.centralwidget)
        self.label_bottom.setGeometry(QtCore.QRect(10, 270, 981, 401))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(18)
        self.label_bottom.setFont(font)
        self.label_bottom.setStyleSheet("background-color:transparent;\n"
"border:1px solid rgb(255, 255, 255);\n"
"border-top-left-radius:5px;\n"
"border-top-right-radius:5px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius:5px;\n"
"color:rgb(255, 255, 255);\n"
"")
        self.label_bottom.setText("")
        self.label_bottom.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_bottom.setObjectName("label_bottom")
        self.label_photo = QtWidgets.QLabel(self.centralwidget)
        self.label_photo.setGeometry(QtCore.QRect(20, 290, 161, 201))
        font = QtGui.QFont()
        font.setFamily("Hobo Std")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_photo.setFont(font)
        self.label_photo.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.label_photo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_photo.setObjectName("label_photo")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(200, 330, 81, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_name.setFont(font)
        self.label_name.setStyleSheet("background-color: rgb(96, 100, 110);\n"
"color: rgb(233, 193, 76);")
        self.label_name.setObjectName("label_name")
        self.label_left = QtWidgets.QLabel(self.centralwidget)
        self.label_left.setGeometry(QtCore.QRect(10, 0, 461, 51))
        self.label_left.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(16)
        self.label_left.setFont(font)
        self.label_left.setStyleSheet("background-color:transparent; \n"
"color:rgb(255, 255, 255);\n"
"border:none;\n"
"border-bottom:1px solid rgb(255, 255, 255);")
        self.label_left.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_left.setObjectName("label_left")
        self.label_number_ = QtWidgets.QLabel(self.centralwidget)
        self.label_number_.setGeometry(QtCore.QRect(300, 410, 191, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_number_.setFont(font)
        self.label_number_.setStyleSheet("background-color: rgb(96, 100, 110);\n"
"color: rgb(233, 193, 76);")
        self.label_number_.setAlignment(QtCore.Qt.AlignCenter)
        self.label_number_.setObjectName("label_number_")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(510, 280, 471, 211))
        self.scrollArea.setStyleSheet("background-color:rgb(103, 116, 166);")
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 456, 600))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 600))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label_tishi = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_tishi.setGeometry(QtCore.QRect(0, 10, 441, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_tishi.setFont(font)
        self.label_tishi.setStyleSheet("background-color:transparent; \n"
"color:rgb(255, 255, 255);\n"
"border:none;\n"
"border-bottom:1px solid rgb(255, 255, 255);")
        self.label_tishi.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tishi.setObjectName("label_tishi")
        self.label_time_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_time_1.setGeometry(QtCore.QRect(0, 60, 441, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_time_1.setFont(font)
        self.label_time_1.setStyleSheet("background-color: rgb(96, 100, 110);\n"
"color: rgb(233, 193, 76);")
        self.label_time_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time_1.setObjectName("label_time_1")
        self.label_time_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_time_2.setGeometry(QtCore.QRect(0, 110, 441, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_time_2.setFont(font)
        self.label_time_2.setStyleSheet("background-color: rgb(96, 100, 110);\n"
"color: rgb(233, 193, 76);")
        self.label_time_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time_2.setObjectName("label_time_2")
        self.label_time_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_time_3.setGeometry(QtCore.QRect(0, 160, 441, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_time_3.setFont(font)
        self.label_time_3.setStyleSheet("background-color: rgb(96, 100, 110);\n"
"color: rgb(233, 193, 76);")
        self.label_time_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time_3.setObjectName("label_time_3")
        self.label_time_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_time_4.setGeometry(QtCore.QRect(0, 210, 441, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_time_4.setFont(font)
        self.label_time_4.setStyleSheet("background-color: rgb(96, 100, 110);\n"
"color: rgb(233, 193, 76);")
        self.label_time_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time_4.setObjectName("label_time_4")
        self.label_time_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_time_5.setGeometry(QtCore.QRect(0, 260, 441, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_time_5.setFont(font)
        self.label_time_5.setStyleSheet("background-color: rgb(96, 100, 110);\n"
"color: rgb(233, 193, 76);")
        self.label_time_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time_5.setObjectName("label_time_5")
        self.label_time_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_time_6.setGeometry(QtCore.QRect(0, 310, 441, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_time_6.setFont(font)
        self.label_time_6.setStyleSheet("background-color: rgb(96, 100, 110);\n"
"color: rgb(233, 193, 76);")
        self.label_time_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time_6.setObjectName("label_time_6")
        self.label_time_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_time_7.setGeometry(QtCore.QRect(0, 360, 441, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_time_7.setFont(font)
        self.label_time_7.setStyleSheet("background-color: rgb(96, 100, 110);\n"
"color: rgb(233, 193, 76);")
        self.label_time_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time_7.setObjectName("label_time_7")
        self.label_time_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_time_8.setGeometry(QtCore.QRect(0, 410, 441, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_time_8.setFont(font)
        self.label_time_8.setStyleSheet("background-color: rgb(96, 100, 110);\n"
"color: rgb(233, 193, 76);")
        self.label_time_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time_8.setObjectName("label_time_8")
        self.label_time_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_time_9.setGeometry(QtCore.QRect(0, 460, 441, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_time_9.setFont(font)
        self.label_time_9.setStyleSheet("background-color: rgb(96, 100, 110);\n"
"color: rgb(233, 193, 76);")
        self.label_time_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time_9.setObjectName("label_time_9")
        self.label_time_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_time_10.setGeometry(QtCore.QRect(0, 510, 441, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_time_10.setFont(font)
        self.label_time_10.setStyleSheet("background-color: rgb(96, 100, 110);\n"
"color: rgb(233, 193, 76);")
        self.label_time_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time_10.setObjectName("label_time_10")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_right = QtWidgets.QLabel(self.centralwidget)
        self.label_right.setGeometry(QtCore.QRect(520, 0, 461, 51))
        self.label_right.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(16)
        self.label_right.setFont(font)
        self.label_right.setStyleSheet("background-color:transparent; \n"
"color:rgb(255, 255, 255);\n"
"border:none;\n"
"border-bottom:1px solid rgb(255, 255, 255);")
        self.label_right.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_right.setObjectName("label_right")
        self.pushButton_daochu = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_daochu.setGeometry(QtCore.QRect(510, 500, 441, 71))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_daochu.setFont(font)
        self.pushButton_daochu.setStyleSheet("QPushButton{\n"
"border:1px solid rgb(255, 255, 255);\n"
"border-top-left-radius:5px;\n"
"border-top-right-radius:5px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius:5px;\n"
"font: 14pt \"楷体\";\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(103, 116, 166);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(123, 140, 199);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(83, 95, 135);\n"
"}\n"
"")
        self.pushButton_daochu.setObjectName("pushButton_daochu")
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(80, 70, 331, 61))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setStyleSheet("border:1px solid rgb(255, 255, 255);\n"
"font: 12pt \"楷体\";\n"
"border-top-left-radius:6px;\n"
"border-top-right-radius:6px;\n"
"border-bottom-left-radius:6px;\n"
"border-bottom-right-radius:6px;\n"
"background-color:rgb(255, 255, 255);")
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.pushButton_fanhui = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_fanhui.setGeometry(QtCore.QRect(510, 580, 441, 71))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_fanhui.setFont(font)
        self.pushButton_fanhui.setStyleSheet("QPushButton{\n"
"border:1px solid rgb(255, 255, 255);\n"
"border-top-left-radius:5px;\n"
"border-top-right-radius:5px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius:5px;\n"
"font: 14pt \"楷体\";\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(103, 116, 166);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(123, 140, 199);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(83, 95, 135);\n"
"}\n"
"")
        self.pushButton_fanhui.setObjectName("pushButton_fanhui")
        self.pushButton_chaxun_gonghao = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_chaxun_gonghao.setGeometry(QtCore.QRect(580, 150, 331, 61))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_chaxun_gonghao.setFont(font)
        self.pushButton_chaxun_gonghao.setStyleSheet("QPushButton{\n"
"border:1px solid rgb(255, 255, 255);\n"
"border-top-left-radius:5px;\n"
"border-top-right-radius:5px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius:5px;\n"
"font: 14pt \"楷体\";\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(103, 116, 166);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(123, 140, 199);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(83, 95, 135);\n"
"}\n"
"")
        self.pushButton_chaxun_gonghao.setObjectName("pushButton_chaxun_gonghao")
        self.lineEdit_gonghao = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_gonghao.setGeometry(QtCore.QRect(580, 70, 331, 61))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_gonghao.setFont(font)
        self.lineEdit_gonghao.setStyleSheet("border:1px solid rgb(255, 255, 255);\n"
"font: 12pt \"楷体\";\n"
"border-top-left-radius:6px;\n"
"border-top-right-radius:6px;\n"
"border-bottom-left-radius:6px;\n"
"border-bottom-right-radius:6px;\n"
"background-color:rgb(255, 255, 255);")
        self.lineEdit_gonghao.setObjectName("lineEdit_gonghao")
        self.pushButton_chaxun_name = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_chaxun_name.setGeometry(QtCore.QRect(80, 150, 331, 61))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_chaxun_name.setFont(font)
        self.pushButton_chaxun_name.setStyleSheet("QPushButton{\n"
"border:1px solid rgb(255, 255, 255);\n"
"border-top-left-radius:5px;\n"
"border-top-right-radius:5px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius:5px;\n"
"font: 14pt \"楷体\";\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(103, 116, 166);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(123, 140, 199);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(83, 95, 135);\n"
"}\n"
"")
        self.pushButton_chaxun_name.setObjectName("pushButton_chaxun_name")
        self.label_name_ = QtWidgets.QLabel(self.centralwidget)
        self.label_name_.setGeometry(QtCore.QRect(300, 330, 191, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_name_.setFont(font)
        self.label_name_.setStyleSheet("background-color: rgb(96, 100, 110);\n"
"color: rgb(233, 193, 76);")
        self.label_name_.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name_.setObjectName("label_name_")
        self.label_number = QtWidgets.QLabel(self.centralwidget)
        self.label_number.setGeometry(QtCore.QRect(200, 410, 81, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_number.setFont(font)
        self.label_number.setStyleSheet("background-color: rgb(96, 100, 110);\n"
"color: rgb(233, 193, 76);")
        self.label_number.setObjectName("label_number")
        self.label_weigui = QtWidgets.QLabel(self.centralwidget)
        self.label_weigui.setGeometry(QtCore.QRect(20, 530, 161, 71))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_weigui.setFont(font)
        self.label_weigui.setStyleSheet("background-color: rgb(96, 100, 110);\n"
"color: rgb(233, 193, 76);")
        self.label_weigui.setObjectName("label_weigui")
        self.label_weigui_ = QtWidgets.QLabel(self.centralwidget)
        self.label_weigui_.setGeometry(QtCore.QRect(230, 530, 221, 71))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_weigui_.setFont(font)
        self.label_weigui_.setStyleSheet("background-color: rgb(96, 100, 110);\n"
"color: rgb(233, 193, 76);")
        self.label_weigui_.setAlignment(QtCore.Qt.AlignCenter)
        self.label_weigui_.setObjectName("label_weigui_")
        MainWindow2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 18))
        self.menubar.setObjectName("menubar")
        MainWindow2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow2)
        self.statusbar.setObjectName("statusbar")
        MainWindow2.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)

    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow2", "MainWindow"))
        self.label_photo.setText(_translate("MainWindow2", "photo"))
        self.label_name.setText(_translate("MainWindow2", "姓名："))
        self.label_left.setText(_translate("MainWindow2", "按姓名查询详细违规记录"))
        self.label_number_.setText(_translate("MainWindow2", "XXX"))
        self.label_tishi.setText(_translate("MainWindow2", "查询到xx次，显示xx次，详情请导出"))
        self.label_time_1.setText(_translate("MainWindow2", "几月几日违规"))
        self.label_time_2.setText(_translate("MainWindow2", "几月几日违规"))
        self.label_time_3.setText(_translate("MainWindow2", "几月几日违规"))
        self.label_time_4.setText(_translate("MainWindow2", "几月几日违规"))
        self.label_time_5.setText(_translate("MainWindow2", "几月几日违规"))
        self.label_time_6.setText(_translate("MainWindow2", "几月几日违规"))
        self.label_time_7.setText(_translate("MainWindow2", "几月几日违规"))
        self.label_time_8.setText(_translate("MainWindow2", "几月几日违规"))
        self.label_time_9.setText(_translate("MainWindow2", "几月几日违规"))
        self.label_time_10.setText(_translate("MainWindow2", "几月几日违规"))
        self.label_right.setText(_translate("MainWindow2", "按工号查询详细违规记录"))
        self.pushButton_daochu.setText(_translate("MainWindow2", "导出此人所有违规信息"))
        self.pushButton_fanhui.setText(_translate("MainWindow2", "< 返回主页面"))
        self.pushButton_chaxun_gonghao.setText(_translate("MainWindow2", "查询"))
        self.pushButton_chaxun_name.setText(_translate("MainWindow2", "查询"))
        self.label_name_.setText(_translate("MainWindow2", "XXX"))
        self.label_number.setText(_translate("MainWindow2", "工号："))
        self.label_weigui.setText(_translate("MainWindow2", "总违规次数："))
        self.label_weigui_.setText(_translate("MainWindow2", "XXX"))
        self.label_tishi.setVisible(False)
        self.label_time_1.setVisible(False)
        self.label_time_2.setVisible(False)
        self.label_time_3.setVisible(False)
        self.label_time_4.setVisible(False)
        self.label_time_5.setVisible(False)
        self.label_time_6.setVisible(False)
        self.label_time_7.setVisible(False)
        self.label_time_8.setVisible(False)
        self.label_time_9.setVisible(False)
        self.label_time_10.setVisible(False)