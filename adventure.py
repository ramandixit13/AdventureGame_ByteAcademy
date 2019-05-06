# Adventure game


#The board or the list that represent the board.
board = []
'''
board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] >> blank board
board[y] is the y coordinate.
board[y][x] is the x coordinate.
'''
#The size of the board. It's set to zero as default.
grid_size = 4
board_size = grid_size - 1
#This stores the current coordinates of the user. It is 0,0 by default.
user_location = ['x','y']
x = user_location[0]
y = user_location[1]




class move:

	def up():
		'''
		since the user is only moving upward, 
		we only have to consider the y coordinate
		cause x is constant
		'''
		if y <= board_size and y != o:
			if board[y-1][x] == 0:
				#print("Cannot move outside the path. Make another choice.")
			elif board[y-1][x] == 1:
				#print("user moved up")
				user_location[1] -= 1
			elif board[y-1][x] == 2:
				#print("user moved up")
				user_location[1] -= 1
		else:
			print("Sorry! You cannot move outside the board.")




	def down():
		'''
		x is constant, y is svariable
		'''


	def right():
		'''
		since the user is only moving right, 
		we only have to consider the x coordinate
		cause y is constant
		'''



	def left():
		'''
		y is constant, x is variable
		'''

	def choice():
		'''
		this function asks the user to make a choice and 
		calls the necessary functions to make the move
		'''
		user_choice = str(input("Where do you want to move next?"))
		
		if user_choice == "up" or user_choice == "u":
			move.up()
		elif user_choice == "down" or user_choice == "d":
			move.down()
		elif user_choice == "right" or user_choice == "r":
			move.right()
		elif user_choice == "left" or user_choice == "l":
			move.left()
		else:
			print("You have made an invalid move. Please try again")
			move.choice() #Wrong choices are excluded from the max move counter.

	