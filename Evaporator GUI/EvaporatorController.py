import pyqtgraph as pg
from PyQt4 import QtGui, QtCore
from twisted.internet.defer import inlineCallbacks
import twisted
import numpy as np
import EvaporatorUI
from PID import PID
import exceptions

#import labrad.errors

class MainWindow(QtGui.QMainWindow, EvaporatorUI.Ui_MainWindow):
    """
    Computer interface for the nSOT Evaporator.  
   
    TO DO ON GUI: Add ability to automate evaporation process. 
    TO DO: Appropriate message errors for what servers are not connected or cannot detect devices. Also prevent
    stupid mistakes that would destroy the turbo. 
    TO DO: Add way to remove old graph names from the box list. Maybe by double clicking? 
    TO DO: update graph to show past x seconds, rather than x points. 
    TO DO: Reprogram file select widget. Add way to create new folder. Also, make it so that directory selection 
    is automatically what the widget shows, rather than needing to press the button.    
    """
    
    #----------------------------------------------------------------------------------------------#
            
    """ The following section initializes, or defines the initialization of the GUI and 
    connecting to servers."""

    ID_NEWSET = 00001
    ID_NEWDATA = 00002
    ID_NEWPARAM = 00003

    def __init__(self, reactor, parent=None):
        """ Evaporator GUI """
        
        super(MainWindow, self).__init__(parent)
        self.reactor = reactor
        self.setupUi(self)

        self.directory_path = ""
        self.num_points = 50
        
        self.isConnected = False
        
        #initialize PID
        self.Kprop = 0
        self.Kint = 0.001
        self.Kderiv = 0
        self.Kint
        self.PID = PID(0,0.001,0,500,-500,0.7,0.45)
        self.evaporating = False
        
        #initalize plots
        self.initPlots()
        
        #Initialize data
        self.prs_data = None
        self.thk_data = None
        self.dep_data = None
        self.volt_data = None
        
        #Initialize power supply and pumps as off. 
        self.powerSupplyState = 'Off'
        self.scrollPumpState = 'Off'
        self.turboPumpState = 'Off'
        
        #Initialize default automatic evaporation parameters
        self.evapInProgress = False
        self.evapTimer = QtCore.QTimer(self)
        self.evapVoltage = 0.45
        self.max_diff = 0.1
        self.checkPoints = 15
        self.setPoint = 0.0
        self.thermTime = 25.0
        self.thermPrs = '1.00E-03'
        self.contactAngle = 105.0
        self.contactThk = 400.0
        self.headThk  = 250.0
        
        #Define what happens when interacting with buttons
        self.comboGraph.activated[str].connect(self.selectData)
        self.comboGraph2.activated[str].connect(self.selectData2)
        self.comboAxes.activated[str].connect(self.selectAxes)
        self.comboAxes2.activated[str].connect(self.selectAxes2)
        self.pushChooseDir.clicked.connect(self.promptDirectory)
        self.pushConnect.clicked.connect(self.connect)
        self.sliderGraph.valueChanged[int].connect(self.set_num_points)
        self.sliderLCD.display(self.num_points)
        
        self.scrollValveButton.clicked.connect(self.toggleScrollValve)
        self.turboValveButton.clicked.connect(self.toggleTurboValve)
        self.gateValveButton.clicked.connect(self.toggleGateValve)
        self.boatShutterButton.clicked.connect(self.toggleShutter)
        self.boatShutterButton_2.clicked.connect(self.toggleShutter)
        self.powerSupplyButton.clicked.connect(self.togglePowerSupply)
        self.scrollPumpButton.clicked.connect(self.toggleScrollPump)
        self.turboPumpButton.clicked.connect(self.toggleTurboPump)
        self.heliumValveButton.clicked.connect(self.toggleHeliumValve)
        self.heliumValveButton_2.clicked.connect(self.toggleHeliumValve)
        
        self.setPointButton.clicked.connect(self.setSetpoint)
        self.thermTimeButton.clicked.connect(self.setThermTime)
        self.thermPrsButton.clicked.connect(self.setThermPrs)
        self.angleButton.clicked.connect(self.setAngle)
        self.contactThkButton.clicked.connect(self.setContactThk)
        self.headThkButton.clicked.connect(self.setHeadThk)
        
        self.propButton.clicked.connect(self.setProp)
        self.intButton.clicked.connect(self.setInt)
        self.intMaxButton.clicked.connect(self.setIntMax)
        self.intMinButton.clicked.connect(self.setIntMin)
        self.derivButton.clicked.connect(self.setDeriv)
        self.vMaxButton.clicked.connect(self.setVMax)
        self.vOffButton.clicked.connect(self.setVOff)
        
        self.startAuto.clicked.connect(self.startAutoEvap)
        self.emergStop.clicked.connect(self.emergStopEvap)
        
        self.evapStartButton.clicked.connect(self.toggleEvap)
        
        self.nomPressButton.clicked.connect(self.setNomPressureButton)
        self.nomPressButton_2.clicked.connect(self.setNomPressureButton)
        
        self.shutterCWButton.clicked.connect(self.rotateShutterCW)
        self.shutterCCWButton.clicked.connect(self.rotateShutterCCW)
        self.cryoCWButton.clicked.connect(self.rotateCryoCW)
        self.cryoCCWButton.clicked.connect(self.rotateCryoCCW)
        
        #self.dvFileSelect.directoryChangeSignal.connect(self.test)
        
    #def test(self,string):
     #   print 'Whoop whoop'
        
    @inlineCallbacks
    def connect(self, cntx):
        """ Each connection can only monitor one dataset at a time. This function creates 
        a connection and signals for each dataset that needs to be simultaneously monitored. 
        We need to monitor pressure, deposition rate, and thickness for the graphical interface
        and two data sets for each of the graphs. After initalizing those connections, it runs
        the data collector connect function. Finally, it makes a connection with the servers 
        to the equipment that needs to be controlled
        which acti"""
        if self.isConnected:
            self.disconnect()
            self.isConnected = False
        try:
           
            from labrad.wrappers import connectAsync
            
            #This connect is used for updating graph 1 
            self.cxn_gph = yield connectAsync(name = 'Evaporator GUI: Graph 1')
            self.dv_gph = self.cxn_gph.data_vault
            #Set signal ID for creation of new dataset
            yield self.dv_gph.signal__new_dataset(self.ID_NEWSET)
            yield self.dv_gph.addListener(listener=self.add_dataset_gph, source=None, ID=self.ID_NEWSET)
            yield self.dv_gph.signal__data_available(self.ID_NEWDATA)
            yield self.dv_gph.addListener(listener=self.update_gph, source=None, ID=self.ID_NEWDATA)
            
            #This connect is used for updating graph 2 
            self.cxn_gph2 = yield connectAsync(name = 'Evaporator GUI: Graph 2')
            self.dv_gph2 = self.cxn_gph2.data_vault
            #No need to signal ID for creation of new dataset since first graph will documents all the creations. 
            yield self.dv_gph2.signal__data_available(self.ID_NEWDATA)
            yield self.dv_gph2.addListener(listener=self.update_gph2, source=None, ID=self.ID_NEWDATA)
                 
            #Next, create a connection for connecting to each server from which we want constant updates. 
            #Create a cxn_prs for monitoring pressure for front pannel. 
            self.cxn_prs = yield connectAsync(name = 'Evaporator GUI: Pressure')
            self.dv_prs = self.cxn_prs.data_vault
            yield self.dv_prs.signal__new_dataset(self.ID_NEWSET)
            yield self.dv_prs.addListener(listener=self.add_dataset_prs, source=None, ID=self.ID_NEWSET)
            yield self.dv_prs.signal__data_available(self.ID_NEWDATA)
            yield self.dv_prs.addListener(listener=self.update_prs, source=None, ID=self.ID_NEWDATA)
            
            #Create a cxn_dep for monitoring deposition rate
            self.cxn_dep = yield connectAsync(name = 'Evaporator GUI: Deposition Rate')
            self.dv_dep = self.cxn_dep.data_vault
            yield self.dv_dep.signal__new_dataset(self.ID_NEWSET)
            yield self.dv_dep.addListener(listener=self.add_dataset_dep, source=None, ID=self.ID_NEWSET)
            yield self.dv_dep.signal__data_available(self.ID_NEWDATA)
            yield self.dv_dep.addListener(listener=self.update_dep, source=None, ID=self.ID_NEWDATA)
            
            #Create a cxn_thk for monitoring thickness
            self.cxn_thk = yield connectAsync(name = 'Evaporator GUI: Thickness')
            self.dv_thk = self.cxn_thk.data_vault
            
            yield self.dv_thk.signal__new_dataset(self.ID_NEWSET)
            yield self.dv_thk.addListener(listener=self.add_dataset_thk, source=None, ID=self.ID_NEWSET)
            yield self.dv_thk.signal__data_available(self.ID_NEWDATA)
            yield self.dv_thk.addListener(listener=self.update_thk, source=None, ID=self.ID_NEWDATA)
            
            #Create a cxn_thk for monitoring voltage
            self.cxn_volt = yield connectAsync(name = 'Evaporator GUI: Voltage')
            self.dv_volt = self.cxn_volt.data_vault
            
            yield self.dv_volt.signal__new_dataset(self.ID_NEWSET)
            yield self.dv_volt.addListener(listener=self.add_dataset_volt, source=None, ID=self.ID_NEWSET)
            yield self.dv_volt.signal__data_available(self.ID_NEWDATA)
            yield self.dv_volt.addListener(listener=self.update_volt, source=None, ID=self.ID_NEWDATA)
            
            #Have the data collector connect
            self.dataCollectorWidget.connect()
            
            #Have the dvFileSelect connect with a connection that won't mess with any other connections, so 
            #you can browse files without causing trouble. 
            self.cxn = yield connectAsync(name = 'Evaporator GUI: General Connection')
            self.dvFileSelect.setConnection(self.cxn)
            
            #Connectors to the valve/relay controller, the rvc pressure controller, 
            #the stepper controller and the power supply controller. 
            self.vrs = self.cxn.valve_relay_server
            self.vrs.select_device()
            self.rvc = self.cxn.rvc_server
            self.rvc.select_device()
            self.ss = self.cxn.stepper_server
            self.ss.select_device()
            self.tdk = self.cxn.power_supply_server
            self.tdk.select_device()
            self.tdk.adr('6')
            self.tdk.rmt_set('REM')
            self.ftm = self.cxn.ftm_server
            self.ftm.select_device()
            
            nom_prs = yield self.rvc.get_nom_prs()
            self.nomPressLabel.setText(nom_prs)
            self.nomPressLabel_2.setText(nom_prs)
            
            self.isConnected = True
            self.textEdit.setPlainText('Successfully connected graphical interface and data collector to servers')
        except twisted.internet.error.ConnectionRefusedError:
            self.textEdit.setPlainText('Labrad not connected. Start labrad and servers before attempting to connect.')
        except exceptions.AttributeError as err:
            err_str = str(err)
            self.textEdit.setPlainText('Server not started. Labrad' + err_str[13:])
        #except labrad.errors.NoDevicesAvailableError:
        #    self.textEdit.setPlainText('No device available')
        except: 
            self.textEdit.setPlainText('Unknown error (or no device available error) occured during connection to servers. Please investigate.')
            #raise
            
    @inlineCallbacks
    def promptDirectory(self, cntx): 
        #Sets the directory of the data collector and all the other to the dv file select location
        #Redo this better
        self.directory_path = self.dvFileSelect.current_directory
        
        print self.directory_path
        yield self.dv_gph.cd(self.directory_path)
        yield self.dv_gph2.cd(self.directory_path)
        yield self.dv_prs.cd(self.directory_path)
        yield self.dv_thk.cd(self.directory_path)
        yield self.dv_dep.cd(self.directory_path)
        yield self.dv_volt.cd(self.directory_path)
        self.dataCollectorWidget.setDirectory(self.directory_path)
        
        self.textEdit.setPlainText('Successfully natigated to vault\\' + self.directory_path[1] + "\\"
                + self.directory_path[2])
        
    def initPlots(self):
        #Set initial plot display
        self.plot.setTitle('Choose Data for Display')
        self.plot.setLabel('right','')
        self.plot.setLabel('left', '')
        self.plot.setLabel('bottom', '')  
        self.gph1Data = [[]]
        
        self.plot2.setTitle('Choose Data for Display')
        self.plot2.setLabel('right','')
        self.plot2.setLabel('left', '')
        self.plot2.setLabel('bottom', '')    
        self.gph2Data = [[]]
        
#----------------------------------------------------------------------------------------------#   
    """ The following section has functions for creating and updating the graphs """
        
    def add_dataset_gph(self, cntx, signal): 
        print "Data created: " + signal
        self.comboGraph.addItem(signal)
        self.comboGraph.adjustSize()
        
        self.comboGraph2.addItem(signal)
        self.comboGraph2.adjustSize()
        
    @inlineCallbacks
    def update_gph(self, cntx, signal):
        #Take all the new data points
        new_data = yield self.dv_gph.get()
        
        #If graph data is empty graph data is new data points
        if self.gph1Data == [[]]:
            self.gph1Data = new_data
        #Otherwise append new data points to the data set
        else:
            self.gph1Data = np.append(self.gph1Data,new_data,axis=0)
            
        #Clears points off of screen
        self.plot.clear()
            
        #Graphs the latest x data points. Can now be modified to graph the last x seconds of data points. 
        if len(self.gph1Data[:,0])<self.num_points:
            self.plot.plot(self.gph1Data[:,0],self.gph1Data[:,1])
        else:
            self.plot.plot(self.gph1Data[-self.num_points:,0],self.gph1Data[-self.num_points:,1])   
        
        #Prevents graph data from taking up too much memory
        if len(self.gph1Data[:,0]) > 10000:
            over = len(self.gph1Data[:,0]) - 10000
            self.gph1Data = np.delete(self.gph1Data,np.arange(over),0)
        
    @inlineCallbacks
    def update_gph2(self, cntx, signal):
        #Take all the new data points
        new_data = yield self.dv_gph2.get()
        
        #If graph data is empty graph data is new data points
        if self.gph2Data == [[]]:
            self.gph2Data = new_data
        #Otherwise append new data points to the data set
        else:
            self.gph2Data = np.append(self.gph2Data,new_data,axis=0)
            
        #Clears points off of screen
        self.plot2.clear()
            
        #Graphs the latest x data points. Can now be modified to graph the last x seconds of data points. 
        if len(self.gph2Data[:,0])<self.num_points:
            self.plot2.plot(self.gph2Data[:,0],self.gph2Data[:,1])
        else:
            self.plot2.plot(self.gph2Data[-self.num_points:,0],self.gph2Data[-self.num_points:,1])   
        
        #Prevents graph data from taking up too much memory
        if len(self.gph2Data[:,0]) > 10000:
            over = len(self.gph2Data[:,0]) - 10000
            self.gph2Data = np.delete(self.gph1Data,np.arange(over),0)
        
    def set_num_points(self,num_points):
        #AT SOME POINT UPDATE THIS TO BE NOT NUMBER OF POINTS, BUT NUMBER OF SECONDS
        self.num_points = int(50 + num_points**1.4922)
        self.sliderLCD.display(self.num_points)
          
    @inlineCallbacks
    def selectData(self,data_name):
        self.gph1Data = [[]]
        name = str(data_name)
        yield self.dv_gph.open(name)
        print 'Opened file in graph 1: ' + name
        self.plot.setTitle(name[8:])
        
        if name[8:] == 'Pressure vs. Time':
            self.plot.setLabel('left', 'Pressure (mbar)')
            self.plot.setLabel('bottom', 'Time','s')   
        elif name[8:] == 'Thickness vs. Time':
            self.plot.setLabel('left', 'Thickness (Anstroms)')
            self.plot.setLabel('bottom', 'Time','s') 
        elif name[8:] == 'Deposition Rate vs. Time':
            self.plot.setLabel('left', 'Deposition Rate (Anstroms / s)')
            self.plot.setLabel('bottom', 'Time','s')     
        elif name[8:] == 'Voltage vs. Time':
            self.plot.setLabel('left', 'Voltage (V)')
            self.plot.setLabel('bottom', 'Time','s')   
            
        self.update_gph(None, 'selectData')
            
    @inlineCallbacks
    def selectData2(self,data_name):
        self.gph2Data = [[]]
        name = str(data_name)
        yield self.dv_gph2.open(name)
        print 'Opened file in graph 2: ' + name
        self.plot2.setTitle(name[8:])
        
        if name[8:] == 'Pressure vs. Time':
            self.plot2.setLabel('left', 'Pressure (mbar)')
            self.plot2.setLabel('bottom', 'Time','s')   
        elif name[8:] == 'Thickness vs. Time':
            self.plot2.setLabel('left', 'Thickness (Anstroms)')
            self.plot2.setLabel('bottom', 'Time','s') 
        elif name[8:] == 'Deposition Rate vs. Time':
            self.plot2.setLabel('left', 'Deposition Rate (Anstroms / s)')
            self.plot2.setLabel('bottom', 'Time','s')     
        elif name[8:] == 'Voltage vs. Time':
            self.plot2.setLabel('left', 'Voltage (V)')
            self.plot2.setLabel('bottom', 'Time','s')   
            
        self.update_gph2(None, 'selectData')
        
    def selectAxes(self,style):
        style = str(style)
        
        if style == 'x vs. y':
            self.plot.setLogMode(0,0)
        elif style == 'x vs. log(y)':
            self.plot.setLogMode(0,1)
        elif style == 'log(x) vs. y':
            self.plot.setLogMode(1,0)
        elif style == 'log(x) vs. log(y)':
            self.plot.setLogMode(1,1)
            
    def selectAxes2(self,style):
        style = str(style)
        
        if style == 'x vs. y':
            self.plot2.setLogMode(0,0)
        elif style == 'x vs. log(y)':
            self.plot2.setLogMode(0,1)
        elif style == 'log(x) vs. y':
            self.plot2.setLogMode(1,0)
        elif style == 'log(x) vs. log(y)':
            self.plot2.setLogMode(1,1)
         
#----------------------------------------------------------------------------------------------#   
    """ The following section has functions for creating and updating the pressure, deposition
        rate, and thickness on the graphical interface. Also sets voltages based on discrete
        PID if evaporating."""
        
    def add_dataset_prs(self, cntx, signal): 
        if signal[8:] == 'Pressure vs. Time':
            self.dv_prs.open(signal)
            self.prs_data = [[]]
            print 'Pressure is now being monitored'
        
    @inlineCallbacks
    def update_prs(self, cntx, signal):
        #Get new data point
        new_data = yield self.dv_prs.get()
        data_string = str(new_data[0,1])
        self.pressureStatus.setText(data_string[0:8])
        self.pressureStatus_2.setText(data_string[0:8])
        
        if self.prs_data == [[]]:
            self.prs_data = new_data
        else:
            self.prs_data = np.append(self.prs_data,new_data,axis=0)
            
        if len(self.prs_data[:,0]) > 1000:
            over = len(self.prs_data[:,0]) - 1000
            self.prs_data = np.delete(self.prs_data,np.arange(over),0)
            
    def add_dataset_dep(self, cntx, signal):
        if signal[8:] == 'Deposition Rate vs. Time':
            self.dv_dep.open(signal)
            self.dep_data = [[]]
            print 'Deposition Rate is now being monitored'
        
    @inlineCallbacks
    def update_dep(self, cntx, signal):
        #Get new data point
        new_data = yield self.dv_dep.get()
        data_string = str(new_data[0,1])
        self.rateStatus.setText(data_string[0:8])
        self.rateStatus_2.setText(data_string[0:8])
        
        if self.evaporating:
            voltage = str(self.PID.update(new_data[0,:]))
            print 'Voltage was set to: ' + voltage
            yield self.tdk.volt_set(voltage)
            
        if self.dep_data == [[]]:
            self.dep_data = new_data
        else:
            self.dep_data = np.append(self.dep_data,new_data,axis=0)
            
        if len(self.dep_data[:,0]) > 1000:
            over = len(self.dep_data[:,0]) - 1000
            self.prs_data = np.delete(self.dep_data,np.arange(over),0)
            
    def add_dataset_thk(self, cntx, signal):
        if signal[8:] == 'Thickness vs. Time':
            self.dv_thk.open(signal)
            self.thk_data = [[]]
            print 'Thickness is now being monitored'
        
    @inlineCallbacks
    def update_thk(self, cntx, signal):
        new_data = yield self.dv_thk.get()
        data_string = str(new_data[0,1])
        self.thicknessStatus.setText(data_string[0:6])
        self.thicknessStatus_2.setText(data_string[0:6])
        
        # Probably add some functionality for when reached final thickness, close 
        # shutter or something
        # If evaporating as part of an automatic evaporation
        if self.evaporating and self.evapInProgress:
            if new_data[0,1] >= self.desiredThk:
                #Stop evaporating and close the shutter
                yield self.toggleEvap(cntx) 
                yield self.toggleShutter(cntx)
            
        if self.thk_data == [[]]:
            self.thk_data = new_data
        else:
            self.thk_data = np.append(self.thk_data,new_data,axis=0)
            
        if len(self.thk_data[:,0]) > 1000:
            over = len(self.thk_data[:,0]) - 1000
            self.thk_data = np.delete(self.thk_data,np.arange(over),0)
            
    def add_dataset_volt(self, cntx, signal):
        if signal[8:] == 'Voltage vs. Time':
            self.dv_volt.open(signal)
            self.volt_data = [[]]
            print 'Voltage is now being monitored'
            
    @inlineCallbacks
    def update_volt(self, cntx, signal):
        new_data = yield self.dv_volt.get()
        
        if self.volt_data == [[]]:
            self.volt_data = new_data
        else:
            self.volt_data = np.append(self.volt_data,new_data,axis=0)
            
        if len(self.volt_data[:,0]) > 1000:
            over = len(self.volt_data[:,0]) - 1000
            self.volt_data = np.delete(self.volt_data,np.arange(over),0)

#----------------------------------------------------------------------------------------------#
            
    """ The following section specifies the actions of all the buttons in the Graphical
    Interface tab"""
       
    @inlineCallbacks
    def toggleHeliumValve(self,cntx):
        if self.heliumValveStatus.text() == 'Open'  or self.heliumValveStatus.text() == 'Setpoint':
            yield self.close_valve(cntx)
        elif self.heliumValveStatus.text() == 'Closed':
            open_valve = True
            if self.turboPumpState == 'On' and self.gateValveStatus.text() == 'Open':
                msgBox = QtGui.QMessageBox()
                msgBox.setIcon(QtGui.QMessageBox.Information)
                msgBox.setText("The turbo is running and the gate valve is open. Are you sure you want to vent the chamber?")
                msgBox.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.Cancel)
                if msgBox.exec_() == QtGui.QMessageBox.Cancel:
                    open_valve = False
            if open_valve == True:
                yield self.open_valve(cntx)
    
    @inlineCallbacks
    def toggleScrollPump(self,cntx):
        if self.scrollPumpState == 'Off':
            self.scrollPumpState = 'On'
            self.scrollPumpButton.setStyleSheet("image:url(:/OnOff/On3.png);"
            + "background: black;")
            yield self.vrs.scroll_on()
        elif self.scrollPumpState == 'On':
            self.scrollPumpState = 'Off'
            self.scrollPumpButton.setStyleSheet("image:url(:/OnOff/Off2.png);"
            + "background: black;")  
            yield self.vrs.scroll_off()
            
    @inlineCallbacks
    def toggleTurboPump(self,cntx):
        if self.turboPumpState == 'Off':
            self.turboPumpState = 'On'
            self.turboPumpButton.setStyleSheet("image:url(:/OnOff/On3.png);"
            + "background: black;")
            yield self.vrs.turbo_on()
        elif self.turboPumpState == 'On':
            self.turboPumpState = 'Off'
            self.turboPumpButton.setStyleSheet("image:url(:/OnOff/Off2.png);"
            + "background: black;")  
            yield self.vrs.turbo_off()
        
    @inlineCallbacks
    def togglePowerSupply(self, cntx):
        if self.powerSupplyState == 'Off':
            self.powerSupplyState = 'On'
            self.powerSupplyButton.setStyleSheet("image:url(:/OnOff/On3.png);"
            + "background: black;")
            yield self.tdk.volt_set('0')
            yield self.tdk.switch('on')
        elif self.powerSupplyState == 'On':
            self.powerSupplyState = 'Off'
            self.powerSupplyButton.setStyleSheet("image:url(:/OnOff/Off2.png);"
            + "background: black;")
            yield self.tdk.volt_set('0')
            yield self.tdk.switch('off')
    
    @inlineCallbacks
    def toggleScrollValve(self, ctnx):
        if self.scrollValveStatus.text() == 'Open':
            self.scrollValveStatus.setText('Closed')
            self.scrollValveButton.setStyleSheet("#scrollValveButton{border-color:"
            "rgb(255, 255, 255); border-width: 4px;border-style: solid;  " +
            "border-radius: 25px;background: black;}")
            yield self.vrs.chamber_valve_close()
        elif self.scrollValveStatus.text() == 'Closed':
            self.scrollValveStatus.setText('Open')
            self.scrollValveButton.setStyleSheet("#scrollValveButton{border-color:"
            "rgb(255, 255, 255); border-width: 4px;border-style: solid;  " +
            "border-radius: 25px;background: white;}")
            yield self.vrs.chamber_valve_open()
    
    @inlineCallbacks
    def toggleTurboValve(self, cntx):
        if self.turboValveStatus.text() == 'Open':
            self.turboValveStatus.setText('Closed')
            self.turboValveButton.setStyleSheet("#turboValveButton{border-color:"
            "rgb(255, 255, 255); border-width: 4px;border-style: solid;  " +
            "border-radius: 25px;background: black;}")
            yield self.vrs.turbo_valve_close()
        elif self.turboValveStatus.text() == 'Closed':
            self.turboValveStatus.setText('Open')
            self.turboValveButton.setStyleSheet("#turboValveButton{border-color:"
            "rgb(255, 255, 255); border-width: 4px;border-style: solid;  " +
            "border-radius: 25px;background: white;}")
            yield self.vrs.turbo_valve_open()
    
    @inlineCallbacks
    def toggleGateValve(self, cntx):
        if self.gateValveStatus.text() == 'Open':
            self.gateValveStatus.setText('Closed')
            self.gateValveButton.setStyleSheet("#gateValveButton{border-color:"
            "rgb(255, 255, 255); border-width: 4px;border-style: solid;  " +
            "border-radius: 25px;background: black;}")
            yield self.vrs.gate_close()
        elif self.gateValveStatus.text() == 'Closed':
            self.gateValveStatus.setText('Open')
            self.gateValveButton.setStyleSheet("#gateValveButton{border-color:"
            "rgb(255, 255, 255); border-width: 4px;border-style: solid;  " +
            "border-radius: 25px;background: white;}")
            yield self.vrs.gate_open()
    
    @inlineCallbacks
    def toggleShutter(self,cntx):
        print "Toggling shutter"
        if self.boatShutterStatus.text() == 'Open':
            self.boatShutterStatus.setText('Closed')
            self.boatShutterButton.setStyleSheet("image:url(:/Shutter/Closed3.png);"
            + "background: black;")
            self.boatShutterButton_2.setStyleSheet("image:url(:/Shutter/Closed3.png);"
            + "background: black;")
            yield self.ss.rot('A','40','C')
            
        elif self.boatShutterStatus.text() == 'Closed':
            self.boatShutterStatus.setText('Open')
            self.boatShutterButton.setStyleSheet("image:url(:/Shutter/Open3.png);"
            + "background: black;")   
            self.boatShutterButton_2.setStyleSheet("image:url(:/Shutter/Open3.png);"
            + "background: black;")   
            yield self.ss.rot('A','40','A')
#----------------------------------------------------------------------------------------------#
    """ The following section defines all the connections for the Automatic Evaporation Controls tab."""
  
    def setSetpoint(self):
        try:
            self.textEdit2.clear()
            self.setPoint = float(self.setPointInput.text())
            self.PID.resetPoint()
            self.PID.setPoint(self.setPoint)
            self.setPointLabel.setText(self.setPointInput.text())
        except:
            self.textEdit2.setPlainText("Man, that ain't a number")
        self.setPointInput.clear()
          
    def setThermTime(self):
        try:
            self.textEdit2.clear()
            time = float(self.thermTimeInput.text())
            self.thermTime = time
            self.thermTimeStatusLabel.setText(self.thermTimeInput.text())
        except:
            self.textEdit2.setPlainText("Man, that ain't a number")
        self.thermTimeInput.clear()  
        
    def setThermPrs(self):
        try:
            self.textEdit2.clear()
            prs = self.thermPrsInput.text()
            self.thermPrs = str(prs)
            self.thermPrsStatusLabel.setText(self.thermPrsInput.text())
        except:
            self.textEdit2.setPlainText("Man, that ain't a number")
        self.thermPrsInput.clear()  
    
    def setAngle(self):
        try:
            self.textEdit2.clear()
            angle = float(self.angleInput.text())
            self.contactAngle = angle
            self.angleStatus.setText(self.angleInput.text())
        except:
            self.textEdit2.setPlainText("Man, that ain't a number")
        self.angleInput.clear()      

    def setContactThk(self):
        try:
            self.textEdit2.clear()
            thk = float(self.contactThkInput.text())
            self.contactThk = thk
            self.contactThkStatus.setText(self.contactThkInput.text())
        except:
            self.textEdit2.setPlainText("Man, that ain't a number")
        self.contactThkInput.clear()   

    def setHeadThk(self):
        try:
            self.textEdit2.clear()
            thk = float(self.headThkInput.text())
            self.headThk = thk
            self.headThkStatus.setText(self.headThkInput.text())
        except:
            self.textEdit2.setPlainText("Man, that ain't a number")
        self.headThkInput.clear()   
          
  #----------------------------------------------------------------------------------------------#
    """ The following section defines all the connections for the PID Settings."""
          
    def setProp(self):
        try:
            self.textEdit2.clear()
            Kp = float(self.propInput.text())
            self.PID.setKp(Kp)
            self.propStatus.setText(self.propInput.text())
        except:
            self.textEdit2.setPlainText("Man, that ain't a number")
        self.propInput.clear()

    def setInt(self):
        try:
            self.textEdit2.clear()
            Ki = float(self.intInput.text())
            self.PID.setKi(Ki)
            self.intStatus.setText(self.intInput.text())
        except:
            self.textEdit2.setPlainText("Man, that ain't a number")
        self.intInput.clear()
        
    def setIntMax(self):
        try:
            self.textEdit2.clear()
            intMax = float(self.intMaxInput.text())
            self.PID.setIntMax(intMax)
            self.intMaxStatus.setText(self.intMaxInput.text())
        except:
            self.textEdit2.setPlainText("Man, that ain't a number")
        self.intMaxInput.clear()
        
    def setIntMin(self):
        try:
            self.textEdit2.clear()
            intMin = float(self.intMinInput.text())
            self.PID.setIntMin(intMin)
            self.intMinStatus.setText(self.intMinInput.text())
        except:
            self.textEdit2.setPlainText("Man, that ain't a number")
        self.intMinInput.clear()
        
    def setDeriv(self):
        try:
            self.textEdit2.clear()
            Kd = float(self.derivInput.text())
            self.PID.setKd(Kd)
            self.derivStatus.setText(self.derivInput.text())
        except:
            self.textEdit2.setPlainText("Man, that ain't a number")
        self.derivInput.clear()
        
    def setVMax(self):
        try:
            self.textEdit2.clear()
            v_max = float(self.vMaxInput.text())
            self.PID.setVMax(v_max)
            self.vMaxStatus.setText(self.vMaxInput.text())
        except:
            self.textEdit2.setPlainText("Man, that ain't a number")
        self.vMaxInput.clear()
        
    def setVOff(self):
        try:
            self.textEdit2.clear()
            v_off = float(self.vOffInput.text())
            self.PID.setVOff(v_off)
            self.vOffStatus.setText(self.vOffInput.text())
        except:
            self.textEdit2.setPlainText("Man, that ain't a number")
        self.vOffInput.clear()
    
    @inlineCallbacks
    def toggleEvap(self, cntx):
        if self.evapStartButton.text() == 'Start Evaporating':
            self.evapStartButton.setText("Stop Evaporating")
            self.evaporating = True
            self.evapStatus.setText("Evaporating!")
        else: 
            self.evapStartButton.setText("Start Evaporating")
            self.evaporating = False
            self.evapStatus.setText("Standby")
            #Add functions to stop all evaporating from happening. 
            yield self.tdk.volt_set('0')
            self.PID.setIntegrator(0)
            self.PID.resetPoint()

#----------------------------------------------------------------------------------------------#
    """ The following section specifies how to set a desired pressure and how to 
    open / close the helium leak valve. """
    
    @inlineCallbacks
    def setNomPressureButton(self,cntx):
        #Figure out which button was pressed to call setNomPressureButton
        sender = self.sender()
        objName = sender.objectName()
        
        if objName == 'nomPressButton':
            self.textEdit.clear()
            prs = str(self.nomPressInput.text())
        elif objName =='nomPressButton_2':
            self.textEdit2.clear()
            prs = str(self.nomPressInput_2.text())
        
        yield self.setNomPressure(cntx, prs, objName)
    
        if objName == 'nomPressButton':
            self.nomPressInput.clear()
        elif objName =='nomPressButton_2':
            self.nomPressInput_2.clear() 
        
    
    @inlineCallbacks
    def setNomPressure(self, cntx, prs, objName = None):
        try:
            self.heliumValveStatus.setText('Setpoint')
            self.heliumValveButton.setStyleSheet("#heliumValveButton{border-color:"
            "rgb(255, 255, 255); border-width: 4px;border-style: solid;  " +
            "border-radius: 25px;background: blue;}")
            self.heliumValveButton_2.setStyleSheet("#heliumValveButton_2{border-color:"
            "rgb(255, 255, 255); border-width: 4px;border-style: solid;  " +
            "border-radius: 25px;background: blue;}")            
            yield self.rvc.set_mode_prs()
            yield self.rvc.set_nom_prs(prs)
            new_prs = yield self.rvc.get_nom_prs()
            self.nomPressLabel.setText(new_prs + ' mbar')
            self.nomPressLabel_2.setText(new_prs + ' mbar')
        except:
            if objName == 'nomPressButton':
                self.textEdit.setPlainText("Error occured.")
            elif objName =='nomPressButton_2':
                self.textEdit2.setPlainText("Error occured.")
            else:
                print "Nominal pressure failed to set."
    
    @inlineCallbacks
    def open_valve(self,cntx):
        try:
            self.heliumValveStatus.setText('Open')
            self.heliumValveButton.setStyleSheet("#heliumValveButton{border-color:"
            "rgb(255, 255, 255); border-width: 4px;border-style: solid;  " +
            "border-radius: 25px;background: white;}")
            self.heliumValveButton_2.setStyleSheet("#heliumValveButton_2{border-color:"
            "rgb(255, 255, 255); border-width: 4px;border-style: solid;  " +
            "border-radius: 25px;background: white;}")
            yield self.rvc.set_mode_flo()
            yield self.rvc.set_nom_flo('100.0')
        except:
            self.textEdit.setPlainText("Error occured.")
            
    @inlineCallbacks
    def close_valve(self,cntx):
        try:
            self.heliumValveStatus.setText('Closed')
            self.heliumValveButton.setStyleSheet("#heliumValveButton{border-color:"
            "rgb(255, 255, 255); border-width: 4px;border-style: solid;  " +
            "border-radius: 25px;background: black;}")
            self.heliumValveButton_2.setStyleSheet("#heliumValveButton_2{border-color:"
            "rgb(255, 255, 255); border-width: 4px;border-style: solid;  " +
            "border-radius: 25px;background: black;}")
            yield self.rvc.set_mode_flo()
            yield self.rvc.set_nom_flo('000.0')
        except:
            self.textEdit.setPlainText("Error occured.")
            
    @inlineCallbacks
    def rotateCryoCW(self,cntx):
        try:
            self.textEdit.clear()
            angle = str(self.cryoInput.text())
            yield self.ss.rot('B',angle,'C')
        except:
            self.textEdit.setPlainText("Error occured.")
        self.cryoInput.clear()
            
    @inlineCallbacks
    def rotateCryoCCW(self,cntx):
        try:
            self.textEdit.clear()
            angle = str(self.cryoInput.text())
            yield self.ss.rot('B',angle,'A')
        except:
            self.textEdit.setPlainText("Error occured.")
        self.cryoInput.clear()
      
    @inlineCallbacks
    def rotateShutterCW(self,cntx):
        try:
            self.textEdit.clear()
            angle = str(self.shutterInput.text())
            yield self.ss.rot('A',angle,'C')
        except:
            self.textEdit.setPlainText("Error occured.")
        self.shutterInput.clear()
        
    @inlineCallbacks
    def rotateShutterCCW(self,cntx):
        try:
            self.textEdit.clear()
            angle = str(self.shutterInput.text())
            yield self.ss.rot('A',angle,'A')
        except:
            self.textEdit.setPlainText("Error occured.")
        self.shutterInput.clear()
        
        
#----------------------------------------------------------------------------------------------#
    """ The following section controls a standard automated three angle evaporation. Functions are 
    called in the order they're presented."""
    
    @inlineCallbacks
    def startAutoEvap(self, cntx):
        self.evapInProgress = True
        
        msgBox = QtGui.QMessageBox()
        msgBox.setIcon(QtGui.QMessageBox.Information)
        msgBox.setText("Check that the following conditions are met: \r\n 1. The cryostat is at the desired temperature and the " + 
        "dewar has sufficient LN2. \r\n 2. The chamber is at the desired base pressure. \r\n 3. The tip is pointing directly away " + 
        "from the evaporation source. \r\n 4. All data " + 
        "is being sampled at a rate appropriate for the PID settings. \r\n 5. Helium gas is connected to the helium leak valve.")
        msgBox.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.Cancel)
        
        if msgBox.exec_() == QtGui.QMessageBox.Cancel:
            self.evapInProgress = False
            
        if self.evapInProgress:
            self.startAuto.setStyleSheet("#startAuto{font: 14pt \"MS Shell Dlg 2\"; border-width: 0px;" + 
            "border-style: solid; border-radius: 20px; background: yellow; color: rgb(212,212,212);}")
            #Lock buttons so that nothing can be done other than emergency stop during auto evaporation.
            self.lock_interface()
            
            #Make sure everything is in the correct settings
            if self.boatShutterStatus.text() != "Closed":
                yield self.toggleShutter(cntx)
            if self.powerSupplyState == "Off":
                yield self.togglePowerSupply(cntx)
            
            #Go to higher pressure to thermalize
            yield self.setNomPressure(cntx, self.thermPrs)
            
            self.minutesRemaining = self.thermTime
            self.waitXMinutes()
        
    def waitXMinutes(self):
        if self.minutesRemaining == 1 and self.evapInProgress:
            self.textEdit2.setText('Thermalization of tip in progress. ' + str(self.minutesRemaining) + ' minutes remaining until complete.')
            print 'Thermalization of tip in progress. ' + str(self.minutesRemaining) + ' minutes remaining until complete.'
            self.minutesRemaining = self.minutesRemaining - 1
            #Change this to 60 seconds instead of 1 when done debugging. 
            self.evapTimer.singleShot(60000,self.pumpOutChamber)
        elif self.minutesRemaining > 1 and self.evapInProgress:
            self.textEdit2.setText('Thermalization of tip in progress. ' + str(self.minutesRemaining) + ' minutes remaining until complete.')
            print 'Thermalization of tip in progress. ' + str(self.minutesRemaining) + ' minutes remaining until complete.'
            self.minutesRemaining = self.minutesRemaining - 1
            #Change this to 60 seconds instead of 1 when done debugging. 
            self.evapTimer.singleShot(60000,self.waitXMinutes)
        
    @inlineCallbacks
    def pumpOutChamber(self):
        if self.evapInProgress:
            yield self.close_valve(None)
            self.textEdit2.setText('Thermalization complete. Pumping out exchange gas.')
            print 'Thermalization complete. Pumping out exchange gas.'
            self.evapTimer.singleShot(30000,self.autoEvapPhase2)
            
    @inlineCallbacks
    def autoEvapPhase2(self):
        if self.evapInProgress:
            self.textEdit2.setText('Calibrating evaporation voltage.')
            print 'Calibrating evaporation voltage.'
            yield self.toggleShutter(None)
            yield self.toggleEvap(None)
            #If this thickness is reached, then then evaporator stops evaporating. Units of angstroms.  
            self.desiredThk = 20000
            self.getBaseVoltage()
            
    def getBaseVoltage(self):
        if self.evapInProgress:
            #Times out if evaporate too much material (whatever set by the desiredThk in autoEvapPhase2)
            #Add functionality to auto stop if hit max voltage. For now this is done manually. 
            max = np.max(np.abs(self.dep_data[-self.checkPoints:,1] - self.setPoint))
            if max >= self.max_diff and self.evaporating:
                self.evapTimer.singleShot(5000,self.getBaseVoltage)
            elif max <= self.max_diff and self.evaporating:
                self.evapVoltage = np.average(self.volt_data[-self.checkPoints:,1])
                self.autoEvapPhase3()
            elif self.evaporating == False:
                self.textEdit2.setText("Took too long to reach equilibrium evaporating rate. Make sure" + 
                " there's enough lead in the evaporator.")
    
    @inlineCallbacks
    def autoEvapPhase3(self):
        if self.evapInProgress:
            #Close the shutter and stops evaporating
            yield self.toggleShutter(None)
            yield self.toggleEvap(None)
            
            #Set the offset voltage to the 
            self.PID.setVOff(self.evapVoltage)
            self.vOffStatus.setText(str(self.evapVoltage))
            
            angle = (360 - 2*self.contactAngle)/2
            yield self.ss.rot('B',str(int(angle)),'C')
            
            self.textEdit2.setText("Base voltage chosen as " + str(self.evapVoltage) + ". Rotating " 
            + str(angle) + " degrees to first contact evaporation.")
            print "Base voltage chosen as " + str(self.evapVoltage) + ". Rotating " + str(angle) + " degrees to first contact evaporation."
            self.pauseUntilRotated1()
            
    @inlineCallbacks
    def pauseUntilRotated1(self):
        if self.evapInProgress:
            status = yield self.ss.status()
            if status.startswith('turning'):
                self.evapTimer.singleShot(1000,self.pauseUntilRotated1)
            else:
                self.autoEvapPhase4()
                
    @inlineCallbacks
    def autoEvapPhase4(self):
        if self.evapInProgress:
            self.PID.setKd(0)
            self.PID.setKp(0)
            self.PID.setKi(0)
            self.PID.setIntegrator(0)
            self.derivStatus.setText(str(0))
            self.propStatus.setText(str(0))
            self.intStatus.setText(str(0))
            #make sure thickness is zeroed
            yield self.ftm.zero_rates_thickness()
            #Start evaporating with shutter closed 
            yield self.toggleEvap(None)
            #Sit at the determined voltage for a minute to get up to desired evaporation rate
            self.textEdit2.setText("Contact evaporation angle reached. Preheating lead before sample deposition.")
            print "Contact evaporation angle reached. Preheating lead before sample deposition."
            self.evapTimer.singleShot(45000,self.autoEvapPhase5)
            
    @inlineCallbacks
    def autoEvapPhase5(self):
        if self.evapInProgress:
            self.desiredThk = self.contactThk
            #Open shutter
            yield self.toggleShutter(None)
            self.textEdit2.setText("Shutter opened. Evaporating first contact.")
            print "Shutter opened. Evaporating first contact."
            #Give a couple seconds for ftm to read correctly
            self.evapTimer.singleShot(5000,self.autoEvapPhase6)
            
    def autoEvapPhase6(self):
        if self.evapInProgress:
            #Set PID parameters back to achieve as constant an evaporation rate as possible
            self.PID.setKd(0)
            self.PID.setKp(0)
            self.PID.setKi(0.001)
            self.PID.setIntegrator(0)
            self.derivStatus.setText(str(0))
            self.propStatus.setText(str(0))
            self.intStatus.setText(str(0.001))
            self.textEdit2.setText("Evaporating first contact. PID enabled.")
            print "Evaporating first contact. PID enabled."
            self.waitForEvap1()
            
    def waitForEvap1(self):
        if self.evapInProgress:
            if self.evaporating:
                self.evapVoltage = self.volt_data[-1,1]
                self.evapTimer.singleShot(1000,self.waitForEvap1)
            else: 
                self.autoEvapPhase7()
            #Add a way to check that the evaporation was successful. 
        
    @inlineCallbacks
    def autoEvapPhase7(self):
        if self.evapInProgress:
            #Set the offset voltage to the updated value from the previous evaporation
            self.PID.setVOff(self.evapVoltage)
            self.vOffStatus.setText(str(self.evapVoltage))
            
            angle = self.contactAngle
            yield self.ss.rot('B',str(int(angle)),'C')
            self.textEdit2.setText("Base voltage updated to " + str(self.evapVoltage) + ". Rotating " 
            + str(angle) + " degrees to head on evaporation.")
            print "Base voltage updated to " + str(self.evapVoltage) + ". Rotating " + str(angle) + " degrees to head on evaporation."
            self.pauseUntilRotated2()
        
    @inlineCallbacks
    def pauseUntilRotated2(self):
        if self.evapInProgress:
            status = yield self.ss.status()
            if status.startswith('turning'):
                self.evapTimer.singleShot(1000,self.pauseUntilRotated2)
            else:
                self.autoEvapPhase8()  
        
    @inlineCallbacks
    def autoEvapPhase8(self):
        if self.evapInProgress:
            self.PID.setKd(0)
            self.PID.setKp(0)
            self.PID.setKi(0)
            self.PID.setIntegrator(0)
            self.derivStatus.setText(str(0))
            self.propStatus.setText(str(0))
            self.intStatus.setText(str(0))
            #make sure thickness is zeroed
            yield self.ftm.zero_rates_thickness()
            #Start evaporating with shutter closed 
            self.desiredThk = 20000
            yield self.toggleEvap(None)
            #Sit at the determined voltage for a minute to get up to desired evaporation rate
            self.textEdit2.setText("Head on orientation reached. Preheating lead before sample deposition.")
            print "Head on orientation reached. Preheating lead before sample deposition."
            self.evapTimer.singleShot(45000,self.autoEvapPhase9)
    
    @inlineCallbacks
    def autoEvapPhase9(self):
        if self.evapInProgress:
            #Set thickness to head on evaporation thickness. Eventuall add (if ==0, then skip)
            self.desiredThk = self.headThk
            #Open shutter
            yield self.toggleShutter(None)
            #Give a couple seconds for ftm to read correctly
            self.textEdit2.setText("Shutter opened. Evaporating head on.")
            print "Shutter opened. Evaporating head on."
            self.evapTimer.singleShot(5000,self.autoEvapPhase10)
            
    def autoEvapPhase10(self):
        if self.evapInProgress:
            #Set PID parameters back to achieve as constant an evaporation rate as possible
            self.PID.setKd(0)
            self.PID.setKp(0)
            self.PID.setKi(0.001)
            self.PID.setIntegrator(0)
            self.derivStatus.setText(str(0))
            self.propStatus.setText(str(0))
            self.intStatus.setText(str(0.001))
            self.textEdit2.setText("Evaporating head on. PID on.")
            print "Evaporating head on. PID on."
            self.waitForEvap2()
            
    def waitForEvap2(self):
        if self.evapInProgress:
            if self.evaporating:
                self.evapVoltage = self.volt_data[-1,1]
                self.evapTimer.singleShot(1000,self.waitForEvap2)
            else: 
                self.autoEvapPhase11()
            #Add a way to check that the evaporation was successful. 
    
    @inlineCallbacks
    def autoEvapPhase11(self):
        if self.evapInProgress:
            #Set the offset voltage to the updated value from the previous evaporation
            self.PID.setVOff(self.evapVoltage)
            self.vOffStatus.setText(str(self.evapVoltage))
            
            angle = self.contactAngle
            yield self.ss.rot('B',str(int(angle)),'C')

            self.textEdit2.setText("Base voltage updated to " + str(self.evapVoltage) + ". Rotating " 
            + str(angle) + " degrees to second contact evaporation.")
            print "Base voltage updated to " + str(self.evapVoltage) + ". Rotating " + str(angle) + " degrees to second contact evaporation."
            self.pauseUntilRotated3()
            
    @inlineCallbacks
    def pauseUntilRotated3(self):
        if self.evapInProgress:
            status = yield self.ss.status()
            if status.startswith('turning'):
                self.evapTimer.singleShot(1000,self.pauseUntilRotated3)
            else:
                self.autoEvapPhase12() 
           
    @inlineCallbacks
    def autoEvapPhase12(self):
        if self.evapInProgress:
            self.PID.setKd(0)
            self.PID.setKp(0)
            self.PID.setKi(0)
            self.PID.setIntegrator(0)
            self.derivStatus.setText(str(0))
            self.propStatus.setText(str(0))
            self.intStatus.setText(str(0))
            #make sure thickness is zeroed
            yield self.ftm.zero_rates_thickness()
            #Start evaporating with shutter closed 
            self.desiredThk = 20000
            yield self.toggleEvap(None)
            #Sit at the determined voltage for a minute to get up to desired evaporation rate
            self.textEdit2.setText("Second contact orientation reached. Preheating lead before sample deposition.")
            print "Second contact orientation reached. Preheating lead before sample deposition."
            self.evapTimer.singleShot(45000,self.autoEvapPhase13)

    @inlineCallbacks
    def autoEvapPhase13(self):
        if self.evapInProgress:
            #Set thickness to head on evaporation thickness (eventually skip if 0)
            self.desiredThk = self.contactThk
            #Open shutter
            yield self.toggleShutter(None)
            self.textEdit2.setText("Shutter opened. Evaporating second contact.")
            print "Shutter opened. Evaporating second contact."
            self.evapTimer.singleShot(5000,self.autoEvapPhase14)
            
    def autoEvapPhase14(self):
        if self.evapInProgress:
            #Set PID parameters back to achieve as constant an evaporation rate as possible
            self.PID.setKd(0)
            self.PID.setKp(0)
            self.PID.setKi(0.001)
            self.PID.setIntegrator(0)
            self.derivStatus.setText(str(0))
            self.propStatus.setText(str(0))
            self.intStatus.setText(str(0.001))
            self.textEdit2.setText("Evaporating second contact. PID on.")
            print "Evaporating second contact. PID on."
            self.waitForEvap3()
            
    def waitForEvap3(self):
        if self.evapInProgress:
            if self.evaporating:
                self.evapVoltage = self.volt_data[-1,1]
                self.evapTimer.singleShot(1000,self.waitForEvap3)
            else: 
                self.autoEvapPhase15()
            #Add a way to check that the evaporation was successful. 
        
    @inlineCallbacks
    def autoEvapPhase15(self):
        if self.evapInProgress:
            #Set the offset voltage to the updated value from the previous evaporation
            self.PID.setVOff(self.evapVoltage)
            self.vOffStatus.setText(str(self.evapVoltage))
            
            angle = (360-2*self.contactAngle)/2
            yield self.ss.rot('B',str(int(angle)),'C')
            
            self.textEdit2.setText("Returning to original orientation.")
            print "Returning to original orientation."
            self.pauseUntilRotated4()
        
    @inlineCallbacks
    def pauseUntilRotated4(self):
        if self.evapInProgress:
            status = yield self.ss.status()
            if status.startswith('turning'):
                self.evapTimer.singleShot(1000,self.pauseUntilRotated4)
            else:
                self.textEdit2.setText("Three angle evaporation complete.")
                print "Three angle evaporation complete."
                self.evapInProgress = False
                self.unlock_interface()
                self.startAuto.setStyleSheet("#startAuto{font: 14pt \"MS Shell Dlg 2\"; border-width: 0px;" + 
                "border-style: solid; border-radius: 20px; background: green; color: rgb(212,212,212);}")
        
    @inlineCallbacks
    def emergStopEvap(self,cntx):
        #Emergency stop everything here
        self.evapInProgress = False
        self.evapTimer.stop()
        self.textEdit2.setText("Evaporation Aborted.")
        self.startAuto.setStyleSheet("#startAuto{font: 14pt \"MS Shell Dlg 2\"; border-width: 0px;" + 
            "border-style: solid; border-radius: 20px; background: green; color: rgb(212,212,212);}")
        self.unlock_interface()
        yield self.close_valve(cntx)
        if self.evaporating:
            yield self.toggleEvap(cntx)
        if self.powerSupplyState != "Off":
            yield self.togglePowerSupply(cntx)    
        if self.boatShutterStatus.text() != "Closed":
            yield self.toggleShutter(cntx)
        
        
#----------------------------------------------------------------------------------------------#
    """ The following section has useful functions called throughout the program. """
    
    
    def lock_interface(self):
        self.dataCollectorWidget.lock_buttons()
        
        self.pushChooseDir.setEnabled(False)
        self.pushConnect.setEnabled(False)
        
        self.scrollValveButton.setEnabled(False)
        self.turboValveButton.setEnabled(False)
        self.gateValveButton.setEnabled(False)
        self.boatShutterButton.setEnabled(False)
        self.boatShutterButton_2.setEnabled(False)
        self.powerSupplyButton.setEnabled(False)
        self.scrollPumpButton.setEnabled(False)
        self.turboPumpButton.setEnabled(False)
        self.heliumValveButton.setEnabled(False)
        self.heliumValveButton_2.setEnabled(False)
        
        self.setPointButton.setEnabled(False)
        self.thermTimeButton.setEnabled(False)
        self.thermPrsButton.setEnabled(False)
        self.angleButton.setEnabled(False)
        self.contactThkButton.setEnabled(False)
        self.headThkButton.setEnabled(False)
        
        self.propButton.setEnabled(False)
        self.intButton.setEnabled(False)
        self.intMaxButton.setEnabled(False)
        self.intMinButton.setEnabled(False)
        self.derivButton.setEnabled(False)
        self.vMaxButton.setEnabled(False)
        self.vOffButton.setEnabled(False)
        
        self.startAuto.setEnabled(False)
        
        self.evapStartButton.setEnabled(False)
        
        self.nomPressButton.setEnabled(False)
        self.nomPressButton_2.setEnabled(False)
        
        self.shutterCWButton.setEnabled(False)
        self.shutterCCWButton.setEnabled(False)
        self.cryoCWButton.setEnabled(False)
        self.cryoCCWButton.setEnabled(False)
        
    def unlock_interface(self):
        self.dataCollectorWidget.unlock_buttons()
        
        self.pushChooseDir.setEnabled(True)
        self.pushConnect.setEnabled(True)
        
        self.scrollValveButton.setEnabled(True)
        self.turboValveButton.setEnabled(True)
        self.gateValveButton.setEnabled(True)
        self.boatShutterButton.setEnabled(True)
        self.boatShutterButton_2.setEnabled(True)
        self.powerSupplyButton.setEnabled(True)
        self.scrollPumpButton.setEnabled(True)
        self.turboPumpButton.setEnabled(True)
        self.heliumValveButton.setEnabled(True)
        self.heliumValveButton_2.setEnabled(True)
        
        self.setPointButton.setEnabled(True)
        self.thermTimeButton.setEnabled(True)
        self.thermPrsButton.setEnabled(True)
        self.angleButton.setEnabled(True)
        self.contactThkButton.setEnabled(True)
        self.headThkButton.setEnabled(True)
        
        self.propButton.setEnabled(True)
        self.intButton.setEnabled(True)
        self.intMaxButton.setEnabled(True)
        self.intMinButton.setEnabled(True)
        self.derivButton.setEnabled(True)
        self.vMaxButton.setEnabled(True)
        self.vOffButton.setEnabled(True)
        
        self.startAuto.setEnabled(True)
        
        self.evapStartButton.setEnabled(True)
        
        self.nomPressButton.setEnabled(True)
        self.nomPressButton_2.setEnabled(True)
        
        self.shutterCWButton.setEnabled(True)
        self.shutterCCWButton.setEnabled(True)
        self.cryoCWButton.setEnabled(True)
        self.cryoCCWButton.setEnabled(True)
        
    def doNothing(self):
        print 'Doing nothing!'
        #self.textEdit2.setText("You have reached the do nothing command!")
        
#----------------------------------------------------------------------------------------------#      
    """ The following section specifies closing actions taken by the GUI when disconnecting."""

    def closeEvent(self, e):
        if self.isConnected:
            self.disconnect()
        self.reactor.stop()
        print 'Reactor shut down and stopped collecting data.'
        
    @inlineCallbacks
    def disconnect(self):
        print 'Closing all existing labrad connections.'
        self.dataCollectorWidget.disconnect()
        yield self.cxn_gph.disconnect()
        self.cxn_gph = None
        yield self.cxn_gph2.disconnect()
        self.cxn_gph2 = None
        yield self.cxn_prs.disconnect()
        self.cxn_prs = None
        yield self.cxn_dep.disconnect()
        self.cxn_dep = None
        yield self.cxn_thk.disconnect()
        self.cxn_thk = None
        yield self.cxn.disconnect()
        self.cxn = None
        print 'Evaporator GUI connections are closed.'
        
        
#----------------------------------------------------------------------------------------------#
            
""" The following runs the GUI"""

if __name__=="__main__":
    app = QtGui.QApplication( [] )
    import qt4reactor
    qt4reactor.install()
    from twisted.internet import reactor
    window = MainWindow(reactor)
    window.show()
    reactor.run()
    
