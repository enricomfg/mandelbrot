import math
from PIL import Image, ImageDraw
from random import randint

iterations = 30
sensibility = 100.0

rgb = [200, 0, 255]

def squareComplex(c):
    return [(c[0] * c[0] - c[1] * c[1]), 2 * c[0] * c[1]]

def magComplex(c):
    return math.sqrt(abs(c[0]) * abs(c[0]) + abs(c[1]) * abs(c[1]))

def sumComplex(c1, c2):
    return [c1[0] + c2[0], c1[1] + c2[1]]

def howBad(c):
    result = [0, 0]

    for i in range(0, iterations):
        result = sumComplex(squareComplex(result), c)
        if magComplex(result) > 2:
            return i

    return 0

w = 4000
h = 4000

image = Image.new("RGBA", (w, h), (0, 0, 0, 255))
pixels = image.load()

center = [math.floor(w/2) + 500, math.floor(h/2)]
pixelValue = .0008

for i in range(0, w):
    for j in range(0, h):
        tone = howBad([(i + 1 - center[0]) * pixelValue, (j + 1 - center[1]) * pixelValue]) / iterations
        pixels[i, j] = (round(tone * rgb[0]), round(tone * rgb[1]), round(tone * rgb[2]), 255)

image.save("mandelbrot.png")