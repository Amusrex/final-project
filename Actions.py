from numpy import array
from Beginning import Begin
from Rooms import Room1
b = Begin()
MOVEMENT = {'U':array([0,0,1]),
	'N':array([0,0,0]),
	'L':array([0,1,0]),
	'R':array([0,-1,0]),
	'F':array([1,0,0]),
	'B':array([-1,0,0]),
	'D':array([0,0,-1])}
class actions():
	def __init__(self):
		self.location = array([0,0,0])
		self.allowed_movement = []
		self.RoomItem = ['map','note']
		self.player_inventory = []
	def move_player(self):
		print(f"{self.allowed_movement}")
		sdirection = input("Which way do you want to move?\n")
		direction = sdirection.upper()
		if direction == 'Q':
			print('Goodbye')
			quit()
		if direction == 'M':
			print(f'{b.menu1()}')
			print(f'{self.allowed_movement}')
			sdirection = input("Which way do you want to move?\n")
		if direction == 'I':
			print('Here is your inventory')
			print(f'{b.menu1()}')
			direction = 'N'
	
			
			direction = sdirection.upper()
		if direction in self.allowed_movement:
			self.location += MOVEMENT[direction]
			if direction == 'N':
				print('')
			if direction == "U":
				print(f"You moved up")
				print(f'{self.location}')
			if direction == "L":
				print("You moved left")
				print(f'{self.location}')
			if direction == "D":
				print("You moved down")
				print(f'{self.location}')
			if direction == "R":
				print("You moved right")
				print(f'{self.location}')
			if direction == "F":
				print("You moved forward")
				print(f'{self.location}')
			if direction == "B":
				print("You moved backwards")
				print(f'{self.location}')
		else:
			print("Invalid direction")
		self.allowed_movement = []
		location = self.location
		return location
	def out(self):
	
		if all(self.location == (0,0,0)):
			self.allowed_movement.append('L')
			self.allowed_movement.append('R')
			self.allowed_movement.append('F')
			
		if all(self.location == (0,1,0)):
			self.allowed_movement.append('R')
			if 'map' in self.RoomItem:
				self.allowed_movement.append('P')
				move = None
				while move != 'P'and'R':
					print(f'{self.allowed_movement}')
					smove = input('''You found a map.
What would you like to do?\n''')
					move = smove.upper()
				
					if move == 'P':
						self.player_inventory.append('map')
						self.RoomItem.remove('map')
						self.allowed_movement.remove('P')
						print('You picked up the map!')
					elif move == 'R':
						self.allowed_movement.remove('P')
						break
					else:
						print("Not a valid action")
					


		if all(self.location == (0,-1,0)):
			self.allowed_movement.append('L')
		if all(self.location == (1,0,0)):
			self.allowed_movement.append('F')
			print("yay")
			quit()
		

		
		return self.allowed_movement




