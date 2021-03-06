# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.centralwidget.setObjectName("centralwidget")
        self.decoding_w = QtWidgets.QWidget(self.centralwidget)
        self.decoding_w.setGeometry(QtCore.QRect(0, 0, 803, 563))
        self.decoding_w.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.decoding_w.setObjectName("decoding_w")
        self.widget = QtWidgets.QWidget(self.decoding_w)
        self.widget.setGeometry(QtCore.QRect(10, 0, 779, 559))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.encrypted_text = QtWidgets.QTextEdit(self.widget)
        self.encrypted_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                          "color: rgb(0, 0, 0);")
        self.encrypted_text.setObjectName("encrypted_text")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.encrypted_text)
        self.open_file = QtWidgets.QPushButton(self.widget)
        self.open_file.setStyleSheet("background-color: rgb(136, 136, 136);\n"
                                     "color: rgb(255, 255, 255);")
        self.open_file.setObjectName("open_file")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.open_file)
        self.cipher = QtWidgets.QComboBox(self.widget)
        self.cipher.setStyleSheet("color: rgb(255, 255, 255);\n"
                                  "background-color: rgb(136, 136, 136);\n"
                                  "")
        self.cipher.setObjectName("cipher")
        self.cipher.addItem("")
        self.cipher.addItem("")
        self.cipher.addItem("")
        self.cipher.addItem("")
        self.cipher.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cipher)
        self.file_name = QtWidgets.QLineEdit(self.widget)
        self.file_name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.file_name.setObjectName("file_name")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.file_name)
        self.do_decrypt = QtWidgets.QPushButton(self.widget)
        self.do_decrypt.setStyleSheet("background-color: rgb(136, 136, 136);\n"
                                      "color: rgb(255, 255, 255);")
        self.do_decrypt.setObjectName("do_decrypt")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.do_decrypt)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.decrypted_text = QtWidgets.QTextEdit(self.widget)
        self.decrypted_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                          "color: rgb(0, 0, 0);")
        self.decrypted_text.setObjectName("decrypted_text")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.decrypted_text)
        self.encoding_w = QtWidgets.QWidget(self.centralwidget)
        self.encoding_w.setGeometry(QtCore.QRect(0, 0, 801, 561))
        self.encoding_w.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.encoding_w.setObjectName("encoding_w")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.encoding_w)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 781, 561))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.source = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.source.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                  "color: rgb(0, 0, 0);")
        self.source.setObjectName("source")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.source)
        self.cipher_2 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.cipher_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(136, 136, 136);\n"
                                    "")
        self.cipher_2.setObjectName("cipher_2")
        self.cipher_2.addItem("")
        self.cipher_2.addItem("")
        self.cipher_2.addItem("")
        self.cipher_2.addItem("")
        self.cipher_2.addItem("")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cipher_2)
        self.do_encrypt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.do_encrypt.setStyleSheet("background-color: rgb(136, 136, 136);\n"
                                      "color: rgb(255, 255, 255);")
        self.do_encrypt.setObjectName("do_encrypt")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.do_encrypt)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.encrypted_text_2 = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.encrypted_text_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "color: rgb(0, 0, 0);")
        self.encrypted_text_2.setObjectName("encrypted_text_2")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.encrypted_text_2)
        self.open_file_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.open_file_2.setStyleSheet("background-color: rgb(136, 136, 136);\n"
                                       "color: rgb(255, 255, 255);")
        self.open_file_2.setObjectName("open_file_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.open_file_2)
        self.file_name_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.file_name_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.file_name_2.setObjectName("file_name_2")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.file_name_2)
        self.verticalLayout.addLayout(self.formLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menu.addAction(self.action_4)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "??????????????????"))
        self.label.setText(_translate("MainWindow", "?????????????????????????? ??????????:"))
        self.open_file.setText(_translate("MainWindow", "?????????????? ????????"))
        self.cipher.setCurrentText(_translate("MainWindow", "???????? ????????????"))
        self.cipher.setItemText(0, _translate("MainWindow", "???????? ????????????"))
        self.cipher.setItemText(1, _translate("MainWindow", "???????? ??????????????"))
        self.cipher.setItemText(2, _translate("MainWindow", "??????????"))
        self.cipher.setItemText(3, _translate("MainWindow", "???????? ????????????????"))
        self.cipher.setItemText(4, _translate("MainWindow", "??????????"))
        self.do_decrypt.setText(_translate("MainWindow", "????????????????????????"))
        self.label_2.setText(_translate("MainWindow", "???????????????????????????? ??????????:"))
        self.label_3.setText(_translate("MainWindow", "???????????????? ??????????:"))
        self.cipher_2.setItemText(0, _translate("MainWindow", "???????? ????????????"))
        self.cipher_2.setItemText(1, _translate("MainWindow", "???????? ??????????????"))
        self.cipher_2.setItemText(2, _translate("MainWindow", "??????????"))
        self.cipher_2.setItemText(3, _translate("MainWindow", "???????? ????????????????"))
        self.cipher_2.setItemText(4, _translate("MainWindow", "??????????"))
        self.do_encrypt.setText(_translate("MainWindow", "??????????????????????"))
        self.label_4.setText(_translate("MainWindow", "?????????????????????????? ??????????:"))
        self.open_file_2.setText(_translate("MainWindow", "?????????????? ????????"))
        self.menu.setTitle(_translate("MainWindow", "????????"))
        self.action.setText(_translate("MainWindow", "??????????????????????"))
        self.action_2.setText(_translate("MainWindow", "??????????????????????????"))
        self.action_3.setText(_translate("MainWindow", "?????????????? ?????????????????? ????????????"))
        self.action_4.setText(_translate("MainWindow", "?????????????????? ??????"))
