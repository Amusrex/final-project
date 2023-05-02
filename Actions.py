import json
import pickle
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
		self.actions = ['Q','S','L','R','M','I','O']
		self.direction = ""
	def save_game(self, filename):
		with open(filename, 'wb') as f:
			pickle.dump(self, f)
		print("Game saved.")


	def load_game(self, filename):
		with open(filename, 'rb') as f:
			loaded_actions = pickle.load(f)
		self.location = loaded_actions.location
		self.direction = loaded_actions.direction
		print("Game loaded.")
	def move_player(self):
		
		print(f"{self.actions}")
		print(f"Allowed movements\n{self.allowed_movement}")
		
		sdirection = input("What would you like to do?\n")
		direction = sdirection.upper()
		if direction == 'Q':
			print('Goodbye')
			quit()
		elif direction == 'S':
			actions.save_game()
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
		elif direction == 'Q':
			syes = input("Do you want to restart? (y/n)\n")
			yes = syes.lower()
			if yes == 'y':
				self.allowed_movement.append('L')
				self.allowed_movement.append('R')
				self.allowed_movement.append('F')
				self.RoomItem = ['map','note','riddle','protective amulet','flash light','torch',
		'grapple hook','machete','wood1','wood2','wood3','key','treasure','rope','nails',
		'sheets','diary','']
				self.animals = ['tree monster','bear','lion','giant spider']
				self.player_inventory = []
				self.location = array([0,0,0])
			if yes == 'no':
				pass
		elif direction == 's' or direction == 'S':
			save_input = input("Do you want to save the game? (y/n): \n")
			if save_input.lower() == 'y':
				filename = input("Enter a filename to save the game: \n")
				self.save_game(filename)
			elif save_input.lower() == 'n':
				pass
			else:
				print("Not a valid input")
		elif direction == 'a' or direction == 'A':
			load_input = input("Do you want to load a saved game? (y/n): ")
			if load_input.lower() == 'y':
				filename = input("Enter the filename of the saved game: ")
				self.load_game(filename)
			elif load_input.lower() == 'n':
				pass
			else:
				print("Not a valid input")
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
                   _ _ _ _|_|_|_|_
               _ _|_|_|_|_|_|_|_|_|
     _ 	      |_|_|_|   |_|   |_|
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
			elif ask == 'diary':
				if 'diary' in self.player_inventory:
					print('''It's been weeks since I arrived on this island, and I still can't believe what I've found.
 I stumbled upon this old cottage in the woods today, and inside, I found this diary. It's amazing to think that someone else was here before me, living and exploring just like I am now.
As I read through the entries, I felt a sense of kinship with the author. 
They, too, were awed by the natural beauty of the island and the mystery that shrouded it. 
They wrote about the same jungle creatures that I've encountered, and the same sense of excitement that comes with discovering something new.
But there was something else in these pages too. 
he author wrote about a darkness that lay beneath the surface of the island, a sense of foreboding that they couldn't quite shake. 
They wrote about feeling watched, about strange noises in the night, about a growing sense of unease.
I can't help but wonder what happened to the author of this diary. Did they make it off the island alive, or did they fall victim to some unknown danger? 
And will I be able to avoid the same fate?
For now, I'll continue to explore, but I'll do so with a greater sense of caution. 
I don't want to end up like the author of this diary.

Until next time,''')
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
		self.direction = direction
		return direction
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
	def vault(self):
		if 'treasure' in self.RoomItem:
			print("You found an ancient vault! there looks to be a key hole on the door.")
			print("[B],[key]")
			move = input("What do you want to do?\n")

			while move not in ['key','b','B']:
				print("Not a valid input")
				move = input("What do you want to do?\n")
			if 'key' in self.player_inventory:
				if move == 'key':
					self.player_inventory.remove('key')
					yes = input('''You opened the vault! You look inside the vault and see old pirate gold.
just as you take a step forward the skeleton of the pirate captian steps in front of you.
If you answer this riddle correctly you can have all his gold, if not he will kill you with his sword.
What has a head and a tail but no body?\n''')
					while yes not in ['coin','Coin']:
						response = input("Wrong answer. Would you like a hint?\n")
						if response == 'yes':
							print("Money")
							yes = input("What is the answer to the riddle?\n")
						elif response == 'no':
							yes = input("What is the answer to the riddle?\n")
						else:
							print("Not a valid input")
					if yes in ['coin','Coin']:
						self.allowed_movement.append('P')
						self.allowed_movement.append('B')
						print('You guessed correctly!')
						smoney = input('''You can have all the treasure.
If you choose to not pick up the treasure now the pirate will close the vault and you will never be able to grab the treasure again.
What would you like to do?\n''')
						money = smoney.upper()
						if money == 'P':
							print("You picked up the treasure!")
							self.allowed_movement.remove('P')
							self.player_inventory.append('treasure')
							self.RoomItem.remove('treasure')
							
						elif money == 'B':
							smove = move.upper()
							direction = smoveprint
							self.allowed_movement.append('F')
							self.allowed_movement.append('R')
							self.allowed_movement.remove('B')
							self.location += MOVEMENT[direction]
							print(f'You moved backwards\n{self.location}')
						else:
							print("Wrong answer")
							print("The vault has been sealed with the treasure inside it forever.")
							self.location = array([8,0,-2])
				
			
				elif move in ['b',"B"]:
					self.allowed_movement.append('F')
					self.allowed_movement.append('R')
					
					smove = move.upper()
					direction = smove
					self.location += MOVEMENT[direction]
					print(f'You moved backwards\n{self.location}')
			elif move in ['b','B']:
				self.allowed_movement.append('F')
				self.allowed_movement.append('R')
				self.allowed_movement.remove('B')
				smove = move.upper()
				direction = smove
				self.location += MOVEMENT[direction]
				print(f'You moved backwards\n{self.location}')
			else:
				print("You don't have the key to the vault")	
					
		else:
			self.allowed_movement.append('B')
						

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
						
						
						self.allowed_movement.remove('P')
						self.allowed_movement.remove('B')
						self.allowed_movement.append('L')
						self.allowed_movement.append('F')
						self.location += MOVEMENT[direction]
						print(f'You moved backwards\n{self.location}')
						break
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
					
					self.allowed_movement.remove('R')
					self.allowed_movement.remove('P')
					
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
			while move not in ['P','B']:
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
					
					self.allowed_movement.remove('P')
					self.allowed_movement.remove('B')
					
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
		if all(self.location == (8,0,-2)):
			self.allowed_movement.append('F')
			self.allowed_movement.append('R')
		if all(self.location == (9,0,-2)):
			
			actions.vault(self)
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
			self.allowed_movement.append('D')
			print("You stumbled across a cave opening!")
		if all(self.location == (8,-4,-1)):
			self.allowed_movement.append('U')
			self.allowed_movement.append('D')
		if all(self.location == (8,-4,-2)):
			self.allowed_movement.append('U')
			self.allowed_movement.append('D')
		if all(self.location == (8,-4,-3)):
			self.allowed_movement.append('F')
			self.allowed_movement.append('B')
			self.allowed_movement.append('U')
			self.allowed_movement.append('D')
		if all(self.location == (8,-4,-4)):
			self.allowed_movement.append('U')
			if 'giant spider' in self.animals:
				move = input("Oh no!\n A giant spider. (fight/run)\n")
				
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
								self.allowed_movement.remove('U')
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

						print('You killed the giant spider. Good job!')
						self.animals.remove('giant spider')
					elif item == 'flash light':
						if 'flash light' in self.player_inventory:
							print('You used the flash light and lived!')
							self.player_inventory.remove('flash light')
							self.animals.remove('giant spider')
						else:
							print("You don't have that item. You died")
							
							option = input("Do you want to play again? (yes/no)\n")
							if option == 'yes':
								self.allowed_movement.remove('U')
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
					else:
						print('Not a valid input. You died')
						option = input("Do you want to play again? (yes/no)\n")
						if option == 'yes':
							self.allowed_movement.remove('U')
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

				elif move not in ('run','fight'):
					print("wrong input. You died")
					option = input("Do you want to play again? (yes/no)\n")
					
					while option not in ['yes','no']:
						print("Not a valid action")
						option = input("Do you want to play again? (yes/no)\n")
					if option == 'yes':
						self.allowed_movement.remove('U')
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
		if all(self.location == (9,-4,-3)):
			self.allowed_movement.append('F')
			self.allowed_movement.append('B')
		if all(self.location == (10,-4,-3)):
			self.allowed_movement.append('B')
			if 'key' in self.RoomItem:
				self.allowed_movement.append('P')
			move = None
			while move not in ['P','B']:
				print(f'{self.allowed_movement}')
				smove = input('''You found a key.
What would you like to do?\n''')
				move = smove.upper()
				if move == 'P':
					self.player_inventory.append('key')
					self.RoomItem.remove('key')
					self.allowed_movement.remove('P')
					print('You picked up the key!')
				elif move == 'B':
					direction = move
					
					self.allowed_movement.remove('P')
					self.allowed_movement.remove('B')
					self.allowed_movement.append('F')
					self.allowed_movement.append('B')
					self.location += MOVEMENT[direction]
					print(f'You moved backwards\n{self.location}')
					break
					
				
				else:
					print("Not a valid action")
		if all(self.location == (7,-4,-3)):
			self.allowed_movement.append('F')
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
			if 'nails' in self.RoomItem:
				self.allowed_movement.append('P')
			move = None
			while move not in ['P','B']:
				print(f'{self.allowed_movement}')
				smove = input('''You found some old nails.
What would you like to do?\n''')
				move = smove.upper()
				if move == 'P':
					self.player_inventory.append('nails')
					self.RoomItem.remove('nails')
					self.allowed_movement.remove('P')
					print('You picked up the nails!')
				elif move == 'B':
					direction = move
					
					self.allowed_movement.remove('P')
					self.allowed_movement.remove('B')
					self.allowed_movement.append('L')
					self.allowed_movement.append('R')
					self.allowed_movement.append('F')
					self.allowed_movement.append('B')
					self.location += MOVEMENT[direction]
					print(f'You moved backwards\n{self.location}')
					break
					
				
				else:
					print("Not a valid action")
		if all(self.location == (11,-10,0)):
			self.allowed_movement.append('L')
		if all(self.location == (10,-9,0)):
			self.allowed_movement.append('F')
			if 'wood2' in self.RoomItem:
				self.allowed_movement.append('P')
			move = None
			while move not in ['P','B']:
				print(f'{self.allowed_movement}')
				smove = input('''You found some wood.
What would you like to do?\n''')
				move = smove.upper()
				if move == 'P':
					self.player_inventory.append('wood2')
					self.RoomItem.remove('wood2')
					self.allowed_movement.remove('P')
					print('You picked up the wood!')
				elif move == 'F':
					direction = move
					
					self.allowed_movement.remove('P')
					self.allowed_movement.remove('F')
					self.allowed_movement.append('L')
					self.allowed_movement.append('R')
					self.allowed_movement.append('F')
					self.allowed_movement.append('B')
					
					self.location += MOVEMENT[direction]
					print(f'You moved forwards\n{self.location}')
					break
					
				
				else:
					print("Not a valid action")
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
			
			self.allowed_movement.append('B')
			if all(player_inventory == ['wood1','wood2','wood3','rope','nails','sheets']):
				choice =  input('''You found an old sail boat! What would you like to do?
repair/explore\n''')
				while choice not in ['repair','explore']:
					print("Not a valid input.")
					choice = input("What would you like to do?\n")

				if choice == 'repair':
					print("You repaired the sail boat! You sailed away from the island.")
					direction = 'F'
					self.location += MOVEMENT[direction]
				if choice == 'explore':
					direction = 'B'
					self.location += MOVEMENT[direction]
					print(f'You moved backwards\n{self.location}')
			else:
				print('''You found an old sail boat but don't have all the items to repair it.
 Keep exploring''')


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
		if all(self.location == (14,-1,0)):
			self.allowed_movement.append('L')
			self.allowed_movement.append('R')
		if all(self.location == (14,0,0)):
			self.allowed_movement.append('L')
			self.allowed_movement.append('R')
			self.allowed_movement.append('F')
		if all (self.location == (15,0,0)):
			self.allowed_movement.append('B')
			if 'diary' in self.RoomItem:
				self.allowed_movement.append('P')
			move = None
			while move not in ['P','B']:
				print(f'{self.allowed_movement}')
				smove = input('''You found a diary.
What would you like to do?\n''')
				move = smove.upper()
				if move == 'P':
					self.player_inventory.append('diary')
					self.RoomItem.remove('diary')
					self.allowed_movement.remove('P')
					print('You picked up the diary!')
				elif move == 'B':
					direction = move
					
					self.allowed_movement.remove('P')
					self.allowed_movement.remove('B')
					self.allowed_movement.append('L')
					self.allowed_movement.append('R')
					self.allowed_movement.append('F')
					self.location += MOVEMENT[direction]
					print(f'You moved backwards\n{self.location}')
					break
					
				
				else:
					print("Not a valid action")
		if all(self.location == (14,1,0)):
			self.allowed_movement.append('L')
			self.allowed_movement.append('R')
			self.allowed_movement.append('B')
		if all(self.location == (13,1,0)):
			self.allowed_movement.append('F')
		if all(self.location == (14,2,0)):
			self.allowed_movement.append('L')
			self.allowed_movement.append('R')
			self.allowed_movement.append('F')
		if all(self.location == (15,2,0)):
			self.allowed_movement.append('B')
			if 'wood3' in self.RoomItem:
				self.allowed_movement.append('P')
			move = None
			while move not in ['P','B']:
				print(f'{self.allowed_movement}')
				smove = input('''You found some wood.
What would you like to do?\n''')
				move = smove.upper()
				if move == 'P':
					self.player_inventory.append('wood3')
					self.RoomItem.remove('wood3')
					self.allowed_movement.remove('P')
					print('You picked up the wood!')
				elif move == 'B':
					direction = move
					
					self.allowed_movement.remove('P')
					self.allowed_movement.remove('B')
					self.allowed_movement.append('L')
					self.allowed_movement.append('R')
					self.allowed_movement.append('F')
					
					self.location += MOVEMENT[direction]
					print(f'You moved backwards\n{self.location}')
					break
					
				
				else:
					print("Not a valid action")
		if all(self.location == (14,3,0)):
			self.allowed_movement.append('R')
			self.allowed_movement.append('B')
		if all(self.location == (13,3,0)):
			self.allowed_movement.append('F')
			if 'rope' in self.RoomItem:
				self.allowed_movement.append('P')
			move = None
			while move not in ['P','F']:
				print(f'{self.allowed_movement}')
				smove = input('''You found some sheets.
What would you like to do?\n''')
				move = smove.upper()
				if move == 'P':
					self.player_inventory.append('sheets')
					self.RoomItem.remove('sheets')
					self.allowed_movement.remove('P')
					print('You picked up the sheets!')
				elif move == 'F':
					direction = move
					
					self.allowed_movement.remove('P')
					self.allowed_movement.remove('F')
					self.allowed_movement.append('R')
					self.allowed_movement.append('F')
					
					self.location += MOVEMENT[direction]
					print(f'You moved forwards\n{self.location}')
					break
					
				
				else:
					print("Not a valid action")





				



			
		

		
		return self.allowed_movement




