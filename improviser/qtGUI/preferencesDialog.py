# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'improviser/qtGUI/preferences.ui'
#
# Created: Mon Jan 26 05:09:30 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_preferencesDialog(object):
    def setupUi(self, preferencesDialog):
        preferencesDialog.setObjectName("preferencesDialog")
        preferencesDialog.setWindowModality(QtCore.Qt.WindowModal)
        preferencesDialog.resize(461, 339)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(preferencesDialog.sizePolicy().hasHeightForWidth())
        preferencesDialog.setSizePolicy(sizePolicy)
        preferencesDialog.setSizeGripEnabled(False)
        preferencesDialog.setModal(True)
        self.verticalLayoutWidget = QtGui.QWidget(preferencesDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 441, 321))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Files = QtGui.QTabWidget(self.verticalLayoutWidget)
        self.Files.setTabPosition(QtGui.QTabWidget.West)
        self.Files.setObjectName("Files")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 391, 231))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(20, 120, 71, 17))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(20, 160, 61, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 341, 71))
        self.label_3.setLineWidth(1)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.username = QtGui.QLineEdit(self.groupBox_2)
        self.username.setGeometry(QtCore.QRect(130, 120, 221, 23))
        self.username.setObjectName("username")
        self.password = QtGui.QLineEdit(self.groupBox_2)
        self.password.setGeometry(QtCore.QRect(130, 160, 221, 23))
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        self.password.setObjectName("password")
        self.nologin = QtGui.QCheckBox(self.groupBox_2)
        self.nologin.setGeometry(QtCore.QRect(20, 200, 83, 22))
        self.nologin.setObjectName("nologin")
        self.Files.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox = QtGui.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 391, 141))
        self.groupBox.setObjectName("groupBox")
        self.no_fluidsynth = QtGui.QCheckBox(self.groupBox)
        self.no_fluidsynth.setGeometry(QtCore.QRect(30, 110, 83, 22))
        self.no_fluidsynth.setObjectName("no_fluidsynth")
        self.browsebutton = QtGui.QPushButton(self.groupBox)
        self.browsebutton.setGeometry(QtCore.QRect(290, 30, 80, 27))
        self.browsebutton.setObjectName("browsebutton")
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(30, 30, 81, 17))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(30, 70, 81, 17))
        self.label_10.setObjectName("label_10")
        self.driver = QtGui.QComboBox(self.groupBox)
        self.driver.setGeometry(QtCore.QRect(130, 70, 231, 22))
        self.driver.setObjectName("driver")
        self.soundfont = QtGui.QLineEdit(self.groupBox)
        self.soundfont.setEnabled(False)
        self.soundfont.setGeometry(QtCore.QRect(130, 30, 151, 23))
        self.soundfont.setObjectName("soundfont")
        self.Files.addTab(self.tab_2, "")
        self.Files1 = QtGui.QWidget()
        self.Files1.setObjectName("Files1")
        self.groupBox_3 = QtGui.QGroupBox(self.Files1)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 391, 101))
        self.groupBox_3.setObjectName("groupBox_3")
        self.browsefolder = QtGui.QPushButton(self.groupBox_3)
        self.browsefolder.setGeometry(QtCore.QRect(290, 30, 80, 27))
        self.browsefolder.setObjectName("browsefolder")
        self.folder = QtGui.QLineEdit(self.groupBox_3)
        self.folder.setEnabled(False)
        self.folder.setGeometry(QtCore.QRect(130, 30, 151, 23))
        self.folder.setObjectName("folder")
        self.label_4 = QtGui.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(30, 30, 51, 21))
        self.label_4.setObjectName("label_4")
        self.checkupdates = QtGui.QCheckBox(self.groupBox_3)
        self.checkupdates.setGeometry(QtCore.QRect(30, 70, 231, 21))
        self.checkupdates.setObjectName("checkupdates")
        self.Files.addTab(self.Files1, "")
        self.verticalLayout.addWidget(self.Files)
        self.buttonBox = QtGui.QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(preferencesDialog)
        self.Files.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), preferencesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(preferencesDialog)

    def retranslateUi(self, preferencesDialog):
        preferencesDialog.setWindowTitle(QtGui.QApplication.translate("preferencesDialog", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("preferencesDialog", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("preferencesDialog", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("preferencesDialog", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("preferencesDialog", "Login if you want to be able to upload your songs, blocks, instruments and/or progressions to the Improviser site (http://improviser.onderstekop.nl/). Login with a name that hasn\'t been used to register it.", None, QtGui.QApplication.UnicodeUTF8))
        self.nologin.setText(QtGui.QApplication.translate("preferencesDialog", "Don\'t login", None, QtGui.QApplication.UnicodeUTF8))
        self.Files.setTabText(self.Files.indexOf(self.tab), QtGui.QApplication.translate("preferencesDialog", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("preferencesDialog", "Audio", None, QtGui.QApplication.UnicodeUTF8))
        self.no_fluidsynth.setStatusTip(QtGui.QApplication.translate("preferencesDialog", "Disable audio output. Only write midi file.", None, QtGui.QApplication.UnicodeUTF8))
        self.no_fluidsynth.setText(QtGui.QApplication.translate("preferencesDialog", "No audio", None, QtGui.QApplication.UnicodeUTF8))
        self.browsebutton.setText(QtGui.QApplication.translate("preferencesDialog", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setStatusTip(QtGui.QApplication.translate("preferencesDialog", "The location of the soundfont to use", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("preferencesDialog", "Soundfont", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("preferencesDialog", "Audio driver", None, QtGui.QApplication.UnicodeUTF8))
        self.soundfont.setStatusTip(QtGui.QApplication.translate("preferencesDialog", "The location of the soundfont to use", None, QtGui.QApplication.UnicodeUTF8))
        self.Files.setTabText(self.Files.indexOf(self.tab_2), QtGui.QApplication.translate("preferencesDialog", "Audio", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("preferencesDialog", "Files", None, QtGui.QApplication.UnicodeUTF8))
        self.browsefolder.setText(QtGui.QApplication.translate("preferencesDialog", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("preferencesDialog", "Folder", None, QtGui.QApplication.UnicodeUTF8))
        self.checkupdates.setToolTip(QtGui.QApplication.translate("preferencesDialog", "Connect to the server and see if there are any new files.", None, QtGui.QApplication.UnicodeUTF8))
        self.checkupdates.setText(QtGui.QApplication.translate("preferencesDialog", "Check for new content on start up", None, QtGui.QApplication.UnicodeUTF8))
        self.Files.setTabText(self.Files.indexOf(self.Files1), QtGui.QApplication.translate("preferencesDialog", "Files", None, QtGui.QApplication.UnicodeUTF8))

