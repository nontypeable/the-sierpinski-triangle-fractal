from random import randint

# Window Dimensions.
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

# Coordinates of the first vertex.
x1 = randint(50, WINDOW_WIDTH - 50)
y1 = randint(50, WINDOW_HEIGHT / 2 - 50)

# Coordinates of the second vertex.
x2 = randint(50, WINDOW_WIDTH / 2 - 50)
y2 = randint(WINDOW_HEIGHT / 2 + 50, WINDOW_HEIGHT - 50)

# Coordinates of the third vertex.
x3 = randint(WINDOW_WIDTH / 2 + 50, WINDOW_HEIGHT - 50)
y3 = randint(WINDOW_HEIGHT / 2 + 50, WINDOW_HEIGHT - 50)

# Coordinates of the starting point.
startX = randint(50, WINDOW_WIDTH - 50)
startY = randint(50, WINDOW_HEIGHT - 50)