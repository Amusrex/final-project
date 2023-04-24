from numpy import array
MOVEMENT = {'U':array([0,0,1]),
	'L':array([0,-1,0]),
	'R':array([0,1,0]),
	'F':array([1,0,0]),
	'B':array([-1,0,0]),
	'D':array([0,0,-1])}
class Room1():
	def __init__(self):
		self.RoomItems = []
		self.location = array([0,0,0])
		self.allowed_movement = []
		self.direction = ''
	def move_player(self):
		new_direction = input("Which way do you want to move?\n")
		directions = new_directions.upper()
		if direction in self.allowed_movement:
			self.location += MOVEMENT[direction]
			if direction == "U":
				print(f"You moved up")
			if direction == "L":
				print("You moved left")
			if direction == "D":
				print("You moved down")
			if direction == "R":
				print("You moved right")
			if direction == "F":
				print("You moved forward")
			if direction == "B":
				print("You moved backwards")
		else:
			print("Invalid direction")
		location = self.location
		return location
room = Room1()


