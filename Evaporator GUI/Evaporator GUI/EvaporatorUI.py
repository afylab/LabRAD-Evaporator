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
        self.scrollPumpLabel.setGeometry(QtCore.QRect(40, 520, 121, 41))
        self.scrollPumpLabel.setStyleSheet(_fromUtf8("#scrollPumpLabel{\n"
"color: white;\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"}"))
        self.scrollPumpLabel.setObjectName(_fromUtf8("scrollPumpLabel"))
        self.scrollValveButton = QtGui.QPushButton(self.graphBackground)
        self.scrollValveButton.setGeometry(QtCore.QRect(76, 410, 50, 50))
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
        self.scrollValveStatus.setGeometry(QtCore.QRect(20, 406, 50, 50))
        self.scrollValveStatus.setStyleSheet(_fromUtf8("#scrollValveStatus{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.scrollValveStatus.setObjectName(_fromUtf8("scrollValveStatus"))
        self.line_3 = QtGui.QFrame(self.graphBackground)
        self.line_3.setGeometry(QtCore.QRect(290, 460, 20, 50))
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
        self.turboValveButton.setGeometry(QtCore.QRect(276, 410, 50, 50))
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
        self.turboValveStatus.setGeometry(QtCore.QRect(340, 406, 50, 50))
        self.turboValveStatus.setStyleSheet(_fromUtf8("#turboValveStatus{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.turboValveStatus.setObjectName(_fromUtf8("turboValveStatus"))
        self.turboPumpLabel = QtGui.QLabel(self.graphBackground)
        self.turboPumpLabel.setGeometry(QtCore.QRect(240, 520, 121, 41))
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
        self.line_8.setGeometry(QtCore.QRect(540, 460, 20, 50))
        self.line_8.setStyleSheet(_fromUtf8("#line_8{\n"
"color: white;\n"
"}"))
        self.line_8.setFrameShadow(QtGui.QFrame.Plain)
        self.line_8.setLineWidth(4)
        self.line_8.setFrameShape(QtGui.QFrame.VLine)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.line_9 = QtGui.QFrame(self.graphBackground)
        self.line_9.setGeometry(QtCore.QRect(540, 360, 20, 50))
        self.line_9.setStyleSheet(_fromUtf8("#line_9{\n"
"color: white\n"
"}"))
        self.line_9.setFrameShadow(QtGui.QFrame.Plain)
        self.line_9.setLineWidth(4)
        self.line_9.setFrameShape(QtGui.QFrame.VLine)
        self.line_9.setObjectName(_fromUtf8("line_9"))
        self.boatShutterButton = QtGui.QPushButton(self.graphBackground)
        self.boatShutterButton.setGeometry(QtCore.QRect(526, 410, 50, 50))
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
        self.boatShutterStatus.setGeometry(QtCore.QRect(460, 406, 50, 50))
        self.boatShutterStatus.setStyleSheet(_fromUtf8("#boatShutterStatus{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.boatShutterStatus.setObjectName(_fromUtf8("boatShutterStatus"))
        self.powerSupplyLabel = QtGui.QLabel(self.graphBackground)
        self.powerSupplyLabel.setGeometry(QtCore.QRect(490, 520, 140, 41))
        self.powerSupplyLabel.setStyleSheet(_fromUtf8("#powerSupplyLabel{\n"
"color: white;\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"}"))
        self.powerSupplyLabel.setObjectName(_fromUtf8("powerSupplyLabel"))
        self.pressureStatus = QtGui.QLabel(self.graphBackground)
        self.pressureStatus.setGeometry(QtCore.QRect(1060, 50, 100, 51))
        self.pressureStatus.setStyleSheet(_fromUtf8("#pressureStatus{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.pressureStatus.setObjectName(_fromUtf8("pressureStatus"))
        self.pressureLabel = QtGui.QLabel(self.graphBackground)
        self.pressureLabel.setGeometry(QtCore.QRect(890, 50, 150, 50))
        self.pressureLabel.setStyleSheet(_fromUtf8("#pressureLabel{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.pressureLabel.setObjectName(_fromUtf8("pressureLabel"))
        self.powerSupplyButton = QtGui.QPushButton(self.graphBackground)
        self.powerSupplyButton.setGeometry(QtCore.QRect(521, 560, 55, 55))
        self.powerSupplyButton.setStyleSheet(_fromUtf8("#powerSupplyButton{\n"
"\n"
"image:url(:/OnOff/Off2.png);\n"
"\n"
"  background: black;\n"
"}"))
        self.powerSupplyButton.setText(_fromUtf8(""))
        self.powerSupplyButton.setObjectName(_fromUtf8("powerSupplyButton"))
        self.turboPumpButton = QtGui.QPushButton(self.graphBackground)
        self.turboPumpButton.setGeometry(QtCore.QRect(271, 560, 56, 56))
        self.turboPumpButton.setStyleSheet(_fromUtf8("#turboPumpButton{\n"
"image:url(:/OnOff/Off2.png);\n"
"background: black;\n"
"}"))
        self.turboPumpButton.setText(_fromUtf8(""))
        self.turboPumpButton.setObjectName(_fromUtf8("turboPumpButton"))
        self.scrollPumpButton = QtGui.QPushButton(self.graphBackground)
        self.scrollPumpButton.setGeometry(QtCore.QRect(71, 560, 55, 55))
        self.scrollPumpButton.setStyleSheet(_fromUtf8("#scrollPumpButton{\n"
"image:url(:/OnOff/Off2.png);\n"
"background: black;\n"
"}"))
        self.scrollPumpButton.setText(_fromUtf8(""))
        self.scrollPumpButton.setObjectName(_fromUtf8("scrollPumpButton"))
        self.cryoAngleLabel = QtGui.QLabel(self.graphBackground)
        self.cryoAngleLabel.setGeometry(QtCore.QRect(680, 420, 171, 41))
        self.cryoAngleLabel.setStyleSheet(_fromUtf8("#cryoAngleLabel{\n"
"color: white;\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"}"))
        self.cryoAngleLabel.setObjectName(_fromUtf8("cryoAngleLabel"))
        self.line_10 = QtGui.QFrame(self.graphBackground)
        self.line_10.setGeometry(QtCore.QRect(550, 360, 125, 3))
        self.line_10.setStyleSheet(_fromUtf8("#line_10{\n"
"color: white\n"
"}"))
        self.line_10.setFrameShadow(QtGui.QFrame.Plain)
        self.line_10.setLineWidth(4)
        self.line_10.setFrameShape(QtGui.QFrame.HLine)
        self.line_10.setObjectName(_fromUtf8("line_10"))
        self.rateLabel = QtGui.QLabel(self.graphBackground)
        self.rateLabel.setGeometry(QtCore.QRect(890, 105, 150, 50))
        self.rateLabel.setStyleSheet(_fromUtf8("#rateLabel{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.rateLabel.setObjectName(_fromUtf8("rateLabel"))
        self.thicknessLabel = QtGui.QLabel(self.graphBackground)
        self.thicknessLabel.setGeometry(QtCore.QRect(890, 160, 150, 50))
        self.thicknessLabel.setStyleSheet(_fromUtf8("#thicknessLabel{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.thicknessLabel.setObjectName(_fromUtf8("thicknessLabel"))
        self.heliumFlowButton = QtGui.QPushButton(self.graphBackground)
        self.heliumFlowButton.setEnabled(True)
        self.heliumFlowButton.setGeometry(QtCore.QRect(670, 336, 50, 50))
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
        self.line_11.setGeometry(QtCore.QRect(720, 360, 125, 3))
        self.line_11.setStyleSheet(_fromUtf8("#line_11{\n"
"color: white\n"
"}"))
        self.line_11.setFrameShadow(QtGui.QFrame.Plain)
        self.line_11.setLineWidth(4)
        self.line_11.setFrameShape(QtGui.QFrame.HLine)
        self.line_11.setObjectName(_fromUtf8("line_11"))
        self.heliumFlowStatus = QtGui.QLabel(self.graphBackground)
        self.heliumFlowStatus.setGeometry(QtCore.QRect(645, 286, 100, 50))
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
        self.line_12.setGeometry(QtCore.QRect(900, 50, 300, 3))
        self.line_12.setStyleSheet(_fromUtf8("#line_12{\n"
"color: white\n"
"}"))
        self.line_12.setFrameShadow(QtGui.QFrame.Plain)
        self.line_12.setLineWidth(1)
        self.line_12.setFrameShape(QtGui.QFrame.HLine)
        self.line_12.setObjectName(_fromUtf8("line_12"))
        self.line_13 = QtGui.QFrame(self.graphBackground)
        self.line_13.setGeometry(QtCore.QRect(900, 210, 300, 3))
        self.line_13.setStyleSheet(_fromUtf8("#line_13{\n"
"color: white\n"
"}"))
        self.line_13.setFrameShadow(QtGui.QFrame.Plain)
        self.line_13.setLineWidth(1)
        self.line_13.setFrameShape(QtGui.QFrame.HLine)
        self.line_13.setObjectName(_fromUtf8("line_13"))
        self.line_14 = QtGui.QFrame(self.graphBackground)
        self.line_14.setGeometry(QtCore.QRect(900, 50, 1, 160))
        self.line_14.setStyleSheet(_fromUtf8("#line_14{\n"
"color: white;\n"
"}"))
        self.line_14.setFrameShadow(QtGui.QFrame.Plain)
        self.line_14.setLineWidth(1)
        self.line_14.setFrameShape(QtGui.QFrame.VLine)
        self.line_14.setObjectName(_fromUtf8("line_14"))
        self.line_15 = QtGui.QFrame(self.graphBackground)
        self.line_15.setGeometry(QtCore.QRect(1200, 50, 1, 160))
        self.line_15.setStyleSheet(_fromUtf8("#line_15{\n"
"color: white;\n"
"}"))
        self.line_15.setFrameShadow(QtGui.QFrame.Plain)
        self.line_15.setLineWidth(1)
        self.line_15.setFrameShape(QtGui.QFrame.VLine)
        self.line_15.setObjectName(_fromUtf8("line_15"))
        self.rateStatus = QtGui.QLabel(self.graphBackground)
        self.rateStatus.setGeometry(QtCore.QRect(1060, 105, 100, 51))
        self.rateStatus.setStyleSheet(_fromUtf8("#rateStatus{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.rateStatus.setObjectName(_fromUtf8("rateStatus"))
        self.thicknessStatus = QtGui.QLabel(self.graphBackground)
        self.thicknessStatus.setGeometry(QtCore.QRect(1060, 160, 100, 51))
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
        self.comboGraph.setGeometry(QtCore.QRect(40, 100, 141, 22))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboGraph.sizePolicy().hasHeightForWidth())
        self.comboGraph.setSizePolicy(sizePolicy)
        self.comboGraph.setObjectName(_fromUtf8("comboGraph"))
        self.comboGraph2 = QtGui.QComboBox(self.detailsBackground)
        self.comboGraph2.setGeometry(QtCore.QRect(40, 380, 141, 22))
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
        self.plot2.raise_()
        self.plot.raise_()
        self.numPointsLabel.raise_()
        self.comboGraph.raise_()
        self.comboGraph2.raise_()
        self.Live_Plotter.raise_()
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
        self.setPointInput.setGeometry(QtCore.QRect(230, 90, 113, 21))
        self.setPointInput.setObjectName(_fromUtf8("setPointInput"))
        self.setPointButton = QtGui.QPushButton(self.evapBackground)
        self.setPointButton.setGeometry(QtCore.QRect(360, 90, 101, 21))
        self.setPointButton.setObjectName(_fromUtf8("setPointButton"))
        self.evapStartButton = QtGui.QPushButton(self.evapBackground)
        self.evapStartButton.setGeometry(QtCore.QRect(960, 90, 100, 21))
        self.evapStartButton.setObjectName(_fromUtf8("evapStartButton"))
        self.setPointLabel = QtGui.QLabel(self.evapBackground)
        self.setPointLabel.setGeometry(QtCore.QRect(480, 90, 47, 21))
        self.setPointLabel.setStyleSheet(_fromUtf8("#setPointLabel{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.setPointLabel.setObjectName(_fromUtf8("setPointLabel"))
        self.Feedback = QtGui.QLabel(self.evapBackground)
        self.Feedback.setGeometry(QtCore.QRect(180, 300, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Feedback.setFont(font)
        self.Feedback.setStyleSheet(_fromUtf8("#Feedback{\n"
"color: rgb(212, 212, 212)\n"
"}"))
        self.Feedback.setObjectName(_fromUtf8("Feedback"))
        self.units = QtGui.QLabel(self.evapBackground)
        self.units.setGeometry(QtCore.QRect(560, 90, 47, 21))
        self.units.setStyleSheet(_fromUtf8("#units{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignLeft\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.units.setObjectName(_fromUtf8("units"))
        self.propInput = QtGui.QLineEdit(self.evapBackground)
        self.propInput.setGeometry(QtCore.QRect(220, 390, 113, 21))
        self.propInput.setObjectName(_fromUtf8("propInput"))
        self.propButton = QtGui.QPushButton(self.evapBackground)
        self.propButton.setGeometry(QtCore.QRect(360, 390, 101, 21))
        self.propButton.setObjectName(_fromUtf8("propButton"))
        self.propStatus = QtGui.QLabel(self.evapBackground)
        self.propStatus.setGeometry(QtCore.QRect(486, 390, 71, 21))
        self.propStatus.setStyleSheet(_fromUtf8("#propStatus{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignCenter\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.propStatus.setObjectName(_fromUtf8("propStatus"))
        self.propLabel = QtGui.QLabel(self.evapBackground)
        self.propLabel.setGeometry(QtCore.QRect(40, 390, 150, 21))
        self.propLabel.setStyleSheet(_fromUtf8("#propLabel{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.propLabel.setObjectName(_fromUtf8("propLabel"))
        self.intStatus = QtGui.QLabel(self.evapBackground)
        self.intStatus.setGeometry(QtCore.QRect(486, 430, 71, 21))
        self.intStatus.setStyleSheet(_fromUtf8("#intStatus{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignCenter\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.intStatus.setObjectName(_fromUtf8("intStatus"))
        self.intButton = QtGui.QPushButton(self.evapBackground)
        self.intButton.setGeometry(QtCore.QRect(360, 430, 101, 21))
        self.intButton.setObjectName(_fromUtf8("intButton"))
        self.intLabel = QtGui.QLabel(self.evapBackground)
        self.intLabel.setGeometry(QtCore.QRect(40, 430, 150, 21))
        self.intLabel.setStyleSheet(_fromUtf8("#intLabel{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.intLabel.setObjectName(_fromUtf8("intLabel"))
        self.intInput = QtGui.QLineEdit(self.evapBackground)
        self.intInput.setGeometry(QtCore.QRect(220, 430, 113, 21))
        self.intInput.setObjectName(_fromUtf8("intInput"))
        self.derivStatus = QtGui.QLabel(self.evapBackground)
        self.derivStatus.setGeometry(QtCore.QRect(486, 550, 71, 21))
        self.derivStatus.setStyleSheet(_fromUtf8("#derivStatus{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignCenter\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.derivStatus.setObjectName(_fromUtf8("derivStatus"))
        self.derivButton = QtGui.QPushButton(self.evapBackground)
        self.derivButton.setGeometry(QtCore.QRect(360, 550, 101, 21))
        self.derivButton.setObjectName(_fromUtf8("derivButton"))
        self.derivLabel = QtGui.QLabel(self.evapBackground)
        self.derivLabel.setGeometry(QtCore.QRect(40, 550, 150, 21))
        self.derivLabel.setStyleSheet(_fromUtf8("#derivLabel{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.derivLabel.setObjectName(_fromUtf8("derivLabel"))
        self.derivInput = QtGui.QLineEdit(self.evapBackground)
        self.derivInput.setGeometry(QtCore.QRect(220, 550, 113, 21))
        self.derivInput.setObjectName(_fromUtf8("derivInput"))
        self.intMaxInput = QtGui.QLineEdit(self.evapBackground)
        self.intMaxInput.setGeometry(QtCore.QRect(220, 470, 113, 21))
        self.intMaxInput.setObjectName(_fromUtf8("intMaxInput"))
        self.intMaxStatus = QtGui.QLabel(self.evapBackground)
        self.intMaxStatus.setGeometry(QtCore.QRect(486, 470, 71, 21))
        self.intMaxStatus.setStyleSheet(_fromUtf8("#intMaxStatus{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignCenter\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.intMaxStatus.setObjectName(_fromUtf8("intMaxStatus"))
        self.intMaxLabel = QtGui.QLabel(self.evapBackground)
        self.intMaxLabel.setGeometry(QtCore.QRect(40, 470, 150, 21))
        self.intMaxLabel.setStyleSheet(_fromUtf8("#intMaxLabel{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.intMaxLabel.setObjectName(_fromUtf8("intMaxLabel"))
        self.intMaxButton = QtGui.QPushButton(self.evapBackground)
        self.intMaxButton.setGeometry(QtCore.QRect(360, 470, 101, 21))
        self.intMaxButton.setObjectName(_fromUtf8("intMaxButton"))
        self.intMinInput = QtGui.QLineEdit(self.evapBackground)
        self.intMinInput.setGeometry(QtCore.QRect(220, 510, 113, 21))
        self.intMinInput.setObjectName(_fromUtf8("intMinInput"))
        self.intMinStatus = QtGui.QLabel(self.evapBackground)
        self.intMinStatus.setGeometry(QtCore.QRect(486, 510, 71, 21))
        self.intMinStatus.setStyleSheet(_fromUtf8("#intMinStatus{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignCenter\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.intMinStatus.setObjectName(_fromUtf8("intMinStatus"))
        self.intMinLabel = QtGui.QLabel(self.evapBackground)
        self.intMinLabel.setGeometry(QtCore.QRect(40, 510, 150, 21))
        self.intMinLabel.setStyleSheet(_fromUtf8("#intMinLabel{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.intMinLabel.setObjectName(_fromUtf8("intMinLabel"))
        self.intMinButton = QtGui.QPushButton(self.evapBackground)
        self.intMinButton.setGeometry(QtCore.QRect(360, 510, 101, 21))
        self.intMinButton.setObjectName(_fromUtf8("intMinButton"))
        self.textEdit2 = QtGui.QTextEdit(self.evapBackground)
        self.textEdit2.setGeometry(QtCore.QRect(870, 420, 271, 131))
        self.textEdit2.setObjectName(_fromUtf8("textEdit2"))
        self.deposRate = QtGui.QLabel(self.evapBackground)
        self.deposRate.setGeometry(QtCore.QRect(9, 90, 201, 21))
        self.deposRate.setStyleSheet(_fromUtf8("#deposRate{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.deposRate.setObjectName(_fromUtf8("deposRate"))
        self.note = QtGui.QLabel(self.evapBackground)
        self.note.setGeometry(QtCore.QRect(180, 170, 271, 91))
        self.note.setStyleSheet(_fromUtf8("#note{\n"
"color: white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"qproperty-alignment: \'AlignVCenter | AlignLeft\';\n"
"qproperty-wordWrap: true;\n"
"}"))
        self.note.setObjectName(_fromUtf8("note"))
        self.evapStatus = QtGui.QLabel(self.evapBackground)
        self.evapStatus.setGeometry(QtCore.QRect(960, 150, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.evapStatus.setFont(font)
        self.evapStatus.setStyleSheet(_fromUtf8("#evapStatus{\n"
"color: rgb(212, 212, 212)\n"
"}"))
        self.evapStatus.setObjectName(_fromUtf8("evapStatus"))
        self.line_31 = QtGui.QFrame(self.EvapControl)
        self.line_31.setGeometry(QtCore.QRect(80, 359, 500, 3))
        self.line_31.setStyleSheet(_fromUtf8("#line_31{\n"
"color: white\n"
"}"))
        self.line_31.setFrameShadow(QtGui.QFrame.Plain)
        self.line_31.setLineWidth(1)
        self.line_31.setFrameShape(QtGui.QFrame.HLine)
        self.line_31.setObjectName(_fromUtf8("line_31"))
        self.line_32 = QtGui.QFrame(self.EvapControl)
        self.line_32.setGeometry(QtCore.QRect(80, 360, 1, 242))
        self.line_32.setStyleSheet(_fromUtf8("#line_32{\n"
"color: white;\n"
"}"))
        self.line_32.setFrameShadow(QtGui.QFrame.Plain)
        self.line_32.setLineWidth(1)
        self.line_32.setFrameShape(QtGui.QFrame.VLine)
        self.line_32.setObjectName(_fromUtf8("line_32"))
        self.line_33 = QtGui.QFrame(self.EvapControl)
        self.line_33.setGeometry(QtCore.QRect(580, 360, 1, 242))
        self.line_33.setStyleSheet(_fromUtf8("#line_33{\n"
"color: white;\n"
"}"))
        self.line_33.setFrameShadow(QtGui.QFrame.Plain)
        self.line_33.setLineWidth(1)
        self.line_33.setFrameShape(QtGui.QFrame.VLine)
        self.line_33.setObjectName(_fromUtf8("line_33"))
        self.line_34 = QtGui.QFrame(self.EvapControl)
        self.line_34.setGeometry(QtCore.QRect(80, 600, 500, 3))
        self.line_34.setStyleSheet(_fromUtf8("#line_34{\n"
"color: white\n"
"}"))
        self.line_34.setFrameShadow(QtGui.QFrame.Plain)
        self.line_34.setLineWidth(1)
        self.line_34.setFrameShape(QtGui.QFrame.HLine)
        self.line_34.setObjectName(_fromUtf8("line_34"))
        self.tabWidget.addTab(self.EvapControl, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
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
        self.cryoAngleLabel.setText(_translate("MainWindow", "Cryostat Position:", None))
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
        self.setPointButton.setText(_translate("MainWindow", "Change Setpoint", None))
        self.evapStartButton.setText(_translate("MainWindow", "Start Evaporating", None))
        self.setPointLabel.setText(_translate("MainWindow", "0", None))
        self.Feedback.setText(_translate("MainWindow", "Feedback PID Settings", None))
        self.units.setText(_translate("MainWindow", "Å/s", None))
        self.propButton.setText(_translate("MainWindow", "Set Kp", None))
        self.propStatus.setText(_translate("MainWindow", "0", None))
        self.propLabel.setText(_translate("MainWindow", "Proportional:", None))
        self.intStatus.setText(_translate("MainWindow", "0", None))
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
        self.note.setText(_translate("MainWindow", "Note: the deposition rate sampling rate (from data collector) determines the speed at which the PID updates the voltage. ", None))
        self.evapStatus.setText(_translate("MainWindow", "Standby", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.EvapControl), _translate("MainWindow", "Evaporation Controls", None))

from dataCollectorWidget import dataCollectorWidget
from labradWidgets import dataVaultFileSelectWidget
from pyqtgraph import PlotWidget
import GUIPictures_rc