#!/usr/bin/env python3
import copy
# Adventure game


#The board is represented as a nested list.
board = [[1,0,0,0],[1,1,0,0],[0,1,0,0],[2,1,1,1]]
'''
board = [[1,0,0,0],[0,1,0,0],[0,1,0,0],[2,1,1,1]] >> board in nested list.
board[y] is the y coordinate.
board[y][x] is the x coordinate.

0[1,0,0,0]
1[1,1,0,0]
2[0,1,0,0]
3[2,1,1,1]
  0 1 2 3

'''
#The size of the board. It's set to zero as default.
grid_size = 4
board_size = grid_size - 1

'''
Create a user class with the ability to move in a direction
'''
class User:
	'''
	Initializing user class with a username and position
	'''
	def __init__(self,username):
		self.username = username
		self.position = (0,0)
		self.pos_x = self.position[0]
		self.pos_y = self.position[1]

	'''
	Each user can move in a certain direction. Currently, this implementation 
	supports only movement by one coordinate
	'''
	def move(self, direction):
		if direction == 'up':
			new_x = self.pos_x
			new_y = self.pos_y - 1

		elif direction == 'down':
			new_x = self.pos_x
			new_y = self.pos_y + 1
		elif direction == 'right':
			new_x = self.pos_x + 1
			new_y = self.pos_y
		elif direction == 'left':
			new_x = self.pos_x - 1
			new_y = self.pos_y

		if check_pos(new_x,new_y)[0]: # Checking if the first output of the function is True i.e. the move is valid
			print(f"Moving to ({new_x},{new_y})...")
			self.position = (new_x,new_y)
			self.pos_x = new_x
			self.pos_y = new_y
			print(f"Your current position is {self.position}")
		elif not check_pos(new_x,new_y)[0]: # Checking if the first output of the fuction is False i.e. the move isn't valid
			print(check_pos(new_x,new_y)[1])
				

'''
This function checks if the users move is valid.
It returns two outputs, one being a boolean stating
if the move is True/False and another detailing the 
descriptive comment for the move
'''
def check_pos(*coordinates):
	x = coordinates[0]
	y = coordinates[1]
	if board[y][x] == 0:
		return False, "Cannot move outside the path. Make another choice."
	if y > board_size or x > board_size or y < 0 or x < 0:
		return False, "Sorry! You cannot move outside the board."
	if board[y][x] == 1:
		return True, "On path"
	if board[y][x] == 2:
		return True, "In room"	

def move():
	choice = input("Please select a move (up, down, left or right)")
	if choice not in ["up","down","left",'right']:
		return False
	else:
		return choice	

user = User("legend")



# class result:

# 	def check():
# 		if board[y][x] == 2:
# 			result.show()
			

# 	def show():
# 		print("Congratulations! You Won!")
# 		break
# 		'''
# 		#Adding the name  in leaderboard.
# 		with open('leaderboard.txt', 'a') as fout:
# 			name = input("Enter your name: ").capitalize()
# 			fout.write(f"{name} , score: {}")  #Maybe use the step of the for loop to formulate the score?
# 		'''
def printing_board(board, user):
	new_board = copy.deepcopy(board)
	new_board[user.pos_y][user.pos_x] = "X"
	[print(i) for i in new_board]

# Prince
def run_rpg():
	i = 1
	while i > 0:
		print("Here's the board:")
		printing_board(board,user)
		choose = move()
		if not choose:
			print("Pick a valid choice.")
			print(f"You've gone through {i} chances")
			i+=1
			continue
		user.move(choose)
		print(f"You've gone through {i} turns")
		if check_pos(user.pos_x,user.pos_y)[0]:
			if check_pos(user.pos_x,user.pos_y)[1] == "In room":
				print("Congratulations! You found the room, you win!")
				calc_score()
				break
		i+=1


def calc_score():
	print("Now calculating your score....")
	print("Your score is....")
	pass

# Ruchir
def Login():
	pass

# Raman
def leaderboard():
	pass

def game():
	Login()
	print("Thank you for logging in User X")
	print("Your top score is xxx")
	i = True
	while i:
		game_action = input(
'''
What would you like to do?
	p: play
	l: leaderboard
	q: quit
''')
		if game_action not in ['p','l','q']:
			print("Please enter a valid option")
			continue
		if game_action == 'q':
			print("Leaving the game now. Good bye.")
			break
		if game_action == 'l':
			print("Printing leaderboard...")
			leaderboard()
			continue
		if game_action == 'p':
			run_rpg()


			




# if __name__ == "__main__":
game()	