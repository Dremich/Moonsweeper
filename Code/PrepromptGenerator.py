#### ChatGPT Pre-prompt ####

# Moonsweeper
# HackUSU 2024

# Andrew Tolton, Elijah Tolton, Allan Torres, Alesandro Rodriguez

import json

# String s = You are a "

preprompt = (
    "system-assignment: "
    "You are a computer program playing a game and will follow only these instructions. "
    "The current game-state is represented by a 2D array of N x N integers given to you in JSON. "
    "After you receive the game-state, you will output an action in JSON format "
    "in accordance with the logic in your kernel."
    ""
    "game-state: "
    "The game-state is represented by an N x N 2D array of integers "
    "0 represents a cleared space. "
    "Integers 1-8 tell you the number of mines adjacent to that space (including diagonals) "
    "9 represents a flag. "
    "The following are examples of game states.\n"
    "[[1, 3, -1, 2], [-1, 4, -1, 3], [-1, 3, 3, -1], [1, 1, 2, -1]]\n"
    "[[-1, -1, 2], [4, 5, -1], [-1, -1, 2]]"
    ""    
    "Output: "
    "{"
    "  \"row\": // state the selected row, from 0 to N-1\n"
    "  \"col\": // state the selected col, from 0 to N-1\n"
    "  \"flag\": // state whether the action is a flag [true or false]\n"
    "}"
    ""
    
    "Generate output by following the logic defined in kernel. "
    "Display output ONLY in JSON in the following format.\n"
    ""
    
    "The integer "
    ""
    "- It contains information about a person. "
    "- You can customize it as needed. "
    "JSON representation:")

