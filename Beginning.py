class Begin():
	def __init__(self):
		self.play_game = False
		self.name = ''
	def start_game(self):
		self.play_game = input("Would you like to play my game? (yes/no) \n")
		if self.play_game == 'yes':
			print('Welcome to The Lost Island')
		elif self.play_game == 'no':
			print("Ok, maybe next time.")
			quit()
		else:
			print("Invalid input. Please type 'yes' or 'no'.")
			self.start_game()
	def player_details(self):
		self.player_name = input("Before we begin explorer. What is your name?\n")
		print(f"Welcome {self.player_name}, your adventure awaits!")
		return self.player_name
	def welcome(self):
		print('''You are a world-famous explorer on a flight across the Pacific Ocean when your plane suddenly experiences a malfunction. \nThe last thing you remember is blacking out during the crash. 
You wake up on the beach of an island. You have no idea how you got there or where anyone else is.
You will need to explore the island to find the necesaryy materials to escape. Be careful, who knows what kinds of things are on the island.''')
	def menu(self):
		print('''	Game menu
Q - quit game
S - save game
M - menu
U - up
D - down
L - left
R - right
F - forward
B - backward
O - use item
P - pick up item
I - inventory\n''')
		print("\nBegin exploring!")
