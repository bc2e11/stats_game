import Game
import engine
import random

times = int(input("Number of simulations: "))

unitOptions = ["Melee", "Ranged", "Cavalry"]

weatherOptions = ["without", "with"]


print(["{0}) ".format(i+1) + unitOptions[i] + "\n" for i in range(len(unitOptions))])
unitSim = int(input())

weatherSim = input("Weather (0/1)? ")
skip = bool(int(weatherSim))
wins = 0 

for i in range(times):
    print("Sim {}".format(i+1))

    gameEngine = engine.Game()

    player = engine.Player("player", unitSim, True, not skip)

    unitA = random.randint(1, 3)
    while(unitA == unitSim):
        unitA = random.randint(1, 3)
    
    ai = engine.Player("ai", unitA, True, bool(random.randint(0,1)))

    player.initStats()
    ai.initStats()
    Game.game(unitSim, skip, player, ai, gameEngine)
    if(player.won == True):
        wins += 1

print()


print("The player won {0} of {1} by using {2}".format(wins, times, unitOptions[unitSim-1]))
print("The player played {0} the weather".format(weatherOptions[int(weatherSim)]))