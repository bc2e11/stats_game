import random
from enum import Enum

weather = ["Typhoon", "Hurricane", "Earthquake"]
units = ["Melee", "Ranged", "Cavalry"]

class UnitsDMG(Enum):
    MELEE_DMG = 20 + random.randint(-3, 3)
    RANGED_DMG = 20 + random.randint(-5, 5)
    CAVALRY_DMG = 20 + random.randint(-2, 2)
class WEATHER(Enum):
    TYPHOON = 1
    HURRICANE = 2
    EARTHQUAKE = 3

class Player():
    def __init__(self, name, unitChoice,firstInit):
        self.firstInit = firstInit
        self.name = name
        self.skipWeather = False
        self.health = 100
        self.damage = 0
        self.unitChoice = unitChoice

    
    def weatherEventFunc(self, weatherEventNum, skipWeather):
        self.weatherEvent = weatherEventNum
        self.skipWeather = skipWeather
        
        if(self.name == "ai"):
          self.skipWeather = bool(random.randint(0,1))
    
        if(weatherEventNum == WEATHER.TYPHOON._value_ and self.unitChoice == 3 and self.skipWeather == False
        or weatherEventNum == WEATHER.EARTHQUAKE._value_ and self.unitChoice == 1 and self.skipWeather == False
        or weatherEventNum == WEATHER.HURRICANE._value_ and self.unitChoice == 2 and self.skipWeather == False):
            self.damage -= 5
            print("-5 DMG for", self.name, "due to the weather.")
        if(weatherEventNum == WEATHER.TYPHOON._value_ and self.unitChoice == 2 and self.skipWeather == False
        or weatherEventNum == WEATHER.EARTHQUAKE._value_ and self.unitChoice == 3 and self.skipWeather == False
        or weatherEventNum == WEATHER.HURRICANE._value_ and self.unitChoice == 1 and self.skipWeather == False):
            self.health += 10
            print("+5 HP for", self.name, "due to the weather.")
            
    def initStats(self, player):
        if(  self.unitChoice == 1 and self.firstInit == True):
             self.damage = UnitsDMG.MELEE_DMG._value_
        if(self.unitChoice == 3 and self.firstInit == True):
             self.damage = UnitsDMG.CAVALRY_DMG._value_
        if(self.unitChoice == 2 and self.firstInit == True):
            self.damage = UnitsDMG.RANGED_DMG._value_

    def takeDamage(self, damageTaken):
        self.health -= damageTaken

    def getHP(self):
        healthDashes = 20
        dashConvert = int(100/healthDashes)            
        currentDashes = int((self.health/dashConvert)/2)           
        remainingHealth = healthDashes - (currentDashes*2)      # Get the health remaining to fill as space => 12 spaces

        healthDisplay = ('-' * currentDashes)   + str(self.name) + ("-" * currentDashes)                # Convert 8 to 8 dashes as a string:   "--------"
        remainingDisplay = ' ' * remainingHealth             # Convert 12 to 12 spaces as a string: "            "
        percent = str(int((self.health/100)*100)) + "%"     # Get the percent as a whole number:   40%

        print("|" + healthDisplay + remainingDisplay + "|")  # Print out textbased healthbar
        print(" "*currentDashes + percent)                         # Print the percent
                    
class Game:
    def __init__(self):
        self.gameOver = False
        self.round = 0

    def newRound(self):
        self.round += 1
        print("\n***   Round: %d   ***\n" %(self.round))  

    # Check if either or both Players is below zero health
    def checkWin(self, player, ai):
        if player.health < 1 and ai.health > 0:
            self.gameOver = True # you lose
            f = open("you_lose.txt", "r")
            text = f.readlines()

            for line in text:
                print(line.strip())

            f.close()
        elif ai.health < 1 and player.health > 0:
            self.gameOver = True
            f = open("you_win.txt", "r")
            text = f.readlines()

            for line in text:
                print(line.strip())
            f.close()
        elif player.health < 1 and ai.health < 1:
            self.gameOver = True
            f = open("you_win.txt", "r")
            text = f.readlines()

            for line in text:
                print(line.strip())
            f.close()
    