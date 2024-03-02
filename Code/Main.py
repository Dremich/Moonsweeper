from Prompt import Prompt
from Game import Game
from TakeAction import takeAction

def printGame(game):
    for ii in range(size):
        print()
        for ij in range(size):
            print(str(game.gameState[ii][ij]).rjust(2), end = ' ')

size = 5

# Create initial prompt
kernel_path = "kernel.txt"
prompt = Prompt(kernel_path, size);

# Initialize game
numMines = 6

firstMove = takeAction(prompt.message)
game = Game(size, numMines, firstMove)
printGame(game)

# Main game sequence
while (not game.over()):
    move = takeAction(prompt.message)
    
    # If any errors, try again
    try:
        game.updateGame(move)
    except:
        continue
    
    gameState = game.gameStateToString()
    prompt.setGameState(gameState)
    
    # Print game
    printGame(game)
    

print("GAME OVER!")