import random
import copy

class Game(object):
    def __init__(self, player1, player2):
        self.players = [player1, player2]

    def play(self):
        input("Press Enter to start the game")
        isPlaying = True
        
        while isPlaying:
            input("Press enter to move\n")
            m = Move(self.players)
            m.move()
            isPlaying = self.checkWin()

    def checkWin(self):
        if self.players[0].hp == 0:
            print("\nPlayer win")
            return False
        elif self.players[1].hp == 0:
            print("\nComputer win")
            return False
        else: return True


class Move(object):

    def __init__(self, players):
        self.players = players
        self.actions = ["bigDmg", "lowDmg", "heal"]

    def move(self):
        currPlayer = random.choice(self.players)    #generate move
        if currPlayer == self.players[0]:
            self.generateAction(currPlayer, self.players[1])
        else:
            self.generateAction(currPlayer, self.players[0])

    def generateAction(self, currPlayer, anotherPlayer):
        if currPlayer.name == "Computer" and currPlayer.hp < 35:
            #Increase computer chance of heal (from 33.33% to 50%) if HP less then 35
            currAction = self.increaseHeal(self.actions)
        else:
            currAction = random.choice(self.actions)    #select from low damage, big damage or heal

        action = getattr(self, currAction)
        action(currPlayer, anotherPlayer)


    def bigDmg(self, currPlayer, anotherPlayer):
        val = -random.randrange(10, 35)
        anotherPlayer.hp = val
        self.showAction(currPlayer.name, anotherPlayer.name, "dmg", -val)
        self.playersInfo()

    def lowDmg(self, currPlayer, anotherPlayer):
        val = -random.randrange(18, 25)
        anotherPlayer.hp = val
        self.showAction(currPlayer.name, anotherPlayer.name, "dmg", -val)
        self.playersInfo()

    def heal(self, currPlayer, anotherPlayer):
        val = random.randrange(10, 25)
        currPlayer.hp = val
        self.showAction(currPlayer.name, anotherPlayer.name, "heal", val)
        self.playersInfo()

    def increaseHeal(self, actions):
        incList = copy.deepcopy(actions)
        incList.append("heal")
        return random.choice(incList)

    def showAction(self, p1, p2, action, value):
        if action == "heal":
            print("{} healed for {}%".format(p1, value))
        else:
            print("{} deal {} {}% damage".format(p1, p2, value))

    def playersInfo(self):
        p1, p2 = self.players
        print("{} - {}% ###### {} - {}%".format(p1.name, p1.hp, p2.name, p2.hp))


class Player(object):
    INITIAL_HP = 100

    def __init__(self, name):
        self.__name = name
        self.__hp = Player.INITIAL_HP
        

    @property
    def name(self):
        return self.__name

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, hp):
        self.__hp = self.__hp + hp
        if self.__hp <= 0: self.__hp = 0


player1 = Player("Computer")
player2 = Player("Player")

game = Game(player1, player2)
game.play()