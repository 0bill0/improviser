# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'improviser/qtGUI/preferences.ui'
#
# Created: Fri Jan 30 06:53:39 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_preferencesDialog(object):
    def setupUi(self, preferencesDialog):
        preferencesDialog.setObjectName("preferencesDialog")
        preferencesDialog.setWindowModality(QtCore.Qt.WindowModal)
        preferencesDialog.resize(457, 317)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(preferencesDialog.sizePolicy().hasHeightForWidth())
        preferencesDialog.setSizePolicy(sizePolicy)
        preferencesDialog.setMinimumSize(QtCore.QSize(450, 0))
        preferencesDialog.setSizeGripEnabled(False)
        preferencesDialog.setModal(True)
        self.horizontalLayout = QtGui.QHBoxLayout(preferencesDialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Files = QtGui.QTabWidget(preferencesDialog)
        self.Files.setTabPosition(QtGui.QTabWidget.West)
        self.Files.setObjectName("Files")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.username = QtGui.QLineEdit(self.groupBox_2)
        self.username.setObjectName("username")
        self.gridLayout.addWidget(self.username, 2, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.password = QtGui.QLineEdit(self.groupBox_2)
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 3, 1, 1, 1)
        self.nologin = QtGui.QCheckBox(self.groupBox_2)
        self.nologin.setObjectName("nologin")
        self.gridLayout.addWidget(self.nologin, 4, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setLineWidth(1)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 2)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.Files.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.tab_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox = QtGui.QGroupBox(self.tab_2)
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
        self.horizontalLayout_3.addWidget(self.groupBox)
        self.Files.addTab(self.tab_2, "")
        self.Files1 = QtGui.QWidget()
        self.Files1.setObjectName("Files1")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.Files1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBox_3 = QtGui.QGroupBox(self.Files1)
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
        self.exportmid = QtGui.QCheckBox(self.groupBox_3)
        self.exportmid.setGeometry(QtCore.QRect(30, 110, 131, 22))
        self.exportmid.setChecked(True)
        self.exportmid.setObjectName("exportmid")
        self.exportpdf = QtGui.QCheckBox(self.groupBox_3)
        self.exportpdf.setGeometry(QtCore.QRect(30, 150, 121, 22))
        self.exportpdf.setObjectName("exportpdf")
        self.exportps = QtGui.QCheckBox(self.groupBox_3)
        self.exportps.setGeometry(QtCore.QRect(30, 190, 83, 22))
        self.exportps.setObjectName("exportps")
        self.horizontalLayout_4.addWidget(self.groupBox_3)
        self.Files.addTab(self.Files1, "")
        self.verticalLayout.addWidget(self.Files)
        self.buttonBox = QtGui.QDialogButtonBox(preferencesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(preferencesDialog)
        self.Files.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), preferencesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(preferencesDialog)

    def retranslateUi(self, preferencesDialog):
        preferencesDialog.setWindowTitle(QtGui.QApplication.translate("preferencesDialog", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("preferencesDialog", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("preferencesDialog", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("preferencesDialog", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.nologin.setText(QtGui.QApplication.translate("preferencesDialog", "Don\'t login", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("preferencesDialog", "Login if you want to be able to upload and download songs, blocks, instruments and/or progressions to the Improviser site (http://improviser.onderstekop.nl/). Login with a name that hasn\'t been used to register it.", None, QtGui.QApplication.UnicodeUTF8))
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
        self.exportmid.setText(QtGui.QApplication.translate("preferencesDialog", "Export .mid", None, QtGui.QApplication.UnicodeUTF8))
        self.exportpdf.setText(QtGui.QApplication.translate("preferencesDialog", "Export .pdf", None, QtGui.QApplication.UnicodeUTF8))
        self.exportps.setText(QtGui.QApplication.translate("preferencesDialog", "Export .ps", None, QtGui.QApplication.UnicodeUTF8))
        self.Files.setTabText(self.Files.indexOf(self.Files1), QtGui.QApplication.translate("preferencesDialog", "Files", None, QtGui.QApplication.UnicodeUTF8))

