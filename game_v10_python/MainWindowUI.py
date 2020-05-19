# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(553, 540)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.newGamePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.newGamePushButton.setObjectName("newGamePushButton")
        self.horizontalLayout.addWidget(self.newGamePushButton, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.minesLcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.minesLcdNumber.setMinimumSize(QtCore.QSize(70, 40))
        self.minesLcdNumber.setBaseSize(QtCore.QSize(0, 0))
        self.minesLcdNumber.setStyleSheet("QLCDNumber {\n"
"  color: rgb(221, 255, 31);\n"
"  background-color: black;\n"
"  size: 30;\n"
"}")
        self.minesLcdNumber.setDigitCount(3)
        self.minesLcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.minesLcdNumber.setObjectName("minesLcdNumber")
        self.horizontalLayout.addWidget(self.minesLcdNumber, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gameFieldTableView = QtWidgets.QTableView(self.centralwidget)
        self.gameFieldTableView.setStyleSheet("QTableView {\n"
"  background-color: silver;\n"
"}")
        self.gameFieldTableView.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gameFieldTableView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.gameFieldTableView.setObjectName("gameFieldTableView")
        self.gameFieldTableView.horizontalHeader().setVisible(False)
        self.gameFieldTableView.horizontalHeader().setDefaultSectionSize(30)
        self.gameFieldTableView.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.gameFieldTableView)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 553, 18))
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
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addSeparator()
        self.menu.addAction(self.action_5)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.newGamePushButton.setText(_translate("MainWindow", "Новая Игра"))
        self.menu.setTitle(_translate("MainWindow", "Игра"))
        self.action.setText(_translate("MainWindow", "&Новая"))
        self.action_2.setText(_translate("MainWindow", "&Параметры"))
        self.action_3.setText(_translate("MainWindow", "-"))
        self.action_5.setText(_translate("MainWindow", "&Выход"))

