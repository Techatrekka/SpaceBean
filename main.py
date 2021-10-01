import time
import vtk


class Model:
    def __init__(self):
        self.ren = vtk.vtkRenderer()
        self.renWin = vtk.vtkRenderWindow()
        self.screenshot_count = 0
        self.colors = vtk.vtkNamedColors()

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
        actor = self.stlToActor("asteroidLow.stl")
        self.ren.AddActor(actor)
        self.ren.SetBackground(self.colors.GetColor3d('Black'))

        # Add an external light ("The sun")
        self.ren.AddLight(self.createLightSource(5, -5, 5))

        # Render scene
        self.renWin.Render()

    def generateLightShots(self, count):
        for i in range(count):
            self.roll()
            self.screenshot(i)
            self.renWin.Render()

    def roll(self):
        # Get the current camera
        camera = self.ren.GetActiveCamera()

        # Create a rotation
        transform = vtk.vtkTransform()
        transform.Identity()
        transform.RotateWXYZ(1, 1, 1, 1)

        # Apply the rotation
        camera.ApplyTransform(transform)
        camera.OrthogonalizeViewUp()
        self.ren.ResetCameraClippingRange()

    def screenshot(self, count, filename=None):
        # Create image filter
        w2if = vtk.vtkWindowToImageFilter()
        w2if.SetInput(self.renWin)
        w2if.Update()

        # Handle default file name
        if filename is None:
            filename = 'screenshot'
        filename = filename + '%d.png' % count

        # Generate and write the image
        writer = vtk.vtkPNGWriter()
        writer.SetFileName(filename)
        writer.SetInputData(w2if.GetOutput())
        writer.Write()


scene = Model()
scene.render()
scene.generateLightShots(10)
