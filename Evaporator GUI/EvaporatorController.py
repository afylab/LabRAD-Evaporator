import pyqtgraph as pg
from PyQt4 import QtGui, QtCore
from twisted.internet.defer import inlineCallbacks
import numpy as np
import EvaporatorUI

class MainWindow(QtGui.QMainWindow, EvaporatorUI.Ui_MainWindow):
    """
    Overall computer interface for Evaporator.  
    
    TO DO: Start and stop buttons for data collector.
    TO DO: Print to GUI screen when something happens. Ie: Successfully connect to server. 
           Or: failed to connect because x y z. WORK IN PROGRESS
    TO DO ON GUI: Add area on main page for buttons to run
    common scripts. 
    """
    
    #----------------------------------------------------------------------------------------------#
            
    """ The following section initializes, or defines the initialization of the GUI and 
    connecting to servers."""

    ID_NEWSET = 00001
    ID_NEWDATA = 00002
    ID_NEWPARAM = 00003

    def __init__(self, reactor, parent=None):
        """
        Evaporator GUI
        :param reactor:
        :param parent:
        :return:
        """
        super(MainWindow, self).__init__(parent)
        self.reactor = reactor
        self.setupUi(self)
        #self.setFixedSize(1366,768)

        self.directory_path = ""
        self.num_points = 50
        
        self.DataCollector = None
        
        #initalize plots
        self.initPlots()
        
        #Initialize power supply and pumps as off. 
        self.powerSupplyState = 'Off'
        self.scrollPumpState = 'Off'
        self.turboPumpState = 'Off'
        
        #Define what happens when interacting with buttons
        self.comboGraph.activated[str].connect(self.selectData)
        self.comboGraph2.activated[str].connect(self.selectData2)
        self.pushChooseDir.clicked.connect(self.promptDirectory)
        self.pushConnect.clicked.connect(self.connect)
        self.sliderGraph.valueChanged[int].connect(self.set_num_points)
        self.sliderLCD.display(self.num_points)
        
        self.scrollValveButton.clicked.connect(self.toggleScrollValve)
        self.turboValveButton.clicked.connect(self.toggleTurboValve)
        self.gateValveButton.clicked.connect(self.toggleGateValve)
        self.boatShutterButton.clicked.connect(self.toggleShutter)
        self.powerSupplyButton.clicked.connect(self.togglePowerSupply)
        self.scrollPumpButton.clicked.connect(self.toggleScrollPump)
        self.turboPumpButton.clicked.connect(self.toggleTurboPump)
        self.heliumFlowButton.clicked.connect(self.toggleHeliumFlow)
                   
    @inlineCallbacks
    def connect(self, cntx):
        """ Each connection can only monitor one dataset at a time. This function creates 
        a connection and signals for each dataset that needs to be simultaneously monitored.
        Then, it runs the data collector connect function."""
        try:
            from labrad.wrappers import connectAsync
            
            #This connect is used for updating the graph 1 on the Details tab. 
            
            self.cxn_gph = yield connectAsync(name = 'Evaporator GUI')
            self.dv_gph = self.cxn_gph.data_vault
            #Set signal ID for creation of new dataset
            yield self.dv_gph.signal__new_dataset(self.ID_NEWSET)
            yield self.dv_gph.addListener(listener=self.add_dataset_gph, source=None, ID=self.ID_NEWSET)
            yield self.dv_gph.signal__data_available(self.ID_NEWDATA)
            yield self.dv_gph.addListener(listener=self.update_gph, source=None, ID=self.ID_NEWDATA)
            yield self.dv_gph.signal__new_parameter(self.ID_NEWPARAM)
            yield self.dv_gph.addListener(listener=self.update_params_gph, source=None, ID=self.ID_NEWPARAM)
            
            #This connect is used for updating the graph 2 on the Details tab. 
            self.cxn_gph2 = yield connectAsync(name = 'Evaporator GUI')
            self.dv_gph2 = self.cxn_gph2.data_vault
            #No need to signal ID for creation of new dataset since first graph will documents all the creations. 
            #yield self.dv_gph2.signal__new_dataset(self.ID_NEWSET)
            #yield self.dv_gph2.addListener(listener=self.add_dataset_gph, source=None, ID=self.ID_NEWSET)
            yield self.dv_gph2.signal__data_available(self.ID_NEWDATA)
            yield self.dv_gph2.addListener(listener=self.update_gph2, source=None, ID=self.ID_NEWDATA)
            yield self.dv_gph2.signal__new_parameter(self.ID_NEWPARAM)
            yield self.dv_gph2.addListener(listener=self.update_params_gph2, source=None, ID=self.ID_NEWPARAM)
                 
            #Next, create a connection for connecting to each server from which we want constant updates. 
            #Ie, create a cxn_prs for monitoring pressure for front pannel. 
            self.cxn_prs = yield connectAsync(name = 'Evaporator GUI')
            self.dv_prs = self.cxn_prs.data_vault
            
            yield self.dv_prs.signal__new_dataset(self.ID_NEWSET)
            yield self.dv_prs.addListener(listener=self.add_dataset_prs, source=None, ID=self.ID_NEWSET)
            yield self.dv_prs.signal__data_available(self.ID_NEWDATA)
            yield self.dv_prs.addListener(listener=self.update_prs, source=None, ID=self.ID_NEWDATA)
            yield self.dv_prs.signal__new_parameter(self.ID_NEWPARAM)
            yield self.dv_prs.addListener(listener=self.update_params_prs, source=None, ID=self.ID_NEWPARAM)
            
            #Have the data collector connect
            self.dataCollectorWidget.connect()
            
            #Have the dvFileSelect connect with a connection that won't mess with any other connections, so 
            #you can browse files without causing trouble. 
            self.cxn = yield connectAsync(name = 'Evaporator GUI')
            self.dvFileSelect.setConnection(self.cxn)
            self.vrs = self.cxn.valve_relay_server
            yield self.vrs.select_device()
            
            self.textEdit.setPlainText('Successfully connected graphical interface and data collector to servers')
        except:
            self.textEdit.setPlainText('Could not detect valve/relay box.')
           
    @inlineCallbacks
    def promptDirectory(self, cntx): 
        #Eventually replace this with running Brunel's dv file select application. 
        #Sets the directory of the data collector and all the other to the dv file select location
        self.directory_path = self.dvFileSelect.current_directory
        
        print self.directory_path
        yield self.dv_gph.cd(self.directory_path)
        yield self.dv_gph2.cd(self.directory_path)
        yield self.dv_prs.cd(self.directory_path)
        self.dataCollectorWidget.setDirectory(self.directory_path)
        
        self.textEdit.setPlainText('Successfully natigated to vault\\' + self.directory_path[1] + "\\"
                + self.directory_path[2])
        
    def initPlots(self):
        #Set initial plot display
        self.plot.setTitle('Choose Data for Display')
        self.plot.setLabel('right','')
        self.plot.setLabel('left', '')
        self.plot.setLabel('bottom', '')  

        self.plot2.setTitle('Choose Data for Display')
        self.plot2.setLabel('right','')
        self.plot2.setLabel('left', '')
        self.plot2.setLabel('bottom', '')          
        
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
        #Take all the data points
        data = yield self.dv_gph.get(10000000,True)
        
        #Clears points off of screen
        self.plot.clear()
            
        #Graphs the latest x data points
        if len(data[:,0])<self.num_points:
            self.plot.plot(data[:,0],data[:,1])
        else:
            self.plot.plot(data[-self.num_points:,0],data[-self.num_points:,1])   
        #Could be re-written in a more memory efficient way if it ends up mattering. 
        # Can also look into pyqt graph 
        
    @inlineCallbacks
    def update_gph2(self, cntx, signal):
        #Take all the data points
        data = yield self.dv_gph2.get(10000000,True)
        
        #Clears points off of screen
        self.plot2.clear()
            
        #Graphs the latest x data points
        if len(data[:,0])<self.num_points:
            self.plot2.plot(data[:,0],data[:,1])
        else:
            self.plot2.plot(data[-self.num_points:,0],data[-self.num_points:,1])   
        #Could be re-written in a more memory efficient way if it ends up mattering. 
        # Can also look into pyqt graph 
            
    @inlineCallbacks
    def update_params_gph(self, cntx, signal):
        #Currently not used
        print signal
        print "params updated"
        params = yield self.dv_gph.get_parameters()
        
    @inlineCallbacks
    def update_params_gph2(self, cntx, signal):
        #Currently not used
        print signal
        print "params updated"
        params = yield self.dv_gph.get_parameters()
        
    def set_num_points(self,num_points):
        #AT SOME POINT UPDATE THIS TO BE NOT NUMBER OF POINTS, BUT NUMBER OF SECONDS
        self.num_points = int(50 + num_points**1.4922)
        self.sliderLCD.display(self.num_points)
        #self.update(cntx = None, )
          
    @inlineCallbacks
    def selectData(self,data_name):
        name = str(data_name)
        yield self.dv_gph.open(name)
        print 'Opened file in graph 1: ' + name
        self.plot.setTitle(name[8:])
        
        if name[8:] == 'Random vs. Time':
            self.plot.setLabel('left', 'Random')
            self.plot.setLabel('bottom', 'Time','s')   
        elif name[8:] == 'Time vs. Time':
            self.plot.setLabel('left', 'Time','s')
            self.plot.setLabel('bottom', 'Time','s') 
            
    @inlineCallbacks
    def selectData2(self,data_name):
        name = str(data_name)
        yield self.dv_gph2.open(name)
        print 'Opened file in graph 2: ' + name
        self.plot2.setTitle(name[8:])
        
        if name[8:] == 'Random vs. Time':
            self.plot2.setLabel('left', 'Random')
            self.plot2.setLabel('bottom', 'Time','s')   
        elif name[8:] == 'Time vs. Time':
            self.plot2.setLabel('left', 'Time','s')
            self.plot2.setLabel('bottom', 'Time','s') 
        
#----------------------------------------------------------------------------------------------#   
    """ The following section has functions for creating and updating the pressure on the 
    graphical interface """
        
    def add_dataset_prs(self, cntx, signal):
        if signal[8:] == 'Pressure vs. Time':
            self.dv_prs.open(signal)
            print 'Pressure is now being monitored'
        
    @inlineCallbacks
    def update_prs(self, cntx, signal):
        #Get new data point
        data = yield self.dv_prs.get()
        data_string = str(data[0,1])
        self.pressureStatus.setText(data_string[0:6])
        
    @inlineCallbacks
    def update_params_prs(self, cntx, signal):
        #Currently not used
        print signal
        print "params updated"
        params = yield self.dv_prs.get_parameters()

#----------------------------------------------------------------------------------------------#
            
    """ The following section specifies the actions of all the buttons in the Graphical
    Interface tab"""
       
    def toggleHeliumFlow(self):
        if self.heliumFlowStatus.text() == 'Flowing':
            self.heliumFlowStatus.setText('Not Flowing')
            self.heliumFlowButton.setStyleSheet("#heliumFlowButton{border-color:"
            "rgb(255, 255, 255); border-width: 4px;border-style: solid;  " +
            "border-radius: 25px;background: black;}")
        elif self.heliumFlowStatus.text() == 'Not Flowing':
            self.heliumFlowStatus.setText('Flowing')
            self.heliumFlowButton.setStyleSheet("#heliumFlowButton{border-color:"
            "rgb(255, 255, 255); border-width: 4px;border-style: solid;  " +
            "border-radius: 25px;background: white;}")
        
    def toggleScrollPump(self):
        if self.scrollPumpState == 'Off':
            self.scrollPumpState = 'On'
            self.scrollPumpButton.setStyleSheet("image:url(:/OnOff/On3.png);"
            + "background: black;")
        elif self.scrollPumpState == 'On':
            self.scrollPumpState = 'Off'
            self.scrollPumpButton.setStyleSheet("image:url(:/OnOff/Off2.png);"
            + "background: black;")  
        
    def toggleTurboPump(self):
        if self.turboPumpState == 'Off':
            self.turboPumpState = 'On'
            self.turboPumpButton.setStyleSheet("image:url(:/OnOff/On3.png);"
            + "background: black;")
        elif self.turboPumpState == 'On':
            self.turboPumpState = 'Off'
            self.turboPumpButton.setStyleSheet("image:url(:/OnOff/Off2.png);"
            + "background: black;")  
        
    def togglePowerSupply(self):
        if self.powerSupplyState == 'Off':
            self.powerSupplyState = 'On'
            self.powerSupplyButton.setStyleSheet("image:url(:/OnOff/On3.png);"
            + "background: black;")
        elif self.powerSupplyState == 'On':
            self.powerSupplyState = 'Off'
            self.powerSupplyButton.setStyleSheet("image:url(:/OnOff/Off2.png);"
            + "background: black;")
    
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
            
    def toggleShutter(self):
        if self.boatShutterStatus.text() == 'Open':
            self.boatShutterStatus.setText('Closed')
            self.boatShutterButton.setStyleSheet("#boatShutterButton{border-color:"
            "rgb(255, 255, 255); border-width: 4px;border-style: solid;  " +
            "border-radius: 25px;background: black;}")
            
            
        elif self.boatShutterStatus.text() == 'Closed':
            self.boatShutterStatus.setText('Open')
            self.boatShutterButton.setStyleSheet("#boatShutterButton{border-color:"
            "rgb(255, 255, 255); border-width: 4px;border-style: solid;  " +
            "border-radius: 25px;background: white;}")   
#----------------------------------------------------------------------------------------------#
            
    """ The following section specifies closing actions taken by the GUI when disconnecting.
    Probably not necessary. """
    '''
    def closeEvent(self, e):
        self.reactor.stop()
        try:
            self.DataCollector.stop()
        except:
            print 'DataCollector not initialized'
        print "stop"
    '''
#----------------------------------------------------------------------------------------------#
            
""" The following runs the program"""

if __name__=="__main__":
    app = QtGui.QApplication( [] )
    import qt4reactor
    qt4reactor.install()
    from twisted.internet import reactor
    window = MainWindow(reactor)
    window.show()
    reactor.run()
    
