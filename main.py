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
        self.actor = self.fileToActor("bennuAsteroid.stl")
        self.x = []
        self.y = []

    def fileToActor(self, filename):
        # Create file reader
        if ".stl" in filename:
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

    def render(self):
        # Create a rendering window and renderer
        self.renWin.AddRenderer(self.ren)
        self.renWin.SetWindowName('ReadSTL')

        # Assign actor to the renderer
        self.ren.AddActor(self.actor)
        self.ren.SetBackground(self.colors.GetColor3d('Black'))

        # Add an external light ("The sun")
        self.ren.AddLight(self.createLightSource(10, 10, 10))

        # Render scene
        self.renWin.Render()

    def start(self, num_iterations, x, y, z):
        for i in range(num_iterations):
            self.roll(x, y, z)
            self.renWin.Render()
            self.screenshot(i)

        plt.plot(self.x, self.y)
        plt.show()

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

        filename = 'screenshot.png'
        if count < 361:
            if count % 36 == 0:
                filename = 'Face' + str(int(count / 36)) + ".png"

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


scene = Model()
scene.render()
scene.start(360, 2, 1, 3)

