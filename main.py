from Beginning import Begin
from Rooms import Room1
from Actions import actions
def main():
	yes = Begin()
	yes.start_game()
	yes.player_details()
	yes.welcome()
	print("Here is the game menu.")
	yes.menu()
	act = actions()
	
	done = (17,-4,0)
	while (act.location[0] != done[0]) or (act.location[1] != done[1]) or (act.location[2] != done[2]):
		act.out()
		act.move_player()
		direction = act.direction
		

	


main()


