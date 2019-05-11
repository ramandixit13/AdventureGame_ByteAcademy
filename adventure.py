# Adventure game


#The board is represented as a nested list.
board = []
'''
board = [[1,0,0,0],[0,1,0,0],[0,1,0,0],[2,1,1,1]] >> board in nested list.
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
			new_pos = (self.pos_x, self.pos_y + 1)
		elif direction == 'down':
			new_pos = (self.pos_x,self.pos_y -1)
		elif direction == 'right':
			new_pos = (self.pos_x + 1,self.pos_y)
		elif direction == 'left':
			new_pos = (self.pos_x - 1,self.pos_y)
		
		
		if check_pos(new_pos)[0]: # Checking if the first output of the function is True i.e. the move is valid
			self.position = new_pos
		elif not check_pos(new_pos)[0]: # Checking if the first output of the fuction is False i.e. the move isn't valid
			print(check_pos(new_pos)[1])
				

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
	if y > board_size or x > board_size:
		return False, "Sorry! You cannot move outside the board."
	if board[y][x] == 1:
		return True, "On path"
	if board[y][x] == 2:
		return True, "In room"	

user = User("legend")

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


def game():
	for i in range(20):	
		choose = input("Please select a move (up, down, left or right)")
		user.move(choose)
		result.check()
		print(f"You got {i} chances left!")


#if __name__ == "__main__":
game()