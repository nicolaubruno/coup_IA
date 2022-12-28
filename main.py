
from models.card import Card
from models.player import Player
from models.game import Game 

p1 = Player("jogador 1")
p2 = Player("jogador 2")
p3 = Player("jogador 3")

players = [p1, p2, p3]

game = Game(players, ambassador = False)

game.start()

print()
print("Cartas no deck: {}".format( game.cards ))
for i in range( len(players) ):
    print("Cartas de {} ({}): {} e {}".format(
        game.players[i].name,
        game.players[i].religion,
        game.players[i].card1,
        game.players[i].card2
    ))


