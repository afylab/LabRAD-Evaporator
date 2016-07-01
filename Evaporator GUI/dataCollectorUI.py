# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dataCollectorUIv3.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1368, 768)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.collectorBackground = QtGui.QFrame(Form)
        self.collectorBackground.setGeometry(QtCore.QRect(0, 0, 1368, 768))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.collectorBackground.sizePolicy().hasHeightForWidth())
        self.collectorBackground.setSizePolicy(sizePolicy)
        self.collectorBackground.setStyleSheet(_fromUtf8("#collectorBackground{\n"
"background: black\n"
"}"))
        self.collectorBackground.setFrameShape(QtGui.QFrame.StyledPanel)
        self.collectorBackground.setFrameShadow(QtGui.QFrame.Raised)
        self.collectorBackground.setObjectName(_fromUtf8("collectorBackground"))
        self.pressureLabel = QtGui.QLabel(self.collectorBackground)
        self.pressureLabel.setGeometry(QtCore.QRect(20, 100, 150, 21))
        self.pressureLabel.setStyleSheet(_fromUtf8("#pressureLabel{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.pressureLabel.setObjectName(_fromUtf8("pressureLabel"))
        self.pressureInput = QtGui.QLineEdit(self.collectorBackground)
        self.pressureInput.setGeometry(QtCore.QRect(180, 100, 113, 21))
        self.pressureInput.setObjectName(_fromUtf8("pressureInput"))
        self.pressureButton = QtGui.QPushButton(self.collectorBackground)
        self.pressureButton.setGeometry(QtCore.QRect(310, 100, 101, 21))
        self.pressureButton.setObjectName(_fromUtf8("pressureButton"))
        self.pressureRate = QtGui.QLabel(self.collectorBackground)
        self.pressureRate.setGeometry(QtCore.QRect(480, 100, 47, 21))
        self.pressureRate.setStyleSheet(_fromUtf8("#pressureRate{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"}"))
        self.pressureRate.setObjectName(_fromUtf8("pressureRate"))
        self.columnRate = QtGui.QLabel(self.collectorBackground)
        self.columnRate.setGeometry(QtCore.QRect(430, 60, 141, 20))
        self.columnRate.setStyleSheet(_fromUtf8("#columnRate{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"}"))
        self.columnRate.setObjectName(_fromUtf8("columnRate"))
        self.thicknessLabel = QtGui.QLabel(self.collectorBackground)
        self.thicknessLabel.setGeometry(QtCore.QRect(20, 140, 150, 21))
        self.thicknessLabel.setStyleSheet(_fromUtf8("#thicknessLabel{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.thicknessLabel.setObjectName(_fromUtf8("thicknessLabel"))
        self.thicknessButton = QtGui.QPushButton(self.collectorBackground)
        self.thicknessButton.setGeometry(QtCore.QRect(310, 140, 101, 21))
        self.thicknessButton.setObjectName(_fromUtf8("thicknessButton"))
        self.thicknessRate = QtGui.QLabel(self.collectorBackground)
        self.thicknessRate.setGeometry(QtCore.QRect(480, 140, 47, 21))
        self.thicknessRate.setStyleSheet(_fromUtf8("#thicknessRate{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"}"))
        self.thicknessRate.setObjectName(_fromUtf8("thicknessRate"))
        self.thicknessInput = QtGui.QLineEdit(self.collectorBackground)
        self.thicknessInput.setGeometry(QtCore.QRect(180, 140, 113, 21))
        self.thicknessInput.setObjectName(_fromUtf8("thicknessInput"))
        self.rateLabel = QtGui.QLabel(self.collectorBackground)
        self.rateLabel.setGeometry(QtCore.QRect(20, 180, 150, 21))
        self.rateLabel.setStyleSheet(_fromUtf8("#rateLabel\n"
"{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: false;\n"
"}"))
        self.rateLabel.setObjectName(_fromUtf8("rateLabel"))
        self.rateButton = QtGui.QPushButton(self.collectorBackground)
        self.rateButton.setGeometry(QtCore.QRect(310, 180, 101, 21))
        self.rateButton.setObjectName(_fromUtf8("rateButton"))
        self.rateRate = QtGui.QLabel(self.collectorBackground)
        self.rateRate.setGeometry(QtCore.QRect(480, 180, 47, 21))
        self.rateRate.setStyleSheet(_fromUtf8("#rateRate{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"}"))
        self.rateRate.setObjectName(_fromUtf8("rateRate"))
        self.rateInput = QtGui.QLineEdit(self.collectorBackground)
        self.rateInput.setGeometry(QtCore.QRect(180, 180, 113, 21))
        self.rateInput.setObjectName(_fromUtf8("rateInput"))
        self.textEdit = QtGui.QTextEdit(self.collectorBackground)
        self.textEdit.setGeometry(QtCore.QRect(690, 540, 250, 141))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.thicknessStartButton = QtGui.QPushButton(self.collectorBackground)
        self.thicknessStartButton.setGeometry(QtCore.QRect(590, 140, 135, 21))
        self.thicknessStartButton.setObjectName(_fromUtf8("thicknessStartButton"))
        self.pressureStartButton = QtGui.QPushButton(self.collectorBackground)
        self.pressureStartButton.setGeometry(QtCore.QRect(590, 100, 135, 21))
        self.pressureStartButton.setObjectName(_fromUtf8("pressureStartButton"))
        self.rateStartButton = QtGui.QPushButton(self.collectorBackground)
        self.rateStartButton.setGeometry(QtCore.QRect(590, 180, 135, 21))
        self.rateStartButton.setObjectName(_fromUtf8("rateStartButton"))
        self.allStartButton = QtGui.QPushButton(self.collectorBackground)
        self.allStartButton.setGeometry(QtCore.QRect(590, 60, 135, 21))
        self.allStartButton.setObjectName(_fromUtf8("allStartButton"))
        self.rateStatus = QtGui.QLabel(self.collectorBackground)
        self.rateStatus.setGeometry(QtCore.QRect(740, 180, 100, 21))
        self.rateStatus.setStyleSheet(_fromUtf8("#rateStatus{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignCenter\';\n"
"qproperty-wordWrap: false;\n"
"}"))
        self.rateStatus.setObjectName(_fromUtf8("rateStatus"))
        self.pressureStatus = QtGui.QLabel(self.collectorBackground)
        self.pressureStatus.setGeometry(QtCore.QRect(740, 100, 100, 21))
        self.pressureStatus.setStyleSheet(_fromUtf8("#pressureStatus{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignCenter\';\n"
"qproperty-wordWrap: false;\n"
"}"))
        self.pressureStatus.setObjectName(_fromUtf8("pressureStatus"))
        self.thicknessStatus = QtGui.QLabel(self.collectorBackground)
        self.thicknessStatus.setGeometry(QtCore.QRect(740, 140, 100, 21))
        self.thicknessStatus.setStyleSheet(_fromUtf8("#thicknessStatus{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignCenter\';\n"
"qproperty-wordWrap: false;\n"
"}"))
        self.thicknessStatus.setObjectName(_fromUtf8("thicknessStatus"))
        self.status = QtGui.QLabel(self.collectorBackground)
        self.status.setGeometry(QtCore.QRect(740, 60, 100, 21))
        self.status.setStyleSheet(_fromUtf8("#status{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignCenter\';\n"
"qproperty-wordWrap: false;\n"
"}"))
        self.status.setObjectName(_fromUtf8("status"))
        self.voltRate = QtGui.QLabel(self.collectorBackground)
        self.voltRate.setGeometry(QtCore.QRect(480, 220, 47, 21))
        self.voltRate.setStyleSheet(_fromUtf8("#voltRate{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"}"))
        self.voltRate.setObjectName(_fromUtf8("voltRate"))
        self.voltStatus = QtGui.QLabel(self.collectorBackground)
        self.voltStatus.setGeometry(QtCore.QRect(740, 220, 100, 21))
        self.voltStatus.setStyleSheet(_fromUtf8("#voltStatus{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignCenter\';\n"
"qproperty-wordWrap: false;\n"
"}"))
        self.voltStatus.setObjectName(_fromUtf8("voltStatus"))
        self.voltLabel = QtGui.QLabel(self.collectorBackground)
        self.voltLabel.setGeometry(QtCore.QRect(20, 220, 150, 21))
        self.voltLabel.setStyleSheet(_fromUtf8("#voltLabel\n"
"{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: false;\n"
"}"))
        self.voltLabel.setObjectName(_fromUtf8("voltLabel"))
        self.voltStartButton = QtGui.QPushButton(self.collectorBackground)
        self.voltStartButton.setGeometry(QtCore.QRect(590, 220, 135, 21))
        self.voltStartButton.setObjectName(_fromUtf8("voltStartButton"))
        self.voltInput = QtGui.QLineEdit(self.collectorBackground)
        self.voltInput.setGeometry(QtCore.QRect(180, 220, 113, 21))
        self.voltInput.setObjectName(_fromUtf8("voltInput"))
        self.voltButton = QtGui.QPushButton(self.collectorBackground)
        self.voltButton.setGeometry(QtCore.QRect(310, 220, 101, 21))
        self.voltButton.setObjectName(_fromUtf8("voltButton"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pressureLabel.setText(_translate("Form", "Pressure:", None))
        self.pressureButton.setText(_translate("Form", "Set Sampling Rate", None))
        self.pressureRate.setText(_translate("Form", "1000", None))
        self.columnRate.setText(_translate("Form", "Sampling Rate (ms)", None))
        self.thicknessLabel.setText(_translate("Form", "Thickness:", None))
        self.thicknessButton.setText(_translate("Form", "Set Sampling Rate", None))
        self.thicknessRate.setText(_translate("Form", "1000", None))
        self.rateLabel.setText(_translate("Form", "Deposition Rate:", None))
        self.rateButton.setText(_translate("Form", "Set Sampling Rate", None))
        self.rateRate.setText(_translate("Form", "1000", None))
        self.thicknessStartButton.setText(_translate("Form", "Start Sampling Thickness", None))
        self.pressureStartButton.setText(_translate("Form", "Start Sampling Pressure", None))
        self.rateStartButton.setText(_translate("Form", "Start Sampling Rate", None))
        self.allStartButton.setText(_translate("Form", "Start Sampling Everything", None))
        self.rateStatus.setText(_translate("Form", "N/A", None))
        self.pressureStatus.setText(_translate("Form", "N/A", None))
        self.thicknessStatus.setText(_translate("Form", "N/A", None))
        self.status.setText(_translate("Form", "Status", None))
        self.voltRate.setText(_translate("Form", "1000", None))
        self.voltStatus.setText(_translate("Form", "N/A", None))
        self.voltLabel.setText(_translate("Form", "Voltage:", None))
        self.voltStartButton.setText(_translate("Form", "Start Sampling Voltage", None))
        self.voltButton.setText(_translate("Form", "Set Sampling Rate", None))

