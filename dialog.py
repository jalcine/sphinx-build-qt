import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui_dialog import Ui_Dialog

class Dlg(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(Dlg, self).__init__(parent)
        self.setupUi(self)        
        self.sourceDir = None
        self.outputDir = None
        
        self.connect(self.sourceButton, SIGNAL('clicked()'), self.getSourceDir)
        self.connect(self.outputButton, SIGNAL('clicked()'), self.getOutputDir)
        self.connect(self.buildButton, SIGNAL('clicked()'), self.buildProject)
        
    def getSourceDir(self):
        self.sourceDir = QFileDialog.getExistingDirectory(self, "Location of your Sphinx source directory")
        if not self.sourceDir.isEmpty():
            self.sourceLineEdit.setText(self.sourceDir)            
            
    def getOutputDir(self):
        self.outputDir = QFileDialog.getExistingDirectory(self, "Location of your Sphinx output directory")
        if not self.outputDir.isEmpty():
            self.outputLineEdit.setText(self.outputDir)
           
    def buildProject(self):
        process = QProcess()
        args = [self.sourceDir, self.outputDir]
        process.start('sphinx-build', args)
        
        if not process.waitForFinished():
            self.statusLabel.setText('<font color="red">Could not build project</font>')
        else:
            self.statusLabel.setText('<font color="green">Build Succesful!</font>')
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dlg()
    dialog.show()
    sys.exit(app.exec_())
    
