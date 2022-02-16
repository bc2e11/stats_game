import engine
import random

name = input("What is your name? ")
playTestResults = "play_test_result_" + name

f = open(playTestResults+".txt", "w")
f.write("Tester name: {}\n".format(name))

def main():
    weather = ["Typhoon", "Hurricane", "Earthquake"]
    units = ["Melee", "Ranged", "Cavalry"]

    for i in range(3):print(str(i+1)+")", "{0}".format(units[i]))

    unitChoiceP = int(input())
    
    
    unitChoiceA = random.randint(1, 3)
    while(unitChoiceA == unitChoiceP):
        unitChoiceA = random.randint(1, 3)

    game = engine.Game()

    player = engine.Player(name, unitChoiceP, True)
    ai = engine.Player("ai", unitChoiceA, True)

    f.write("Unit choice {}\n".format(player.unitChoice))
    f.write("Unit choice: {}, {}\n".format(player.unitChoice, units[player.unitChoice-1]))
    f.write("AI Unit choice: {}, {}\n".format(ai.unitChoice, units[ai.unitChoice-1]))


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

    f.write("{0}'s hp: {1}\n".format(name, player.health))
    f.write("{0}'s dmg: {1}\n".format(name, player.damage))

    f.write("{0}'s hp: {1}\n".format("ai", ai.health))
    f.write("{0}'s dmg: {1}\n".format("ai", ai.damage))

    while not game.gameOver:
        game.newRound()

        weatherP = player.weatherEventFunc(random.randint(1,3),not bool(input("Enter 1 to use weather, or press enter to skip it: ")) )
        weatherA = ai.weatherEventFunc(random.randint(1,3), not bool(random.randint(1,2)))
        
        

        f.write("\nRound {} \n[\n\tplayerSW: {}\n".format(game.round, player.skipWeather))
        f.write("\tAISW: {}\n".format(game.round, ai.skipWeather))
        f.write("\t{0}W: {1}\n".format(player.name, weatherP))
        f.write("\tAIW: {}\n".format(weatherA))


        if(player.skipWeather == False):
            print(player.name, "incurred the effects of a", weather[player.weatherEvent-1])
        else:
            print()
            print(player.name, "chose to skip the weather")
        if(ai.skipWeather == False):
            print(ai.name, "incurred the effects of a", weather[player.weatherEvent-1])
        else:
            print("The ai chose to skip the weather")

        crit = random.randint(1,6)
        playerN = random.randint(1,2)
        if(crit == 1 and playerN == 1):
            print(player.name, "dealt a Critcal hit!")
            player.damage += 5 
            player.crit = True
        else:
            player.damage += 0
        if(crit == 1 and playerN == 2):
            print(ai.name, "dealt a Critcal hit!")
            ai.damage += 5 
            ai.crit = True
        else:
            ai.damage += 0


        f.write("\tcrit{0}: {1}\n".format(player.name.upper, str(player.crit)))
        f.write("\tcritA: {}\n".format(str(player.crit)))

        player.takeDamage(ai.damage)
        f.write("\t{} took {} dmg\n".format(player.name, ai.damage))
        print(player.name, "attacked {0} for {1} dmg".format(ai.name, player.damage))
        ai.takeDamage(player.damage)

        f.write("\t{} took {} dmg\n".format(ai.name, player.damage))
        print(ai.name, "attacked {0} for {1} dmg".format(player.name, ai.damage))

        print()

        f.write("\tEnd HP:{}\n".format(player.health)) 
        f.write("\tAI End HP:{}\n".format(ai.health)) 

        f.write("\n]\n")

        print("===   END TURN   ===")
        player.getHP()
        print()
        ai.getHP()
        print()
        game.checkWin(player, ai)
    f.write("\n {0} won: {1}".format(player.name, player.won))
    f.write("\n {0} won: {1}".format(ai.name, ai.won))

main()

f.close()
