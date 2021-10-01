import time

import vtk
from PIL import Image
import matplotlib.pyplot as plt

ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
iren = vtk.vtkRenderWindowInteractor()
x = []
y = []


def render():
    colors = vtk.vtkNamedColors()

    filename = "asteroid.stl"

    reader = vtk.vtkSTLReader()
    reader.SetFileName(filename)

    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(reader.GetOutputPort())

    polydata = reader.GetOutput()
    print(polydata)

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetDiffuseColor(colors.GetColor3d('Light_Grey'))

    # Create a rendering window and renderer
    renWin.AddRenderer(ren)
    renWin.SetWindowName('ReadSTL')

    # Create a renderwindowinteractor
    iren.SetRenderWindow(renWin)

    # Assign actor to the renderer
    ren.AddActor(actor)
    ren.SetBackground(colors.GetColor3d('Black'))

    light = vtk.vtkLight()
    light.SetIntensity(5)
    light.SetPosition(1, -1, 1)
    light.SetDiffuseColor(1, 1, 1)
    ren.AddLight(light)
    plt.ylabel('Lumens per (square meter)')
    # Enable user interface
    iren.Initialize()
    renWin.Render()
    camera = ren.GetActiveCamera()
    # iren.Start()
    transform = vtk.vtkTransform()
    for i in range(360):
        actor.RotateY(1)
        # Roll(camera)
        screenshot(i)
        renWin.Render()

    plt.plot(x, y)
    plt.show()


def Roll(camera):
    transform = vtk.vtkTransform()
    transform.Identity()
    transform.RotateWXYZ(1, 1, 1, 1)
    camera.ApplyTransform(transform)
    camera.OrthogonalizeViewUp()
    ren.ResetCameraClippingRange()


def screenshot(screenshot_count):
    w2if = vtk.vtkWindowToImageFilter()
    w2if.SetInput(renWin)
    w2if.Update()
    filename = 'screenshot.png'
    writer = vtk.vtkPNGWriter()
    writer.SetFileName(filename)
    writer.SetInputData(w2if.GetOutput())
    writer.Write()
    print(" ")
    image = Image.open(filename)
    print("%s\t%s" % (filename, calculate_brightness(image)))
    y.append(calculate_brightness(image))
    x.append(screenshot_count)


def calculate_brightness(image):
    greyscale_image = image.convert('L')
    histogram = greyscale_image.histogram()
    pixels = sum(histogram)
    brightness = scale = len(histogram)

    for index in range(0, scale):
        ratio = histogram[index] / pixels
        brightness += ratio * (-scale + index)

    return 1 if brightness == 255 else brightness / scale


render()