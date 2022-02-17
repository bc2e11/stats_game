# Player 1 picks a unit
# Player 2 (ai) picks a unit (that is not tbe same as Player 1)

# All units are based around melee, ranged, cavalry

# Player 1 and 2 pick one type of unit. Everyone has a base damage of 20 but depending on the unit, the damage they deal will range by a random number. 
# Melee DMG: 20 + [-1, 1]
# Ranged DMG: 20 + [-3, 3]
# Cavalry DMG: 20 + [-2, 2]

# Meaning:
# Your unit’s base damage is defined by 20 plus or minus a random integer defined above. 
# Therefore: 
# Melee damage range: 19-21 dmg
# Ranged damage range: 17-23 dmg
# Cavalry damage range: 18-22 dmg

# Each turn there is a 1 in 6 chance that either players deal a critical hit

# Player 1 will choose a weather event that will affect both participants in the following ways based on their unit choice: 

# Typhoon will      disadvantage cavalry (-5 dmg),  advantage ranged  (+5 hp)
# Hurricane will    disadvantage ranged  (-5 dmg),   advantage melee   (+5 hp)
# Earthquake will   disadvantage melee   (-5 dmg),    advantage cavalry (+5 hp)

# If player 1 or ai (50% chance of skipping) chooses to skip the weather:
# A random advantage will be generated to the skipping player based on the following:
# Melee beats cavalry 
# Ranged beats melee
# Cavalry beats ranged  

# This means if you skip the weather and have a melee unit and the ai has cavalry, you will gain a random amount of damage from 1-5

# **The goal of the game is reduce the other player’s health points (hp) to zero.**
