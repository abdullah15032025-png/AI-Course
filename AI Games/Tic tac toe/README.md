Tic-Tac-Toe with Alpha-Beta Pruning Algorithm
Game Description
This is an implementation of the classic Tic-Tac-Toe game featuring an AI opponent that uses the Alpha-Beta pruning algorithm for optimal decision-making. The game allows a human player to compete against an intelligent computer opponent that never loses.

How to Run the File
Ensure you have Python installed on your system (Python 3.6 or higher recommended)

Download the tic_tac_toe_alpha_beta.py file

Open terminal/command prompt and navigate to the file directory

Run the command: python tic_tac_toe_alpha_beta.py

Prerequisites
Python 3.x (No additional libraries required - uses only built-in Python modules)

How to Play
The game starts with an empty 3x3 board

You play as 'X' and the AI plays as 'O'

On your turn, enter row and column numbers (0-2) when prompted

Example: Enter 0 for row and 0 for column to place your mark in the top-left corner

The AI will automatically respond with its move after your turn

The game continues until either player wins or the board is full (tie)

Game Rules
Players take turns placing their marks ('X' or 'O') on a 3x3 grid

The first player to get 3 of their marks in a row (horizontally, vertically, or diagonally) wins

If all 9 squares are filled and no player has 3 in a row, the game ends in a tie

Algorithm Used
Alpha-Beta Pruning Algorithm

Type: Adversarial search algorithm

Purpose: Optimized version of Minimax algorithm for game theory

How it works:

Explores the game tree to find optimal moves

Prunes branches that cannot influence the final decision

Uses alpha (best already explored for maximizer) and beta (best already explored for minimizer) values to eliminate unnecessary computations

Advantage: Reduces computation time by avoiding evaluation of irrelevant game states

Algorithm Complexity
Time Complexity: O(b^(d/2)) where b is branching factor and d is depth (compared to O(b^d) for Minimax)

Space Complexity: O(d) for recursion stack

Optimality: Guaranteed to find the same optimal move as Minimax but more efficiently

Applications of Alpha-Beta Algorithm
Game playing AI (Chess, Checkers, Othello)

Decision-making in competitive environments

Resource allocation in adversarial scenarios

Anytime algorithms where quick decisions are needed

Game Features
Clean console-based interface

Input validation to prevent errors

Optimal AI opponent that cannot be beaten

Real-time move evaluation using Alpha-Beta pruning

Sample Game Output
<img width="1920" height="1020" alt="tictactoe py - algorithms implemention - Visual Studio Code 10_26_2025 9_08_54 PM" src="https://github.com/user-attachments/assets/095754f5-a45e-4271-8561-cb4c1f17a435" />
