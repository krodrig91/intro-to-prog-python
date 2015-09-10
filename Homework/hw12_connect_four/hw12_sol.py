'''
Created on Apr 27, 2015
@author:	Kelvin Rodriguez
'''
MARKERS = {'X', 'O'}

class Board(object):
	def __init__(self, width = 7, height = 6):
		'''	Contructs an object of type Board.
			Precondition: the methods for this class assume minimum 
			values of width = 7 and height = 6.
		'''
		self.__width = width
		self.__height = height
		self.__board = [[' '] * width for row in range(height)]

	def __str__(self):
		'''	Returns a string representation for an object of type Board.
		'''
		board = ''
		for row in range(self.__height):
			board += '|'
			for col in range(self.__width):
				board += self.__board[row][col] + '|'
			board += '\n'

		for col in range(self.__width):
			board += '--'
		board += '-'
		board += '\n'
		board += ' '

		for col in range(self.__width):
			board += str(col) + ' '

		return board

	def allowsMove(self, col):
		'''	Returns True if the calling Board object can allow a move
			into column col (because there is space available). Returns
			False if col does not have space available or if it is not
			a valid column.
		'''
		if col not in range(self.__width) : return False
		
		height_index = self.__height - 1
		while height_index >= 0:
			if self.__board[height_index][col] == ' ': return True
			else: height_index += -1
		return False

	def addMove(self, col, ox):
		'''	Adds an ox checker, where ox is a variable holding a string
			that is either "X" or "O", into column col.
		'''
		height_index = self.__height - 1
		while height_index >= 0:
			if self.__board[height_index][col] == ' ': 
				self.__board[height_index][col] = ox
				return
			else: height_index += -1
	
	def setBoard(self, moveString):
		'''	Takes in a string of columns and places alternating checkers
			in those columns, starting with 'X'.
		'''
		nextCh = 'X'
		for colString in moveString:
			col = int(colString)
			if 0 <= col <= self.__width: self.addMove(col, nextCh)
			if nextCh == 'X': nextCh = 'O'
			else: nextCh = 'X'

	def delMove(self, col):
		'''	Removes the top checker from the column col. If the column
			is empty, then delMove() does nothing.
		'''
		for row in range(self.__height):
			if self.__board[row][col] in MARKERS:
				self.__board[row][col] = ' '
				return
		print "You can't delete a move from this column."

	def horizontalWin(self, ox):
		'''	Helper method for winsFor() method. Returns True if four
			consecutive checkers are found within any row of the board
			object and returns False otherwise.
		'''
		for row in range(self.__height):
			for col in range(self.__width - 3):
				if self.__board[row][col]     \
				== self.__board[row][col + 1] \
				== self.__board[row][col + 2] \
				== self.__board[row][col + 3] \
				== ox:
					return True
		return False

	def verticalWin(self, ox):
		'''	Helper method for winsFor() method. Returns True if four
			consecutive checkers are found within any column of the 
			board object and returns False otherwise.
		'''
		for row in range(self.__height - 3):
			for col in range(self.__width):
				if self.__board[row][col] 	  \
				== self.__board[row + 1][col] \
				== self.__board[row + 2][col] \
				== self.__board[row + 3][col] \
				== ox:
					return True
		return False

	def diagonalWin(self, ox):
		'''	Helper method for winsFor() method. Returns True if four
			consecutive checkers are found within any diagonal of the 
			board object and returns False otherwise.
		'''
		# check for backward diagonal
		for row in range(self.__height - 3):
			for col in range(self.__width - 3):
				if self.__board[row][col]		  \
				== self.__board[row + 1][col + 1] \
				== self.__board[row + 2][col + 2] \
				== self.__board[row + 3][col + 3] \
				== ox:
					return True

		# check for forward diagonal
		for row in range(self.__height - 3):
			for col in range(self.__width - 1, -1, -1):
				if self.__board[row][col]	      \
				== self.__board[row + 1][col - 1] \
				== self.__board[row + 2][col - 2] \
				== self.__board[row + 3][col - 3] \
				== ox:
					return True
		return False

	def winsFor(self, ox):
		'''	Returns True if the given checker, 'X' or 'O', held in ox,
			has won the calling Board object. Returns False otherwise.
		'''
		if self.horizontalWin(ox): return True
		elif self.verticalWin(ox): return True
		elif self.diagonalWin(ox): return True
		else: return False

	def hostGame(self):
		'''	Runs a loop allowing the user(s) to play a game once a board
			object calls it.
		'''
		
		print 'Welcome to Connect Four!'
		counter = 0
		turns = self.__width * self.__height # set number of turns to play

		while turns > 0:

			if counter % 2 == 0: player = 'X'
			else: player = 'O'

			print 
			print self
			print 

			ok = False
			while not ok:
				str_move = raw_input(player + "'s choice: ")
				try:
					move = int(str_move)
					if self.allowsMove(move):
						self.addMove(move, player)
						ok = True
					else:
						print "Can't play there, try again.\n"
						print self
						print 
				except:
					print '\nSorry, ' + str_move + ' is not valid input.'
					print 'Please enter a number.\n'
					print self
			
			if self.winsFor('X'):
				print self
				print '\nX Wins -- Congratulations!'
				return

			if self.winsFor('O'):
				print self
				print '\nO Wins -- Congratulations!'
				return 

			counter += 1
			turns -= 1

		print self	
		print 'The board is full, nobody won :('
		return

if __name__ == "__main__":

	board = Board()
	board.hostGame()
	'''
	# calls to test methods
	board = Board()
	board.setBoard('012345')
	print board
	board.delMove(5)
	print board
	board.addMove(4,'X')
	print board
	'''
# END

