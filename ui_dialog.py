# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created: Sun Oct  9 09:00:24 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(273, 117)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.sourceLineEdit = QtGui.QLineEdit(Dialog)
        self.sourceLineEdit.setObjectName(_fromUtf8("sourceLineEdit"))
        self.gridLayout.addWidget(self.sourceLineEdit, 0, 1, 1, 1)
        self.sourceButton = QtGui.QPushButton(Dialog)
        self.sourceButton.setObjectName(_fromUtf8("sourceButton"))
        self.gridLayout.addWidget(self.sourceButton, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.outputLineEdit = QtGui.QLineEdit(Dialog)
        self.outputLineEdit.setObjectName(_fromUtf8("outputLineEdit"))
        self.gridLayout.addWidget(self.outputLineEdit, 1, 1, 1, 1)
        self.outputButton = QtGui.QPushButton(Dialog)
        self.outputButton.setObjectName(_fromUtf8("outputButton"))
        self.gridLayout.addWidget(self.outputButton, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.buildButton = QtGui.QPushButton(Dialog)
        self.buildButton.setObjectName(_fromUtf8("buildButton"))
        self.horizontalLayout.addWidget(self.buildButton)
        self.statusLabel = QtGui.QLabel(Dialog)
        self.statusLabel.setObjectName(_fromUtf8("statusLabel"))
        self.horizontalLayout.addWidget(self.statusLabel)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "sphinx-build-qt", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Source", None, QtGui.QApplication.UnicodeUTF8))
        self.sourceButton.setText(QtGui.QApplication.translate("Dialog", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.outputButton.setText(QtGui.QApplication.translate("Dialog", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.buildButton.setText(QtGui.QApplication.translate("Dialog", "Build", None, QtGui.QApplication.UnicodeUTF8))
        self.statusLabel.setText(QtGui.QApplication.translate("Dialog", "Ready!", None, QtGui.QApplication.UnicodeUTF8))

