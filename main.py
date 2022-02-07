import random
from enum import Enum

leader1 = "leader1"
leader2 = "leader2"
leader3 = "leader3"

leaders = [leader1, leader2, leader3]

class Leader:
    def __init__(self, leader):
        self.leader = leader

    def getUnit(self, leaderName, n):
        units = []

        if leaderName == leader1: units = ["leader1Melee", "leader1Ranged", "leader1Cavalry"]
        if leaderName == leader2: units = ["leader2Melee", "leader2Ranged", "leader2Cavalry"]
        if leaderName == leader3: units = ["leader3Melee", "leader3Ranged", "leader3Cavalry"]
        # Returns list with units available per leader
        return units[n]
    
 
print("1){0}\n2){1}\n3){2}".format(leader1, leader2, leader3))

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




