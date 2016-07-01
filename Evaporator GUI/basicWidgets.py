from PyQt4 import QtCore as core, QtGui as gui



class label(gui.QLineEdit):
    def __init__(
        self,
        parent,
        position,
        size,
        text='',
        tooltip = None,
        ):

        super(label,self).__init__(parent)
        self.setFixedSize(size[0],size[1])
        self.move(position[0],position[1])
        if tooltip != None:self.setToolTip(tooltip)
        self.setReadOnly(True)
        self.setText(text)

class stringInput(gui.QLineEdit):
    def __init__(
        self,
        parent,
        position,
        size,
        default_text='',
        placeholder_text=None,
        tooltip = None,
        ):

        super(stringInput,self).__init__(parent)
        self.setFixedSize(size[0],size[1])
        self.move(position[0],position[1])
        if tooltip != None:self.setToolTip(tooltip)
        self.setText(default_text)
        if not (placeholder_text == None):
            self.setPlaceholderText(placeholder_text)

class simpleButton(gui.QPushButton):
    def __init__(
        self,
        parent,
        position,
        size,
        text,
        function,
        tooltip = None,
        ):

        super(simpleButton,self).__init__(text,parent)
        self.setFixedSize(size[0],size[1])
        self.move(position[0],position[1])
        if tooltip != None:self.setToolTip(tooltip)
        self.pressed.connect(function)

class simpleList(gui.QListWidget):
    def __init__(
        self,
        parent,
        position,
        size,
        items,
        tooltip = None,
        ):

        super(simpleList,self).__init__(parent)
        self.size     = size
        self.items    = items
        self.position = position

        self.setFixedSize(self.size[0],self.size[1])
        self.move(self.position[0],self.position[1])
        if tooltip != None:self.setToolTip(tooltip)

        self.updateItems(items)

    def updateItems(self,items):
        self.clear()
        for item in items:
            self.addItem(item)


class textBox(gui.QPlainTextEdit):
    def __init__(
        self,
        parent,
        position,
        size,
        text,
        line_wrap = 1,
        tooltip = None,
        ):

        super(textBox,self).__init__(parent)

        self.position = position
        self.size     = size

        self.setFixedSize(size[0],size[1])
        self.move(position[0],position[1])
        if tooltip != None:self.setToolTip(tooltip)

        self.setReadOnly(True)
        self.setLineWrapMode(line_wrap)
        self.setPlainText(text)