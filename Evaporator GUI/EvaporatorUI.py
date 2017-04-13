# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EvaporatorUI.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1300, 700)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1300, 700))
        MainWindow.setMaximumSize(QtCore.QSize(1300, 700))
        MainWindow.setStyleSheet(_fromUtf8(""))
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        MainWindow.setDockOptions(QtGui.QMainWindow.AllowTabbedDocks|QtGui.QMainWindow.AnimatedDocks)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1300, 700))
        self.tabWidget.setStyleSheet(_fromUtf8(""))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.GraphicalInterface = QtGui.QWidget()
        self.GraphicalInterface.setStyleSheet(_fromUtf8(""))
        self.GraphicalInterface.setObjectName(_fromUtf8("GraphicalInterface"))
        self.graphBackground = QtGui.QFrame(self.GraphicalInterface)
        self.graphBackground.setEnabled(True)
        self.graphBackground.setGeometry(QtCore.QRect(0, 0, 1294, 674))
        self.graphBackground.setStyleSheet(_fromUtf8("#graphBackground{\n"
"background: black\n"
"}"))
        self.graphBackground.setFrameShape(QtGui.QFrame.StyledPanel)
        self.graphBackground.setFrameShadow(QtGui.QFrame.Raised)
        self.graphBackground.setObjectName(_fromUtf8("graphBackground"))
        self.line = QtGui.QFrame(self.graphBackground)
        self.line.setGeometry(QtCore.QRect(90, 460, 20, 50))
        self.line.setStyleSheet(_fromUtf8("#line{\n"
"color:white;\n"
"}"))
        self.line.setFrameShadow(QtGui.QFrame.Plain)
        self.line.setLineWidth(4)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setObjectName(_fromUtf8("line"))
        self.scrollPumpLabel = QtGui.QLabel(self.graphBackground)
        self.scrollPumpLabel.setGeometry(QtCore.QRect(240, 590, 121, 41))
        self.scrollPumpLabel.setStyleSheet(_fromUtf8("#scrollPumpLabel{\n"
"color: white;\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"}"))
        self.scrollPumpLabel.setObjectName(_fromUtf8("scrollPumpLabel"))
        self.scrollValveButton = QtGui.QPushButton(self.graphBackground)
        self.scrollValveButton.setGeometry(QtCore.QRect(275, 410, 50, 50))
        self.scrollValveButton.setStyleSheet(_fromUtf8("#scrollValveButton{\n"
"  border-color: rgb(255, 255, 255);\n"
"  border-width: 4px;        \n"
"  border-style: solid;\n"
"  border-radius: 25px;\n"
"background: black;\n"
"}"))
        self.scrollValveButton.setText(_fromUtf8(""))
        self.scrollValveButton.setObjectName(_fromUtf8("scrollValveButton"))
        self.line_2 = QtGui.QFrame(self.graphBackground)
        self.line_2.setGeometry(QtCore.QRect(90, 360, 20, 50))
        self.line_2.setStyleSheet(_fromUtf8("#line_2{\n"
"color: white\n"
"}"))
        self.line_2.setFrameShadow(QtGui.QFrame.Plain)
        self.line_2.setLineWidth(4)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.scrollValveStatus = QtGui.QLabel(self.graphBackground)
        self.scrollValveStatus.setGeometry(QtCore.QRect(330, 406, 50, 50))
        self.scrollValveStatus.setStyleSheet(_fromUtf8("#scrollValveStatus{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.scrollValveStatus.setObjectName(_fromUtf8("scrollValveStatus"))
        self.line_3 = QtGui.QFrame(self.graphBackground)
        self.line_3.setGeometry(QtCore.QRect(290, 460, 20, 100))
        self.line_3.setStyleSheet(_fromUtf8("#line_3{\n"
"color: white;\n"
"}"))
        self.line_3.setFrameShadow(QtGui.QFrame.Plain)
        self.line_3.setLineWidth(4)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.line_4 = QtGui.QFrame(self.graphBackground)
        self.line_4.setGeometry(QtCore.QRect(290, 360, 20, 50))
        self.line_4.setStyleSheet(_fromUtf8("#line_4{\n"
"color: white\n"
"}"))
        self.line_4.setFrameShadow(QtGui.QFrame.Plain)
        self.line_4.setLineWidth(4)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.turboValveButton = QtGui.QPushButton(self.graphBackground)
        self.turboValveButton.setGeometry(QtCore.QRect(75, 410, 50, 50))
        self.turboValveButton.setStyleSheet(_fromUtf8("#turboValveButton{\n"
"  border-color: rgb(255, 255, 255);\n"
"  border-width: 4px;        \n"
"  border-style: solid;\n"
"  border-radius: 25px;\n"
" background: black;\n"
"}"))
        self.turboValveButton.setText(_fromUtf8(""))
        self.turboValveButton.setObjectName(_fromUtf8("turboValveButton"))
        self.turboValveStatus = QtGui.QLabel(self.graphBackground)
        self.turboValveStatus.setGeometry(QtCore.QRect(10, 406, 50, 50))
        self.turboValveStatus.setStyleSheet(_fromUtf8("#turboValveStatus{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.turboValveStatus.setObjectName(_fromUtf8("turboValveStatus"))
        self.turboPumpLabel = QtGui.QLabel(self.graphBackground)
        self.turboPumpLabel.setGeometry(QtCore.QRect(40, 290, 121, 41))
        self.turboPumpLabel.setStyleSheet(_fromUtf8("#turboPumpLabel{\n"
"color: white;\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"}"))
        self.turboPumpLabel.setObjectName(_fromUtf8("turboPumpLabel"))
        self.line_5 = QtGui.QFrame(self.graphBackground)
        self.line_5.setGeometry(QtCore.QRect(100, 360, 75, 3))
        self.line_5.setStyleSheet(_fromUtf8("#line_5{\n"
"color: white\n"
"}"))
        self.line_5.setFrameShadow(QtGui.QFrame.Plain)
        self.line_5.setLineWidth(4)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.line_6 = QtGui.QFrame(self.graphBackground)
        self.line_6.setGeometry(QtCore.QRect(225, 360, 75, 3))
        self.line_6.setStyleSheet(_fromUtf8("#line_6{\n"
"color: white\n"
"}"))
        self.line_6.setFrameShadow(QtGui.QFrame.Plain)
        self.line_6.setLineWidth(4)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.gateValveButton = QtGui.QPushButton(self.graphBackground)
        self.gateValveButton.setGeometry(QtCore.QRect(175, 336, 50, 50))
        self.gateValveButton.setStyleSheet(_fromUtf8("#gateValveButton{\n"
"  border-color: rgb(255, 255, 255);\n"
"  border-width: 4px;        \n"
"  border-style: solid;\n"
"  border-radius: 25px;\n"
"background: black;\n"
"}"))
        self.gateValveButton.setText(_fromUtf8(""))
        self.gateValveButton.setObjectName(_fromUtf8("gateValveButton"))
        self.gateValveStatus = QtGui.QLabel(self.graphBackground)
        self.gateValveStatus.setGeometry(QtCore.QRect(175, 286, 50, 50))
        self.gateValveStatus.setStyleSheet(_fromUtf8("#gateValveStatus{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"\n"
"qproperty-alignment: \'AlignVCenter | AlignHCenter\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.gateValveStatus.setObjectName(_fromUtf8("gateValveStatus"))
        self.gateValveLabel = QtGui.QLabel(self.graphBackground)
        self.gateValveLabel.setGeometry(QtCore.QRect(165, 378, 100, 50))
        self.gateValveLabel.setStyleSheet(_fromUtf8("#gateValveLabel{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"}"))
        self.gateValveLabel.setObjectName(_fromUtf8("gateValveLabel"))
        self.line_7 = QtGui.QFrame(self.graphBackground)
        self.line_7.setGeometry(QtCore.QRect(300, 360, 250, 3))
        self.line_7.setStyleSheet(_fromUtf8("#line_7{\n"
"color: white\n"
"}"))
        self.line_7.setFrameShadow(QtGui.QFrame.Plain)
        self.line_7.setLineWidth(4)
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.line_8 = QtGui.QFrame(self.graphBackground)
        self.line_8.setGeometry(QtCore.QRect(500, 460, 20, 100))
        self.line_8.setStyleSheet(_fromUtf8("#line_8{\n"
"color: white;\n"
"}"))
        self.line_8.setFrameShadow(QtGui.QFrame.Plain)
        self.line_8.setLineWidth(4)
        self.line_8.setFrameShape(QtGui.QFrame.VLine)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.line_9 = QtGui.QFrame(self.graphBackground)
        self.line_9.setGeometry(QtCore.QRect(500, 360, 20, 50))
        self.line_9.setStyleSheet(_fromUtf8("#line_9{\n"
"color: white\n"
"}"))
        self.line_9.setFrameShadow(QtGui.QFrame.Plain)
        self.line_9.setLineWidth(4)
        self.line_9.setFrameShape(QtGui.QFrame.VLine)
        self.line_9.setObjectName(_fromUtf8("line_9"))
        self.boatShutterButton = QtGui.QPushButton(self.graphBackground)
        self.boatShutterButton.setGeometry(QtCore.QRect(477, 400, 66, 66))
        self.boatShutterButton.setStyleSheet(_fromUtf8("#boatShutterButton{\n"
"image: url(:/Shutter/Closed3.png);\n"
"background: black;\n"
"}"))
        self.boatShutterButton.setText(_fromUtf8(""))
        self.boatShutterButton.setObjectName(_fromUtf8("boatShutterButton"))
        self.boatShutterStatus = QtGui.QLabel(self.graphBackground)
        self.boatShutterStatus.setGeometry(QtCore.QRect(410, 406, 50, 50))
        self.boatShutterStatus.setStyleSheet(_fromUtf8("#boatShutterStatus{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.boatShutterStatus.setObjectName(_fromUtf8("boatShutterStatus"))
        self.powerSupplyLabel = QtGui.QLabel(self.graphBackground)
        self.powerSupplyLabel.setGeometry(QtCore.QRect(490, 590, 140, 41))
        self.powerSupplyLabel.setStyleSheet(_fromUtf8("#powerSupplyLabel{\n"
"color: white;\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"}"))
        self.powerSupplyLabel.setObjectName(_fromUtf8("powerSupplyLabel"))
        self.pressureStatus = QtGui.QLabel(self.graphBackground)
        self.pressureStatus.setGeometry(QtCore.QRect(1060, 40, 100, 51))
        self.pressureStatus.setStyleSheet(_fromUtf8("#pressureStatus{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.pressureStatus.setObjectName(_fromUtf8("pressureStatus"))
        self.pressureLabel = QtGui.QLabel(self.graphBackground)
        self.pressureLabel.setGeometry(QtCore.QRect(890, 40, 150, 50))
        self.pressureLabel.setStyleSheet(_fromUtf8("#pressureLabel{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.pressureLabel.setObjectName(_fromUtf8("pressureLabel"))
        self.powerSupplyButton = QtGui.QPushButton(self.graphBackground)
        self.powerSupplyButton.setGeometry(QtCore.QRect(483, 530, 55, 55))
        self.powerSupplyButton.setStyleSheet(_fromUtf8("#powerSupplyButton{\n"
"\n"
"image:url(:/OnOff/Off2.png);\n"
"\n"
"  background: black;\n"
"}"))
        self.powerSupplyButton.setText(_fromUtf8(""))
        self.powerSupplyButton.setObjectName(_fromUtf8("powerSupplyButton"))
        self.turboPumpButton = QtGui.QPushButton(self.graphBackground)
        self.turboPumpButton.setGeometry(QtCore.QRect(73, 333, 56, 56))
        self.turboPumpButton.setStyleSheet(_fromUtf8("#turboPumpButton{\n"
"image:url(:/OnOff/Off2.png);\n"
"background: black;\n"
"}"))
        self.turboPumpButton.setText(_fromUtf8(""))
        self.turboPumpButton.setObjectName(_fromUtf8("turboPumpButton"))
        self.scrollPumpButton = QtGui.QPushButton(self.graphBackground)
        self.scrollPumpButton.setGeometry(QtCore.QRect(273, 530, 55, 55))
        self.scrollPumpButton.setStyleSheet(_fromUtf8("#scrollPumpButton{\n"
"image:url(:/OnOff/Off2.png);\n"
"background: black;\n"
"}"))
        self.scrollPumpButton.setText(_fromUtf8(""))
        self.scrollPumpButton.setObjectName(_fromUtf8("scrollPumpButton"))
        self.rateLabel = QtGui.QLabel(self.graphBackground)
        self.rateLabel.setGeometry(QtCore.QRect(890, 95, 150, 50))
        self.rateLabel.setStyleSheet(_fromUtf8("#rateLabel{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.rateLabel.setObjectName(_fromUtf8("rateLabel"))
        self.thicknessLabel = QtGui.QLabel(self.graphBackground)
        self.thicknessLabel.setGeometry(QtCore.QRect(890, 150, 150, 50))
        self.thicknessLabel.setStyleSheet(_fromUtf8("#thicknessLabel{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.thicknessLabel.setObjectName(_fromUtf8("thicknessLabel"))
        self.heliumValveButton = QtGui.QPushButton(self.graphBackground)
        self.heliumValveButton.setEnabled(True)
        self.heliumValveButton.setGeometry(QtCore.QRect(600, 336, 50, 50))
        self.heliumValveButton.setStyleSheet(_fromUtf8("#heliumValveButton{\n"
"  border-color: rgb(255, 255, 255);\n"
"  border-width: 4px;        \n"
"  border-style: solid;\n"
"  border-radius: 25px;\n"
" background: black;\n"
"}"))
        self.heliumValveButton.setText(_fromUtf8(""))
        self.heliumValveButton.setObjectName(_fromUtf8("heliumValveButton"))
        self.heliumValveStatus = QtGui.QLabel(self.graphBackground)
        self.heliumValveStatus.setGeometry(QtCore.QRect(573, 288, 100, 50))
        self.heliumValveStatus.setStyleSheet(_fromUtf8("#heliumValveStatus{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignHCenter\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.heliumValveStatus.setObjectName(_fromUtf8("heliumValveStatus"))
        self.pushChooseDir = QtGui.QPushButton(self.graphBackground)
        self.pushChooseDir.setGeometry(QtCore.QRect(100, 80, 139, 23))
        self.pushChooseDir.setObjectName(_fromUtf8("pushChooseDir"))
        self.pushConnect = QtGui.QPushButton(self.graphBackground)
        self.pushConnect.setGeometry(QtCore.QRect(100, 40, 139, 23))
        self.pushConnect.setObjectName(_fromUtf8("pushConnect"))
        self.line_12 = QtGui.QFrame(self.graphBackground)
        self.line_12.setGeometry(QtCore.QRect(900, 40, 300, 3))
        self.line_12.setStyleSheet(_fromUtf8("#line_12{\n"
"color: white\n"
"}"))
        self.line_12.setFrameShadow(QtGui.QFrame.Plain)
        self.line_12.setLineWidth(1)
        self.line_12.setFrameShape(QtGui.QFrame.HLine)
        self.line_12.setObjectName(_fromUtf8("line_12"))
        self.line_13 = QtGui.QFrame(self.graphBackground)
        self.line_13.setGeometry(QtCore.QRect(900, 260, 300, 3))
        self.line_13.setStyleSheet(_fromUtf8("#line_13{\n"
"color: white\n"
"}"))
        self.line_13.setFrameShadow(QtGui.QFrame.Plain)
        self.line_13.setLineWidth(1)
        self.line_13.setFrameShape(QtGui.QFrame.HLine)
        self.line_13.setObjectName(_fromUtf8("line_13"))
        self.line_14 = QtGui.QFrame(self.graphBackground)
        self.line_14.setGeometry(QtCore.QRect(900, 41, 1, 220))
        self.line_14.setStyleSheet(_fromUtf8("#line_14{\n"
"color: white;\n"
"}"))
        self.line_14.setFrameShadow(QtGui.QFrame.Plain)
        self.line_14.setLineWidth(1)
        self.line_14.setFrameShape(QtGui.QFrame.VLine)
        self.line_14.setObjectName(_fromUtf8("line_14"))
        self.line_15 = QtGui.QFrame(self.graphBackground)
        self.line_15.setGeometry(QtCore.QRect(1200, 41, 1, 221))
        self.line_15.setStyleSheet(_fromUtf8("#line_15{\n"
"color: white;\n"
"}"))
        self.line_15.setFrameShadow(QtGui.QFrame.Plain)
        self.line_15.setLineWidth(1)
        self.line_15.setFrameShape(QtGui.QFrame.VLine)
        self.line_15.setObjectName(_fromUtf8("line_15"))
        self.rateStatus = QtGui.QLabel(self.graphBackground)
        self.rateStatus.setGeometry(QtCore.QRect(1060, 95, 100, 51))
        self.rateStatus.setStyleSheet(_fromUtf8("#rateStatus{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.rateStatus.setObjectName(_fromUtf8("rateStatus"))
        self.thicknessStatus = QtGui.QLabel(self.graphBackground)
        self.thicknessStatus.setGeometry(QtCore.QRect(1060, 150, 100, 51))
        self.thicknessStatus.setStyleSheet(_fromUtf8("#thicknessStatus{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.thicknessStatus.setObjectName(_fromUtf8("thicknessStatus"))
        self.dvFileSelect = dataVaultFileSelectWidget(self.graphBackground)
        self.dvFileSelect.setGeometry(QtCore.QRect(530, 40, 256, 207))
        self.dvFileSelect.setObjectName(_fromUtf8("dvFileSelect"))
        self.textEdit = QtGui.QTextEdit(self.graphBackground)
        self.textEdit.setGeometry(QtCore.QRect(290, 40, 200, 63))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.nomPressInput = QtGui.QLineEdit(self.graphBackground)
        self.nomPressInput.setGeometry(QtCore.QRect(910, 350, 113, 21))
        self.nomPressInput.setObjectName(_fromUtf8("nomPressInput"))
        self.nomPressLabel = QtGui.QLabel(self.graphBackground)
        self.nomPressLabel.setGeometry(QtCore.QRect(1130, 340, 151, 41))
        self.nomPressLabel.setStyleSheet(_fromUtf8("#nomPressLabel{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignCenter\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.nomPressLabel.setObjectName(_fromUtf8("nomPressLabel"))
        self.nomPress = QtGui.QLabel(self.graphBackground)
        self.nomPress.setGeometry(QtCore.QRect(750, 350, 141, 21))
        self.nomPress.setStyleSheet(_fromUtf8("#nomPress{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.nomPress.setObjectName(_fromUtf8("nomPress"))
        self.nomPressButton = QtGui.QPushButton(self.graphBackground)
        self.nomPressButton.setGeometry(QtCore.QRect(1040, 350, 81, 21))
        self.nomPressButton.setObjectName(_fromUtf8("nomPressButton"))
        self.nomPressFormat = QtGui.QLabel(self.graphBackground)
        self.nomPressFormat.setGeometry(QtCore.QRect(930, 310, 81, 21))
        self.nomPressFormat.setStyleSheet(_fromUtf8("#nomPressFormat{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.nomPressFormat.setObjectName(_fromUtf8("nomPressFormat"))
        self.line_16 = QtGui.QFrame(self.graphBackground)
        self.line_16.setGeometry(QtCore.QRect(100, 507, 200, 3))
        self.line_16.setStyleSheet(_fromUtf8("#line_16{\n"
"color: white\n"
"}"))
        self.line_16.setFrameShadow(QtGui.QFrame.Plain)
        self.line_16.setLineWidth(4)
        self.line_16.setFrameShape(QtGui.QFrame.HLine)
        self.line_16.setObjectName(_fromUtf8("line_16"))
        self.shutterWarning = QtGui.QLabel(self.graphBackground)
        self.shutterWarning.setGeometry(QtCore.QRect(560, 390, 251, 81))
        self.shutterWarning.setStyleSheet(_fromUtf8("#shutterWarning{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignLeft\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.shutterWarning.setObjectName(_fromUtf8("shutterWarning"))
        self.line_10 = QtGui.QFrame(self.graphBackground)
        self.line_10.setGeometry(QtCore.QRect(550, 360, 50, 3))
        self.line_10.setStyleSheet(_fromUtf8("#line_10{\n"
"color: white\n"
"}"))
        self.line_10.setFrameShadow(QtGui.QFrame.Plain)
        self.line_10.setLineWidth(4)
        self.line_10.setFrameShape(QtGui.QFrame.HLine)
        self.line_10.setObjectName(_fromUtf8("line_10"))
        self.voltageStatus = QtGui.QLabel(self.graphBackground)
        self.voltageStatus.setGeometry(QtCore.QRect(1060, 205, 100, 51))
        self.voltageStatus.setStyleSheet(_fromUtf8("#voltageStatus{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.voltageStatus.setObjectName(_fromUtf8("voltageStatus"))
        self.voltageLabel = QtGui.QLabel(self.graphBackground)
        self.voltageLabel.setGeometry(QtCore.QRect(890, 205, 150, 50))
        self.voltageLabel.setStyleSheet(_fromUtf8("#voltageLabel{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.voltageLabel.setObjectName(_fromUtf8("voltageLabel"))
        self.tabWidget.addTab(self.GraphicalInterface, _fromUtf8(""))
        self.Plotting = QtGui.QWidget()
        self.Plotting.setStyleSheet(_fromUtf8(""))
        self.Plotting.setObjectName(_fromUtf8("Plotting"))
        self.sliderGraph = QtGui.QSlider(self.Plotting)
        self.sliderGraph.setGeometry(QtCore.QRect(540, 70, 180, 30))
        self.sliderGraph.setOrientation(QtCore.Qt.Horizontal)
        self.sliderGraph.setObjectName(_fromUtf8("sliderGraph"))
        self.sliderLCD = QtGui.QLCDNumber(self.Plotting)
        self.sliderLCD.setGeometry(QtCore.QRect(740, 60, 70, 40))
        self.sliderLCD.setObjectName(_fromUtf8("sliderLCD"))
        self.detailsBackground = QtGui.QFrame(self.Plotting)
        self.detailsBackground.setGeometry(QtCore.QRect(0, 0, 1294, 674))
        self.detailsBackground.setStyleSheet(_fromUtf8("#detailsBackground{\n"
"background: rgb(0,0, 0)\n"
"}\n"
""))
        self.detailsBackground.setFrameShape(QtGui.QFrame.StyledPanel)
        self.detailsBackground.setFrameShadow(QtGui.QFrame.Raised)
        self.detailsBackground.setObjectName(_fromUtf8("detailsBackground"))
        self.numPointsLabel = QtGui.QLabel(self.detailsBackground)
        self.numPointsLabel.setGeometry(QtCore.QRect(390, 70, 131, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.numPointsLabel.setFont(font)
        self.numPointsLabel.setStyleSheet(_fromUtf8("#numPointsLabel{\n"
"color: rgb(212, 212, 212)\n"
"}\n"
""))
        self.numPointsLabel.setObjectName(_fromUtf8("numPointsLabel"))
        self.comboGraph = QtGui.QComboBox(self.detailsBackground)
        self.comboGraph.setGeometry(QtCore.QRect(40, 100, 140, 22))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboGraph.sizePolicy().hasHeightForWidth())
        self.comboGraph.setSizePolicy(sizePolicy)
        self.comboGraph.setObjectName(_fromUtf8("comboGraph"))
        self.comboGraph2 = QtGui.QComboBox(self.detailsBackground)
        self.comboGraph2.setGeometry(QtCore.QRect(40, 380, 140, 22))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboGraph2.sizePolicy().hasHeightForWidth())
        self.comboGraph2.setSizePolicy(sizePolicy)
        self.comboGraph2.setObjectName(_fromUtf8("comboGraph2"))
        self.plot2 = PlotWidget(self.detailsBackground)
        self.plot2.setGeometry(QtCore.QRect(40, 380, 1200, 275))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot2.sizePolicy().hasHeightForWidth())
        self.plot2.setSizePolicy(sizePolicy)
        self.plot2.setObjectName(_fromUtf8("plot2"))
        self.Live_Plotter = QtGui.QLabel(self.detailsBackground)
        self.Live_Plotter.setGeometry(QtCore.QRect(520, 20, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Live_Plotter.setFont(font)
        self.Live_Plotter.setStyleSheet(_fromUtf8("#Live_Plotter{\n"
"color: rgb(212, 212, 212)\n"
"}"))
        self.Live_Plotter.setObjectName(_fromUtf8("Live_Plotter"))
        self.plot = PlotWidget(self.detailsBackground)
        self.plot.setGeometry(QtCore.QRect(40, 100, 1200, 275))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot.sizePolicy().hasHeightForWidth())
        self.plot.setSizePolicy(sizePolicy)
        self.plot.setObjectName(_fromUtf8("plot"))
        self.comboAxes = QtGui.QComboBox(self.detailsBackground)
        self.comboAxes.setGeometry(QtCore.QRect(1100, 100, 140, 22))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboAxes.sizePolicy().hasHeightForWidth())
        self.comboAxes.setSizePolicy(sizePolicy)
        self.comboAxes.setStyleSheet(_fromUtf8("#comboAxes{\n"
"color: black;\n"
"}"))
        self.comboAxes.setObjectName(_fromUtf8("comboAxes"))
        self.comboAxes.addItem(_fromUtf8(""))
        self.comboAxes.addItem(_fromUtf8(""))
        self.comboAxes.addItem(_fromUtf8(""))
        self.comboAxes.addItem(_fromUtf8(""))
        self.comboAxes2 = QtGui.QComboBox(self.detailsBackground)
        self.comboAxes2.setGeometry(QtCore.QRect(1100, 380, 140, 22))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboAxes2.sizePolicy().hasHeightForWidth())
        self.comboAxes2.setSizePolicy(sizePolicy)
        self.comboAxes2.setObjectName(_fromUtf8("comboAxes2"))
        self.comboAxes2.addItem(_fromUtf8(""))
        self.comboAxes2.addItem(_fromUtf8(""))
        self.comboAxes2.addItem(_fromUtf8(""))
        self.comboAxes2.addItem(_fromUtf8(""))
        self.plot2.raise_()
        self.plot.raise_()
        self.numPointsLabel.raise_()
        self.comboGraph.raise_()
        self.comboGraph2.raise_()
        self.Live_Plotter.raise_()
        self.comboAxes.raise_()
        self.comboAxes2.raise_()
        self.detailsBackground.raise_()
        self.sliderGraph.raise_()
        self.sliderLCD.raise_()
        self.tabWidget.addTab(self.Plotting, _fromUtf8(""))
        self.DataCollector = QtGui.QWidget()
        self.DataCollector.setObjectName(_fromUtf8("DataCollector"))
        self.dataCollectorWidget = dataCollectorWidget(self.DataCollector)
        self.dataCollectorWidget.setGeometry(QtCore.QRect(0, 0, 1294, 674))
        self.dataCollectorWidget.setObjectName(_fromUtf8("dataCollectorWidget"))
        self.tabWidget.addTab(self.DataCollector, _fromUtf8(""))
        self.EvapControl = QtGui.QWidget()
        self.EvapControl.setObjectName(_fromUtf8("EvapControl"))
        self.evapBackground = QtGui.QFrame(self.EvapControl)
        self.evapBackground.setGeometry(QtCore.QRect(0, 0, 1294, 674))
        self.evapBackground.setStyleSheet(_fromUtf8("#evapBackground{\n"
"background: rgb(0,0, 0)\n"
"}\n"
""))
        self.evapBackground.setFrameShape(QtGui.QFrame.StyledPanel)
        self.evapBackground.setFrameShadow(QtGui.QFrame.Raised)
        self.evapBackground.setObjectName(_fromUtf8("evapBackground"))
        self.setPointInput = QtGui.QLineEdit(self.evapBackground)
        self.setPointInput.setGeometry(QtCore.QRect(590, 110, 113, 21))
        self.setPointInput.setObjectName(_fromUtf8("setPointInput"))
        self.setPointButton = QtGui.QPushButton(self.evapBackground)
        self.setPointButton.setGeometry(QtCore.QRect(730, 110, 101, 21))
        self.setPointButton.setObjectName(_fromUtf8("setPointButton"))
        self.evapStartButton = QtGui.QPushButton(self.evapBackground)
        self.evapStartButton.setGeometry(QtCore.QRect(800, 390, 100, 21))
        self.evapStartButton.setObjectName(_fromUtf8("evapStartButton"))
        self.setPointLabel = QtGui.QLabel(self.evapBackground)
        self.setPointLabel.setGeometry(QtCore.QRect(830, 110, 47, 21))
        self.setPointLabel.setStyleSheet(_fromUtf8("#setPointLabel{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.setPointLabel.setObjectName(_fromUtf8("setPointLabel"))
        self.Feedback = QtGui.QLabel(self.evapBackground)
        self.Feedback.setGeometry(QtCore.QRect(130, 330, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Feedback.setFont(font)
        self.Feedback.setStyleSheet(_fromUtf8("#Feedback{\n"
"color: rgb(212, 212, 212)\n"
"}"))
        self.Feedback.setObjectName(_fromUtf8("Feedback"))
        self.rateUnits = QtGui.QLabel(self.evapBackground)
        self.rateUnits.setGeometry(QtCore.QRect(890, 110, 47, 21))
        self.rateUnits.setStyleSheet(_fromUtf8("#rateUnits{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignLeft\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.rateUnits.setObjectName(_fromUtf8("rateUnits"))
        self.propInput = QtGui.QLineEdit(self.evapBackground)
        self.propInput.setGeometry(QtCore.QRect(150, 390, 113, 21))
        self.propInput.setObjectName(_fromUtf8("propInput"))
        self.propButton = QtGui.QPushButton(self.evapBackground)
        self.propButton.setGeometry(QtCore.QRect(290, 390, 101, 21))
        self.propButton.setObjectName(_fromUtf8("propButton"))
        self.propStatus = QtGui.QLabel(self.evapBackground)
        self.propStatus.setGeometry(QtCore.QRect(400, 390, 71, 21))
        self.propStatus.setStyleSheet(_fromUtf8("#propStatus{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignCenter\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.propStatus.setObjectName(_fromUtf8("propStatus"))
        self.propLabel = QtGui.QLabel(self.evapBackground)
        self.propLabel.setGeometry(QtCore.QRect(-30, 390, 150, 21))
        self.propLabel.setStyleSheet(_fromUtf8("#propLabel{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.propLabel.setObjectName(_fromUtf8("propLabel"))
        self.intStatus = QtGui.QLabel(self.evapBackground)
        self.intStatus.setGeometry(QtCore.QRect(400, 430, 71, 21))
        self.intStatus.setStyleSheet(_fromUtf8("#intStatus{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignCenter\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.intStatus.setObjectName(_fromUtf8("intStatus"))
        self.intButton = QtGui.QPushButton(self.evapBackground)
        self.intButton.setGeometry(QtCore.QRect(290, 430, 101, 21))
        self.intButton.setObjectName(_fromUtf8("intButton"))
        self.intLabel = QtGui.QLabel(self.evapBackground)
        self.intLabel.setGeometry(QtCore.QRect(-30, 430, 150, 21))
        self.intLabel.setStyleSheet(_fromUtf8("#intLabel{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.intLabel.setObjectName(_fromUtf8("intLabel"))
        self.intInput = QtGui.QLineEdit(self.evapBackground)
        self.intInput.setGeometry(QtCore.QRect(150, 430, 113, 21))
        self.intInput.setObjectName(_fromUtf8("intInput"))
        self.derivStatus = QtGui.QLabel(self.evapBackground)
        self.derivStatus.setGeometry(QtCore.QRect(400, 550, 71, 21))
        self.derivStatus.setStyleSheet(_fromUtf8("#derivStatus{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignCenter\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.derivStatus.setObjectName(_fromUtf8("derivStatus"))
        self.derivButton = QtGui.QPushButton(self.evapBackground)
        self.derivButton.setGeometry(QtCore.QRect(290, 550, 101, 21))
        self.derivButton.setObjectName(_fromUtf8("derivButton"))
        self.derivLabel = QtGui.QLabel(self.evapBackground)
        self.derivLabel.setGeometry(QtCore.QRect(-30, 550, 150, 21))
        self.derivLabel.setStyleSheet(_fromUtf8("#derivLabel{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.derivLabel.setObjectName(_fromUtf8("derivLabel"))
        self.derivInput = QtGui.QLineEdit(self.evapBackground)
        self.derivInput.setGeometry(QtCore.QRect(150, 550, 113, 21))
        self.derivInput.setObjectName(_fromUtf8("derivInput"))
        self.intMaxInput = QtGui.QLineEdit(self.evapBackground)
        self.intMaxInput.setGeometry(QtCore.QRect(150, 470, 113, 21))
        self.intMaxInput.setObjectName(_fromUtf8("intMaxInput"))
        self.intMaxStatus = QtGui.QLabel(self.evapBackground)
        self.intMaxStatus.setGeometry(QtCore.QRect(400, 470, 71, 21))
        self.intMaxStatus.setStyleSheet(_fromUtf8("#intMaxStatus{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignCenter\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.intMaxStatus.setObjectName(_fromUtf8("intMaxStatus"))
        self.intMaxLabel = QtGui.QLabel(self.evapBackground)
        self.intMaxLabel.setGeometry(QtCore.QRect(-30, 470, 150, 21))
        self.intMaxLabel.setStyleSheet(_fromUtf8("#intMaxLabel{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.intMaxLabel.setObjectName(_fromUtf8("intMaxLabel"))
        self.intMaxButton = QtGui.QPushButton(self.evapBackground)
        self.intMaxButton.setGeometry(QtCore.QRect(290, 470, 101, 21))
        self.intMaxButton.setObjectName(_fromUtf8("intMaxButton"))
        self.intMinInput = QtGui.QLineEdit(self.evapBackground)
        self.intMinInput.setGeometry(QtCore.QRect(150, 510, 113, 21))
        self.intMinInput.setObjectName(_fromUtf8("intMinInput"))
        self.intMinStatus = QtGui.QLabel(self.evapBackground)
        self.intMinStatus.setGeometry(QtCore.QRect(400, 510, 71, 21))
        self.intMinStatus.setStyleSheet(_fromUtf8("#intMinStatus{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignCenter\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.intMinStatus.setObjectName(_fromUtf8("intMinStatus"))
        self.intMinLabel = QtGui.QLabel(self.evapBackground)
        self.intMinLabel.setGeometry(QtCore.QRect(-30, 510, 150, 21))
        self.intMinLabel.setStyleSheet(_fromUtf8("#intMinLabel{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.intMinLabel.setObjectName(_fromUtf8("intMinLabel"))
        self.intMinButton = QtGui.QPushButton(self.evapBackground)
        self.intMinButton.setGeometry(QtCore.QRect(290, 510, 101, 21))
        self.intMinButton.setObjectName(_fromUtf8("intMinButton"))
        self.textEdit2 = QtGui.QTextEdit(self.evapBackground)
        self.textEdit2.setGeometry(QtCore.QRect(770, 20, 491, 71))
        self.textEdit2.setStyleSheet(_fromUtf8("#textEdit2{\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"}"))
        self.textEdit2.setObjectName(_fromUtf8("textEdit2"))
        self.deposRate = QtGui.QLabel(self.evapBackground)
        self.deposRate.setGeometry(QtCore.QRect(380, 110, 201, 21))
        self.deposRate.setStyleSheet(_fromUtf8("#deposRate{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.deposRate.setObjectName(_fromUtf8("deposRate"))
        self.note = QtGui.QLabel(self.evapBackground)
        self.note.setGeometry(QtCore.QRect(480, 530, 221, 81))
        self.note.setStyleSheet(_fromUtf8("#note{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignLeft\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.note.setObjectName(_fromUtf8("note"))
        self.evapStatus = QtGui.QLabel(self.evapBackground)
        self.evapStatus.setGeometry(QtCore.QRect(750, 430, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.evapStatus.setFont(font)
        self.evapStatus.setStyleSheet(_fromUtf8("#evapStatus{\n"
"color: rgb(212, 212, 212);\n"
"qproperty-alignment: \'AlignVCenter | AlignCenter\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.evapStatus.setObjectName(_fromUtf8("evapStatus"))
        self.vMaxButton = QtGui.QPushButton(self.evapBackground)
        self.vMaxButton.setGeometry(QtCore.QRect(290, 590, 101, 21))
        self.vMaxButton.setObjectName(_fromUtf8("vMaxButton"))
        self.vMaxLabel = QtGui.QLabel(self.evapBackground)
        self.vMaxLabel.setGeometry(QtCore.QRect(-30, 590, 150, 21))
        self.vMaxLabel.setStyleSheet(_fromUtf8("#vMaxLabel{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.vMaxLabel.setObjectName(_fromUtf8("vMaxLabel"))
        self.vMaxInput = QtGui.QLineEdit(self.evapBackground)
        self.vMaxInput.setGeometry(QtCore.QRect(150, 590, 113, 21))
        self.vMaxInput.setObjectName(_fromUtf8("vMaxInput"))
        self.vMaxStatus = QtGui.QLabel(self.evapBackground)
        self.vMaxStatus.setGeometry(QtCore.QRect(400, 590, 71, 21))
        self.vMaxStatus.setStyleSheet(_fromUtf8("#vMaxStatus{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignCenter\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.vMaxStatus.setObjectName(_fromUtf8("vMaxStatus"))
        self.vOffLabel = QtGui.QLabel(self.evapBackground)
        self.vOffLabel.setGeometry(QtCore.QRect(-30, 630, 150, 21))
        self.vOffLabel.setStyleSheet(_fromUtf8("#vOffLabel{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.vOffLabel.setObjectName(_fromUtf8("vOffLabel"))
        self.vOffButton = QtGui.QPushButton(self.evapBackground)
        self.vOffButton.setGeometry(QtCore.QRect(290, 630, 101, 21))
        self.vOffButton.setObjectName(_fromUtf8("vOffButton"))
        self.vOffStatus = QtGui.QLabel(self.evapBackground)
        self.vOffStatus.setGeometry(QtCore.QRect(400, 630, 71, 21))
        self.vOffStatus.setStyleSheet(_fromUtf8("#vOffStatus{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignCenter\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.vOffStatus.setObjectName(_fromUtf8("vOffStatus"))
        self.vOffInput = QtGui.QLineEdit(self.evapBackground)
        self.vOffInput.setGeometry(QtCore.QRect(150, 630, 113, 21))
        self.vOffInput.setObjectName(_fromUtf8("vOffInput"))
        self.shutterInput = QtGui.QLineEdit(self.evapBackground)
        self.shutterInput.setGeometry(QtCore.QRect(911, 580, 113, 21))
        self.shutterInput.setObjectName(_fromUtf8("shutterInput"))
        self.shutterCWButton = QtGui.QPushButton(self.evapBackground)
        self.shutterCWButton.setGeometry(QtCore.QRect(1051, 580, 101, 21))
        self.shutterCWButton.setObjectName(_fromUtf8("shutterCWButton"))
        self.shutterLabel = QtGui.QLabel(self.evapBackground)
        self.shutterLabel.setGeometry(QtCore.QRect(710, 580, 171, 21))
        self.shutterLabel.setStyleSheet(_fromUtf8("#shutterLabel{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.shutterLabel.setObjectName(_fromUtf8("shutterLabel"))
        self.shutterCCWButton = QtGui.QPushButton(self.evapBackground)
        self.shutterCCWButton.setGeometry(QtCore.QRect(1180, 580, 101, 21))
        self.shutterCCWButton.setObjectName(_fromUtf8("shutterCCWButton"))
        self.cryoLabel = QtGui.QLabel(self.evapBackground)
        self.cryoLabel.setGeometry(QtCore.QRect(710, 620, 171, 21))
        self.cryoLabel.setStyleSheet(_fromUtf8("#cryoLabel{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.cryoLabel.setObjectName(_fromUtf8("cryoLabel"))
        self.cryoCCWButton = QtGui.QPushButton(self.evapBackground)
        self.cryoCCWButton.setGeometry(QtCore.QRect(1180, 620, 101, 21))
        self.cryoCCWButton.setObjectName(_fromUtf8("cryoCCWButton"))
        self.cryoInput = QtGui.QLineEdit(self.evapBackground)
        self.cryoInput.setGeometry(QtCore.QRect(911, 620, 113, 21))
        self.cryoInput.setObjectName(_fromUtf8("cryoInput"))
        self.cryoCWButton = QtGui.QPushButton(self.evapBackground)
        self.cryoCWButton.setGeometry(QtCore.QRect(1051, 620, 101, 21))
        self.cryoCWButton.setObjectName(_fromUtf8("cryoCWButton"))
        self.Manual = QtGui.QLabel(self.evapBackground)
        self.Manual.setGeometry(QtCore.QRect(770, 330, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Manual.setFont(font)
        self.Manual.setStyleSheet(_fromUtf8("#Manual{\n"
"color: rgb(212, 212, 212)\n"
"}"))
        self.Manual.setObjectName(_fromUtf8("Manual"))
        self.Auto = QtGui.QLabel(self.evapBackground)
        self.Auto.setGeometry(QtCore.QRect(80, 40, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Auto.setFont(font)
        self.Auto.setStyleSheet(_fromUtf8("#Auto{\n"
"color: rgb(212, 212, 212)\n"
"}"))
        self.Auto.setObjectName(_fromUtf8("Auto"))
        self.thicknessStatus_2 = QtGui.QLabel(self.evapBackground)
        self.thicknessStatus_2.setGeometry(QtCore.QRect(590, 410, 100, 51))
        self.thicknessStatus_2.setStyleSheet(_fromUtf8("#thicknessStatus_2{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.thicknessStatus_2.setObjectName(_fromUtf8("thicknessStatus_2"))
        self.rateStatus_2 = QtGui.QLabel(self.evapBackground)
        self.rateStatus_2.setGeometry(QtCore.QRect(590, 365, 100, 51))
        self.rateStatus_2.setStyleSheet(_fromUtf8("#rateStatus_2{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.rateStatus_2.setObjectName(_fromUtf8("rateStatus_2"))
        self.rateLabel_2 = QtGui.QLabel(self.evapBackground)
        self.rateLabel_2.setGeometry(QtCore.QRect(420, 365, 150, 50))
        self.rateLabel_2.setStyleSheet(_fromUtf8("#rateLabel_2{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.rateLabel_2.setObjectName(_fromUtf8("rateLabel_2"))
        self.thicknessLabel_2 = QtGui.QLabel(self.evapBackground)
        self.thicknessLabel_2.setGeometry(QtCore.QRect(420, 410, 150, 50))
        self.thicknessLabel_2.setStyleSheet(_fromUtf8("#thicknessLabel_2{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.thicknessLabel_2.setObjectName(_fromUtf8("thicknessLabel_2"))
        self.pressureStatus_2 = QtGui.QLabel(self.evapBackground)
        self.pressureStatus_2.setGeometry(QtCore.QRect(590, 320, 100, 51))
        self.pressureStatus_2.setStyleSheet(_fromUtf8("#pressureStatus_2{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.pressureStatus_2.setObjectName(_fromUtf8("pressureStatus_2"))
        self.pressureLabel_2 = QtGui.QLabel(self.evapBackground)
        self.pressureLabel_2.setGeometry(QtCore.QRect(420, 320, 150, 50))
        self.pressureLabel_2.setStyleSheet(_fromUtf8("#pressureLabel_2{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.pressureLabel_2.setObjectName(_fromUtf8("pressureLabel_2"))
        self.emergStop = QtGui.QPushButton(self.evapBackground)
        self.emergStop.setGeometry(QtCore.QRect(600, 30, 91, 51))
        self.emergStop.setStyleSheet(_fromUtf8("#emergStop{\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"border-width: 0px;        \n"
"border-style: solid;\n"
"border-radius: 20px;\n"
"background: red;\n"
"color: rgb(212,212,212)\n"
"}"))
        self.emergStop.setObjectName(_fromUtf8("emergStop"))
        self.angleStatus = QtGui.QLabel(self.evapBackground)
        self.angleStatus.setGeometry(QtCore.QRect(1150, 150, 71, 21))
        self.angleStatus.setStyleSheet(_fromUtf8("#angleStatus{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignCenter\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.angleStatus.setObjectName(_fromUtf8("angleStatus"))
        self.angleButton = QtGui.QPushButton(self.evapBackground)
        self.angleButton.setGeometry(QtCore.QRect(1040, 150, 101, 21))
        self.angleButton.setObjectName(_fromUtf8("angleButton"))
        self.angleLabel = QtGui.QLabel(self.evapBackground)
        self.angleLabel.setGeometry(QtCore.QRect(730, 150, 150, 21))
        self.angleLabel.setStyleSheet(_fromUtf8("#angleLabel{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.angleLabel.setObjectName(_fromUtf8("angleLabel"))
        self.angleInput = QtGui.QLineEdit(self.evapBackground)
        self.angleInput.setGeometry(QtCore.QRect(900, 150, 113, 21))
        self.angleInput.setObjectName(_fromUtf8("angleInput"))
        self.contactThkStatus = QtGui.QLabel(self.evapBackground)
        self.contactThkStatus.setGeometry(QtCore.QRect(1150, 195, 71, 21))
        self.contactThkStatus.setStyleSheet(_fromUtf8("#contactThkStatus{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignCenter\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.contactThkStatus.setObjectName(_fromUtf8("contactThkStatus"))
        self.contactThkInput = QtGui.QLineEdit(self.evapBackground)
        self.contactThkInput.setGeometry(QtCore.QRect(900, 195, 113, 21))
        self.contactThkInput.setObjectName(_fromUtf8("contactThkInput"))
        self.contactThkButton = QtGui.QPushButton(self.evapBackground)
        self.contactThkButton.setGeometry(QtCore.QRect(1040, 195, 101, 21))
        self.contactThkButton.setObjectName(_fromUtf8("contactThkButton"))
        self.contactThkLabel = QtGui.QLabel(self.evapBackground)
        self.contactThkLabel.setGeometry(QtCore.QRect(730, 195, 150, 21))
        self.contactThkLabel.setStyleSheet(_fromUtf8("#contactThkLabel{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.contactThkLabel.setObjectName(_fromUtf8("contactThkLabel"))
        self.startAuto = QtGui.QPushButton(self.evapBackground)
        self.startAuto.setGeometry(QtCore.QRect(420, 30, 91, 51))
        self.startAuto.setStyleSheet(_fromUtf8("#startAuto{\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"border-width: 0px;        \n"
"border-style: solid;\n"
"border-radius: 20px;\n"
"background: green;\n"
"color: rgb(212,212,212)\n"
"}"))
        self.startAuto.setObjectName(_fromUtf8("startAuto"))
        self.contactThkUnits = QtGui.QLabel(self.evapBackground)
        self.contactThkUnits.setGeometry(QtCore.QRect(1210, 195, 47, 21))
        self.contactThkUnits.setStyleSheet(_fromUtf8("#contactThkUnits{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignLeft\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.contactThkUnits.setObjectName(_fromUtf8("contactThkUnits"))
        self.contactAngleUnits = QtGui.QLabel(self.evapBackground)
        self.contactAngleUnits.setGeometry(QtCore.QRect(1210, 150, 47, 21))
        self.contactAngleUnits.setStyleSheet(_fromUtf8("#contactAngleUnits{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignLeft\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.contactAngleUnits.setObjectName(_fromUtf8("contactAngleUnits"))
        self.headThkUnits = QtGui.QLabel(self.evapBackground)
        self.headThkUnits.setGeometry(QtCore.QRect(1210, 240, 47, 21))
        self.headThkUnits.setStyleSheet(_fromUtf8("#headThkUnits{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignLeft\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.headThkUnits.setObjectName(_fromUtf8("headThkUnits"))
        self.headThkButton = QtGui.QPushButton(self.evapBackground)
        self.headThkButton.setGeometry(QtCore.QRect(1040, 240, 101, 21))
        self.headThkButton.setObjectName(_fromUtf8("headThkButton"))
        self.headThkLabel = QtGui.QLabel(self.evapBackground)
        self.headThkLabel.setGeometry(QtCore.QRect(730, 240, 150, 21))
        self.headThkLabel.setStyleSheet(_fromUtf8("#headThkLabel{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.headThkLabel.setObjectName(_fromUtf8("headThkLabel"))
        self.headThkStatus = QtGui.QLabel(self.evapBackground)
        self.headThkStatus.setGeometry(QtCore.QRect(1150, 240, 71, 21))
        self.headThkStatus.setStyleSheet(_fromUtf8("#headThkStatus{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignCenter\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.headThkStatus.setObjectName(_fromUtf8("headThkStatus"))
        self.headThkInput = QtGui.QLineEdit(self.evapBackground)
        self.headThkInput.setGeometry(QtCore.QRect(900, 240, 113, 21))
        self.headThkInput.setObjectName(_fromUtf8("headThkInput"))
        self.line_34 = QtGui.QFrame(self.evapBackground)
        self.line_34.setGeometry(QtCore.QRect(710, 311, 1, 363))
        self.line_34.setStyleSheet(_fromUtf8("#line_34{\n"
"color: white;\n"
"}"))
        self.line_34.setFrameShadow(QtGui.QFrame.Plain)
        self.line_34.setLineWidth(1)
        self.line_34.setFrameShape(QtGui.QFrame.VLine)
        self.line_34.setObjectName(_fromUtf8("line_34"))
        self.line_21 = QtGui.QFrame(self.evapBackground)
        self.line_21.setGeometry(QtCore.QRect(470, 510, 240, 3))
        self.line_21.setStyleSheet(_fromUtf8("#line_21{\n"
"color: white\n"
"}"))
        self.line_21.setFrameShadow(QtGui.QFrame.Plain)
        self.line_21.setLineWidth(1)
        self.line_21.setFrameShape(QtGui.QFrame.HLine)
        self.line_21.setObjectName(_fromUtf8("line_21"))
        self.thermTimeUnits = QtGui.QLabel(self.evapBackground)
        self.thermTimeUnits.setGeometry(QtCore.QRect(530, 150, 47, 21))
        self.thermTimeUnits.setStyleSheet(_fromUtf8("#thermTimeUnits{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignLeft\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.thermTimeUnits.setObjectName(_fromUtf8("thermTimeUnits"))
        self.thermTimeInput = QtGui.QLineEdit(self.evapBackground)
        self.thermTimeInput.setGeometry(QtCore.QRect(230, 150, 113, 21))
        self.thermTimeInput.setObjectName(_fromUtf8("thermTimeInput"))
        self.thermTimeButton = QtGui.QPushButton(self.evapBackground)
        self.thermTimeButton.setGeometry(QtCore.QRect(370, 150, 101, 21))
        self.thermTimeButton.setObjectName(_fromUtf8("thermTimeButton"))
        self.thermTimeStatusLabel = QtGui.QLabel(self.evapBackground)
        self.thermTimeStatusLabel.setGeometry(QtCore.QRect(470, 150, 47, 21))
        self.thermTimeStatusLabel.setStyleSheet(_fromUtf8("#thermTimeStatusLabel{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.thermTimeStatusLabel.setObjectName(_fromUtf8("thermTimeStatusLabel"))
        self.thermTimeLabel = QtGui.QLabel(self.evapBackground)
        self.thermTimeLabel.setGeometry(QtCore.QRect(20, 150, 201, 21))
        self.thermTimeLabel.setStyleSheet(_fromUtf8("#thermTimeLabel{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.thermTimeLabel.setObjectName(_fromUtf8("thermTimeLabel"))
        self.nomPressFormat_2 = QtGui.QLabel(self.evapBackground)
        self.nomPressFormat_2.setGeometry(QtCore.QRect(920, 500, 81, 21))
        self.nomPressFormat_2.setStyleSheet(_fromUtf8("#nomPressFormat_2{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.nomPressFormat_2.setObjectName(_fromUtf8("nomPressFormat_2"))
        self.nomPress_2 = QtGui.QLabel(self.evapBackground)
        self.nomPress_2.setGeometry(QtCore.QRect(750, 540, 141, 21))
        self.nomPress_2.setStyleSheet(_fromUtf8("#nomPress_2{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.nomPress_2.setObjectName(_fromUtf8("nomPress_2"))
        self.nomPressInput_2 = QtGui.QLineEdit(self.evapBackground)
        self.nomPressInput_2.setGeometry(QtCore.QRect(910, 540, 113, 21))
        self.nomPressInput_2.setObjectName(_fromUtf8("nomPressInput_2"))
        self.nomPressLabel_2 = QtGui.QLabel(self.evapBackground)
        self.nomPressLabel_2.setGeometry(QtCore.QRect(1140, 530, 151, 41))
        self.nomPressLabel_2.setStyleSheet(_fromUtf8("#nomPressLabel_2{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignCenter\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.nomPressLabel_2.setObjectName(_fromUtf8("nomPressLabel_2"))
        self.nomPressButton_2 = QtGui.QPushButton(self.evapBackground)
        self.nomPressButton_2.setGeometry(QtCore.QRect(1060, 540, 81, 21))
        self.nomPressButton_2.setObjectName(_fromUtf8("nomPressButton_2"))
        self.boatShutterButton_2 = QtGui.QPushButton(self.evapBackground)
        self.boatShutterButton_2.setGeometry(QtCore.QRect(1060, 390, 66, 66))
        self.boatShutterButton_2.setStyleSheet(_fromUtf8("#boatShutterButton_2{\n"
"image: url(:/Shutter/Closed3.png);\n"
"background: black;\n"
"}"))
        self.boatShutterButton_2.setText(_fromUtf8(""))
        self.boatShutterButton_2.setObjectName(_fromUtf8("boatShutterButton_2"))
        self.heliumValveButton_2 = QtGui.QPushButton(self.evapBackground)
        self.heliumValveButton_2.setEnabled(True)
        self.heliumValveButton_2.setGeometry(QtCore.QRect(1190, 400, 50, 50))
        self.heliumValveButton_2.setStyleSheet(_fromUtf8("#heliumValveButton_2{\n"
"  border-color: rgb(255, 255, 255);\n"
"  border-width: 4px;        \n"
"  border-style: solid;\n"
"  border-radius: 25px;\n"
" background: black;\n"
"}"))
        self.heliumValveButton_2.setText(_fromUtf8(""))
        self.heliumValveButton_2.setObjectName(_fromUtf8("heliumValveButton_2"))
        self.thermPrsUnits = QtGui.QLabel(self.evapBackground)
        self.thermPrsUnits.setGeometry(QtCore.QRect(560, 240, 47, 21))
        self.thermPrsUnits.setStyleSheet(_fromUtf8("#thermPrsUnits{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignLeft\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.thermPrsUnits.setObjectName(_fromUtf8("thermPrsUnits"))
        self.thermPrsInput = QtGui.QLineEdit(self.evapBackground)
        self.thermPrsInput.setGeometry(QtCore.QRect(230, 240, 113, 21))
        self.thermPrsInput.setObjectName(_fromUtf8("thermPrsInput"))
        self.thermPrsLabel = QtGui.QLabel(self.evapBackground)
        self.thermPrsLabel.setGeometry(QtCore.QRect(20, 240, 201, 21))
        self.thermPrsLabel.setStyleSheet(_fromUtf8("#thermPrsLabel{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.thermPrsLabel.setObjectName(_fromUtf8("thermPrsLabel"))
        self.thermPrsStatusLabel = QtGui.QLabel(self.evapBackground)
        self.thermPrsStatusLabel.setGeometry(QtCore.QRect(480, 240, 71, 21))
        self.thermPrsStatusLabel.setStyleSheet(_fromUtf8("#thermPrsStatusLabel{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.thermPrsStatusLabel.setObjectName(_fromUtf8("thermPrsStatusLabel"))
        self.thermPrsButton = QtGui.QPushButton(self.evapBackground)
        self.thermPrsButton.setGeometry(QtCore.QRect(370, 240, 101, 21))
        self.thermPrsButton.setObjectName(_fromUtf8("thermPrsButton"))
        self.nomPressFormat_3 = QtGui.QLabel(self.evapBackground)
        self.nomPressFormat_3.setGeometry(QtCore.QRect(81, 273, 231, 21))
        self.nomPressFormat_3.setStyleSheet(_fromUtf8("#nomPressFormat_3{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.nomPressFormat_3.setObjectName(_fromUtf8("nomPressFormat_3"))
        self.voltageLabel_2 = QtGui.QLabel(self.evapBackground)
        self.voltageLabel_2.setGeometry(QtCore.QRect(420, 455, 150, 50))
        self.voltageLabel_2.setStyleSheet(_fromUtf8("#voltageLabel_2{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.voltageLabel_2.setObjectName(_fromUtf8("voltageLabel_2"))
        self.voltageStatus_2 = QtGui.QLabel(self.evapBackground)
        self.voltageStatus_2.setGeometry(QtCore.QRect(590, 455, 100, 51))
        self.voltageStatus_2.setStyleSheet(_fromUtf8("#voltageStatus_2{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.voltageStatus_2.setObjectName(_fromUtf8("voltageStatus_2"))
        self.thermTimeButton_2 = QtGui.QPushButton(self.evapBackground)
        self.thermTimeButton_2.setGeometry(QtCore.QRect(370, 195, 101, 21))
        self.thermTimeButton_2.setObjectName(_fromUtf8("thermTimeButton_2"))
        self.thermTimeUnits_2 = QtGui.QLabel(self.evapBackground)
        self.thermTimeUnits_2.setGeometry(QtCore.QRect(530, 195, 47, 21))
        self.thermTimeUnits_2.setStyleSheet(_fromUtf8("#thermTimeUnits_2{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignLeft\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.thermTimeUnits_2.setObjectName(_fromUtf8("thermTimeUnits_2"))
        self.thermTimeStatusLabel_2 = QtGui.QLabel(self.evapBackground)
        self.thermTimeStatusLabel_2.setGeometry(QtCore.QRect(470, 195, 47, 21))
        self.thermTimeStatusLabel_2.setStyleSheet(_fromUtf8("#thermTimeStatusLabel_2{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.thermTimeStatusLabel_2.setObjectName(_fromUtf8("thermTimeStatusLabel_2"))
        self.thermTimeInput_2 = QtGui.QLineEdit(self.evapBackground)
        self.thermTimeInput_2.setGeometry(QtCore.QRect(230, 195, 113, 21))
        self.thermTimeInput_2.setObjectName(_fromUtf8("thermTimeInput_2"))
        self.thermTimeLabel_2 = QtGui.QLabel(self.evapBackground)
        self.thermTimeLabel_2.setGeometry(QtCore.QRect(20, 195, 201, 21))
        self.thermTimeLabel_2.setStyleSheet(_fromUtf8("#thermTimeLabel_2{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.thermTimeLabel_2.setObjectName(_fromUtf8("thermTimeLabel_2"))
        self.zeroThkButton = QtGui.QPushButton(self.evapBackground)
        self.zeroThkButton.setGeometry(QtCore.QRect(1060, 500, 81, 23))
        self.zeroThkButton.setObjectName(_fromUtf8("zeroThkButton"))
        self.line_31 = QtGui.QFrame(self.EvapControl)
        self.line_31.setGeometry(QtCore.QRect(0, 310, 1294, 3))
        self.line_31.setStyleSheet(_fromUtf8("#line_31{\n"
"color: white\n"
"}"))
        self.line_31.setFrameShadow(QtGui.QFrame.Plain)
        self.line_31.setLineWidth(1)
        self.line_31.setFrameShape(QtGui.QFrame.HLine)
        self.line_31.setObjectName(_fromUtf8("line_31"))
        self.line_33 = QtGui.QFrame(self.EvapControl)
        self.line_33.setGeometry(QtCore.QRect(470, 311, 1, 363))
        self.line_33.setStyleSheet(_fromUtf8("#line_33{\n"
"color: white;\n"
"}"))
        self.line_33.setFrameShadow(QtGui.QFrame.Plain)
        self.line_33.setLineWidth(1)
        self.line_33.setFrameShape(QtGui.QFrame.VLine)
        self.line_33.setObjectName(_fromUtf8("line_33"))
        self.tabWidget.addTab(self.EvapControl, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Kickass Gui of the Year", None))
        self.scrollPumpLabel.setText(_translate("MainWindow", "Scroll Pump", None))
        self.scrollValveStatus.setText(_translate("MainWindow", "Closed", None))
        self.turboValveStatus.setText(_translate("MainWindow", "Closed", None))
        self.turboPumpLabel.setText(_translate("MainWindow", "Turbo Pump", None))
        self.gateValveStatus.setText(_translate("MainWindow", "Closed", None))
        self.gateValveLabel.setText(_translate("MainWindow", "Gate Valve", None))
        self.boatShutterStatus.setText(_translate("MainWindow", "Closed", None))
        self.powerSupplyLabel.setText(_translate("MainWindow", "Power Supply", None))
        self.pressureStatus.setText(_translate("MainWindow", "Not Initialized", None))
        self.pressureLabel.setText(_translate("MainWindow", "Pressure:", None))
        self.rateLabel.setText(_translate("MainWindow", "Deposition Rate:", None))
        self.thicknessLabel.setText(_translate("MainWindow", "Thickness:", None))
        self.heliumValveStatus.setText(_translate("MainWindow", "Closed", None))
        self.pushChooseDir.setText(_translate("MainWindow", "Select Directory", None))
        self.pushConnect.setText(_translate("MainWindow", "Connect to Servers", None))
        self.rateStatus.setText(_translate("MainWindow", "Not Initialized", None))
        self.thicknessStatus.setText(_translate("MainWindow", "Not Initialized", None))
        self.nomPressLabel.setText(_translate("MainWindow", "N/A", None))
        self.nomPress.setText(_translate("MainWindow", "Pressure Setpoint:", None))
        self.nomPressButton.setText(_translate("MainWindow", "Set Pressure", None))
        self.nomPressFormat.setText(_translate("MainWindow", "x.xxEsxx", None))
        self.shutterWarning.setText(_translate("MainWindow", "Make sure that shutter position matches GUI after reloading lead.", None))
        self.voltageStatus.setText(_translate("MainWindow", "Not Initialized", None))
        self.voltageLabel.setText(_translate("MainWindow", "Voltage:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.GraphicalInterface), _translate("MainWindow", "Graphical Interface", None))
        self.numPointsLabel.setText(_translate("MainWindow", "Number of Points:", None))
        self.Live_Plotter.setText(_translate("MainWindow", "Live Plotter", None))
        self.comboAxes.setItemText(0, _translate("MainWindow", "x vs. y", None))
        self.comboAxes.setItemText(1, _translate("MainWindow", "x vs. log(y)", None))
        self.comboAxes.setItemText(2, _translate("MainWindow", "log(x) vs. y", None))
        self.comboAxes.setItemText(3, _translate("MainWindow", "log(x) vs. log(y)", None))
        self.comboAxes2.setItemText(0, _translate("MainWindow", "x vs. y", None))
        self.comboAxes2.setItemText(1, _translate("MainWindow", "x vs. log(y)", None))
        self.comboAxes2.setItemText(2, _translate("MainWindow", "log(x) vs. y", None))
        self.comboAxes2.setItemText(3, _translate("MainWindow", "log(x) vs. log(y)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Plotting), _translate("MainWindow", "Plotting", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DataCollector), _translate("MainWindow", "Data Collector", None))
        self.setPointButton.setText(_translate("MainWindow", "Change Setpoint", None))
        self.evapStartButton.setText(_translate("MainWindow", "Start Evaporating", None))
        self.setPointLabel.setText(_translate("MainWindow", "5", None))
        self.Feedback.setText(_translate("MainWindow", "PID Settings", None))
        self.rateUnits.setText(_translate("MainWindow", "Å/s", None))
        self.propButton.setText(_translate("MainWindow", "Set Kp", None))
        self.propStatus.setText(_translate("MainWindow", "0", None))
        self.propLabel.setText(_translate("MainWindow", "Proportional:", None))
        self.intStatus.setText(_translate("MainWindow", "0.001", None))
        self.intButton.setText(_translate("MainWindow", "Set Ki", None))
        self.intLabel.setText(_translate("MainWindow", "Integral:", None))
        self.derivStatus.setText(_translate("MainWindow", "0", None))
        self.derivButton.setText(_translate("MainWindow", "Set Kd", None))
        self.derivLabel.setText(_translate("MainWindow", "Derivative:", None))
        self.intMaxStatus.setText(_translate("MainWindow", "500", None))
        self.intMaxLabel.setText(_translate("MainWindow", "Integral Max:", None))
        self.intMaxButton.setText(_translate("MainWindow", "Set Max", None))
        self.intMinStatus.setText(_translate("MainWindow", "-500", None))
        self.intMinLabel.setText(_translate("MainWindow", "Integral Min:", None))
        self.intMinButton.setText(_translate("MainWindow", "Set Min", None))
        self.deposRate.setText(_translate("MainWindow", "Desired Deposition Rate:", None))
        self.note.setText(_translate("MainWindow", "The deposition rate sampling rate (from data collector) determines the speed at which the PID updates the voltage. ", None))
        self.evapStatus.setText(_translate("MainWindow", "Standby", None))
        self.vMaxButton.setText(_translate("MainWindow", "Set V Max", None))
        self.vMaxLabel.setText(_translate("MainWindow", "Max Voltage:", None))
        self.vMaxStatus.setText(_translate("MainWindow", "0.7", None))
        self.vOffLabel.setText(_translate("MainWindow", "Offset Voltage:", None))
        self.vOffButton.setText(_translate("MainWindow", "Set V Offset", None))
        self.vOffStatus.setText(_translate("MainWindow", "0.45", None))
        self.shutterCWButton.setText(_translate("MainWindow", "Turn CW", None))
        self.shutterLabel.setText(_translate("MainWindow", "Shutter Blade Control:", None))
        self.shutterCCWButton.setText(_translate("MainWindow", "Turn CCW", None))
        self.cryoLabel.setText(_translate("MainWindow", "Cryostat Control:", None))
        self.cryoCCWButton.setText(_translate("MainWindow", "Turn  CCW", None))
        self.cryoCWButton.setText(_translate("MainWindow", "Turn CW", None))
        self.Manual.setText(_translate("MainWindow", "Manual Controls", None))
        self.Auto.setText(_translate("MainWindow", "Automatic Evaporation", None))
        self.thicknessStatus_2.setText(_translate("MainWindow", "Not Initialized", None))
        self.rateStatus_2.setText(_translate("MainWindow", "Not Initialized", None))
        self.rateLabel_2.setText(_translate("MainWindow", "Dep. Rate:", None))
        self.thicknessLabel_2.setText(_translate("MainWindow", "Thickness:", None))
        self.pressureStatus_2.setText(_translate("MainWindow", "Not Initialized", None))
        self.pressureLabel_2.setText(_translate("MainWindow", "Pressure:", None))
        self.emergStop.setText(_translate("MainWindow", "STOP", None))
        self.angleStatus.setText(_translate("MainWindow", "105", None))
        self.angleButton.setText(_translate("MainWindow", "Set Angle", None))
        self.angleLabel.setText(_translate("MainWindow", "Contact Angle:", None))
        self.contactThkStatus.setText(_translate("MainWindow", "250", None))
        self.contactThkButton.setText(_translate("MainWindow", "Set Thickness", None))
        self.contactThkLabel.setText(_translate("MainWindow", "Contact Thickness:", None))
        self.startAuto.setText(_translate("MainWindow", "START", None))
        self.contactThkUnits.setText(_translate("MainWindow", "Å", None))
        self.contactAngleUnits.setText(_translate("MainWindow", "°", None))
        self.headThkUnits.setText(_translate("MainWindow", "Å", None))
        self.headThkButton.setText(_translate("MainWindow", "Set Thickness", None))
        self.headThkLabel.setText(_translate("MainWindow", "Head On Thickness:", None))
        self.headThkStatus.setText(_translate("MainWindow", "170", None))
        self.thermTimeUnits.setText(_translate("MainWindow", "min", None))
        self.thermTimeButton.setText(_translate("MainWindow", "Set Time", None))
        self.thermTimeStatusLabel.setText(_translate("MainWindow", "15", None))
        self.thermTimeLabel.setText(_translate("MainWindow", "Thermalization Time 1: ", None))
        self.nomPressFormat_2.setText(_translate("MainWindow", "x.xxEsxx", None))
        self.nomPress_2.setText(_translate("MainWindow", "Pressure Setpoint:", None))
        self.nomPressLabel_2.setText(_translate("MainWindow", "N/A", None))
        self.nomPressButton_2.setText(_translate("MainWindow", "Set Pressure", None))
        self.thermPrsUnits.setText(_translate("MainWindow", "mbar", None))
        self.thermPrsLabel.setText(_translate("MainWindow", "Thermalization Pressure: ", None))
        self.thermPrsStatusLabel.setText(_translate("MainWindow", "5.00E-03", None))
        self.thermPrsButton.setText(_translate("MainWindow", "Set Pressure", None))
        self.nomPressFormat_3.setText(_translate("MainWindow", "Input Format:       x.xxEsxx", None))
        self.voltageLabel_2.setText(_translate("MainWindow", "Voltage:", None))
        self.voltageStatus_2.setText(_translate("MainWindow", "Not Initialized", None))
        self.thermTimeButton_2.setText(_translate("MainWindow", "Set Time", None))
        self.thermTimeUnits_2.setText(_translate("MainWindow", "min", None))
        self.thermTimeStatusLabel_2.setText(_translate("MainWindow", "6", None))
        self.thermTimeLabel_2.setText(_translate("MainWindow", "Thermalization Time 2: ", None))
        self.zeroThkButton.setText(_translate("MainWindow", "Zero Thickness", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.EvapControl), _translate("MainWindow", "Evaporation", None))

from dataCollectorWidget import dataCollectorWidget
from labradWidgets import dataVaultFileSelectWidget
from pyqtgraph import PlotWidget
import GUIPictures_rc
