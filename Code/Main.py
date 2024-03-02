from Prompt import Prompt
from Game import Game
from TakeAction import takeAction
import json

def printGame(game):
    for ii in range(size):
        print()
        for ij in range(size):
            print(str(game.gameState[ii][ij]).rjust(2), end = ' ')

# Initialize game
numMines = 6
size = 5

# Create initial prompt
kernel_path = "kernel.txt"
prompt = Prompt(kernel_path, size);

# Start game
firstMove = takeAction(prompt.message)
prompt.addChatResponse(firstMove)

game = Game(size, numMines, firstMove)
prompt.addGameState(json.dumps(game.gameStateToString()))

printGame(game)

# Main game sequence
while (not game.over()):
    move = takeAction(prompt.message)
    
    # If any errors, try again
    try:
        game.updateGame(move)
    except:
        prompt.addChatResponse(move)
        prompt.addString("Invalid tile, choose another")
        continue
    
    gameState = game.gameStateToString()
    prompt.addChatResponse(move)
    prompt.addGameState(json.dumps(game.gameStateToString()))
    
    # Print game
    printGame(game)
    

print("GAME OVER!")