# Adventure game


#The board or the list that represent the board.
board = []
'''
board = [[1,0,0,0],[0,1,0,0],[0,1,0,0],[2,1,1,1]] >> blank board
board[y] is the y coordinate.
board[y][x] is the x coordinate.

0[1,0,0,0]
1[0,1,0,0]
2[0,1,0,0]
3[2,1,1,1]
  0 1 2 3

'''
#The size of the board. It's set to zero as default.
grid_size = 4
board_size = grid_size - 1

#This stores the current coordinates of the user. It is 0,0 by default.
#user_location = ['x', 'y'] >> Syntax
user_location = [0,0]
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
			elif(board[y-1][x] == 1):

				#print("user moved up")
				user_location[1] -= 1
			
			elif board[y-1][x] == 2:
				#print("user moved up")
				user_location[1] -= 1
		
		else:
			print("Sorry! You cannot move outside the board.")
			move.choice()

	def down():
		'''
		x is constant, y is variable
		'''
		
		if y < board_size:
			if board[y+1][x] == 0:
				#print("Cannot move outside the path. Make another choice.")
			elif board[y+1][x] == 1:
				#print("user moved down")
				user_location[1] += 1
			elif board[y+1][x] == 2:
				#print("user moved down")
				user_location[1] += 1
		else:
			print("Sorry! You cannot move outside the board.")
			move.choice()

	def right():
		'''		
		since the user is only moving right, 
		we only have to consider the x coordinate
		cause y is constant
		'''
		if x < board_size:
			if board[y][x+1] == 0:
				#print("Cannot move outside the path. Make another choice.")
			elif board[y][x+1] == 1:
		
				#print("user moved right")
				user_location[0] += 1
			elif board[y][x+1] == 2:
				#print("user moved right")
				user_location[0] += 1
		else:
			print("Sorry! You cannot move outside the board.")
			move.choice()

	def left():
		'''
		y is constant, x is variable
		'''
		if x <= board_size and x != 0:
			if board[y][x-1] == 0:
				#print("Cannot move outside the path. Make another choice.")
			elif board[y][x-1] == 1:
				#print("user moved left")
				user_location[0] -= 1
			elif board[y][x-1] == 2:
				#print("user moved left")
				user_location[0] -= 1
		else:
			print("Sorry! You cannot move outside the board.")
			move.choice()

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
		#For when the user enters anything other than our predefined commands.
		else:
			print("You have made an invalid move. Please try again.\n")
			move.choice() #Wrong choices are excluded from the max move counter.

class result:

	def check():
		if board[y][x] == 2:
			result.show()

	def show():
		print("Congratulations! You Won!")
		break
		'''
		#Adding the name  in leaderboard.
		with open('leaderboard.txt', 'a') as fout:
			name = input("Enter your name: ").capitalize()
			fout.write(f"{name} , score: {}")  #Maybe use the step of the for loop to formulate the score?
		'''