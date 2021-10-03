# import system module
import sys
import vtk
import math

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
    def __init__(self, stlDir):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.stlDir = stlDir

        self.orbiter = OrbitClass()

        self.vtkWidget = QVTKRenderWindowInteractor(self)
        self.ui.vtkMainLayout.addWidget(self.vtkWidget)

        self.ren = vtk.vtkRenderer()
        self.vtkWidget.GetRenderWindow().AddRenderer(self.ren)
        self.iren = self.vtkWidget.GetRenderWindow().GetInteractor()

        self.scene = Model(self.ren, self.vtkWidget.GetRenderWindow(), self.stlDir)
        self.scene.render()
        self.ui.startSimulation_Button.clicked.connect(self.startScene)

        self.ui.xObjectScale_SpinBox.valueChanged.connect(self.updateScale)
        self.ui.yObjectScale_SpinBox.valueChanged.connect(self.updateScale)
        self.ui.zObjectScale_SpinBox.valueChanged.connect(self.updateScale)

        self.ui.xObjectRotation_SpinBox.setValue(1)

        self.ui.xObjectScale_SpinBox.setValue(1)
        self.ui.yObjectScale_SpinBox.setValue(1)
        self.ui.zObjectScale_SpinBox.setValue(1)

        self.ui.earthDistance_Slider.valueChanged.connect(self.updateEarthControlsSlider)
        self.ui.earthDistance_ComboBox.valueChanged.connect(self.updateEarthControlsCombo)
        self.ui.sunDistance_Slider.valueChanged.connect(self.updateSunDistanceSlider)
        self.ui.sunDistance_Slider.sliderReleased.connect(self.updateSunDistanceSliderReleased)
        self.ui.sunDistance_SpinBox.valueChanged.connect(self.updateSunDistanceCombo)
        self.ui.xSunRotation_Slider.valueChanged.connect(self.updateSunRotationSlider)
        self.ui.xSunRotation_Slider.sliderReleased.connect(self.updateSunRotationComboReleased)
        self.ui.xSunRotation_SpinBox.valueChanged.connect(self.updateSunRotationCombo)
        self.ui.xSunRotation_Slider.setMaximum(360)
        self.ui.xSunRotation_Slider.setMinimum(1)

        self.updateOrbit()

        self.show()
        self.iren.Initialize()
        self.iren.Disable()
        self.ui.zObjectScale_SpinBox

        # List of products the user can select from
    def startScene(self):
        objectRotateX = self.ui.xObjectRotation_SpinBox.value()
        objectRotateY = self.ui.yObjectRotation_SpinBox.value()
        objectRotateZ = self.ui.zObjectRotation_SpinBox.value()
        rotations = self.ui.rotationNo_SpinBox.value()
        objectRotations = [0, 0, 0]
        if not ((objectRotateX == 0) and (objectRotateY == 0) and (objectRotateZ == 0)):
            objectRotateMagnitude = math.sqrt(objectRotateX ** 2 + objectRotateY ** 2 + objectRotateZ ** 2)
            Xnew = objectRotateX / objectRotateMagnitude
            Ynew = objectRotateY / objectRotateMagnitude
            Znew = objectRotateZ / objectRotateMagnitude
            objectRotations = [Xnew, Ynew, Znew]
        self.scene.start(360 * rotations, objectRotations)
        self.updateGraphs()
        self.resetScene()

    def updateGraphs(self):
        pixmap = QtGui.QPixmap("plot.png")
        self.ui.currentLight_Label.setPixmap(pixmap)

    def updateOrbit(self):
        pixmap = QtGui.QPixmap("OrbitPol.png")
        self.ui.topDownImage_Label.setPixmap(pixmap)

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

    def updateEarthControlsCombo(self):
        self.ui.earthDistance_Slider.setValue(self.ui.earthDistance_ComboBox.value())
        self.scene.updateEarth(self.ui.earthDistance_Slider.value())

    def updateEarthControlsSlider(self):
        self.ui.earthDistance_ComboBox.setValue(self.ui.earthDistance_Slider.value())
        self.scene.updateEarth(self.ui.earthDistance_Slider.value())

    def updateSunDistanceCombo(self):
        self.ui.sunDistance_Slider.setValue(self.ui.sunDistance_SpinBox.value())
        self.scene.updateSunDistance(self.ui.sunDistance_SpinBox.value())

    def updateSunDistanceSlider(self):
        self.ui.sunDistance_SpinBox.setValue(self.ui.sunDistance_Slider.value())
        self.scene.updateSunDistance(self.ui.sunDistance_SpinBox.value())

    def updateSunDistanceSliderReleased(self):
        self.scene.updateGraph()
        self.updateOrbit()

    def updateSunRotationComboReleased(self):
        self.scene.updateGraph()
        self.updateOrbit()

    def updateSunRotationCombo(self):
        self.ui.xSunRotation_Slider.setValue(self.ui.xSunRotation_SpinBox.value())
        self.scene.updateSunRotation(self.ui.xSunRotation_Slider.value() - 1)

    def updateSunRotationSlider(self):
        self.ui.xSunRotation_SpinBox.setValue(self.ui.xSunRotation_Slider.value())
        self.scene.updateSunRotation(self.ui.xSunRotation_Slider.value() - 1)

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
        self.ui.startCustomSim_Button.clicked.connect(self.startCustomSim)
        self.stlDir = ""
        pixmap = QPixmap("./images/logo.jpg")
        self.ui.label_4.setPixmap(pixmap)
        pixmap = QPixmap("./images/Space_Apps_Logo_Black_1.jpeg")
        self.ui.label_5.setPixmap(pixmap)

        self.show()

    def folderBrowser(self):
        dir = QFileDialog.getOpenFileName(self, 'Select Save Directory', 'C:\\users')
        self.ui.stlDir_LinerEdit.setText(dir[0])
        self.stlDir = dir[0]

    def startSim(self):
        # open Main window
        if self.ui.comboBox.currentText() == "Bennu Asteroid":
            self.stlDir = "bennuAsteroid.stl"
        elif self.ui.comboBox.currentText() == "Geographos":
            self.stlDir = "geographos.stl"

        self.dialog = simulation(self.stlDir)
        self.close()
        self.dialog.show()

    def startCustomSim(self):
        # open Main window
        if (self.ui.stlDir_LinerEdit.text()):
            self.stlDir = self.ui.stlDir_LinerEdit.text()
            self.dialog = simulation(self.stlDir)
            self.dialog.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create and show mainWindow
    mainWindow = mainMenu()
    mainWindow.show()

    sys.exit(app.exec_())

