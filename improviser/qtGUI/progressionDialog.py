# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'improviser/qtGUI/progression.ui'
#
# Created: Mon Jan 26 05:09:30 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_progressionDialog(object):
    def setupUi(self, progressionDialog):
        progressionDialog.setObjectName("progressionDialog")
        progressionDialog.resize(393, 498)
        progressionDialog.setModal(True)
        self.buttonBox = QtGui.QDialogButtonBox(progressionDialog)
        self.buttonBox.setGeometry(QtCore.QRect(120, 450, 261, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox = QtGui.QGroupBox(progressionDialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 380, 371, 61))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.bars = QtGui.QComboBox(self.groupBox)
        self.bars.setEnabled(False)
        self.bars.setGeometry(QtCore.QRect(240, 20, 51, 22))
        self.bars.setObjectName("bars")
        self.romannumeral = QtGui.QComboBox(self.groupBox)
        self.romannumeral.setGeometry(QtCore.QRect(70, 20, 51, 22))
        self.romannumeral.setObjectName("romannumeral")
        self.chordsuffix = QtGui.QComboBox(self.groupBox)
        self.chordsuffix.setGeometry(QtCore.QRect(130, 20, 61, 22))
        self.chordsuffix.setObjectName("chordsuffix")
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(200, 20, 41, 17))
        self.label_2.setObjectName("label_2")
        self.accidentals = QtGui.QComboBox(self.groupBox)
        self.accidentals.setGeometry(QtCore.QRect(10, 20, 51, 22))
        self.accidentals.setObjectName("accidentals")
        self.groupBox_2 = QtGui.QGroupBox(progressionDialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 210, 371, 161))
        self.groupBox_2.setObjectName("groupBox_2")
        self.repeat = QtGui.QSpinBox(self.groupBox_2)
        self.repeat.setGeometry(QtCore.QRect(290, 120, 61, 23))
        self.repeat.setObjectName("repeat")
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(290, 100, 56, 17))
        self.label_3.setObjectName("label_3")
        self.progression = QtGui.QListWidget(self.groupBox_2)
        self.progression.setGeometry(QtCore.QRect(20, 20, 261, 91))
        self.progression.setObjectName("progression")
        self.upprogression = QtGui.QPushButton(self.groupBox_2)
        self.upprogression.setGeometry(QtCore.QRect(290, 20, 61, 27))
        self.upprogression.setObjectName("upprogression")
        self.downprogression = QtGui.QPushButton(self.groupBox_2)
        self.downprogression.setGeometry(QtCore.QRect(290, 50, 61, 27))
        self.downprogression.setObjectName("downprogression")
        self.removeprogression = QtGui.QPushButton(self.groupBox_2)
        self.removeprogression.setGeometry(QtCore.QRect(90, 120, 61, 27))
        self.removeprogression.setObjectName("removeprogression")
        self.clearprogression = QtGui.QPushButton(self.groupBox_2)
        self.clearprogression.setGeometry(QtCore.QRect(160, 120, 61, 27))
        self.clearprogression.setObjectName("clearprogression")
        self.addchord = QtGui.QPushButton(self.groupBox_2)
        self.addchord.setGeometry(QtCore.QRect(20, 120, 61, 27))
        self.addchord.setObjectName("addchord")
        self.groupBox_3 = QtGui.QGroupBox(progressionDialog)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 371, 191))
        self.groupBox_3.setObjectName("groupBox_3")
        self.progressionsequence = QtGui.QListWidget(self.groupBox_3)
        self.progressionsequence.setGeometry(QtCore.QRect(20, 60, 261, 81))
        self.progressionsequence.setObjectName("progressionsequence")
        self.progressionname = QtGui.QLineEdit(self.groupBox_3)
        self.progressionname.setGeometry(QtCore.QRect(90, 30, 261, 23))
        self.progressionname.setObjectName("progressionname")
        self.label = QtGui.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(20, 30, 56, 17))
        self.label.setObjectName("label")
        self.clearsequence = QtGui.QPushButton(self.groupBox_3)
        self.clearsequence.setGeometry(QtCore.QRect(160, 150, 61, 27))
        self.clearsequence.setObjectName("clearsequence")
        self.removesequence = QtGui.QPushButton(self.groupBox_3)
        self.removesequence.setGeometry(QtCore.QRect(90, 150, 61, 27))
        self.removesequence.setObjectName("removesequence")
        self.upsequence = QtGui.QPushButton(self.groupBox_3)
        self.upsequence.setGeometry(QtCore.QRect(290, 60, 61, 27))
        self.upsequence.setObjectName("upsequence")
        self.downsequence = QtGui.QPushButton(self.groupBox_3)
        self.downsequence.setGeometry(QtCore.QRect(290, 90, 61, 27))
        self.downsequence.setObjectName("downsequence")
        self.addprogression = QtGui.QPushButton(self.groupBox_3)
        self.addprogression.setGeometry(QtCore.QRect(20, 150, 61, 27))
        self.addprogression.setObjectName("addprogression")

        self.retranslateUi(progressionDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), progressionDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), progressionDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(progressionDialog)
        progressionDialog.setTabOrder(self.progressionname, self.progressionsequence)
        progressionDialog.setTabOrder(self.progressionsequence, self.removesequence)
        progressionDialog.setTabOrder(self.removesequence, self.clearsequence)
        progressionDialog.setTabOrder(self.clearsequence, self.upsequence)
        progressionDialog.setTabOrder(self.upsequence, self.downsequence)
        progressionDialog.setTabOrder(self.downsequence, self.progression)
        progressionDialog.setTabOrder(self.progression, self.repeat)
        progressionDialog.setTabOrder(self.repeat, self.removeprogression)
        progressionDialog.setTabOrder(self.removeprogression, self.clearprogression)
        progressionDialog.setTabOrder(self.clearprogression, self.addprogression)
        progressionDialog.setTabOrder(self.addprogression, self.upprogression)
        progressionDialog.setTabOrder(self.upprogression, self.downprogression)
        progressionDialog.setTabOrder(self.downprogression, self.accidentals)
        progressionDialog.setTabOrder(self.accidentals, self.romannumeral)
        progressionDialog.setTabOrder(self.romannumeral, self.chordsuffix)
        progressionDialog.setTabOrder(self.chordsuffix, self.bars)
        progressionDialog.setTabOrder(self.bars, self.addchord)
        progressionDialog.setTabOrder(self.addchord, self.buttonBox)

    def retranslateUi(self, progressionDialog):
        progressionDialog.setWindowTitle(QtGui.QApplication.translate("progressionDialog", "Edit Progression", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("progressionDialog", "Chord", None, QtGui.QApplication.UnicodeUTF8))
        self.bars.setToolTip(QtGui.QApplication.translate("progressionDialog", "Number of bars this progression should last", None, QtGui.QApplication.UnicodeUTF8))
        self.romannumeral.setToolTip(QtGui.QApplication.translate("progressionDialog", "Note to build chord on", None, QtGui.QApplication.UnicodeUTF8))
        self.chordsuffix.setToolTip(QtGui.QApplication.translate("progressionDialog", "Chord suffix", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setToolTip(QtGui.QApplication.translate("progressionDialog", "Number of bars this progression should last", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("progressionDialog", "Bars:", None, QtGui.QApplication.UnicodeUTF8))
        self.accidentals.setToolTip(QtGui.QApplication.translate("progressionDialog", "Accidentals", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("progressionDialog", "Progression", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("progressionDialog", "Repeat:", None, QtGui.QApplication.UnicodeUTF8))
        self.progression.setToolTip(QtGui.QApplication.translate("progressionDialog", "Progression", None, QtGui.QApplication.UnicodeUTF8))
        self.upprogression.setText(QtGui.QApplication.translate("progressionDialog", "Up", None, QtGui.QApplication.UnicodeUTF8))
        self.downprogression.setText(QtGui.QApplication.translate("progressionDialog", "Down", None, QtGui.QApplication.UnicodeUTF8))
        self.removeprogression.setText(QtGui.QApplication.translate("progressionDialog", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.clearprogression.setText(QtGui.QApplication.translate("progressionDialog", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.addchord.setToolTip(QtGui.QApplication.translate("progressionDialog", "Add chord to progression", None, QtGui.QApplication.UnicodeUTF8))
        self.addchord.setText(QtGui.QApplication.translate("progressionDialog", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("progressionDialog", "Progression sequence", None, QtGui.QApplication.UnicodeUTF8))
        self.progressionsequence.setToolTip(QtGui.QApplication.translate("progressionDialog", "Progression sequence", None, QtGui.QApplication.UnicodeUTF8))
        self.progressionname.setToolTip(QtGui.QApplication.translate("progressionDialog", "Name of the progression sequence", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("progressionDialog", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.clearsequence.setText(QtGui.QApplication.translate("progressionDialog", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.removesequence.setText(QtGui.QApplication.translate("progressionDialog", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.upsequence.setText(QtGui.QApplication.translate("progressionDialog", "Up", None, QtGui.QApplication.UnicodeUTF8))
        self.downsequence.setText(QtGui.QApplication.translate("progressionDialog", "Down", None, QtGui.QApplication.UnicodeUTF8))
        self.addprogression.setToolTip(QtGui.QApplication.translate("progressionDialog", "Add progression to sequence", None, QtGui.QApplication.UnicodeUTF8))
        self.addprogression.setText(QtGui.QApplication.translate("progressionDialog", "Add", None, QtGui.QApplication.UnicodeUTF8))

