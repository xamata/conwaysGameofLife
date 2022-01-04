'''
# conwaysGameofLife.py 
Conway's game of Life
Rules:
1. Filled in sqaure = 'alive'
2. Empty square = 'dead'
3. if 'alive' sqaure has 2 or 3 neighbors(touching, corner squares included)
	it will continue to live
4. if 'de#mes 'alive'
5. every other 'alive' square will become 'dead'
'''

# need to create a random board for the game
import random,copy, time

boardWidth = 100
boardHeight = 20

nextSquare = []
for x in range(boardWidth):
	column = []
	for y in range(boardHeight):
		# create a single glider with: 'if (x, y) in ((1, 0), (2, 1), (0, 2), (1, 2), (2, 2)):'
		if random.randint(0,1) == 0: # sqaure is alive
			column.append('#')
		else:
			column.append(' ') # sqaure is dead
	nextSquare.append(column) # nextSqaure is a list of column lists

# create the main code for the game
while True:
	# creating the game board
	print('\n\n\n\n')
	currentSquare = copy.deepcopy(nextSquare)
	for y in range(boardHeight): # for loop begins with y bc of how command line prints horizontally first
		for x in range(boardWidth):
			print(currentSquare[x][y], end='')
		print()

	# create the parameters for the game rules, checking the filled in boxes around each box
	# we have x and y, we need the surrounding coordinates:
	for x in range(boardWidth):
		for y in range(boardHeight):
			# we add/subtract depending on left or right
			# the % ensures leftCoord is always between 0 and Width-1
			# if it was (0-1) = -1 , that needs to be within 0 and boardWidth
			# mod will make it 99 (this is a mod wraparound technique)
			leftCoord = (x-1) % boardWidth
			rightCoord = (x+1) % boardWidth
			aboveCoord = (y+1) % boardHeight
			belowCoord = (y-1) % boardHeight 

			numOfNeighbors = 0
			if currentSquare[leftCoord][aboveCoord] == '#':
				numOfNeighbors += 1 # Neighbor on TopLeft
			if currentSquare[x][aboveCoord] == '#':
				numOfNeighbors += 1 # Neighbor on Top	
			if currentSquare[rightCoord][aboveCoord] == '#':
				numOfNeighbors += 1 # Neighbor on TopRight
			if currentSquare[leftCoord][y] == '#':
				numOfNeighbors += 1 # Neighbor on Left		
			if currentSquare[rightCoord][y] == '#':
				numOfNeighbors += 1 # Neighbor on Right	
			if currentSquare[leftCoord][belowCoord] == '#':
				numOfNeighbors += 1 # Neighbor on BottomLeft
			if currentSquare[x][belowCoord] == '#':
				numOfNeighbors += 1 # Neighbor on Bottom
			if currentSquare[rightCoord][belowCoord] == '#':
				numOfNeighbors += 1 # Neighbor on BottomRight

			# add or delete '#' depending on the rules of the game
			if currentSquare[x][y] == '#' and (numOfNeighbors == 2 or numOfNeighbors == 3):
				nextSquare[x][y] = '#'
			elif currentSquare[x][y] == ' ' and (numOfNeighbors == 3):
				nextSquare[x][y] = '#'
			else: 
				nextSquare[x][y] = ' '

	time.sleep(0.25)
