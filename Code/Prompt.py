from PrepromptGenerator import preprompt
import json

class Prompt:
    
    def __init__(self, kernel_path, N):
        instructions = ""
        
        # Read user kernel
        with open(kernel_path, "r") as file:            
            # Iterate over each line in the file
            for line in file:
                # Append the line to the string variable
                instructions += line
                
        # Create initial empty game state
        emptyBoard = [["unexplored" for _ in range(N)] for _ in range(N)]
        
        self.message = [{"role": "system", "content": instructions}]
        self.message.append({"role": "user", "content": json.dumps(emptyBoard)})
        

    def setGameState(self, gameState):
        if len(self.message) > 0:
            self.message[-1]["content"] = gameState

