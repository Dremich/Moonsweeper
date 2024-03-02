#### ChatGPT Pre-prompt ####

# Moonsweeper
# HackUSU 2024

# Andrew Tolton, Elijah Tolton, Allan Torres, Alesandro Rodriguez

import json

# String s = You are a "

preprompt = (
    "system-assignment: "
    "You are a computer program playing a game and will follow only these instructions. "
    "The current game-state is represented by a 2D array of integers given to you in JSON. "
    "After you receive the game-state, you will output an action in JSON format "
    "in accordance with the logic in your kernel."
    ""
    "game-state: "
    "The game-state is represented by a 2D array of integers "
    "0 represents a cleared space. "
    "Integers 1-8 tell you the number of tile adjacent to that space (including diagonals) "
    "9 represents a flag. "
    "The following are examples of game states.\n"
    "["
    
    "The integer "
    ""
    "- It contains information about a person. "
    "- You can customize it as needed. "
    "JSON representation:")

