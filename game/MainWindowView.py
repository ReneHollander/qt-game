# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/MainWindow.ui'
#
# Created: Mon Dec 21 17:06:03 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(687, 239)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.centralWidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_title = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_title.setFont(font)
        self.label_title.setIndent(-4)
        self.label_title.setObjectName("label_title")
        self.horizontalLayout.addWidget(self.label_title)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_offen = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_offen.setFont(font)
        self.label_offen.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_offen.setObjectName("label_offen")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_offen)
        self.label_open = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_open.setFont(font)
        self.label_open.setAlignment(QtCore.Qt.AlignCenter)
        self.label_open.setObjectName("label_open")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.label_open)
        self.label_korrekt = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_korrekt.setFont(font)
        self.label_korrekt.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_korrekt.setObjectName("label_korrekt")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_korrekt)
        self.label_correct = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_correct.setFont(font)
        self.label_correct.setAlignment(QtCore.Qt.AlignCenter)
        self.label_correct.setObjectName("label_correct")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.label_correct)
        self.label_falsch = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_falsch.setFont(font)
        self.label_falsch.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_falsch.setObjectName("label_falsch")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_falsch)
        self.label_wrong = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_wrong.setFont(font)
        self.label_wrong.setAlignment(QtCore.Qt.AlignCenter)
        self.label_wrong.setObjectName("label_wrong")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.label_wrong)
        self.label_gesamt = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_gesamt.setFont(font)
        self.label_gesamt.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_gesamt.setObjectName("label_gesamt")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_gesamt)
        self.label_total = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_total.setFont(font)
        self.label_total.setAlignment(QtCore.Qt.AlignCenter)
        self.label_total.setObjectName("label_total")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.label_total)
        self.label_spiele = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        self.label_spiele.setFont(font)
        self.label_spiele.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_spiele.setObjectName("label_spiele")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_spiele)
        self.label_games = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_games.setFont(font)
        self.label_games.setAlignment(QtCore.Qt.AlignCenter)
        self.label_games.setObjectName("label_games")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.label_games)
        self.horizontalLayout_3.addLayout(self.formLayout)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.button_order_1 = QtGui.QPushButton(self.centralWidget)
        self.button_order_1.setObjectName("button_order_1")
        self.gridLayout.addWidget(self.button_order_1, 0, 1, 1, 1)
        self.button_order_0 = QtGui.QPushButton(self.centralWidget)
        self.button_order_0.setObjectName("button_order_0")
        self.gridLayout.addWidget(self.button_order_0, 0, 0, 1, 1)
        self.button_order_3 = QtGui.QPushButton(self.centralWidget)
        self.button_order_3.setObjectName("button_order_3")
        self.gridLayout.addWidget(self.button_order_3, 0, 3, 1, 1)
        self.button_order_2 = QtGui.QPushButton(self.centralWidget)
        self.button_order_2.setObjectName("button_order_2")
        self.gridLayout.addWidget(self.button_order_2, 0, 2, 1, 1)
        self.button_order_6 = QtGui.QPushButton(self.centralWidget)
        self.button_order_6.setObjectName("button_order_6")
        self.gridLayout.addWidget(self.button_order_6, 1, 1, 1, 1)
        self.button_order_8 = QtGui.QPushButton(self.centralWidget)
        self.button_order_8.setObjectName("button_order_8")
        self.gridLayout.addWidget(self.button_order_8, 1, 3, 1, 1)
        self.button_order_13 = QtGui.QPushButton(self.centralWidget)
        self.button_order_13.setObjectName("button_order_13")
        self.gridLayout.addWidget(self.button_order_13, 2, 3, 1, 1)
        self.button_order_5 = QtGui.QPushButton(self.centralWidget)
        self.button_order_5.setObjectName("button_order_5")
        self.gridLayout.addWidget(self.button_order_5, 1, 0, 1, 1)
        self.button_order_7 = QtGui.QPushButton(self.centralWidget)
        self.button_order_7.setObjectName("button_order_7")
        self.gridLayout.addWidget(self.button_order_7, 1, 2, 1, 1)
        self.button_order_14 = QtGui.QPushButton(self.centralWidget)
        self.button_order_14.setObjectName("button_order_14")
        self.gridLayout.addWidget(self.button_order_14, 2, 4, 1, 1)
        self.button_order_4 = QtGui.QPushButton(self.centralWidget)
        self.button_order_4.setObjectName("button_order_4")
        self.gridLayout.addWidget(self.button_order_4, 0, 4, 1, 1)
        self.button_order_10 = QtGui.QPushButton(self.centralWidget)
        self.button_order_10.setObjectName("button_order_10")
        self.gridLayout.addWidget(self.button_order_10, 2, 0, 1, 1)
        self.button_order_12 = QtGui.QPushButton(self.centralWidget)
        self.button_order_12.setObjectName("button_order_12")
        self.gridLayout.addWidget(self.button_order_12, 2, 2, 1, 1)
        self.button_order_11 = QtGui.QPushButton(self.centralWidget)
        self.button_order_11.setObjectName("button_order_11")
        self.gridLayout.addWidget(self.button_order_11, 2, 1, 1, 1)
        self.button_order_9 = QtGui.QPushButton(self.centralWidget)
        self.button_order_9.setObjectName("button_order_9")
        self.gridLayout.addWidget(self.button_order_9, 1, 4, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.button_new = QtGui.QPushButton(self.centralWidget)
        self.button_new.setObjectName("button_new")
        self.horizontalLayout_2.addWidget(self.button_new)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.button_exit = QtGui.QPushButton(self.centralWidget)
        self.button_exit.setObjectName("button_exit")
        self.horizontalLayout_2.addWidget(self.button_exit)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.button_exit, QtCore.SIGNAL("clicked()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "QTGame", None, QtGui.QApplication.UnicodeUTF8))
        self.label_title.setText(QtGui.QApplication.translate("MainWindow", "Drücken Sie die Buttons in aufsteigender Reihenfolge!", None, QtGui.QApplication.UnicodeUTF8))
        self.label_offen.setText(QtGui.QApplication.translate("MainWindow", "offen", None, QtGui.QApplication.UnicodeUTF8))
        self.label_open.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_korrekt.setText(QtGui.QApplication.translate("MainWindow", "korrekt", None, QtGui.QApplication.UnicodeUTF8))
        self.label_correct.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_falsch.setText(QtGui.QApplication.translate("MainWindow", "falsch", None, QtGui.QApplication.UnicodeUTF8))
        self.label_wrong.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_gesamt.setText(QtGui.QApplication.translate("MainWindow", "gesamt", None, QtGui.QApplication.UnicodeUTF8))
        self.label_total.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_spiele.setText(QtGui.QApplication.translate("MainWindow", "Spiele", None, QtGui.QApplication.UnicodeUTF8))
        self.label_games.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.button_order_1.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.button_order_0.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.button_order_3.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.button_order_2.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.button_order_6.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.button_order_8.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.button_order_13.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.button_order_5.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.button_order_7.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.button_order_14.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.button_order_4.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.button_order_10.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.button_order_12.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.button_order_11.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.button_order_9.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.button_new.setText(QtGui.QApplication.translate("MainWindow", "Neu", None, QtGui.QApplication.UnicodeUTF8))
        self.button_exit.setText(QtGui.QApplication.translate("MainWindow", "Ende", None, QtGui.QApplication.UnicodeUTF8))
