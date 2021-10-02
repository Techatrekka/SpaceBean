# import system module
import sys
import vtk

# import some PyQt5 modules
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage, QWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer

from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

from main import *
from mainMenu import *
from simulation import *

sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    print(exctype, value, traceback)
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook

class simulation(QMainWindow):
    # class constructor
    def __init__(self):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.vtkWidget = QVTKRenderWindowInteractor(self)
        self.ui.vtkMainLayout.addWidget(self.vtkWidget)

        self.ren = vtk.vtkRenderer()
        self.vtkWidget.GetRenderWindow().AddRenderer(self.ren)
        self.iren = self.vtkWidget.GetRenderWindow().GetInteractor()

        scene = Model(self.ren, self.vtkWidget.GetRenderWindow())
        scene.render()
        self.ui.startSimulation_Button.clicked.connect(lambda: scene.start(360, 6, 8, 3))

        self.show()
        self.iren.Initialize()
        self.iren.Disable()


        # List of products the user can select from



# This class opens the Setup Screen where users can change their save directory
class mainMenu(QWidget):
    def __init__(self):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        #Setup Env file for to be read into line edit
        self.ui.importSTL_Button.clicked.connect(self.folderBrowser)
        self.ui.startSim_Button.clicked.connect(self.startSim)

        self.show()
    
    def folderBrowser(self):
        dir = QFileDialog.getOpenFileName(self,'Select Save Directory', 'C:\\users')
        self.ui.stlDir_LinerEdit.setText(dir[0])  
            
    def startSim(self):
        #open Main window
        print (self.ui.comboBox.currentText())
        self.dialog = simulation()
        self.dialog.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create and show mainWindow
    mainWindow = mainMenu()
    mainWindow.show()

    sys.exit(app.exec_())

