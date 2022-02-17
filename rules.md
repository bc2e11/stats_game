# Player 1 picks a unit
# Player 2 (ai) picks a unit (that is not tbe same as Player 1)

# All units are based around melee, ranged, cavalry

# Player 1 will choose a weather event that will affect both participants in the following ways based on their unit choice: 

# Player 1 and 2 pick one type of unit. Everyone has a base damage of 20 but depending on the unit, the damage they deal will range by a random number. 
# Melee DMG: 20 + [-1, 1]
# Ranged DMG: 20 + [-3, 3]
# Cavalry DMG: 20 + [-2, 2]

# Typhoon will disadvtange cavalry (-5 dmg), advantage ranged   (+5 hp)
# Hurricane will disadvantage ranged (-5 dmg), advtange melee   (+5 hp)
# Earthquake will disadvantage melee (-5 dmg), advrange cavalry (+5 hp)

# The information above means that at the beginning of a game, 
# your unit’s base damage is defined by 20 plus or minus a random integer defined above. 
# Therefore: 
# Melee damage range: 19-21 dmg
# Ranged damage range: 17-23 dmg
# Cavalry damage range: 18-22

# **The goal of the game is reduce the other player’s health points (hp) to zero.**
