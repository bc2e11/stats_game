import random
from enum import Enum
leaders = ["leader1", "leader2", "leader3"]

class Leader(Enum):
    ONE =   "leader1"
    TWO =   "leader2"
    THREE = "leader3"
    def __init__(self, leader):
        self.leader = leader

    def getUnit(self, leaderName, n):
        units = []

        if leaderName == Leader.ONE: units = ["leader1Melee", "leader1Ranged", "leader1Cavalry"]
        if leaderName == Leader.TWO: units = ["leader2Melee", "leader2Ranged", "leader2Cavalry"]
        if leaderName == Leader.THREE: units = ["leader3Melee", "leader3Ranged", "leader3Cavalry"]
        # Returns list with units available per leader
        self.units = units
        return units[n]

class Units(Enum):
    MELEE = 30 
    RANGED = 25
    CAVALRY = 40
 
for i in range(3):
    print(str(i+1)+")", "{0}".format(leaders[i]))

leaderNumber = int(input("Which leader would you like to choose? "))
Player = Leader(leaders[leaderNumber-1])

print("You are the great", Player.leader)


cpuLeader = random.randint(1,3)

while(leaderNumber == cpuLeader):
    cpuLeader = random.randint(1,3)

Computer = Leader(leaders[cpuLeader-1])

# print(Computer.leader, Player.leader)

computerUnitChoice = random.randint(0,2)
computerUnit = Computer.getUnit(Computer.leader, int(computerUnitChoice))

print("The units available for your leader are:\n" )

for i in range(3): print(str(i+1)+")", "{0}".format(Player.getUnit(Player.leader, i)))

weatherDecision = random.randint(1,3)


