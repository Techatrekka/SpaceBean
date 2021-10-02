import time
import vtk
from PIL import Image
import matplotlib.pyplot as plt
import os


class Model:
    def __init__(self, ren, renWin):
        self.ren = ren
        self.renWin = renWin
        self.screenshot_count = 0
        self.colors = vtk.vtkNamedColors()
        self.filename = "bennuAsteroid.STL"
        self.actor = self.fileToActor(self.filename)
        self.isRunning = 0

        self.sun = self.createLightSource(10, 10, 10)
        self.updateCameraPosition(-7, 7, 7)

        self.x = []
        self.y = []

    def fileToActor(self, filename):
        # Create file reader
        if (".stl" in filename) or (".STL" in filename):
            reader = vtk.vtkSTLReader()
        else:
            reader = vtk.vtkOBJReader()

        reader.SetFileName(filename)

        # Create map to convert STL to Polydata
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(reader.GetOutputPort())

        # Use above map to convert STL to an Actor
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)

        # Set actors default transform
        transform = vtk.vtkTransform()
        transform.PostMultiply()
        actor.SetUserTransform(transform)

        # Set the actor colour
        actor.GetProperty().SetDiffuseColor(self.colors.GetColor3d('Light_Grey'))
        actor.SetOrigin(0, 0, 0)

        return actor

    @staticmethod
    def createLightSource(x, y, z):
        light = vtk.vtkLight()
        light.SetIntensity(1)
        light.SetPosition(x, y, z)
        light.SetDiffuseColor(1, 1, 1)
        return light

    def updateScale(self, objectScale):
        transform = self.actor.GetUserTransform()
        transform.PostMultiply()

        # Adjust scale
        oldObjectScale = transform.GetScale()
        transform.Scale(objectScale[0] / oldObjectScale[0], objectScale[1] / oldObjectScale[1], objectScale[2] / oldObjectScale[2])

        # Apply new rotations
        self.actor.SetUserTransform(transform)

    def updateEarth(self, input):
        self.updateCameraPosition(-7,7,input)

    def updateSunRotation(self, input):
        pass

    def updateSunDistance(self, input):
        self.updateLightPosition(input, input, input)

    def resetActor(self):
        self.ren.RemoveActor(self.actor)
        self.actor = self.fileToActor(self.filename)
        self.ren.AddActor(self.actor)

    def updateLightPosition(self, x, y, z):
        self.sun.SetPosition(x, y, z)

    def updateCameraPosition(self, x, y, z):
        camera = self.ren.GetActiveCamera()
        camera.SetFocalPoint(0, 0, 0)
        camera.SetPosition(x, y, z)

    def render(self):
        # Assign actor to the renderer
        self.ren.AddActor(self.actor)
        self.ren.SetBackground(self.colors.GetColor3d('Black'))

        # Add an external light ("The sun")
        self.ren.AddLight(self.sun)

    def start(self, num_iterations, objectRotations):
        if self.isRunning == 0:
            self.x = []
            self.y = []
            self.isRunning = 1
            for i in range(num_iterations):
                self.roll(objectRotations[0], objectRotations[1], objectRotations[2])
                self.renWin.Render()
                self.screenshot(i)

            plt.plot(self.x, self.y)
            if os.path.isfile("plot.png"):
                os.replace("plot.png", "oldplot.png")
            plt.savefig("plot.png")
            self.isRunning = 0

    def roll(self, x, y, z):
        # Get current rotation rotation
        rotationTransform = self.actor.GetUserTransform()
        rotationTransform.PostMultiply()

        # Add new rotations
        rotationTransform.RotateX(x)
        rotationTransform.RotateY(y)
        rotationTransform.RotateZ(z)

        # Apply new rotations
        self.actor.SetUserTransform(rotationTransform)

    def screenshot(self, count):
        # Create image filter
        w2if = vtk.vtkWindowToImageFilter()
        w2if.SetInput(self.renWin)
        w2if.Update()

        filename = './images/screenshot.png'
        if count < 361:
            if count % 36 == 0:
                filename = './images/Face' + str(int(count / 36)) + ".png"

        # Generate and write the image
        writer = vtk.vtkPNGWriter()
        writer.SetFileName(filename)
        writer.SetInputData(w2if.GetOutput())
        writer.Write()

        image = Image.open(filename)
        self.y.append(self.calculate_brightness(image))
        self.x.append(count)


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
