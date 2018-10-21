import os
import time

def clearTerminalWindow():
	os.system('cls' if os.name == 'nt' else 'clear')

gridX = 100
gridY = 8

letterMap = {
	"a": [[0, 6], [0, 5], [0, 4], [1, 3], [2, 2], [3, 3], [4, 4], [2, 4], [4, 5], [4, 6]],
	"b": [[0, 6], [0, 5], [0, 4], [0, 3], [0, 2], ],
	"c": [[1, 2], [2, 2], [3, 2], [0, 3], [0, 4], [0, 5], [1, 6], [2, 6], [3, 6]],
	"d": [],
	"e": [[0, 6], [0, 5], [0, 4], [0, 3], [0, 2], [1, 6], [2, 6], [1, 2], [2, 2], [1, 4], [2, 4]],
	"f": [],
	"g": [],
	"h": [[0, 6], [0, 5], [0, 4], [0, 3], [0, 2], [3, 6], [3, 5], [3, 4], [3, 3], [3, 2], [1, 4], [2, 4]],
	"i": [[0, 2], [1, 2], [2, 2], [3, 2], [4, 2], [0, 6], [1, 6], [2, 6], [3, 6], [4, 6], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6]],
	"j": [],
	"k": [],
	"l": [[0, 6], [0, 5], [0, 4], [0, 3], [0, 2], [1, 6], [2, 6]],
	"m": [[0, 6], [0, 5], [0, 4], [0, 3], [0, 2], [1, 3], [2, 4], [3, 3], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6]],
	"n": [],
	"o": [[2, 2], [3, 3], [4, 4], [3, 5], [2, 6], [1, 5], [0, 4], [1, 3]],
	"p": [],
	"q": [],
	"r": [],
	"s": [],
	"t": [],
	"u": [],
	"v": [[0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [3, 5], [3, 4], [4, 3], [4, 2]],
	"w": [],
	"x": [],
	"y": [],
	"z": [],
}

def drawLetter(matrix, letter, xPos):
	if letter == " ":
		return {
			"maxX": xPos + 2
		}

	items = letterMap[letter]

	maxX = xPos

	for coord in items:
		x = coord[0] + xPos
		y = coord[1]

		if x < gridX and y < gridY and x >= 0 and y >= 0:
			matrix[x][y] = 1
			maxX = max(maxX, x)

	return {
		"maxX": maxX + 2
	}

def createEmptyMatrix():
	return [[0 for i in range(gridY)] for j in range(gridX)]

def printMatrix(matrix):
	for i in range(gridY):
		for j in range(gridX):
			print('@' if matrix[j][i] == 1 else ' ', end='', flush=True)
		print()

def resetMatrix(matrix):
	for i in range(len(matrix)):
		row = matrix[i]

		for j in range(len(row)):
			row[j] = 0

def main():
	letters = "i love mia hello"
	matrix = createEmptyMatrix()

	for offset in reversed(range(0, 100, 2)):
		x = offset


		for letter in letters:
			x = drawLetter(matrix, letter, x)["maxX"]

		clearTerminalWindow()
		printMatrix(matrix)
		resetMatrix(matrix)
		time.sleep(.2)

main()
