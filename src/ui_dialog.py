# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/dialog.ui'
#
# Created: Wed Feb 29 19:20:54 2012
#      by: PyQt4 UI code generator 4.8.5
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
        Dialog.resize(373, 539)
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "sphinx-build-qt", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Sphinx Project", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setText(QtGui.QApplication.translate("Dialog", "Source Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.sourceLineEdit = QtGui.QLineEdit(self.groupBox)
        self.sourceLineEdit.setObjectName(_fromUtf8("sourceLineEdit"))
        self.horizontalLayout.addWidget(self.sourceLineEdit)
        self.sourceButton = QtGui.QPushButton(self.groupBox)
        self.sourceButton.setText(QtGui.QApplication.translate("Dialog", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.sourceButton.setObjectName(_fromUtf8("sourceButton"))
        self.horizontalLayout.addWidget(self.sourceButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Output Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.outputLineEdit = QtGui.QLineEdit(self.groupBox)
        self.outputLineEdit.setObjectName(_fromUtf8("outputLineEdit"))
        self.horizontalLayout_2.addWidget(self.outputLineEdit)
        self.outputButton = QtGui.QPushButton(self.groupBox)
        self.outputButton.setText(QtGui.QApplication.translate("Dialog", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.outputButton.setObjectName(_fromUtf8("outputButton"))
        self.horizontalLayout_2.addWidget(self.outputButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Dialog", "Build", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.projectRadioButton = QtGui.QRadioButton(self.groupBox_2)
        self.projectRadioButton.setText(QtGui.QApplication.translate("Dialog", "Project", None, QtGui.QApplication.UnicodeUTF8))
        self.projectRadioButton.setChecked(True)
        self.projectRadioButton.setObjectName(_fromUtf8("projectRadioButton"))
        self.verticalLayout.addWidget(self.projectRadioButton)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.fileRadioButton = QtGui.QRadioButton(self.groupBox_2)
        self.fileRadioButton.setText(QtGui.QApplication.translate("Dialog", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.fileRadioButton.setObjectName(_fromUtf8("fileRadioButton"))
        self.horizontalLayout_3.addWidget(self.fileRadioButton)
        self.fileLineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.fileLineEdit.setObjectName(_fromUtf8("fileLineEdit"))
        self.horizontalLayout_3.addWidget(self.fileLineEdit)
        self.fileButton = QtGui.QPushButton(self.groupBox_2)
        self.fileButton.setText(QtGui.QApplication.translate("Dialog", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.fileButton.setObjectName(_fromUtf8("fileButton"))
        self.horizontalLayout_3.addWidget(self.fileButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.logButton = QtGui.QPushButton(Dialog)
        self.logButton.setText(QtGui.QApplication.translate("Dialog", "Log", None, QtGui.QApplication.UnicodeUTF8))
        self.logButton.setCheckable(True)
        self.logButton.setObjectName(_fromUtf8("logButton"))
        self.horizontalLayout_4.addWidget(self.logButton)
        self.statusLabel = QtGui.QLabel(Dialog)
        self.statusLabel.setText(QtGui.QApplication.translate("Dialog", "Ready", None, QtGui.QApplication.UnicodeUTF8))
        self.statusLabel.setObjectName(_fromUtf8("statusLabel"))
        self.horizontalLayout_4.addWidget(self.statusLabel)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.buildButton = QtGui.QPushButton(Dialog)
        self.buildButton.setText(QtGui.QApplication.translate("Dialog", "Build", None, QtGui.QApplication.UnicodeUTF8))
        self.buildButton.setObjectName(_fromUtf8("buildButton"))
        self.horizontalLayout_4.addWidget(self.buildButton)
        self.closeButton = QtGui.QPushButton(Dialog)
        self.closeButton.setText(QtGui.QApplication.translate("Dialog", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.horizontalLayout_4.addWidget(self.closeButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.dockWidget = QtGui.QDockWidget(Dialog)
        self.dockWidget.setWindowTitle(_fromUtf8(""))
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.dockWidgetContents)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.logBrowser = QtGui.QTextBrowser(self.dockWidgetContents)
        self.logBrowser.setObjectName(_fromUtf8("logBrowser"))
        self.horizontalLayout_5.addWidget(self.logBrowser)
        self.dockWidget.setWidget(self.dockWidgetContents)
        self.verticalLayout_3.addWidget(self.dockWidget)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.label.setBuddy(self.sourceLineEdit)
        self.label_2.setBuddy(self.outputLineEdit)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.sourceLineEdit, self.sourceButton)
        Dialog.setTabOrder(self.sourceButton, self.outputLineEdit)
        Dialog.setTabOrder(self.outputLineEdit, self.outputButton)
        Dialog.setTabOrder(self.outputButton, self.projectRadioButton)
        Dialog.setTabOrder(self.projectRadioButton, self.fileRadioButton)
        Dialog.setTabOrder(self.fileRadioButton, self.fileLineEdit)
        Dialog.setTabOrder(self.fileLineEdit, self.fileButton)
        Dialog.setTabOrder(self.fileButton, self.buildButton)
        Dialog.setTabOrder(self.buildButton, self.closeButton)
        Dialog.setTabOrder(self.closeButton, self.logButton)

    def retranslateUi(self, Dialog):
        pass

