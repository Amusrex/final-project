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
	def move_player(self, direction):
		if direction in MOVEMENT:
			self.location += MOVEMENT[direction]
			print(f"You moved {direction}")
		else:
			print("Invalid direction")
room = Room1()


