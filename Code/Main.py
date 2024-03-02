import Prompt
import Game
from TakeAction import takeAction

# Create initial prompt
kernel_path = "kernel.txt"
prompt = Prompt.__init__(kernel_path);

# Initialize game
size = 5
numMines = 12

firstMove = takeAction(prompt.message)
game = Game.__init__(size, numMines, firstMove)

# Main game sequence
while (not game.Over()):
    move = takeAction(prompt.message)
    gameState = game.updateGame(move)
    prompt.setGameState(gameState)
    


