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


        player.weatherEventFunc(random.randint(1,3),not bool(input("Enter 1 to use weather, or press enter to skip it: ")) )
        ai.weatherEventFunc(random.randint(1,3) ,None)


        if(ai.skipWeather == True):
            print("AI chose to skip the weather")
        else:
            print("AI WEATHER: {} ".format(weather[ai.weatherEvent-1]), )
            
        if(player.skipWeather == True):
            print("You chose to skip the weather")
        else:
            print("PLAYER WEATHER: {} ".format(weather[player.weatherEvent-1]), )

        print()
        f.write("\nRound {} \n[\n\tskip weather: {}\n".format(game.round, player.skipWeather))
        f.write("\tW: {}\n".format(weather))


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

        if(player.unitChoice == 1 and ai.unitChoice == 3 and player.skipWeather == True or 
        player.unitChoice == 2 and ai.unitChoice == 1 and player.skipWeather == True or
        player.unitChoice == 3 and ai.unitChoice == 2 and player.skipWeather == True):
            player.damage += random.randint(1,5)
            print("Since the ai picked {0} and you skipped weather, you beat their unit and your damage is now {1}".format(units[player.unitChoice-1], player.damage))
        
        if(player.unitChoice == 3 and ai.unitChoice == 1 and ai.skipWeather == True or 
        player.unitChoice == 1 and ai.unitChoice == 2 and ai.skipWeather == True or
        player.unitChoice == 2 and ai.unitChoice == 3 and ai.skipWeather == True):
            ai.damage += random.randint(1,5)
            print("Since the ai picked {0} and skipped weather, they beat your unit and their damage is now {1}".format(units[ai.unitChoice-1], ai.damage))
        
        f.write("\tcrit{0}: {1}\n".format(name.upper(), player.crit))
        f.write("\tcritA: {}\n".format(ai.crit))

        
        player.takeDamage(ai.damage, player, ai)
        ai.takeDamage(player.damage, player, ai)

        print(player.name, "attacked {0} for {1} dmg".format(ai.name, player.damage))
        print(ai.name, "attacked {0} for {1} dmg".format(player.name, ai.damage))
        
        f.write("\t{0} took {1} dmg\n".format(ai.name, player.damage))
        f.write("\t{0} took {1} dmg\n".format(player.name, ai.damage))

        if(ai.dAffected == 0):
            ai.damage += 5
        if(player.dAffected == 0):
            player.damage += 5

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
