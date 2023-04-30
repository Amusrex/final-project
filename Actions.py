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
		self.RoomItem = ['map','note','riddle','protective amulet','flash light','torch',
		'grapple hook','machete','wood1','wood2','wood3','key','treasure','rope','nails',
		'sheets','diary','']
		self.animals = ['tree monster','bear','lion','giant spider']
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
			print(f'{self.actions}')
			print("allowed movements")
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
				if 'map' in self.player_inventory:
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
  |_|_ _ _ _ _
  |_|_|_|_|_|_|_
	|_|_ _|_|
	|_|_|_|_|
	 _|_|_
	|_|_|_|''')
				else:
					print("You don't have that item.")
			elif ask == 'riddle':
				if 'riddle' in self.player_inventory:
					print('''In a fiery tomb, the treasure lies,
Amidst the ash and smoke that rise.
The earth may shake, the lava flow,
But riches beyond measure, it will show.
Only the bravest, the cleverest too,
Can find the way to this hidden loot.''')
				else:
					print("You don't have that item.")
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
	def dead(self):
		print("You fell into the lava. You died")
		option = input("Do you want to play again? (yes/no)\n")
		if option == 'yes':
	
			self.allowed_movement.append('L')
			self.allowed_movement.append('R')
			self.allowed_movement.append('F')
			self.RoomItem = ['map','note','riddle','protective amulet','flash light','torch',
		'grapple hook','machete','wood1','wood2','wood3','key','treasure','rope','nails',
		'sheets','diary','']
			self.animals = ['tree monster','bear','lion','giant spider']
			self.player_inventory = []
			self.location = array([0,0,0])
		elif option == 'no':
			print("Goodbye")
			quit()
		else:
			print("Not a valid input")
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
			choice = None
			if choice == 'B':
				print("You left the beach and are now on the beach")
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
			self.allowed_movement.append('R')
		if all(self.location == (4,-1,0)):
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
						if 'torch' not in self.player_inventory:
							print("You don't have this item. You died")
							option = input("Do you want to play again? (yes/no)\n")
							if option == 'yes':
								
								self.allowed_movement.append('R')
								self.allowed_movement.append('F')
								self.RoomItem = ['map','note','riddle','protective amulet','flash light','torch',
		'grapple hook','machete','wood1','wood2','wood3','key','treasure','rope','nails',
		'sheets','diary','']
								self.animals = ['tree monster','bear','lion','giant spider']
								self.player_inventory = []
								self.location = array([0,0,0])
							elif option == 'no':
								print("Goodbye")
								quit()
							else:
								print("Not a valid input")

						print('You torched the tree monster and killed it. Good job!')
						self.animals.remove('tree monster')
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
								self.RoomItem = ['map','note','riddle','protective amulet','flash light','torch',
		'grapple hook','machete','wood1','wood2','wood3','key','treasure','rope','nails',
		'sheets','diary','']
								self.animals = ['tree monster','bear','lion','giant spider']
								self.player_inventory = []
								self.location = array([0,0,0])
							elif option == 'no':
								print("Goodbye")
								quit()
							else:
								print("Not a valid input")
					else:
						print('Not a valid input. You died')
						option = input("Do you want to play again? (yes/no)\n")
						if option == 'yes':
							self.allowed_movement.append('R')
							self.allowed_movement.append('F')
							self.RoomItem = ['map','note','riddle','protective amulet','flash light','torch',
		'grapple hook','machete','wood1','wood2','wood3','key','treasure','rope','nails',
		'sheets','diary','']
							self.animals = ['tree monster','bear','lion','giant spider']
							self.player_inventory = []
							self.location = array([0,0,0])
						elif option == 'no':
							print("Goodbye")
							quit()							
						else:
								print("Not a valid input")

				elif move not in ('run','fight'):
					print("wrong input. You died")
					option = input("Do you want to play again? (yes/no)\n")
					
					while option not in ['yes','no']:
						print("Not a valid action")
						option = input("Do you want to play again? (yes/no)\n")
					if option == 'yes':
						
						self.allowed_movement.append('R')
						self.allowed_movement.append('F')
						
						self.RoomItem = ['map','note','riddle','protective amulet','flash light','torch',
		'grapple hook','machete','wood1','wood2','wood3','key','treasure','rope','nails',
		'sheets','diary','']
						self.animals = ['tree monster','bear','lion','giant spider']
						self.player_inventory = []
						self.location = array([0,0,0])
						
					elif option == 'no':
						print("Goodbye")
						quit()
						
				
		if all(self.location == (4,1,0)):
			self.allowed_movement.append('L')
			self.allowed_movement.append('R')
			self.allowed_movement.append('B')
			if 'torch' in self.RoomItem:
				self.allowed_movement.append('P')
				move = None
				while move not in ['P','R','L','B']:
					print(f'{self.allowed_movement}')
					smove = input('''You found a torch.
What would you like to do?\n''')
					move = smove.upper()
					if move == 'P':
						self.player_inventory.append('torch')
						self.RoomItem.remove('torch')
						self.allowed_movement.remove('P')
						print('You picked up the torch!')
					elif move == 'B':
						direction = move
						self.allowed_movement.remove('R')
						self.allowed_movement.remove('L')
						self.allowed_movement.remove('P')
						self.allowed_movement.remove('B')
						self.allowed_movement.append('F')
						self.allowed_movement.append('B')
						self.location += MOVEMENT[direction]
						print(f'You moved backwards\n{self.location}')
						break
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
						self.allowed_movement.remove('L')
						self.allowed_movement.remove('R')
						self.allowed_movement.remove('P')
						self.allowed_movement.remove('B')
						self.allowed_movement.append('L')
						self.allowed_movement.append('R')
						self.location += MOVEMENT[direction]
						print(f'You moved right\n{self.location}')
						break
					else:
						print("Not a valid action")
			
				
		
		if all(self.location == (4,2,0)):
			self.allowed_movement.append('L')
			self.allowed_movement.append('R')
			choice = None
			if choice == 'L':
				print("You entered the jungle")
		if all(self.location == (4,3,0)):
			self.allowed_movement.append('L')
			self.allowed_movement.append('R')
			choice = None
			if choice == 'R':
				print("You entered the haunted forest")
		if all(self.location == (4,4,0)):
			self.allowed_movement.append('R')
			self.allowed_movement.append('F')
			if 'machete' in self.RoomItem:
				self.allowed_movement.append('P')
				move = None
				while move not in ['P','R','L','B','F']:
					print(f'{self.allowed_movement}')
					smove = input('''You found a machete.
What would you like to do?\n''')
					move = smove.upper()
				if move == 'P':
					self.player_inventory.append('machete')
					self.RoomItem.remove('machete')
					self.allowed_movement.remove('P')
					print('You picked up the machete!')
				
				elif move == 'R':
					direction = move
					self.allowed_movement.remove('R')
					self.allowed_movement.remove('L')
					self.allowed_movement.remove('P')
					self.allowed_movement.remove('B')
					self.allowed_movement.append('L')
					self.allowed_movement.append('R')
					self.location += MOVEMENT[direction]
					print(f'You moved right\n{self.location}')
					
				elif move == 'F':
					direction = move
					self.allowed_movement.remove('R')
					self.allowed_movement.remove('P')
					self.allowed_movement.remove('F')
					
					
					
					self.location += MOVEMENT[direction]
					print(f'You moved forward\n{self.location}')
					
					
				else:
					print("Not a valid action")
		if all(self.location == (5,4,0)):
			self.allowed_movement.append('F')
			self.allowed_movement.append('B')
		if all(self.location == (6,4,0)):
			self.allowed_movement.append('L')
			self.allowed_movement.append('R')
			self.allowed_movement.append('B')
			if 'grapple hook' in self.RoomItem:
				self.allowed_movement.append('P')
				move = None
				while move not in ['P','R','L','B']:
					print(f'{self.allowed_movement}')
					smove = input('''You found a grapple hook.
What would you like to do?\n''')
					move = smove.upper()
					if move == 'P':
						self.player_inventory.append('grapple hook')
						self.RoomItem.remove('grapple hook')
						self.allowed_movement.remove('P')
						print('You picked up the grapple hook!')
						
						break
					elif move == 'B':
						direction = move
						self.allowed_movement.remove('R')
						self.allowed_movement.remove('L')
						self.allowed_movement.remove('P')
						self.allowed_movement.remove('B')
						
						self.location += MOVEMENT[direction]
						print(f'You moved backwards\n{self.location}')
						break
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
						self.allowed_movement.remove('L')
						self.allowed_movement.remove('R')
						self.allowed_movement.remove('P')
						self.allowed_movement.remove('B')
						
						self.location += MOVEMENT[direction]
						print(f'You moved right\n{self.location}')
						break
					else:
						print("Not a valid action")
		if all(self.location == (6,5,0)):
			self.allowed_movement.append('L')
			self.allowed_movement.append('R')
		if all(self.location == (6,6,0)):
			self.allowed_movement.append('R')
			if 'wood1' in self.RoomItem:
				self.allowed_movement.append('P')
			move = None
			while move not in ['P','R','L','B']:
				print(f'{self.allowed_movement}')
				smove = input('''You found some wood.
What would you like to do?\n''')
				move = smove.upper()
				if move == 'P':
					self.player_inventory.append('wood1')
					self.RoomItem.remove('wood1')
					self.allowed_movement.remove('P')
					print('You picked up the wood!')
				elif move == 'B':
					direction = move
					self.allowed_movement.remove('R')
					self.allowed_movement.remove('L')
					self.allowed_movement.remove('P')
					self.allowed_movement.remove('B')
					self.allowed_movement.append('F')
					self.allowed_movement.append('B')
					self.location += MOVEMENT[direction]
					print(f'You moved backwards\n{self.location}')
					break
					
				elif move == 'R':
					direction = move
					self.allowed_movement.remove('L')
					self.allowed_movement.remove('R')
					self.allowed_movement.remove('P')
					self.allowed_movement.remove('B')
					self.allowed_movement.append('L')
					self.allowed_movement.append('R')
					self.location += MOVEMENT[direction]
					print(f'You moved right\n{self.location}')
					break
				else:
					print("Not a valid action")
		if all(self.location == (6,3,0)):
			self.allowed_movement.append('L')
			self.allowed_movement.append('R')
			self.allowed_movement.append('F')
		if all(self.location == (6,2,0)):
			self.allowed_movement.append('L')
			if 'lion' in self.animals:
				move = input("Oh no!\n A lion. (fight/run)\n")
				
				if move == 'run':
					print("You ran all the way back to the beach")
					
					self.allowed_movement.append('R')
					self.allowed_movement.append('F')
					self.location = array([0,0,0])
				elif move == 'fight':
					item = input("What item do you want to use\n")
					if item == 'machete':
						if 'machete' not in self.player_inventory:
							print("You don't have this item. You died")
							option = input("Do you want to play again? (yes/no)\n")
							if option == 'yes':
								
								self.allowed_movement.append('R')
								self.allowed_movement.append('F')
								self.RoomItem = ['map','note','riddle','protective amulet','flash light','torch',
		'grapple hook','machete','wood1','wood2','wood3','key','treasure','rope','nails',
		'sheets','diary','']
								self.animals = ['tree monster','bear','lion','giant spider']
								self.player_inventory = []
								self.location = array([0,0,0])
							elif option == 'no':
								print("Goodbye")
								quit()
							else:
								print("Not a valid input")

						print('You killed the lion. Good job!')
						self.animals.remove('lion')
					elif item == 'protective amulet':
						if 'protective amulet' in self.player_inventory:
							print('You used the protective amulet and lived but you broke the protective amulet.')
							self.player_inventory.remove('protective amulet')
							self.animals.remove('lion')
						else:
							print("You don't have that item. You died")
							
							option = input("Do you want to play again? (yes/no)\n")
							if option == 'yes':
								
								self.allowed_movement.append('R')
								self.allowed_movement.append('F')
								self.RoomItem = ['map','note','riddle','protective amulet','flash light','torch',
		'grapple hook','machete','wood1','wood2','wood3','key','treasure','rope','nails',
		'sheets','diary','']
								self.animals = ['tree monster','bear','lion','giant spider']
								self.player_inventory = []
								self.location = array([0,0,0])
							elif option == 'no':
								print("Goodbye")
								quit()
							else:
								print("Not a valid input")
					else:
						print('Not a valid input. You died')
						option = input("Do you want to play again? (yes/no)\n")
						if option == 'yes':
							self.allowed_movement.append('R')
							self.allowed_movement.append('F')
							self.RoomItem = ['map','note','riddle','protective amulet','flash light','torch',
		'grapple hook','machete','wood1','wood2','wood3','key','treasure','rope','nails',
		'sheets','diary','']
							self.animals = ['tree monster','bear','lion','giant spider']
							self.player_inventory = []
							self.location = array([0,0,0])
						elif option == 'no':
							print("Goodbye")
							quit()							
						else:
								print("Not a valid input")

				elif move not in ('run','fight'):
					print("wrong input. You died")
					option = input("Do you want to play again? (yes/no)\n")
					
					while option not in ['yes','no']:
						print("Not a valid action")
						option = input("Do you want to play again? (yes/no)\n")
					if option == 'yes':
						
						self.allowed_movement.append('R')
						self.allowed_movement.append('F')
						
						self.RoomItem = ['map','note','riddle','protective amulet','flash light','torch',
		'grapple hook','machete','wood1','wood2','wood3','key','treasure','rope','nails',
		'sheets','diary','']
						self.animals = ['tree monster','bear','lion','giant spider']
						self.player_inventory = []
						self.location = array([0,0,0])
						
					elif option == 'no':
						print("Goodbye")
						quit()
		if all(self.location == (7,3,0)):
			self.allowed_movement.append('F')
			self.allowed_movement.append('B')
		if all(self.location == (9,4,0)):
			self.allowed_movement.append('B')
			if 'rope' in self.RoomItem:
				self.allowed_movement.append('P')
			move = None
			while move not in ['P','R','L','B']:
				print(f'{self.allowed_movement}')
				smove = input('''You found some rope.
What would you like to do?\n''')
				move = smove.upper()
				if move == 'P':
					self.player_inventory.append('rope')
					self.RoomItem.remove('rope')
					self.allowed_movement.remove('P')
					print('You picked up the rope!')
				elif move == 'B':
					direction = move
					self.allowed_movement.remove('R')
					self.allowed_movement.remove('L')
					self.allowed_movement.remove('P')
					self.allowed_movement.remove('B')
					self.allowed_movement.append('F')
					self.allowed_movement.append('R')
					self.location += MOVEMENT[direction]
					print(f'You moved backwards\n{self.location}')
					break
					
				
				else:
					print("Not a valid action")
		if all(self.location == (8,3,0)):
			self.allowed_movement.append('L')
			self.allowed_movement.append('R')
			self.allowed_movement.append('B')
		if all(self.location == (8,4,0)):
			self.allowed_movement.append('R')
			self.allowed_movement.append('F')
		if all(self.location == (8,2,0)):
			self.allowed_movement.append('L')
			self.allowed_movement.append('R')
		if all(self.location == (8,1,0)):
			self.allowed_movement.append('L')
			self.allowed_movement.append('R')
			choice = None
			if choice == 'R':
				print("You left the jungle and now stare at the base of a volcano")
		if all(self.location == (8,0,0)):
			self.allowed_movement.append('L')
			self.allowed_movement.append('R')
			choice = None
			if choice == 'L':
				print("You entered the jungle")
		if all(self.location == (8,-1,0)):
			self.allowed_movement.append('L')
			self.allowed_movement.append('R')
			self.allowed_movement.append('D')
			print("You found the entrance to an old volcano!")
		if all(self.location == (8,-1,-1)):
			self.allowed_movement.append('U')
			self.allowed_movement.append('D')
		if all(self.location == (8,-1,-2)):
			self.allowed_movement.append('U')
			self.allowed_movement.append('D')
			self.allowed_movement.append('L')
		if all(self.location == (8,-1,-3)):
			self.allowed_movement.append('U')
			print('''You can feel the heat coming off of the lava''')
		if all(self.location == (8,-1,-4)):
			actions.dead()
		if all(self.location == (8,-2,0)):
			self.allowed_movement.append('L')
			self.allowed_movement.append('R')
		if all(self.location == (8,-3,0)):
			self.allowed_movement.append('L')
			self.allowed_movement.append('R')
			self.allowed_movement.append('F')
		if all(self.location == (8,-4,0)):
			self.allowed_movement.append('L')
		if all(self.location == (9,-3,0)):
			self.allowed_movement.append('F')
			self.allowed_movement.append('B')
		if all(self.location == (10,-3,0)):
			self.allowed_movement.append('L')
			self.allowed_movement.append('F')
			self.allowed_movement.append('B')
		if all(self.location == (10,-2,0)):
			self.allowed_movement.append('L')
			self.allowed_movement.append('R')
		if all(self.location == (10,-1,0)):
			self.allowed_movement.append('R')
		if all(self.location == (11,-3,0)):
			self.allowed_movement.append('R')
			self.allowed_movement.append('B')
		if all(self.location == (11,-4,0)):
			self.allowed_movement.append('L')
			self.allowed_movement.append('R')
		if all(self.location == (11,-5,0)):
			self.allowed_movement.append('L')
			self.allowed_movement.append('R')
		if all(self.location == (11,-6,0)):
			self.allowed_movement.append('L')
			self.allowed_movement.append('R')
			self.allowed_movement.append('B')
		if all(self.location == (10,-6,0)):
			self.allowed_movement.append('F')
			self.allowed_movement.append('B')
		if all(self.location == (9,-6,0)):
			self.allowed_movement.append('F')
		if all(self.location == (11,-7,0)):
			self.allowed_movement.append('L')
			self.allowed_movement.append('R')
			self.allowed_movement.append('F')
		if all(self.location == (11,-8,0)):
			self.allowed_movement.append('L')
			self.allowed_movement.append('R')
		if all(self.location == (11,-9,0)):
			self.allowed_movement.append('L')
			self.allowed_movement.append('R')
			self.allowed_movement.append('F')
			self.allowed_movement.append('B')
		if all(self.location == (12,-9,0)):
			self.allowed_movement.append('B')
		if all(self.location == (11,-8,0)):
			self.allowed_movement.append('L')
		if all(self.location == (10,-9,0)):
			self.allowed_movement.append('F')
		if all(self.location == (12,-7,0)):
			self.allowed_movement.append('F')
			self.allowed_movement.append('B')
		if all(self.location == (13,-7,0)):
			self.allowed_movement.append('L')
			self.allowed_movement.append('B')
		if all(self.location == (13,-6,0)):
			self.allowed_movement.append('L')
			self.allowed_movement.append('R')
		if all(self.location == (13,-5,0)):
			self.allowed_movement.append('L')
			self.allowed_movement.append('R')
		if all(self.location == (13,-4,0)):
			self.allowed_movement.append('L')
			self.allowed_movement.append('R')
			self.allowed_movement.append('F')
		if all(self.location == (14,-4,0)):
			self.allowed_movement.append('F')
			self.allowed_movement.append('B')
		if all(self.location == (15,-4,0)):
			self.allowed_movement.append('F')
			self.allowed_movement.append('B')
		if all(self.location == (16,-4,0)):
			self.allowed_movement.append('F')
			self.allowed_movement.append('B')
		if all(self.location == (13,-3,0)):
			self.allowed_movement.append('L')
			self.allowed_movement.append('R')
		if all(self.location == (13,-2,0)):
			self.allowed_movement.append('R')
			self.allowed_movement.append('F')
		if all(self.location == (14,-2,0)):
			self.allowed_movement.append('L')
			self.allowed_movement.append('F')
			self.allowed_movement.append('B')
		if all(self.location == (15,-2,0)):
			self.allowed_movement.append('B')





				



			
		

		
		return self.allowed_movement




