from PyQt4 import QtCore as core, QtGui as gui
from basicWidgets import label, stringInput, simpleButton, simpleList, textBox
from twisted.internet.defer import inlineCallbacks
#import labrad, os

class labradConnectWidget(gui.QWidget):
    def __init__(self,
        parent,
        position,
        connection_destinations = [],
        line_height   = 23,
        input_length  = 128,
        label_length  = 64,
        button_length = 64,
        status_length = 256,
        default_password = None,
        default_host     = "localhost",
        default_status   = "not connected",
        ):

        super(labradConnectWidget,self).__init__(parent)

        # This is a list of objects to send the connection to once it's been made
        # This widget will call object.setConnection(connection) for each object in the list
        self.connection_destinations = connection_destinations

        self.line_height   = line_height
        self.input_length  = input_length
        self.label_length  = label_length
        self.button_length = button_length
        self.status_length = status_length
        self.position      = position

        self.isConnected = False
        self.connection  = None

        self.default_status   = default_status 
        self.default_host     = default_host
        self.default_password = default_password if default_password else os.environ['LABRADPASSWORD']

        self.doUI()

    def setStatus(self,label):
        self.label_status.setText("Labrad satus: %s"%label)

    def connect(self):
        try:
            password = str(self.input_password.text())
            host     = str(self.input_host.text())
            self.connection  = labrad.connect(password = password, host = host)
            self.isConnected = True
            self.setStatus("Connected to '%s'"%host)
            self.label_console.setText("Success: connected to LabRAD")
            self.sendConnections()
        except:
            self.label_console.setText("Error: could not connect to LabRAD")

    def sendConnections(self):
        for obj in self.connection_destinations:
            try:obj.setConnection(self.connection)
            except:print("Warning: object <%s> failed to accept connection. May be missing method <setConnection>"%obj)
    def reset(self):
        self.input_password.setText(self.default_password)
        self.input_host.setText(self.default_host)
        self.label_console.setText("")


    def doUI(self):
        self.label_status = label(self,[0,0],[self.status_length,self.line_height],"","Status of the connection to LabRAD")
        self.setStatus(self.default_status)

        self.label_host     = label(self,       [0,self.line_height*1],[self.label_length,self.line_height],"host",    "Host IP for LabRAD connection")
        self.label_password = label(self,       [0,self.line_height*2],[self.label_length,self.line_height],"Password","Password for LabRAD connection")
        self.input_host     = stringInput(self, [self.label_length,self.line_height*1],[self.input_length,self.line_height],self.default_host,    "Enter host",           "Host IP for LabRAD connection")
        self.input_password = stringInput(self, [self.label_length,self.line_height*2],[self.input_length,self.line_height],self.default_password,"Enter LabRAD Password","Password for LabRAD connection")
        self.button_connect = simpleButton(self,[self.label_length+self.input_length,self.line_height*1],[self.button_length,self.line_height],"connect",self.connect,"Attempt to connect to LabRAD")
        self.button_reset   = simpleButton(self,[self.label_length+self.input_length,self.line_height*2],[self.button_length,self.line_height],"reset",  self.reset  ,"Reset IP & Host inputs to default values.\nNote: Does not terminate LabRAD connection if one has been made.")

        self.label_console  = label(self,[0,self.line_height*3],[self.status_length,self.line_height],"","This box will print the result of an attempted LabRAD connection.")

        self.setFixedSize(max([self.status_length,self.button_length+self.label_length+self.input_length]),self.line_height*4)
        self.move(self.position[0],self.position[1])


class dataVaultFileSelectWidget(gui.QWidget):
    def __init__(self,
        parent,
        position = [0,0],
        dv_destionations  = [],
        file_destinations = [],
        line_height       = 23,
        button_length     = 64,
        length            = 256,
        ):

        super(dataVaultFileSelectWidget,self).__init__(parent)
        self.position = position

        self.connection  = None
        self.isConnected = False
        self.current_directory = [""]

        self.dv_destionations  = dv_destionations  # List of objects to send DataVault connection to
        self.file_destinations = file_destinations # List of objects to send file paths to

        self.line_height    = line_height
        self.button_length  = button_length
        self.length         = length
        
        #self.directoryChangeSignal = core.pyqtSignal()
        
        self.doUI()

    def doUI(self):
        self.label_status = label(self, [0,0], [self.length,self.line_height],"","Status of connection to Data Vault")
        self.setStatus("LabRAD not connected")

        self.list_folders = simpleList(self,[0,self.line_height*1],[self.length,self.line_height*3],[],"List of folders in current directory")
        self.list_files   = simpleList(self,[0,self.line_height*5],[self.length,self.line_height*4],[],"List of files in current directory")

        self.button_open  = simpleButton(self,[self.length-self.button_length,self.line_height*4],[self.button_length,self.line_height],"select file",self.dvOpen,"Open the currently selected file")
        self.button_home  = simpleButton(self,[0                             ,self.line_height*4],[self.button_length,self.line_height],"home"       ,self.dvHome,"Return to the root directory")
        self.button_up    = simpleButton(self,[self.button_length            ,self.line_height*4],[self.button_length,self.line_height],"up"         ,self.dvUp  ,"Go up one folder from the current directory")
        #self.text_details = textBox(self,[0,self.line_height*9],[self.length,self.line_height*4],"",tooltip="Details of currently selected dataset (file)")

        self.list_folders.itemActivated.connect(self.dvSelectFolder)
        self.list_files.itemActivated.connect(self.dvOpen)
        #self.list_files.currentItemChanged.connect(self.dvUpdateDetails)


        self.setFixedSize(self.length,self.line_height*13)
        self.move(self.position[0],self.position[1])

    def setStatus(self,status):
        self.label_status.setText("DataVault status: %s"%status)
    
    
    def setConnection(self,connection):
        try:
            self.dv          = connection.data_vault
            self.isConnected = True
            self.dvSetDirectory(self.current_directory) # force update lists
            self.setStatus("DataVault connected")
            self.sendConnections()
            
        except:
            self.setStatus("DataVault not running")
            raise

    def sendConnections(self):
        """Sends the successful data vault connection to each specified object"""
        for obj in self.dv_destionations:
            try:obj.setDV(self.dv)
            except:print("Warning: object <%s> failed to accept DataVault connection. May be missing method <setDV>"%obj)
    
    @inlineCallbacks
    def dvSetDirectory(self,directory):
        """Sets the current directory and updates the lists"""
        self.current_directory = directory
        yield self.dv.cd(self.current_directory)
        folders, files = yield self.dv.dir()

        self.list_folders.updateItems(folders)
        self.list_files.updateItems(files)
        
        #self.directoryChangeSignal.emit()
        #Emit signal here with self.current_directory

    def dvSelectFolder(self,folder):
        """Changes directory to a selected folder in the current directory"""
        if self.isConnected:
            try:
                self.dvSetDirectory(self.current_directory+[str(folder.text())])
            except:
                print("Warning: tried to move to invalid folder")

    '''
    def dvUpdateDetails(self,current,previous):
        """Updates the details panel upon selecting a different file"""
        filename = str(current.text()) if current else None

        if filename == None:
            self.text_details.setPlainText("")

        else:    
            self.dv.open(filename)

            indep,dep = self.dv.variables()
            name      = self.dv.get_name()

            lines = [
                "Filename:\n %s\n"%name,
                "Dependents:\n %s\n"%dep,
                "Independents:\n %s"%indep,
            ]

            self.text_details.setPlainText(lines[0]+lines[1]+lines[2])
            
    '''

    def dvOpen(self,file=None):
        """If a valid file is chosen, send it to each object in self.file_destinations"""
        if self.isConnected:
            if file == None:
                filename = "" if self.list_files.currentItem() == None else str(self.list_files.currentItem().text())
            else:
                filename = str(file.text())

            if filename != "":

                for obj in self.file_destinations:
                    try:obj.pushFile(filename)
                    except:print("Warning: object <%s> failed to accept file. May be missing method <pushFile>"%obj)


    def dvHome(self):
        """Returns to the root directory"""
        if self.isConnected:
            self.dvSetDirectory([''])

    def dvUp(self):
        """Goes up one directory from the current directory"""
        if self.isConnected:
            if len(self.current_directory) > 1:self.dvSetDirectory(self.current_directory[:-1])
            else:self.dvSetDirectory([''])