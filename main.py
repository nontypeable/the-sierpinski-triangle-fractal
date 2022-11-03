from tkinter import *
from random import randint
from datetime import datetime

import technicalData

dots = int(input("How many points should I use to build a fractal?\n> "))

window = Tk()
window.title(f"Number of points: {dots}")
canvas = Canvas(window, width=technicalData.WINDOW_WIDTH, height=technicalData.WINDOW_HEIGHT, bg="white")
canvas.pack()


# Function for drawing circles.
def drawCircle(radius, centerX, centerY):
    canvas.create_oval(centerX - radius, centerY - radius, centerX + radius, centerY + radius, fill="black")


# Drawing vertices.
drawCircle(4, technicalData.x1, technicalData.y1)
drawCircle(4, technicalData.x2, technicalData.y2)
drawCircle(4, technicalData.x3, technicalData.y3)

# Drawing a starting point.
drawCircle(1, technicalData.startX, technicalData.startY)

# Getting the start time of fractal generation.
startConstruction = datetime.now()

# Fractal generation.
for i in range(dots):

    # The essence of generating these points is
    # to find the middle between the last point
    # and a randomly selected vertex of the triangle.

    vertex = randint(1, 3)
    if (vertex == 1):
        technicalData.startX = (technicalData.x1 + technicalData.startX) / 2
        technicalData.startY = (technicalData.y1 + technicalData.startY) / 2
        drawCircle(1, technicalData.startX, technicalData.startY)

    if (vertex == 2):
        technicalData.startX = (technicalData.x2 + technicalData.startX) / 2
        technicalData.startY = (technicalData.y2 + technicalData.startY) / 2
        drawCircle(1, technicalData.startX, technicalData.startY)

    if (vertex == 3):
        technicalData.startX = (technicalData.x3 + technicalData.startX) / 2
        technicalData.startY = (technicalData.y3 + technicalData.startY) / 2
        drawCircle(1, technicalData.startX, technicalData.startY)

# We give the user the time spent on generating the fractal.
print(f"\nThe construction of the Sierpinski triangle took {datetime.now() - startConstruction} seconds.")

window.mainloop()
