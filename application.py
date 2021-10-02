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

        self.scene = Model(self.ren, self.vtkWidget.GetRenderWindow())
        self.scene.render()
        self.ui.startSimulation_Button.clicked.connect(self.startScene)

        self.ui.xObjectScale_SpinBox.valueChanged.connect(self.updateScale)
        self.ui.yObjectScale_SpinBox.valueChanged.connect(self.updateScale)
        self.ui.zObjectScale_SpinBox.valueChanged.connect(self.updateScale)

        self.show()
        self.iren.Initialize()
        self.iren.Disable()
        self.ui.zObjectScale_SpinBox

        # List of products the user can select from
    def startScene(self):
        objectRotateX = self.ui.xObjectRotation_SpinBox.value()
        objectRotateY = self.ui.yObjectRotation_SpinBox.value()
        objectRotateZ = self.ui.zObjectRotation_SpinBox.value()
        objectRotations = [objectRotateX, objectRotateY, objectRotateZ]
        self.scene.start(360, objectRotations)
        self.resetScene()

    def resetScene(self):
        self.scene.resetActor()
        self.updateScale()

    def updateScale(self):
        scaleX = self.ui.xObjectScale_SpinBox.value()
        scaleY = self.ui.yObjectScale_SpinBox.value()
        scaleZ = self.ui.zObjectScale_SpinBox.value()
        objectScale = [scaleX, scaleY, scaleZ]
        self.scene.updateScale(objectScale)
        self.vtkWidget.GetRenderWindow().Render()




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

