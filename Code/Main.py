from Prompt import Prompt
from Game import Game
from TakeAction import takeAction

size = 5

# Create initial prompt
kernel_path = "kernel.txt"
prompt = Prompt(kernel_path, size);

# Initialize game
size = 5
numMines = 12

firstMove = takeAction(prompt.message)
game = Game.__init__(size, numMines, firstMove)

# Main game sequence
while (not game.over()):
    move = takeAction(prompt.message)
    game.updateGame(move)
    gameState = game.gameStateToString()
    prompt.setGameState(gameState)
    
    # Print game
    for ii in range(size):
        print()
        for ij in range(size):
            print(str(game.gameState[ii][ij]).rjust(2), end = ' ')
    


