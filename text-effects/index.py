#!/usr/bin/env python3

import os
import time

import sys
from neopixel import *

LED_COUNT      = 256      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 10     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

def clearTerminalWindow():
	os.system('cls' if os.name == 'nt' else 'clear')

gridX = 32
gridY = 8

letterMap = {
	"a": [[0, 6], [0, 5], [0, 4], [1, 3], [2, 2], [3, 3], [4, 4], [2, 4], [4, 5], [4, 6]],
	"b": [[0, 6], [0, 5], [0, 4], [0, 3], [0, 2], [1, 2], [2, 2], [3, 3], [2, 4], [1, 4], [3, 5], [2, 6], [1, 6]],
	"c": [[1, 2], [2, 2], [3, 2], [0, 3], [0, 4], [0, 5], [1, 6], [2, 6], [3, 6]],
	"d": [[0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [1, 2], [2, 2], [3, 3], [3, 4], [3, 5], [2, 6], [1, 6]],
	"e": [[0, 6], [0, 5], [0, 4], [0, 3], [0, 2], [1, 6], [2, 6], [1, 2], [2, 2], [1, 4], [2, 4]],
	"f": [[0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [1, 2], [2, 2], [3, 2], [1, 4], [2, 4], [3, 4]],
	"g": [[1, 2], [2, 2], [0, 3], [0, 4], [0, 5], [1, 6], [2, 6], [3, 5], [3, 4], [2, 4]],
	"h": [[0, 6], [0, 5], [0, 4], [0, 3], [0, 2], [3, 6], [3, 5], [3, 4], [3, 3], [3, 2], [1, 4], [2, 4]],
	"i": [[0, 2], [1, 2], [2, 2], [3, 2], [4, 2], [0, 6], [1, 6], [2, 6], [3, 6], [4, 6], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6]],
	"j": [[4, 2], [4, 3], [4, 4], [4, 5], [3, 6], [2, 6], [1, 6], [0, 5]],
	"k": [[0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [1, 4], [2, 3], [3, 2], [2, 5], [3, 6]],
	"l": [[0, 6], [0, 5], [0, 4], [0, 3], [0, 2], [1, 6], [2, 6]],
	"m": [[0, 6], [0, 5], [0, 4], [0, 3], [0, 2], [1, 3], [2, 4], [3, 3], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6]],
	"n": [[0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [1, 3], [2, 4], [3, 5], [4, 6], [4, 5], [4, 4], [4, 3], [4, 2]],
	"o": [[2, 2], [3, 2], [4, 3], [4, 4], [4, 5], [3, 6], [2, 6], [1, 6], [0, 5], [0, 4], [0, 3], [1, 2]],
	"p": [[0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [1, 2], [2, 2], [3, 3], [2, 4], [1, 4]],
	"q": [[2, 2], [3, 2], [4, 3], [4, 4], [4, 5], [3, 6], [2, 6], [1, 6], [0, 5], [0, 4], [0, 3], [1, 2], []],
	"r": [[0, 6], [0, 5], [0, 4], [0, 3], [0, 2], [1, 2], [2, 2], [3, 3], [2, 4], [1, 4], [3, 5], [4, 6]],
	"s": [[3, 2], [2, 2], [1, 2], [0, 3], [1, 4], [2, 4], [3, 5], [2, 6], [1, 6], [0, 6]],
	"t": [[2, 6], [2, 5], [2, 4], [2, 3], [2, 2], [0, 2], [1, 2], [3, 2], [4, 2]],
	"u": [[0, 2], [0, 3], [0, 4], [0, 5], [1, 6], [2, 6], [3, 5], [3, 4], [3, 3], [3, 2]],
	"v": [[0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [3, 5], [3, 4], [4, 3], [4, 2]],
	"w": [[0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [3, 5], [3, 4], [4, 3], [4, 2], [5, 3], [5, 4], [6, 5], [6, 6], [7, 5], [7, 4], [8, 3], [8, 2]],
	"x": [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [0, 6], [1, 5], [3, 3], [4, 2]],
	"y": [[0, 2], [1, 3], [2, 4], [3, 3], [4, 2], [2, 5], [2, 6]],
	"z": [[0, 2], [1, 2], [2, 2], [3, 2], [4, 2], [3, 3], [2, 4], [1, 5], [0, 6], [1, 6], [2, 6], [3, 6], [4, 6]],
}

def drawLetter(matrix, letter, xPos):
	if letter == " ":
		return xPos + 2

	items = letterMap[letter]

	maxX = xPos

	for coord in items:
		x = coord[0] + xPos
		y = coord[1]

		if x < gridX and y < gridY and x >= 0 and y >= 0:
			matrix[x][y] = 1

		maxX = max(maxX, x)

	return maxX + 2

def createEmptyMatrix():
	return [[0 for i in range(gridY)] for j in range(gridX)]

def printMatrixConsole(matrix):
	for i in range(gridY):
		for j in range(gridX):
			print('@' if matrix[j][i] == 1 else ' ', end='', flush=True)
		print(flush=True)

def printMatrix(matrix, strip):
	for i in range(gridY):
		for j in range(gridX):
					if matrix[j][i] == 1:
						drawPixel(strip, j, i, Color(0, (255 / gridX) * j, 255 - (255 / gridX) * j))
		strip.show()

		for i in range(gridY):
			for j in range(gridX):
				if matrix[j][i] == 1:
					drawPixel(strip, j, i, Color(0, 0, 0))
					matrix[j][i] = 0

def resetMatrix(matrix):
	for i in range(len(matrix)):
		row = matrix[i]

		for j in range(len(row)):
			row[j] = 0

def drawPixel(strip, x, y, color):
	modifiedY = 7 - y if x % 2 == 1 else y
	strip.setPixelColor(x * 8 + modifiedY, color)

def colorScreen(strip, color):
	for i in range(0, 8):
		for j in range(0, 32):
			drawPixel(strip, j, i, color)

def colorWipe(strip):
	colorScreen(strip, Color(0, 0, 0))
	strip.show()

def rgb(r, g, b):
	return Color(g, r, b)

def animateText(strip, word):
	matrix = createEmptyMatrix()
	offset = 0

	# for offset in reversed(range(0, gridX, 2)):
	while True:
		x = gridX - offset

		for letter in word.lower():
			x = drawLetter(matrix, letter, x)

		clearTerminalWindow()
		printMatrix(matrix, strip)
		resetMatrix(matrix)
		time.sleep(.2)

		if x < 0:
			break

		offset += 1


if __name__ == '__main__':
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
	strip.begin()

	try:
		animateText(strip, "hello, world!")
		animateText(strip, "woohoo!!")
		colorWipe(strip)

	except KeyboardInterrupt:
		colorWipe(strip)
