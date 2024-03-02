# -*- coding: utf-8 -*-
"""
HackUSU Prompt

@author Andrew Tolton, Allan Torres, Waldo, Elijah Tolton
"""

import random
import json

class Game:
    safe = 0
    mine = -1
    flag = -2
    unexplored = -3
    exploded = -4    
    
    def __init__(self, size, numMines, firstMove):  # Fixed method name (init instead of init)
        # Parse first move
        row, col = firstMove["row"], firstMove["col"]
    
        # Generate valid map
        while(True):
            self.board = Game.generateMap(size, numMines)
            if not self.board[row][col] == -1:
                break

    
        self.gamestate = [[Game.unexplored for ii in range(size)] for ii in range(size)]  # Initialize gamestate with -3
        
    def updateGame(self, actionString):
        action = json.loads(actionString)
        row, col = action["row"], action["col"]

        if action.get("flag"):
            self.gameState[row][col] = Game.flag  # Flag the cell
        else:
            if self.gameState[row][col] == Game.mine:  # If it's a mine
                self.gameState[row][col] = Game.exploded  # Game over, triggered mine
            
            elif self.gameState[row][col] == Game.unexplored:  # Reveal the cell
                self.revealTiles(row, col)
            else:
                raise Exception("Invalid tile")

        return self.gameState

    def revealTiles(self, row, col):
        """
        Reveals tiles on the Minesweeper board starting from the specified row and column.
        
        Args:
            board (list): The Minesweeper board represented as a 2D list.
            row (int): The row of the tile to start revealing from.
            col (int): The column of the tile to start revealing from.
            gameState (list): A 2D list representing which tiles have been revealed.
        """
        # Base case: if the current tile is already revealed or out of bounds, return
        if row < 0 or row >= len(self.board) or col < 0 or col >= len(self.board[0]) or self.gameState[row][col] != self.unexplored:
            return
        
        # Mark the current tile as revealed
        self.gameState[row][col] = self.board[row][col]
        
        # If the current tile is safe and has no adjacent mines, recursively reveal adjacent tiles
        if self.board[row][col] == Game.safe:
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if not dr == 0 and dc == 0:
                        self.revealTiles(row + dr, col + dc)
        
    def generateMap(size, difficulty):
        map = [[0] * size for ii in range(size)]
        rng = random.Random()

        # Place mines randomly
        for ii in range(difficulty):  # Fixed missing iterator variable
            while True:
                row, col = rng.randint(0, size-1), rng.randint(0, size-1)
                if map[row][col] != -1:
                    map[row][col] = -1
                    break

        # Calculate adjacent mines for each cell
        for i in range(size):
            for j in range(size):
                if map[i][j] != -1:
                    map[i][j] = sum(1 for di in [-1, 0, 1] for dj in [-1, 0, 1]
                                    if 0 <= i+di < size and 0 <= j+dj < size and map[i+di][j+dj] == -1)
        return map
        