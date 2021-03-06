# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simulation.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1075, 740)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(1075, 740))
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.388, y1:1, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.995025 rgba(0, 0, 120, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.vtkMainLayout = QtWidgets.QVBoxLayout()
        self.vtkMainLayout.setObjectName("vtkMainLayout")
        self.horizontalLayout.addLayout(self.vtkMainLayout)
        self.lightGraphLayout = QtWidgets.QVBoxLayout()
        self.lightGraphLayout.setObjectName("lightGraphLayout")
        self.currentLight_Label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentLight_Label.sizePolicy().hasHeightForWidth())
        self.currentLight_Label.setSizePolicy(sizePolicy)
        self.currentLight_Label.setMinimumSize(QtCore.QSize(300, 250))
        self.currentLight_Label.setMaximumSize(QtCore.QSize(300, 300))
        self.currentLight_Label.setStyleSheet("border: 1px solid;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgba(230, 230, 230, 0);")
        self.currentLight_Label.setText("")
        self.currentLight_Label.setScaledContents(True)
        self.currentLight_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.currentLight_Label.setObjectName("currentLight_Label")
        self.lightGraphLayout.addWidget(self.currentLight_Label)
        self.horizontalLayout.addLayout(self.lightGraphLayout)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.topDownImage_Label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topDownImage_Label.sizePolicy().hasHeightForWidth())
        self.topDownImage_Label.setSizePolicy(sizePolicy)
        self.topDownImage_Label.setMinimumSize(QtCore.QSize(300, 300))
        self.topDownImage_Label.setMaximumSize(QtCore.QSize(300, 300))
        self.topDownImage_Label.setStyleSheet("border: 1px solid;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgba(230, 230, 230, 255);")
        self.topDownImage_Label.setText("")
        self.topDownImage_Label.setScaledContents(True)
        self.topDownImage_Label.setObjectName("topDownImage_Label")
        self.verticalLayout_6.addWidget(self.topDownImage_Label)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_4.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_4.addWidget(self.label_10)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_4.addWidget(self.label_19)
        self.xObjectRotation_SpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.xObjectRotation_SpinBox.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255, 255);")
        self.xObjectRotation_SpinBox.setDecimals(1)
        self.xObjectRotation_SpinBox.setMinimum(-100.0)
        self.xObjectRotation_SpinBox.setMaximum(100.0)
        self.xObjectRotation_SpinBox.setSingleStep(0.1)
        self.xObjectRotation_SpinBox.setObjectName("xObjectRotation_SpinBox")
        self.horizontalLayout_4.addWidget(self.xObjectRotation_SpinBox)
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_4.addWidget(self.label_18)
        self.yObjectRotation_SpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.yObjectRotation_SpinBox.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255, 255);")
        self.yObjectRotation_SpinBox.setDecimals(1)
        self.yObjectRotation_SpinBox.setMinimum(-100.0)
        self.yObjectRotation_SpinBox.setMaximum(100.0)
        self.yObjectRotation_SpinBox.setSingleStep(0.1)
        self.yObjectRotation_SpinBox.setObjectName("yObjectRotation_SpinBox")
        self.horizontalLayout_4.addWidget(self.yObjectRotation_SpinBox)
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_4.addWidget(self.label_17)
        self.zObjectRotation_SpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.zObjectRotation_SpinBox.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255, 255);")
        self.zObjectRotation_SpinBox.setDecimals(1)
        self.zObjectRotation_SpinBox.setMinimum(-100.0)
        self.zObjectRotation_SpinBox.setMaximum(100.0)
        self.zObjectRotation_SpinBox.setSingleStep(0.1)
        self.zObjectRotation_SpinBox.setObjectName("zObjectRotation_SpinBox")
        self.horizontalLayout_4.addWidget(self.zObjectRotation_SpinBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_4.addWidget(self.label_11)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_6.addWidget(self.label_12)
        self.xObjectScale_SpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.xObjectScale_SpinBox.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255, 255);")
        self.xObjectScale_SpinBox.setDecimals(1)
        self.xObjectScale_SpinBox.setMinimum(0.1)
        self.xObjectScale_SpinBox.setMaximum(4.0)
        self.xObjectScale_SpinBox.setSingleStep(0.1)
        self.xObjectScale_SpinBox.setObjectName("xObjectScale_SpinBox")
        self.horizontalLayout_6.addWidget(self.xObjectScale_SpinBox)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.yObjectScale_SpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.yObjectScale_SpinBox.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255, 255);")
        self.yObjectScale_SpinBox.setDecimals(1)
        self.yObjectScale_SpinBox.setMinimum(0.1)
        self.yObjectScale_SpinBox.setMaximum(4.0)
        self.yObjectScale_SpinBox.setSingleStep(0.1)
        self.yObjectScale_SpinBox.setObjectName("yObjectScale_SpinBox")
        self.horizontalLayout_6.addWidget(self.yObjectScale_SpinBox)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.zObjectScale_SpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.zObjectScale_SpinBox.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255, 255);")
        self.zObjectScale_SpinBox.setDecimals(1)
        self.zObjectScale_SpinBox.setMinimum(0.1)
        self.zObjectScale_SpinBox.setMaximum(4.0)
        self.zObjectScale_SpinBox.setSingleStep(0.1)
        self.zObjectScale_SpinBox.setObjectName("zObjectScale_SpinBox")
        self.horizontalLayout_6.addWidget(self.zObjectScale_SpinBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.xSunRotation_Slider = QtWidgets.QSlider(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xSunRotation_Slider.sizePolicy().hasHeightForWidth())
        self.xSunRotation_Slider.setSizePolicy(sizePolicy)
        self.xSunRotation_Slider.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.xSunRotation_Slider.setMinimum(1)
        self.xSunRotation_Slider.setMaximum(359)
        self.xSunRotation_Slider.setSingleStep(10)
        self.xSunRotation_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.xSunRotation_Slider.setObjectName("xSunRotation_Slider")
        self.horizontalLayout_7.addWidget(self.xSunRotation_Slider)
        self.xSunRotation_SpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.xSunRotation_SpinBox.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255, 255);")
        self.xSunRotation_SpinBox.setMaximum(360)
        self.xSunRotation_SpinBox.setObjectName("xSunRotation_SpinBox")
        self.xSunRotation_SpinBox.setReadOnly(True)
        self.xSunRotation_SpinBox.setDisabled(True)
        self.horizontalLayout_7.addWidget(self.xSunRotation_SpinBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.sunDistance_Slider = QtWidgets.QSlider(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sunDistance_Slider.sizePolicy().hasHeightForWidth())
        self.sunDistance_Slider.setSizePolicy(sizePolicy)
        self.sunDistance_Slider.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.sunDistance_Slider.setMaximum(10)
        self.sunDistance_Slider.setMinimum(1)
        self.sunDistance_Slider.setSingleStep(1)
        self.sunDistance_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.sunDistance_Slider.setTickInterval(0)
        self.sunDistance_Slider.setObjectName("sunDistance_Slider")
        self.horizontalLayout_9.addWidget(self.sunDistance_Slider)
        self.sunDistance_SpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.sunDistance_SpinBox.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255, 255);")
        self.sunDistance_SpinBox.setMaximum(100)
        self.sunDistance_SpinBox.setObjectName("sunDistance_SpinBox")
        self.sunDistance_SpinBox.setReadOnly(True)
        self.sunDistance_SpinBox.setDisabled(True)
        self.horizontalLayout_9.addWidget(self.sunDistance_SpinBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.earthDistance_Slider = QtWidgets.QSlider(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.earthDistance_Slider.sizePolicy().hasHeightForWidth())
        self.earthDistance_Slider.setSizePolicy(sizePolicy)
        self.earthDistance_Slider.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.earthDistance_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.earthDistance_Slider.setObjectName("earthDistance_Slider")
        self.earthDistance_Slider.setMinimum(1)
        self.earthDistance_Slider.setMaximum(10)
        self.horizontalLayout_12.addWidget(self.earthDistance_Slider)
        self.earthDistance_ComboBox = QtWidgets.QSpinBox(self.centralwidget)
        self.earthDistance_ComboBox.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255, 255);")
        self.earthDistance_ComboBox.setMaximum(10)
        self.earthDistance_ComboBox.setMinimum(1)
        self.earthDistance_ComboBox.setReadOnly(True)
        self.earthDistance_ComboBox.setDisabled(True)
        self.earthDistance_ComboBox.setObjectName("earthDistance_ComboBox")
        self.horizontalLayout_12.addWidget(self.earthDistance_ComboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem4)
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_16.setObjectName("label_16")
        self.verticalLayout_5.addWidget(self.label_16)
        self.rotationNo_SpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.rotationNo_SpinBox.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255, 255);")
        self.rotationNo_SpinBox.setMinimum(1)
        self.rotationNo_SpinBox.setMaximum(10)
        self.rotationNo_SpinBox.setObjectName("rotationNo_SpinBox")
        self.verticalLayout_5.addWidget(self.rotationNo_SpinBox)
        self.startSimulation_Button = QtWidgets.QPushButton(self.centralwidget)
        self.startSimulation_Button.setStyleSheet("background-color: rgb(185, 185, 185);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(143, 143, 143);\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"\n"
"color: rgb(255, 255, 255);")
        self.startSimulation_Button.setObjectName("startSimulation_Button")
        self.verticalLayout_5.addWidget(self.startSimulation_Button)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_13.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_9.setText(_translate("MainWindow", "Object Controls"))
        self.label_10.setText(_translate("MainWindow", "Rotation Weights"))
        self.label_19.setText(_translate("MainWindow", "X"))
        self.label_18.setText(_translate("MainWindow", "Y"))
        self.label_17.setText(_translate("MainWindow", "Z"))
        self.label_11.setText(_translate("MainWindow", "Scale"))
        self.label_12.setText(_translate("MainWindow", "X"))
        self.label.setText(_translate("MainWindow", "Y"))
        self.label_2.setText(_translate("MainWindow", "Z"))
        self.label_5.setText(_translate("MainWindow", "Object Orbit Controls"))
        self.label_6.setText(_translate("MainWindow", "Rotation"))
        self.label_8.setText(_translate("MainWindow", "Distance"))
        #self.label_4.setText(_translate("MainWindow", "Earth Controls"))
        self.label_3.setText(_translate("MainWindow", "Zoom"))
        self.label_16.setText(_translate("MainWindow", "Number of rotations"))
        self.startSimulation_Button.setText(_translate("MainWindow", "Start Simulation"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
