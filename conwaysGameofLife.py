'''
# conwaysGameofLife.py 
Conway's game of Life
Rules:
1. Filled in sqaure = 'alive'
2. Empty square = 'dead'
3. if 'alive' sqaure has 2 or 3 neighbors(touching, corner squares included)
	it will continue to live
4. if 'dead' square has 3 neighbors, it becomes 'alive'
5. every other 'alive' square will become 'dead'
'''

import random, copy, time
# need to create a random scenario for the game to start
boardWidth = 150
boardHeight = 20

nextCells = [] # stores the current boards cell information
for x in range(boardWidth):
	column = []
	for y in range(boardHeight): 
		if random.randint(0,1) == 0:
			column.append('#') # adds a living cell
		else: 
			column.append(' ') # adds a dead cell
	nextCells.append(column)

# create the game within a While loop
while True:
	print('\n\n\n\n\n') # separating the different boards
	currentCells = copy.deepcopy(nextCells)

	# print current cells on the screen
	for y in range(boardHeight):
		for x in range(boardWidth):
			print(nextCells[x][y], end='') # print the # or space
		print() # print a newline at the end of the row.

	# Cacluate the next step's cells based on current step's cells:
	for x in range(boardWidth):
		for y in range(boardHeight):
			# Get the neighboring coordinates: 
			leftCoord = (x-1) % boardWidth
			rightCoord = (x+1) % boardWidth
			aboveCoord = (y-1) % boardHeight
			belowCoord = (y+1) % boardHeight

			# Count number of living neighbors:
			numNeighbors = 0
			if currentCells[leftCoord][aboveCoord] == '#':
				numNeighbors += 1 # Top-left neighbor is alive.
			if currentCells[x][aboveCoord] == '#':
				numNeighbors += 1 # Top neighbor is alive.
			if currentCells[rightCoord][aboveCoord] == '#':
				numNeighbors += 1 # Top-right neighbor is alive.
			if currentCells[leftCoord][y] == '#':
				numNeighbors += 1 # Left neighbor is alive.
			if currentCells[rightCoord][y] == '#':
				numNeighbors += 1 # Right neighbor is alive.	
			if currentCells[leftCoord][belowCoord] == '#':
				numNeighbors += 1 # Bottom-Left neighbor is alive.
			if currentCells[x][belowCoord] == '#':
				numNeighbors += 1 # Bottom neighbor is alive.
			if currentCells[rightCoord][belowCoord] == '#':
				numNeighbors += 1 # Bottom-Right neighbor is alive.

			# set cell based on conways game of life rules
			if currentCells[x][y] == '#' and (numNeighbors ==2 or numNeighbors==3):
				nextCells[x][y] = '#'
			elif currentCells[x][y] == ' ' and numNeighbors == 3:
				nextCells[x][y] = '#'
			else:
				nextCells[x][y] = ' '
	time.sleep(0.5)




























for x in range(boardWidth):
	for y in range(boardHeight):
		numNeighbors = 0
		if nextCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors ==3):
			# Living cells with 2 or 3 neightbors stay alive:
			nextCells[x][y] = '#'
		elif nextCells[x][y] == ' ' and numNeighbors == 3:
			# Dead cells with 3 neighbors become alive:
			nextCells[x][y] = '#'
		else: 
			# Everything else dies or stays dead:
			nextCells[x][y] = ' '

# create the next cells information, where the game loops as well
	
