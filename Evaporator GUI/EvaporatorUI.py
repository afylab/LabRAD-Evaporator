# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EvaporatorUIv3.ui'
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
        MainWindow.resize(1366, 768)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1366, 768))
        MainWindow.setMaximumSize(QtCore.QSize(1366, 768))
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
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1366, 768))
        self.tabWidget.setStyleSheet(_fromUtf8(""))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.GraphicalInterface = QtGui.QWidget()
        self.GraphicalInterface.setStyleSheet(_fromUtf8(""))
        self.GraphicalInterface.setObjectName(_fromUtf8("GraphicalInterface"))
        self.graphBackground = QtGui.QFrame(self.GraphicalInterface)
        self.graphBackground.setEnabled(True)
        self.graphBackground.setGeometry(QtCore.QRect(0, 0, 1360, 742))
        self.graphBackground.setStyleSheet(_fromUtf8("#graphBackground{\n"
"background: black\n"
"}"))
        self.graphBackground.setFrameShape(QtGui.QFrame.StyledPanel)
        self.graphBackground.setFrameShadow(QtGui.QFrame.Raised)
        self.graphBackground.setObjectName(_fromUtf8("graphBackground"))
        self.line = QtGui.QFrame(self.graphBackground)
        self.line.setGeometry(QtCore.QRect(100, 520, 20, 50))
        self.line.setStyleSheet(_fromUtf8("#line{\n"
"color:white;\n"
"}"))
        self.line.setFrameShadow(QtGui.QFrame.Plain)
        self.line.setLineWidth(4)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setObjectName(_fromUtf8("line"))
        self.scrollPumpLabel = QtGui.QLabel(self.graphBackground)
        self.scrollPumpLabel.setGeometry(QtCore.QRect(50, 580, 121, 41))
        self.scrollPumpLabel.setStyleSheet(_fromUtf8("#scrollPumpLabel{\n"
"color: white;\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"}"))
        self.scrollPumpLabel.setObjectName(_fromUtf8("scrollPumpLabel"))
        self.scrollValveButton = QtGui.QPushButton(self.graphBackground)
        self.scrollValveButton.setGeometry(QtCore.QRect(86, 470, 50, 50))
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
        self.line_2.setGeometry(QtCore.QRect(100, 420, 20, 50))
        self.line_2.setStyleSheet(_fromUtf8("#line_2{\n"
"color: white\n"
"}"))
        self.line_2.setFrameShadow(QtGui.QFrame.Plain)
        self.line_2.setLineWidth(4)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.scrollValveStatus = QtGui.QLabel(self.graphBackground)
        self.scrollValveStatus.setGeometry(QtCore.QRect(30, 470, 50, 50))
        self.scrollValveStatus.setStyleSheet(_fromUtf8("#scrollValveStatus{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.scrollValveStatus.setObjectName(_fromUtf8("scrollValveStatus"))
        self.line_3 = QtGui.QFrame(self.graphBackground)
        self.line_3.setGeometry(QtCore.QRect(300, 520, 20, 50))
        self.line_3.setStyleSheet(_fromUtf8("#line_3{\n"
"color: white;\n"
"}"))
        self.line_3.setFrameShadow(QtGui.QFrame.Plain)
        self.line_3.setLineWidth(4)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.line_4 = QtGui.QFrame(self.graphBackground)
        self.line_4.setGeometry(QtCore.QRect(300, 420, 20, 50))
        self.line_4.setStyleSheet(_fromUtf8("#line_4{\n"
"color: white\n"
"}"))
        self.line_4.setFrameShadow(QtGui.QFrame.Plain)
        self.line_4.setLineWidth(4)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.turboValveButton = QtGui.QPushButton(self.graphBackground)
        self.turboValveButton.setGeometry(QtCore.QRect(286, 470, 50, 50))
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
        self.turboValveStatus.setGeometry(QtCore.QRect(350, 470, 50, 50))
        self.turboValveStatus.setStyleSheet(_fromUtf8("#turboValveStatus{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.turboValveStatus.setObjectName(_fromUtf8("turboValveStatus"))
        self.turboPumpLabel = QtGui.QLabel(self.graphBackground)
        self.turboPumpLabel.setGeometry(QtCore.QRect(250, 580, 121, 41))
        self.turboPumpLabel.setStyleSheet(_fromUtf8("#turboPumpLabel{\n"
"color: white;\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"}"))
        self.turboPumpLabel.setObjectName(_fromUtf8("turboPumpLabel"))
        self.line_5 = QtGui.QFrame(self.graphBackground)
        self.line_5.setGeometry(QtCore.QRect(110, 420, 75, 3))
        self.line_5.setStyleSheet(_fromUtf8("#line_5{\n"
"color: white\n"
"}"))
        self.line_5.setFrameShadow(QtGui.QFrame.Plain)
        self.line_5.setLineWidth(4)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.line_6 = QtGui.QFrame(self.graphBackground)
        self.line_6.setGeometry(QtCore.QRect(235, 420, 75, 3))
        self.line_6.setStyleSheet(_fromUtf8("#line_6{\n"
"color: white\n"
"}"))
        self.line_6.setFrameShadow(QtGui.QFrame.Plain)
        self.line_6.setLineWidth(4)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.gateValveButton = QtGui.QPushButton(self.graphBackground)
        self.gateValveButton.setGeometry(QtCore.QRect(185, 396, 50, 50))
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
        self.gateValveStatus.setGeometry(QtCore.QRect(185, 350, 50, 50))
        self.gateValveStatus.setStyleSheet(_fromUtf8("#gateValveStatus{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"\n"
"qproperty-alignment: \'AlignVCenter | AlignHCenter\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.gateValveStatus.setObjectName(_fromUtf8("gateValveStatus"))
        self.gateValveLabel = QtGui.QLabel(self.graphBackground)
        self.gateValveLabel.setGeometry(QtCore.QRect(175, 442, 100, 50))
        self.gateValveLabel.setStyleSheet(_fromUtf8("#gateValveLabel{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"}"))
        self.gateValveLabel.setObjectName(_fromUtf8("gateValveLabel"))
        self.line_7 = QtGui.QFrame(self.graphBackground)
        self.line_7.setGeometry(QtCore.QRect(310, 420, 250, 3))
        self.line_7.setStyleSheet(_fromUtf8("#line_7{\n"
"color: white\n"
"}"))
        self.line_7.setFrameShadow(QtGui.QFrame.Plain)
        self.line_7.setLineWidth(4)
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.line_8 = QtGui.QFrame(self.graphBackground)
        self.line_8.setGeometry(QtCore.QRect(550, 520, 20, 50))
        self.line_8.setStyleSheet(_fromUtf8("#line_8{\n"
"color: white;\n"
"}"))
        self.line_8.setFrameShadow(QtGui.QFrame.Plain)
        self.line_8.setLineWidth(4)
        self.line_8.setFrameShape(QtGui.QFrame.VLine)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.line_9 = QtGui.QFrame(self.graphBackground)
        self.line_9.setGeometry(QtCore.QRect(550, 420, 20, 50))
        self.line_9.setStyleSheet(_fromUtf8("#line_9{\n"
"color: white\n"
"}"))
        self.line_9.setFrameShadow(QtGui.QFrame.Plain)
        self.line_9.setLineWidth(4)
        self.line_9.setFrameShape(QtGui.QFrame.VLine)
        self.line_9.setObjectName(_fromUtf8("line_9"))
        self.boatShutterButton = QtGui.QPushButton(self.graphBackground)
        self.boatShutterButton.setGeometry(QtCore.QRect(536, 470, 50, 50))
        self.boatShutterButton.setStyleSheet(_fromUtf8("#boatShutterButton{\n"
"  border-color: rgb(255, 255, 255);\n"
"  border-width: 4px;        \n"
"  border-style: solid;\n"
"  border-radius: 25px;\n"
" background: black;\n"
"}"))
        self.boatShutterButton.setText(_fromUtf8(""))
        self.boatShutterButton.setObjectName(_fromUtf8("boatShutterButton"))
        self.boatShutterStatus = QtGui.QLabel(self.graphBackground)
        self.boatShutterStatus.setGeometry(QtCore.QRect(470, 470, 50, 50))
        self.boatShutterStatus.setStyleSheet(_fromUtf8("#boatShutterStatus{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.boatShutterStatus.setObjectName(_fromUtf8("boatShutterStatus"))
        self.powerSupplyLabel = QtGui.QLabel(self.graphBackground)
        self.powerSupplyLabel.setGeometry(QtCore.QRect(500, 580, 140, 41))
        self.powerSupplyLabel.setStyleSheet(_fromUtf8("#powerSupplyLabel{\n"
"color: white;\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"}"))
        self.powerSupplyLabel.setObjectName(_fromUtf8("powerSupplyLabel"))
        self.pressureStatus = QtGui.QLabel(self.graphBackground)
        self.pressureStatus.setGeometry(QtCore.QRect(840, 520, 100, 51))
        self.pressureStatus.setStyleSheet(_fromUtf8("#pressureStatus{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.pressureStatus.setObjectName(_fromUtf8("pressureStatus"))
        self.pressureLabel = QtGui.QLabel(self.graphBackground)
        self.pressureLabel.setGeometry(QtCore.QRect(670, 520, 150, 50))
        self.pressureLabel.setStyleSheet(_fromUtf8("#pressureLabel{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.pressureLabel.setObjectName(_fromUtf8("pressureLabel"))
        self.powerSupplyButton = QtGui.QPushButton(self.graphBackground)
        self.powerSupplyButton.setGeometry(QtCore.QRect(531, 620, 55, 55))
        self.powerSupplyButton.setStyleSheet(_fromUtf8("#powerSupplyButton{\n"
"\n"
"image:url(:/OnOff/Off2.png);\n"
"\n"
"  background: black;\n"
"}"))
        self.powerSupplyButton.setText(_fromUtf8(""))
        self.powerSupplyButton.setObjectName(_fromUtf8("powerSupplyButton"))
        self.turboPumpButton = QtGui.QPushButton(self.graphBackground)
        self.turboPumpButton.setGeometry(QtCore.QRect(281, 620, 56, 56))
        self.turboPumpButton.setStyleSheet(_fromUtf8("#turboPumpButton{\n"
"image:url(:/OnOff/Off2.png);\n"
"background: black;\n"
"}"))
        self.turboPumpButton.setText(_fromUtf8(""))
        self.turboPumpButton.setObjectName(_fromUtf8("turboPumpButton"))
        self.scrollPumpButton = QtGui.QPushButton(self.graphBackground)
        self.scrollPumpButton.setGeometry(QtCore.QRect(81, 620, 55, 55))
        self.scrollPumpButton.setStyleSheet(_fromUtf8("#scrollPumpButton{\n"
"image:url(:/OnOff/Off2.png);\n"
"background: black;\n"
"}"))
        self.scrollPumpButton.setText(_fromUtf8(""))
        self.scrollPumpButton.setObjectName(_fromUtf8("scrollPumpButton"))
        self.cryoAngleLabel = QtGui.QLabel(self.graphBackground)
        self.cryoAngleLabel.setGeometry(QtCore.QRect(860, 350, 140, 41))
        self.cryoAngleLabel.setStyleSheet(_fromUtf8("#cryoAngleLabel{\n"
"color: white;\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"}"))
        self.cryoAngleLabel.setObjectName(_fromUtf8("cryoAngleLabel"))
        self.line_10 = QtGui.QFrame(self.graphBackground)
        self.line_10.setGeometry(QtCore.QRect(560, 420, 125, 3))
        self.line_10.setStyleSheet(_fromUtf8("#line_10{\n"
"color: white\n"
"}"))
        self.line_10.setFrameShadow(QtGui.QFrame.Plain)
        self.line_10.setLineWidth(4)
        self.line_10.setFrameShape(QtGui.QFrame.HLine)
        self.line_10.setObjectName(_fromUtf8("line_10"))
        self.rateLabel = QtGui.QLabel(self.graphBackground)
        self.rateLabel.setGeometry(QtCore.QRect(670, 575, 150, 50))
        self.rateLabel.setStyleSheet(_fromUtf8("#rateLabel{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.rateLabel.setObjectName(_fromUtf8("rateLabel"))
        self.thicknessLabel = QtGui.QLabel(self.graphBackground)
        self.thicknessLabel.setGeometry(QtCore.QRect(670, 630, 150, 50))
        self.thicknessLabel.setStyleSheet(_fromUtf8("#thicknessLabel{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.thicknessLabel.setObjectName(_fromUtf8("thicknessLabel"))
        self.heliumFlowButton = QtGui.QPushButton(self.graphBackground)
        self.heliumFlowButton.setEnabled(True)
        self.heliumFlowButton.setGeometry(QtCore.QRect(680, 396, 50, 50))
        self.heliumFlowButton.setStyleSheet(_fromUtf8("#heliumFlowButton{\n"
"  border-color: rgb(255, 255, 255);\n"
"  border-width: 4px;        \n"
"  border-style: solid;\n"
"  border-radius: 25px;\n"
" background: black;\n"
"}"))
        self.heliumFlowButton.setText(_fromUtf8(""))
        self.heliumFlowButton.setObjectName(_fromUtf8("heliumFlowButton"))
        self.line_11 = QtGui.QFrame(self.graphBackground)
        self.line_11.setGeometry(QtCore.QRect(730, 420, 125, 3))
        self.line_11.setStyleSheet(_fromUtf8("#line_11{\n"
"color: white\n"
"}"))
        self.line_11.setFrameShadow(QtGui.QFrame.Plain)
        self.line_11.setLineWidth(4)
        self.line_11.setFrameShape(QtGui.QFrame.HLine)
        self.line_11.setObjectName(_fromUtf8("line_11"))
        self.heliumFlowStatus = QtGui.QLabel(self.graphBackground)
        self.heliumFlowStatus.setGeometry(QtCore.QRect(655, 350, 100, 50))
        self.heliumFlowStatus.setStyleSheet(_fromUtf8("#heliumFlowStatus{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignHCenter\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.heliumFlowStatus.setObjectName(_fromUtf8("heliumFlowStatus"))
        self.pushChooseDir = QtGui.QPushButton(self.graphBackground)
        self.pushChooseDir.setGeometry(QtCore.QRect(100, 80, 139, 23))
        self.pushChooseDir.setObjectName(_fromUtf8("pushChooseDir"))
        self.pushConnect = QtGui.QPushButton(self.graphBackground)
        self.pushConnect.setGeometry(QtCore.QRect(100, 40, 139, 23))
        self.pushConnect.setObjectName(_fromUtf8("pushConnect"))
        self.line_12 = QtGui.QFrame(self.graphBackground)
        self.line_12.setGeometry(QtCore.QRect(690, 520, 300, 3))
        self.line_12.setStyleSheet(_fromUtf8("#line_12{\n"
"color: white\n"
"}"))
        self.line_12.setFrameShadow(QtGui.QFrame.Plain)
        self.line_12.setLineWidth(1)
        self.line_12.setFrameShape(QtGui.QFrame.HLine)
        self.line_12.setObjectName(_fromUtf8("line_12"))
        self.line_13 = QtGui.QFrame(self.graphBackground)
        self.line_13.setGeometry(QtCore.QRect(690, 680, 300, 3))
        self.line_13.setStyleSheet(_fromUtf8("#line_13{\n"
"color: white\n"
"}"))
        self.line_13.setFrameShadow(QtGui.QFrame.Plain)
        self.line_13.setLineWidth(1)
        self.line_13.setFrameShape(QtGui.QFrame.HLine)
        self.line_13.setObjectName(_fromUtf8("line_13"))
        self.line_14 = QtGui.QFrame(self.graphBackground)
        self.line_14.setGeometry(QtCore.QRect(690, 521, 1, 160))
        self.line_14.setStyleSheet(_fromUtf8("#line_14{\n"
"color: white;\n"
"}"))
        self.line_14.setFrameShadow(QtGui.QFrame.Plain)
        self.line_14.setLineWidth(1)
        self.line_14.setFrameShape(QtGui.QFrame.VLine)
        self.line_14.setObjectName(_fromUtf8("line_14"))
        self.line_15 = QtGui.QFrame(self.graphBackground)
        self.line_15.setGeometry(QtCore.QRect(990, 521, 1, 160))
        self.line_15.setStyleSheet(_fromUtf8("#line_15{\n"
"color: white;\n"
"}"))
        self.line_15.setFrameShadow(QtGui.QFrame.Plain)
        self.line_15.setLineWidth(1)
        self.line_15.setFrameShape(QtGui.QFrame.VLine)
        self.line_15.setObjectName(_fromUtf8("line_15"))
        self.rateStatus = QtGui.QLabel(self.graphBackground)
        self.rateStatus.setGeometry(QtCore.QRect(840, 575, 100, 51))
        self.rateStatus.setStyleSheet(_fromUtf8("#rateStatus{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.rateStatus.setObjectName(_fromUtf8("rateStatus"))
        self.thicknessStatus = QtGui.QLabel(self.graphBackground)
        self.thicknessStatus.setGeometry(QtCore.QRect(840, 630, 100, 51))
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
        self.detailsBackground.setGeometry(QtCore.QRect(0, 0, 1360, 742))
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
        self.comboGraph.setGeometry(QtCore.QRect(40, 70, 141, 22))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboGraph.sizePolicy().hasHeightForWidth())
        self.comboGraph.setSizePolicy(sizePolicy)
        self.comboGraph.setObjectName(_fromUtf8("comboGraph"))
        self.comboGraph2 = QtGui.QComboBox(self.detailsBackground)
        self.comboGraph2.setGeometry(QtCore.QRect(40, 410, 141, 22))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboGraph2.sizePolicy().hasHeightForWidth())
        self.comboGraph2.setSizePolicy(sizePolicy)
        self.comboGraph2.setObjectName(_fromUtf8("comboGraph2"))
        self.plot2 = PlotWidget(self.detailsBackground)
        self.plot2.setGeometry(QtCore.QRect(40, 440, 1280, 300))
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
        self.plot.setGeometry(QtCore.QRect(40, 100, 1280, 300))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot.sizePolicy().hasHeightForWidth())
        self.plot.setSizePolicy(sizePolicy)
        self.plot.setObjectName(_fromUtf8("plot"))
        self.detailsBackground.raise_()
        self.sliderGraph.raise_()
        self.sliderLCD.raise_()
        self.tabWidget.addTab(self.Plotting, _fromUtf8(""))
        self.DataCollector = QtGui.QWidget()
        self.DataCollector.setObjectName(_fromUtf8("DataCollector"))
        self.dataCollectorWidget = dataCollectorWidget(self.DataCollector)
        self.dataCollectorWidget.setGeometry(QtCore.QRect(0, 0, 1360, 742))
        self.dataCollectorWidget.setObjectName(_fromUtf8("dataCollectorWidget"))
        self.tabWidget.addTab(self.DataCollector, _fromUtf8(""))
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
        self.cryoAngleLabel.setText(_translate("MainWindow", "Cryostat Angle:", None))
        self.rateLabel.setText(_translate("MainWindow", "Deposition Rate:", None))
        self.thicknessLabel.setText(_translate("MainWindow", "Thickness:", None))
        self.heliumFlowStatus.setText(_translate("MainWindow", "Not Flowing", None))
        self.pushChooseDir.setText(_translate("MainWindow", "Select Directory", None))
        self.pushConnect.setText(_translate("MainWindow", "Connect to Servers", None))
        self.rateStatus.setText(_translate("MainWindow", "Not Initialized", None))
        self.thicknessStatus.setText(_translate("MainWindow", "Not Initialized", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.GraphicalInterface), _translate("MainWindow", "Graphical Interface", None))
        self.numPointsLabel.setText(_translate("MainWindow", "Number of Points:", None))
        self.Live_Plotter.setText(_translate("MainWindow", "Live Plotter", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Plotting), _translate("MainWindow", "Plotting", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DataCollector), _translate("MainWindow", "Data Collector", None))

from dataCollectorWidget import dataCollectorWidget
from labradWidgets import dataVaultFileSelectWidget
from pyqtgraph import PlotWidget
import GUIPictures_rc
