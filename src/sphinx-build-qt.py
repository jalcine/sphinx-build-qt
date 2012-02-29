SPHINX_BUILD='sphinx-build'

import sys
from PyQt4.QtCore import (QProcess, QString, QVariant, QSettings, QSize, QPoint)
from PyQt4.QtGui import (QApplication, QDialog, QFileDialog)
from ui_dialog import Ui_Dialog

#__version__ = '0.2'

class Dlg(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(Dlg, self).__init__(parent)
        self.setupUi(self)
        self.dockWidget.hide()
        self.fileLineEdit.setDisabled(True)
        self.fileButton.setDisabled(True)
        
        self.closeButton.clicked.connect(self.close)
        self.buildButton.clicked.connect(self.build)
        self.fileButton.clicked.connect(self.getFile)
        self.fileRadioButton.toggled.connect(self.fileLineEdit.setEnabled)
        self.fileRadioButton.toggled.connect(self.fileButton.setEnabled)
        self.logButton.toggled.connect(self.dockWidget.setVisible)
        
        for button in (self.sourceButton, self.outputButton):
            button.clicked.connect(self.getDirectory)
            
        self.sourceDirectory = None
        self.outputDirectory = None
        
        self.process = QProcess()
        self.process.readyReadStandardOutput.connect(self.readOutput)
        self.process.readyReadStandardError.connect(self.readErrors)
        
        #restore settings
        settings = QSettings()
        size = settings.value('Dialog/Size', QVariant(QSize(600, 500))).toSize()
        self.resize(size)
        pos = settings.value('Dialog/Position', QVariant(QPoint(0, 0))).toPoint()
        self.move(pos)

        for widget, setting in ((self.sourceLineEdit, 'Data/SourceDirectory'),
                              (self.outputLineEdit, 'Data/OutputDirectory')):
            widget.setText(settings.value(setting).toString())
            

    def closeEvent(self, event):
        """Save settings and exit"""
        settings = QSettings()
        for value, setting in ((self.size(), 'Dialog/Size'), 
                              (self.pos(), 'Dialog/Position'), 
                              (self.sourceDirectory, 'Data/SourceDirectory'), 
                              (self.outputDirectory, 'Data/OutputDirectory')):
                settings.setValue(setting, QVariant(value))

    def getDirectory(self):
        """Opens the platform dialog to select directory"""
        sender = self.sender()
        if sender is self.sourceButton:
            receiver = self.sourceLineEdit
        elif sender is self.outputButton:
            receiver = self.outputLineEdit

        fname = QFileDialog.getExistingDirectory(self, 'Select Directory') 
        if fname:
            receiver.setText(fname)
            
    def getFile(self):
        """Opens the platform file open dialog to select a file"""
        if not self.sourceDirectory:
            source_dir =  self.sourceLineEdit.text()
        else:
            source_dir = self.sourceDirectory
        fname = QFileDialog.getOpenFileName(self, 'Select File', source_dir)
        if fname:
            self.fileLineEdit.setText(fname)
    
    def build(self):
        """Main function calling sphinx-build to generate the project"""
        self.statusLabel.clear()
        self.buildButton.setDisabled(True)
        self.sourceDirectory = str(self.sourceLineEdit.text().trimmed())
        self.outputDirectory = str(self.outputLineEdit.text().trimmed())
        
        if not len(self.sourceDirectory):
            self.logBrowser.append('Source directory cannot be empty')
        if not len(self.outputDirectory):
            self.logBrowser.append('Output directory cannot be empty')

        if not(len(self.sourceDirectory) or len(self.outputDirectory)):
            self.buildButton.setDisabled(False)
            return
        
        self.logBrowser.clear()
        self.logBrowser.append(self.formatInfoMsg('Building. Please wait...'))
        
        fname = None
        if self.fileRadioButton.isChecked():
            fname = str(self.fileLineEdit.text().trimmed())
            
        args = ['-b', 'html', self.sourceDirectory, self.outputDirectory]
        if fname:
            args.append(fname)
        self.statusLabel.setText(self.formatInfoMsg('Running sphinx-build...'))
        QApplication.processEvents()
        
        self.process.start(SPHINX_BUILD, args)
        if (not self.process.waitForFinished(-1)):
            msg = self.formatErrorMsg('Build Failed!')
            self.logBrowser.append(msg)
            self.statusLabel.setText(msg)
            self.buildButton.setEnabled(True)
            return
        
        QApplication.processEvents()
        self.buildButton.setEnabled(True)
        self.statusLabel.setText(self.formatInfoMsg('Finished'))
        
    def readOutput(self):
        """Read and append sphinx-build output to the logBrowser"""
        msg = str(QString(self.process.readAllStandardOutput()))
        self.logBrowser.append(msg)
        
    def readErrors(self):
        """Read and append sphinx-build errors to the logBrowser"""
        msg = str(QString(self.process.readAllStandardError()))
        self.logBrowser.append(self.formatErrorMsg(msg))
        
    def formatErrorMsg(self, msg):
        """Format error messages in red color"""
        return self.formatMsg(msg, 'red')
        
    def formatInfoMsg(self, msg):
        """Format informative messages in blue color"""
        return self.formatMsg(msg, 'blue')
    
    def formatMsg(self, msg, color):
        """Format message with the given color"""
        msg = '<font color="%s">%s</font>' % (color, msg)
        return msg

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setOrganizationName("vkvn")
    app.setOrganizationDomain("vimalkumar.in")
    app.setApplicationName("sphinx-build-qt")
#    app.setWindowIcon(QIcon(":/logo.png"))
    
    dialog = Dlg()
    dialog.show()
    sys.exit(app.exec_())
    
