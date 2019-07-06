import sys

gameplan = list(range(1, 10, 1))


class Player(object):

    marker = ""
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker

class Gameplay(object):

	def __init__(self, name1, name2):
		self.player1 = Player(name1, 'X')
		self.player2 = Player(name2, 'O')
		
	def print_gameplan(self):
		global gameplan
		count = 0
		for i in gameplan:
			print(i, end=' ')
			count += 1
			if count == 3:
				print("\n")
				count = 0
	def check_win(self):
		global gameplan
		win_cond = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
		players = [self.player1.marker,self.player2.marker]
		for p in players:
			print(p)
			for i in win_cond:
				count = 0
				for j in i:
					if gameplan[j] == p:
						count += 1
						if count == 3:
							if self.player1.marker==p or self.player2.marker==p:
								print(self.player1.name, "Win The Game !!!")
                                                                sys.exit(0)
class Game(object):
	
	def __init__(self, name1, name2):

		self.player1 = Player(name1, 'X')
		self.player2 = Player(name2, 'O')
		self.game = Gameplay(player1, player2)
		
	def play(self):
		global gameplan
		self.game.print_gameplan()
		turn = 1
		round_check = 0
		while True:
			if turn == 1:
				player = self.player1
				turn += 1
			elif turn == 2:
				player=self.player2
				turn -= 1
			print ("Now it's " + player.name + " turn")
			while True:
				move = int(input("Make your move: "))
				move -= 1
				if move <= 8 and move >= 0:
					if isinstance(gameplan[move], int):
						gameplan[move] = player.marker
						break
			self.game.print_gameplan()
			self.game.check_win()
			round_check += 1
			if round_check == 9:
				print ("It's a draw!")
				sys.exit(0)

if __name__=='__main__':
    player1 = input("Enter Player 1 name :")
    player2 = input("Enter Player 2 name :")
    game = Game(player1, player2)
    game.play()
