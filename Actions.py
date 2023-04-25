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
		self.RoomItem = ['map','note','riddle','protective amulet','flash light','torch']
		self.animals = ['tree monster']
		self.player_inventory = []
		self.actions = ['Q','S','M','I','O']
	def move_player(self):
		print(f"{self.actions}")
		print(f"Allowed movements\n{self.allowed_movement}")
		
		sdirection = input("What would you like to do?\n")
		direction = sdirection.upper()
		if direction == 'Q':
			print('Goodbye')
			quit()
		elif direction == 'M':
			print(f'{b.menu1()}')
			print(f'{self.allowed_movement}')
			sdirection = input("Which way do you want to move?\n")
		elif direction == 'I':
			if not self.player_inventory:
				print('Your inventory is empty. Explore to find and gather items.')
			else:
				print('Here is your inventory')
				print(f'{self.player_inventory}')
			direction = 'N'
		elif direction == 'O':
			ask = input("What item would you like to use\n")
			if ask == 'map':
				print('''
                         _
             _   _   _  |_|	
           _|_|_|_|_|_| |_|	
          |_|_|_|_|_|_|_|_|_ _ _
          |_| |_|   |_|_|_|_|_|_|  _        
                   _ _ _ _ _ _|_|_|_|_
               _ _|_|_|_|_|_|_|_|_|_|_|
     _ 	      |_|_|_|       |_|   |_|
    |_|_ _ _ _ _ _|_|_  
    |_|_|_|_|_|_|_|_|_|	
 _ _ _|_|_	
|_|_|_|_|_|		
  |_|_ _ _ _
  |_|_|_|_|_|  _
	|_|_ _|_|
	|_|_|_|_|
	 _|_|_
	|_|_|_|''')
			elif ask == 'riddle':
				print('''In a fiery tomb, the treasure lies,
Amidst the ash and smoke that rise.
The earth may shake, the lava flow,
But riches beyond measure, it will show.
Only the bravest, the cleverest too,
Can find the way to this hidden loot.''')
			else:
				print('Cannot use that item')

	
			
			direction = sdirection.upper()
		elif direction in self.allowed_movement:
			self.location += MOVEMENT[direction]
			if direction == 'N':
				print('')
			elif direction == "U":
				print(f"You moved up")
				print(f'{self.location}')
			elif direction == "L":
				print("You moved left")
				print(f'{self.location}')
			elif direction == "D":
				print("You moved down")
				print(f'{self.location}')
			elif direction == "R":
				print("You moved right")
				print(f'{self.location}')
			elif direction == "F":
				print("You moved forward")
				print(f'{self.location}')
			elif direction == "B":
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
						direction = move
						self.allowed_movement.remove('P')
						self.allowed_movement.remove('R')
						self.allowed_movement.append('L')
						self.allowed_movement.append('R')
						self.allowed_movement.append('F')
						self.location += MOVEMENT[direction]
						print(f'You moved right\n{self.location}')
						break
					else:
						print("Not a valid action")
					


		if all(self.location == (0,-1,0)):
			self.allowed_movement.append('L')
			if 'riddle' in self.RoomItem:
				self.allowed_movement.append('P')
				move = None
				while move != 'P'and'L':
					print(f'{self.allowed_movement}')
					smove = input('''You found an old riddle.
What would you like to do?\n''')
					move = smove.upper()
				
					if move == 'P':
						self.player_inventory.append('riddle')
						self.RoomItem.remove('riddle')
						self.allowed_movement.remove('P')
						print('You picked up the riddle!')
					elif move == 'L':
						direction = move
						self.allowed_movement.remove('P')
						self.allowed_movement.append('R')
						self.allowed_movement.append('F')
						self.location += MOVEMENT[direction]
						print(f'You moved left\n{self.location}')
						
						break
					else:
						print("Not a valid action")

		if all(self.location == (1,0,0)):
			self.allowed_movement.append('F')
			self.allowed_movement.append('B')
		if all(self.location == (2,0,0)):
			self.allowed_movement.append('L')
			self.allowed_movement.append('R')
			self.allowed_movement.append('B')
			if 'flash light' in self.RoomItem:
				self.allowed_movement.append('P')
				move = None
				while move != 'P'and'L'and'R'and'B':
					print(f'{self.allowed_movement}')
					smove = input('''You found a flash light.
What would you like to do?\n''')
					move = smove.upper()
					if move == 'P':
						self.player_inventory.append('flash light')
						self.RoomItem.remove('flash light')
						self.allowed_movement.remove('P')
						print('You picked up the flash light!')
					elif move == 'L':
						direction = move
						self.allowed_movement.remove('R')
						self.allowed_movement.remove('L')
						self.allowed_movement.remove('P')
						self.allowed_movement.remove('B')
						self.location += MOVEMENT[direction]
						print(f'You moved left\n{self.location}')
						
						break
					elif move == 'R':
						direction = move
						self.allowed_movement = []
						
						self.location += MOVEMENT[direction]
						print(f'You moved left\n{self.location}')
						
						break
					elif move == 'B':
						direction = move
						self.allowed_movement.remove('P')
						self.allowed_movement.remove('R')
						self.allowed_movement.append('F')
						self.allowed_movement.remove('L')
						self.allowed_movement.remove('B')
						self.allowed_movement.append('B')
						self.location += MOVEMENT[direction]
						print(f'You moved left\n{self.location}')

					else:

						print("Not a valid action")
		if all(self.location == (2,1,0)):
			self.allowed_movement.append('R')
			self.allowed_movement.append('F')
		if all(self.location == (2,-1,0)):
			self.allowed_movement.append('L')
			self.allowed_movement.append('R')
		if all(self.location == (2,-2,0)):
			self.allowed_movement.append('L')
			self.allowed_movement.append('F')
		if all(self.location == (3,1,0)):
			self.allowed_movement.append('F')
			self.allowed_movement.append('B')
		if all(self.location == (3,-2,0)):
			self.allowed_movement.append('B')
			if 'protective amulet' in self.RoomItem:
				self.allowed_movement.append('P')
				move = None
				while move != 'P'and'B':
					print(f'{self.allowed_movement}')
					smove = input('''You found a protective amulet.
What would you like to do?\n''')
					move = smove.upper()
					if move == 'P':
						self.player_inventory.append('protective amulet')
						self.RoomItem.remove('protective amulet')
						self.allowed_movement.remove('P')
						print('You picked up the protective amulet!')
					elif move == 'B':
						direction = move
						self.allowed_movement.remove('R')
						self.allowed_movement.remove('L')
						self.allowed_movement.remove('P')
						self.allowed_movement.remove('B')
						self.location += MOVEMENT[direction]
						print(f'You moved backwards\n{self.location}')
					else:
						print("Not a valid action")
		if all(self.location == (4,0,0)):
			self.allowed_movement.append('L')
			
			if 'tree monster' in self.animals:
				move = input("Oh no!\n A tree monster. (fight/run)\n")
				if move == 'run':
					print("You ran all the way back to the beach")
					
					self.allowed_movement.append('R')
					self.allowed_movement.append('F')
					self.location = array([0,0,0])
				elif move == 'fight':
					item = input("What item do you want to use\n")
					if item == 'torch':
						print('You torched the tree monster and killed it. Good job!')
					elif item == 'protective amulet':
						if 'protective amulet' in self.player_inventory:
							print('You used the protective amulet and lived but you broke the protective amulet.')
							self.player_inventory.remove('protective amulet')
							self.animal.remove('tree monster')
						else:
							print("You don't have that item. You died")
							
							option = input("Do you want to play again? (yes/no)\n")
							if option == 'yes':
								
								self.allowed_movement.append('R')
								self.allowed_movement.append('F')
								self.RoomItem = ['map','note','riddle','protective amulet','flash light']
								self.animals = ['tree monster']
								self.player_inventory = []
								self.location = array([0,0,0])
							elif option == 'no':
								print("Goodbye")
								quit()
							else:
								print("Not a valid input")
					else:
						print("wrong item. You died")
						option = input("Do you want to play again? (yes/no)\n")
						if option == 'yes':
							
							self.allowed_movement.append('R')
							self.allowed_movement.append('F')
							
							self.RoomItem = ['map','note','riddle','protective amulet','flash light','torch']
							self.animals = ['tree monster']
							self.player_inventory = []
							self.location = array([0,0,0])
						
						elif option == 'no':
							print("Goodbye")
							quit()
						else:
							print("Not a valid input")
		if all(self.location == (4,1,0)):
			self.allowed_movement.append('L')
			self.allowed_movement.append('R')
			self.allowed_movement.append('B')
		
		if all(self.location == (4,2,0)):
			self.allowed_movement.append('L')
			self.allowed_movement.append('R')
		if all(self.location == (4,3,0)):
			self.allowed_movement.append('L')
			self.allowed_movement.append('R')
		if all(self.location == (4,4,0)):
			self.allowed_movement.append('R')
			self.allowed_movement.append('F')


			
		

		
		return self.allowed_movement




