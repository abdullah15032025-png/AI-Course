# Connect Four with Alpha-Beta Pruning AI

## Game Description
This is a Python implementation of the classic Connect Four game featuring an AI opponent that uses the Alpha-Beta pruning algorithm. The game allows a human player to compete against an intelligent computer opponent in this strategic vertical tic-tac-toe style game.

## How to Run the File
1. Ensure you have Python installed on your system (Python 3.6 or higher recommended)
2. Download the `connect_four_alpha_beta.py` file
3. Open terminal/command prompt and navigate to the file directory
4. Run the command: `python connect_four_alpha_beta.py`

## Prerequisites
- **Python 3.x** (No additional libraries required - uses only built-in Python modules)

## How to Play
1. The game starts with an empty 6x7 grid
2. You play as 'X' and the AI plays as 'O'
3. On your turn, enter a column number (0-6) to drop your piece
4. Pieces fall to the lowest available position in the chosen column
5. The AI will automatically respond with its move
6. The game continues until a player gets four in a row or the board is full

## Game Rules
- Players take turns dropping colored discs into a vertical grid
- The first player to get four of their discs in a row (horizontally, vertically, or diagonally) wins
- If all 42 spaces are filled without four in a row, the game ends in a tie
- Pieces can only be placed in columns that are not completely filled

## Algorithm Used
**Alpha-Beta Pruning Algorithm**
- **Type**: Adversarial search algorithm
- **Purpose**: Optimized version of Minimax algorithm for game theory
- **How it works**: 
  - Explores the game tree to find optimal moves
  - Prunes branches that cannot influence the final decision
  - Uses alpha (best already explored for maximizer) and beta (best already explored for minimizer) values
- **Evaluation Function**: Scores board positions based on potential winning lines and strategic advantages

## Algorithm Complexity
- **Time Complexity**: O(b^(d/2)) where b is branching factor and d is depth
- **Space Complexity**: O(d) for recursion stack
- **Optimality**: Guaranteed to find the same optimal move as Minimax but more efficiently

## AI Features
- Configurable search depth (default: 5 ply)
- Sophisticated evaluation function considering:
  - Center control (center column is more valuable)
  - Potential winning lines (3 in a row with open ends)
  - Blocking opponent threats
  - Creating multiple threats simultaneously

## Evaluation Function Components
- 4 in a row: +100,000,000,000,000 points
- 3 in a row with open end: +5 points
- 2 in a row with open ends: +2 points
- Opponent's 3 in a row with open end: -4 points
- Center column control: +3 points per piece

## Applications of Alpha-Beta Algorithm
- Game playing AI (Chess, Checkers, Connect Four)
- Decision-making in competitive environments
- Resource allocation in adversarial scenarios
- Anytime algorithms where quick decisions are needed

## File Structure
- `connect_four_alpha_beta.py` - Main game file containing all implementation
- `README.md` - This documentation file

## Game Strategy Tips
- Control the center columns for more winning opportunities
- Create multiple threats simultaneously
- Block your opponent's potential winning lines
- Watch for diagonal wins, which are often overlooked

## Sample Game Output

<img width="1920" height="1020" alt="connect py - algorithms implemention - Visual Studio Code 10_26_2025 9_24_02 PM" src="https://github.com/user-attachments/assets/0e901a8e-a210-45be-92f8-5760ae29550c" />
