from Beginning import Begin
from Rooms import Room1
def main():
	yes = Begin()
	yes.start_game()
	yes.player_details()
	yes.welcome()
	print("Here is the game menu.")
	yes.menu()
	y = input("Which way do you want to move?")
	y = y.upper()
	room = Room1()
	room.move_player(y)


main()


