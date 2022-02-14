import engine
import random


weather = ["Typhoon", "Hurricane", "Earthquake"]
units = ["Melee", "Ranged", "Cavalry"]

for i in range(3):print(str(i+1)+")", "{0}".format(units[i]))

unitChoiceP = int(input())

unitChoiceA = random.randint(1, 3)
while(unitChoiceA == unitChoiceP):
    unitChoiceA = random.randint(1, 3)

game = engine.Game()

player = engine.Player("player", unitChoiceP, True)
ai = engine.Player("ai", unitChoiceA, True)

player.initStats(player)
ai.initStats(ai)

print("You picked", units[player.unitChoice-1],"\nHP: {0}".format(player.health), "\nDMG: {0}".format(player.damage))
print()
print("ai picked", units[ai.unitChoice-1],"\nHP: {0}".format(ai.health), "\nDMG: {0}".format(ai.damage))

print()

player.getHP()
print()
ai.getHP()
print()

while not game.gameOver:
    game.newRound()

    player.weatherEventFunc(random.randint(1,3),not bool(input("Enter 1 to use weather, or press enter to skip it: ")) )
    ai.weatherEventFunc(random.randint(1,3), not bool(random.randint(1,2)))

    if(player.skipWeather == False):
        print(player.name, "incurred the effects of a", weather[player.weatherEvent-1])
    else:
        print()
        print(player.name, "chose to skip the weather")
    if(ai.skipWeather == False):
        print(ai.name, "incurred the effects of a", weather[player.weatherEvent-1])
    else:
        print("The ai chose to skip the weather")


    crit = random.randint(1,5)
    playerN = random.randint(1,2)
    if(crit == 1 and playerN == 1):
        print(player.name, "dealt a Critcal hit!")
        player.damage += 5 
    else:
        player.damage += 0
    if(crit == 1 and playerN == 2):
        print(ai.name, "dealt a Critcal hit!")
        ai.damage += 5 
    else:
        ai.damage += 0


    player.takeDamage(ai.damage)
    print(player.name, "attacked {0} for {1} dmg".format(ai.name, player.damage))
    ai.takeDamage(player.damage)
    print(ai.name, "attacked {0} for {1} dmg".format(player.name, ai.damage))
    
    print()

    print("===   END TURN   ===")
    player.getHP()
    print()
    ai.getHP()
    print()
    game.checkWin(player, ai)
