import argparse, random

class Tally:
	switch = [0,0]
	stay = [0,0]
	totalGames = 0
	
	switch_winning_percentage = 0
	stay_winning_percentage = 0
	
	def calculateWinPercentage(self):
		if self.switch[0] > 0:
			self.switch_winning_percentage = (float(self.switch[0])/float(self.switch[0] + self.switch[1])) * 100
		if self.stay[0] > 0:
			self.stay_winning_percentage = (float(self.stay[0])/float(self.stay[0] + self.stay[1])) * 100

class Game:

	num_doors = 0
	door_list = []
	winning_door = 0
	user_door = 0
	
	def setUserDoor(self, door):
		# pick a random door
		if door == -1:
			self.user_door = random.choice(self.door_list)
		# use user choice
		else:
			self.user_door = door
	
	def winningDoor(self):
		self.winning_door = random.choice(self.door_list)
		
	def createDoorList(self):
		self.door_list = list(range(self.num_doors))
		
	def revealDoor(self):
		while len(self.door_list) > 2:
			# Randomly open a door then remove it
			open_door = random.choice(self.door_list)
			
			# Well, don't remove it if it is the winning door or the user choice
			if open_door == self.winning_door or open_door == self.user_door:
				continue
			else:
				self.door_list.remove(open_door)
		
		# Make sure we didn't remove too many
		try:
			assert len(self.door_list) == 2
		except AssertionError:
			print "Oops, we revealed too many doors. Fix your code, dummy."
			exit(1)
			
	def switchUserDoor(self):
		# We should switch the choice of the user automatically
		choice_list = list(self.door_list)
		choice_list.remove(self.user_door)
		self.user_door = choice_list.pop()
	
	def __init__(self,num_doors):
		# Set up the game parameters
		self.num_doors = num_doors
		self.createDoorList()
		self.winningDoor()
		
		
	def checkWin(self):
		if self.user_door == self.winning_door:
			return True
		else:
			return False
			
def simulate(doors, trials, verbose):

	print "Starting Monty Hall simulation with %d doors for %d trials." % (doors, trials)
	
	#initiate tally
	tally = Tally()
	
	# Run trials with switch option
	while tally.totalGames < trials:
		tally.totalGames = tally.totalGames + 1
		if verbose:
			print "Starting game %d with switching strategy." % tally.totalGames
		
		# Instantiate the game, set a user picked door
		game = Game(doors)
		game.setUserDoor(-1)
		
		if verbose:
			print "Winning door is %d" % game.winning_door
			print "User picked door %d." % game.user_door
		
		# ReveaL the doors and switch
		game.revealDoor()
		game.switchUserDoor()
		
		if verbose:
			print "The following doors remain after reveal: %d and %d" % (game.door_list[0],game.door_list[1])
			print "User has switched to door %d" % game.user_door
		
		# Check win
		if game.checkWin():
			if verbose:
				print "User picked door %d has won. (Winning door %d)" % (game.user_door, game.winning_door)
				print "Adding this one to the switch strategy win tally"
			tally.switch[0] = tally.switch[0] + 1
		else:
			if verbose:
				print "User picked door %d has lost. (Winning door %d)" % (game.user_door, game.winning_door)
				print "Adding this one to the switch strategy lose tally"
			tally.switch[1] = tally.switch[1] + 1
	
	# Run trials with stay option
	while tally.totalGames < 2*trials:
		tally.totalGames = tally.totalGames + 1
		if verbose:
			print "Starting game %d with stay strategy." % tally.totalGames
		
		# Instantiate the game, set a user picked door
		game = Game(doors)
		game.setUserDoor(-1)
		
		if verbose:
			print "Winning door is %d" % game.winning_door
			print "User picked door %d." % game.user_door
		
		# ReveaL the doors and switch
		game.revealDoor()
		
		if verbose:
			print "The following doors remain after reveal: %d and %d" % (game.door_list[0],game.door_list[1])
			print "User has stayed at door %d" % game.user_door
		
		# Check win
		if game.checkWin():
			if verbose:
				print "User picked door %d has won. (Winning door %d)" % (game.user_door, game.winning_door)
				print "Adding this one to the stay strategy win tally"
			tally.stay[0] = tally.stay[0] + 1
		else:
			if verbose:
				print "User picked door %d has lost. (Winning door %d)" % (game.user_door, game.winning_door)
				print "Adding this one to the switch strategy lose tally"
			tally.stay[1] = tally.stay[1] + 1
		#calculate percentage again
		tally.calculateWinPercentage()
			
	print "Switch W/L WinPct %d/%d %d." % (tally.switch[0],tally.switch[1],tally.switch_winning_percentage)
	print "Stay W/L WinPCT %d/%d %d." % (tally.stay[0],tally.stay[1],tally.stay_winning_percentage)
		
def manual(doors):

	# Instantiate the game
	game = Game(doors)

	# General Intro
	print "Welcome to the Monty Hall Simulator!"
	print "You have chosen to play with %d doors." % doors
	print "%d doors contain goats, while one contains a car." % (doors - 1)
	print "After your first pick, all doors aside from your choice and one other will be revealed."
	print "Should you chose to do so, you may switch doors."
	print "You may choose from doors 0 - %d, or enter -1 for a random door." % (doors - 1)

	# Grab the choice and start the game
	choice = -1
	while True:
		choice = input("Please enter your choice:")
		if (choice >= 0 and choice < doors) or choice == -1:
			break
		print "You have entered an invalid choice."

	if choice == -1:
		game.setUserDoor(choice)
	
	print "You have chosen door number %d" % game.user_door
	
	# Now reveal all of the other doors
	print "Now we are revealing the doors."
	game.revealDoor()
	print "The following doors are remaining: %d and %d" % (game.door_list[0],game.door_list[1])
	while True:
		switch = raw_input("Would you like to switch doors? (y/n):")
		if switch == 'y' or switch == 'n':
			break
		print "Please enter a valid input: y or n"
	
	if switch == 'y':
		game.switchUserDoor()
		print "You have now chosen door %d" % game.user_door
	else:
		print "You are staying with door %d" % game.user_door

	# Time to see if we win
	if game.checkWin():
		print "Congrats, you picked %d and it was %d!" % (game.user_door, game.winning_door)
	else:
		print "Sorry, you picked %d and it was %d. :(" % (game.user_door, game.winning_door)
		
		
def main():
	
	# Parse the arguments
	parser = argparse.ArgumentParser(description="A program to simulate the counter-intuitive statistics of the Monty-Hall problem.")
	parser.add_argument('-d','--doors',default=3,type=int,metavar='int',help='Designate the number of doors.')
	parser.add_argument('-t','--trials',default=10000,type=int,metavar='int',help='Designate the number of trials to run.')
	parser.add_argument('-v','--verbose',default=False,action='store_true',help='Display the details of each trial.')
	parser.add_argument('-p','--play',default=False,action='store_true',help='Play the game manually. Only one trial will be run.')
	args = parser.parse_args()
	
	# Run the game manually.
	if args.play:
		manual(args.doors)
	# Run a simulation
	else:
		simulate(args.doors,args.trials,args.verbose)
	
if __name__ == '__main__':
	main()