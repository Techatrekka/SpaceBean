import time
import vtk
from PIL import Image
import matplotlib.pyplot as plt
import os

class Model:
    def __init__(self):
        self.ren = vtk.vtkRenderer()
        self.renWin = vtk.vtkRenderWindow()
        self.screenshot_count = 0
        self.colors = vtk.vtkNamedColors()
        self.actor = self.stlToActor("asteroidLow.stl")
        self.x = []
        self.y = []

    def stlToActor(self, filename):
        # Create STL reader
        reader = vtk.vtkSTLReader()
        reader.SetFileName(filename)

        # Create map to convert STL to Polydata
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(reader.GetOutputPort())

        # Use above map to convert STL to an Actor
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        # Set the actor colour
        actor.GetProperty().SetDiffuseColor(self.colors.GetColor3d('Light_Grey'))

        return actor

    @staticmethod
    def createLightSource(x, y, z):
        light = vtk.vtkLight()
        light.SetIntensity(1)
        light.SetPosition(x, y, z)
        light.SetDiffuseColor(1, 1, 1)
        return light

    def render(self):
        # Create a rendering window and renderer
        self.renWin.AddRenderer(self.ren)
        self.renWin.SetWindowName('ReadSTL')

        # Assign actor to the renderer
        self.ren.AddActor(self.actor)
        self.ren.SetBackground(self.colors.GetColor3d('Black'))

        # Add an external light ("The sun")
        self.ren.AddLight(self.createLightSource(5, -5, 5))

        # Render scene
        self.renWin.Render()

    def generateLightShots(self, count):
        for i in range(count):
            self.roll(0, 0, 1)
            self.screenshot(i)
            self.renWin.Render()

    def roll(self, x, y, z):
        self.actor.RotateWXYZ(1, x, y, z)

    def screenshot(self, count, filename=None):
        # Create image filter
        w2if = vtk.vtkWindowToImageFilter()
        w2if.SetInput(self.renWin)
        w2if.Update()

        # Handle default file name
        if filename is None:
            filename = 'screenshot'
        filename = filename + '.png'

        # Generate and write the image
        writer = vtk.vtkPNGWriter()
        writer.SetFileName(filename)
        writer.SetInputData(w2if.GetOutput())
        writer.Write()

        # print(" ")
        image = Image.open(filename)
        # print("%s\t%s" % (filename, self.calculate_brightness(image)))
        self.y.append(self.calculate_brightness(image))
        self.x.append(count)
        
        name = 'Face'+ str(count) + '.png'
        if count < 361:
            if count%36 == 0:
                print("works")
                os.replace(filename,name)

    @staticmethod
    def calculate_brightness(image):
        greyscale_image = image.convert('L')
        histogram = greyscale_image.histogram()
        pixels = sum(histogram)
        brightness = scale = len(histogram)

        for index in range(0, scale):
            ratio = histogram[index] / pixels
            brightness += ratio * (-scale + index)

        return 1 if brightness == 255 else brightness / scale


scene = Model()
scene.render()
scene.generateLightShots(360*5)
plt.plot(scene.x, scene.y)
plt.show()
