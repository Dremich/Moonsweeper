Moonsweeper: A Natural Language Coding Activity

"For the NASA Artemis project, NASA needs an accurate map of the lunar surface.​ You are an astronaut driving along the lunar surface, and you need to explore the lunar terrain without getting your rover stuck in hazardous terrain.​ But your rover has a critical failure, and you need to make repairs.​ You need to program your autopilot to take over for you.​"

This project was made in ~12 hours of work during HackUSU 2024 by Andrew Tolton, Elijah Tolton, Allan Torres, and Alesandro Rodriguez. We created a simple implementation of the game minesweeper, and imported the OpenAI API to use GPT 3.5 turbo to run the game based on the English instructions written in the file kernel.txt. The game is currently played in the Main script. There is no GUI, and it just outputs each round to the command window in the form of text. To make a simple grid, this is in the form of integers, where

0 is a safe tile
-1 is a mine
-2 is a flag
-3 is an unexplored tile
-4 is exploded
Integers 1-8 are the number of adjacent tiles iwth a mine.

Game.py is the model and creates a game object. This generates a map of random mines and tiles known as the board, and calculates the players view of the map known as the gamestate. It also provides methods to allow the player to update the gamestate.

TakeAction.py is the method that allows you to actually prompt ChatGPT and return its text output.

PrepromptGenerator provides the prompt strings that force ChatGPT to only output JSON of the form:
{int row, int col, bool flag} where row and col refer to the tile position in the minesweeper game, and flag refers to whether the action flags the tile or selects the tile.

Main has ChatGPT play minesweeper by created a game using an initial position selected by ChatGPT, and then repeatedly giving ChatGPT the new gamestate, storing its action, and updating the gamestate until the game is over. It build and stores the chat history becuase in our testing it seems that ChatGPT is better able to follow instructions when it knows what its previous moves have been. Note that to use this app, you need a OpenAI API key saved in your local environment, and some money tied to your OpenAI account (using GPT 3.5 is really cheap, but without having money on your account you are limited to 3 requests per minute).

For a future activity, I would like to
1) Improve the mine generation--instead of it being random, implement an algorithm like described in "A Strong Algorithm" here: https://stackoverflow.com/questions/3578456/whats-the-algorithm-behind-minesweeper-generation
2) Create a GUI (moon themed?) so that students can see the minesweeper game
3) Have 2 rounds: in round 1 the students play the game completely manually so they can figure out how it works.
   In round 2 the student switches off playing with ChatGPT. i.e. student plays a few rounds, ChatGPT does, etc. so that it is still interactive and the student has to learn to make ChatGPT use flags to communicate with them.
4) Figure out how to use the OpenAI API without needed to store our key locally on their computer, but also not have the key in the code
5) Figure out how to distrubite the game to kids for an activity
