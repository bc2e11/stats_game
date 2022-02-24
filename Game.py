import engine
import random
def game(unit, skip, player, ai, gameEngine):
    # simulation -> T/F
    # unit -> 1-3
    # weather -> T/F (skipping)
    while not gameEngine.gameOver:
        gameEngine.newRound()
        
        player.weatherEventFunc(random.randint(1,3), skip)
        ai.weatherEventFunc(random.randint(1,3) ,None)

        if(player.unitChoice == 1 and ai.unitChoice == 3 and player.skipWeather == True or 
        player.unitChoice == 2 and ai.unitChoice == 1 and player.skipWeather == True or
        player.unitChoice == 3 and ai.unitChoice == 2 and player.skipWeather == True):
            player.damage += random.randint(1,5)
        
        if(player.unitChoice == 3 and ai.unitChoice == 1 and ai.skipWeather == True or 
        player.unitChoice == 1 and ai.unitChoice == 2 and ai.skipWeather == True or
        player.unitChoice == 2 and ai.unitChoice == 3 and ai.skipWeather == True):
            ai.damage += random.randint(1,5)
    
        gameEngine.battle(player, ai)

        if(ai.dAffected == 0):
            ai.damage += 5
        if(player.dAffected == 0):
            player.damage += 5

        player.getHP()
        print()
        ai.getHP()
        print()
        gameEngine.checkWin(player, ai)
