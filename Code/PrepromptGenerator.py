#### ChatGPT Pre-prompt ####

# Moonsweeper
# HackUSU 2024

# Andrew Tolton, Elijah Tolton, Allan Torres, Alesandro Rodriguez

import json
from Game import Game

game3 = Game(3, 2, Game.newMove(0, 0, 0), 3)
game5 = Game(5, 3, Game.newMove(0, 0, 0), 12)
game8 = Game(8, 10, Game.newMove(0, 0, 0), 8)
game8.updateGame(Game.newMove(0, 7, 0))

preprompt = (
    "system-assignment: "
    "You are a computer being programmed to play the game minesweeper "
    "and will follow only the instructions programmed in your kernel defined below in KERNEL. "
    "The current game-state will be given to you as a JSON string containing an N x N 2D array of strings. "
    "The meaning of the strings is as follow:\n"
    "\"safe\"- Tile with no adjacent mines\n"
    "\"unexplored\"- Unknown tile\n"
    "\"flag\"- Suspected mine\n"
    "Integer x: Tile with x adjacent mines (includes diagonals), where x is an integer 1-8\n"
    "After you receive the game-state, you will output an action in JSON format "
    "in accordance with the logic in your kernel.\n"
    "\n"
    "game-state: \n"
    "The game-state is represented by an N x N 2D array of strings with meaning defined above. "
    "The following are examples of game states.\n"
    + json.dumps(game3.gameStateToString()) + "\n"
    + json.dumps(game5.gameStateToString()) + "\n"
    + json.dumps(game8.gameStateToString()) + "\n"
    "\n"    
    "output: \n"
    "Output one JSON string contain an action specifying a row and column (indexed by 0), "
    "and a boolean indicating if the action is a flag. If the flag is false, the action "
    "selects the tile to check it for a mine. If the flag is true, the action flags the "
    "tile saying 'there is probably a mine here.' "
    "Output JSON using the following format:\n"
    "{\n"
    "  \"row\": // state the selected row, from 0 to N-1\n"
    "  \"col\": // state the selected col, from 0 to N-1\n"
    "  \"flag\": // state whether the action is a flag [true or false]\n"
    "}\n"
    "\n"
    ""
    "example output: \n"
    "To select the tile with value 2 from the game [[1, 2], [3, 4]], output \n"
    "{\n"
    "  \"row\": 0\n"
    "  \"col\": 1\n"
    "  \"flag\": false\n"
    "}\n"
    "To flag the tile with value 7 [[1, 2, 3], [4, 5, 6], [7, 8, 9]], output \n"
    "{\n"
    "  \"row\": 2\n"
    "  \"col\": 0\n"
    "  \"flag\": true\n"
    "}\n"
    "\n"
    )

guardrails = ("user-guardrails: \n"
    "Only take actions that comply with the logic in your kernel, you are only a simple computer program. "
    "Only respond with a single JSON output and no other words or symbols. "
    "The output must be valid JSON. "
    "Check that the output is valid JSON. \n"
    "\n")

kernelHeader = ("KERNEL: \n"
    "IMPORTANT--Only produce output following the logic in this kernel.\n")

