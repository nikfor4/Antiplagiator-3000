# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '00.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Main_Start(object):
    def setupUi1(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(419, 280)
        Dialog.setStyleSheet("background-color: black;")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(190, 0, 31, 51))
        self.label.setStyleSheet("color: white;\n"
"font-family: Impact, fantasy;\n"
"font-size:30px;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(90, 40, 261, 51))
        self.label_2.setStyleSheet("color: white;\n"
"font-family: Arial Narrow, sans-serif ;\n"
"font-size:30px;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 80, 381, 61))
        self.label_3.setStyleSheet("color: white;\n"
"font-family: Impact, fantasy;\n"
"font-size:30px;")
        self.label_3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(110, 130, 191, 31))
        self.label_4.setStyleSheet("color: white;\n"
"font-family: Arial Narrow, sans-serif ;\n"
"font-size:15px;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(132, 160, 141, 51))
        self.label_5.setStyleSheet("color: white;\n"
"font-family: Impact, fantasy;\n"
"font-size:30px;")
        self.label_5.setObjectName("label_5")
        self.btn = QtWidgets.QPushButton(Dialog)
        self.btn.setGeometry(QtCore.QRect(130, 210, 131, 41))
        self.btn.setStyleSheet("QPushButton {\n"
"background-color: rgb(36,36,36);\n"
"color: white;\n"
"font-family: Impact, fantasy;\n"
"font-size:30px;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"  background-color: rgb(100,100,100);\n"
"color: white;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"   background-color: rgb(50,50,50);\n"
"color: white;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:disabled {\n"
"   background-color: rgb(70,70,70);\n"
"color: white;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"")
        self.btn.setObjectName("btn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "??"))
        self.label_2.setText(_translate("Dialog", "?????????????????????????? 3000"))
        self.label_3.setText(_translate("Dialog", "?? ?????????????? ???????? ??????????????!"))
        self.label_4.setText(_translate("Dialog", "???????? ???????????? ???????? ??????????????????????"))
        self.label_5.setText(_translate("Dialog", "???????????????"))
        self.btn.setText(_translate("Dialog", "??????????????!"))
