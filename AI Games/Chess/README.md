# Chess Game with Alpha-Beta Pruning AI

## Game Description
This is a Python implementation of the classic Chess game featuring an AI opponent that uses the Minimax algorithm with Alpha-Beta pruning. The game allows a human player to compete against an intelligent computer opponent in the strategic game of Chess.

## How to Run the File
1. Ensure you have Python installed on your system (Python 3.6 or higher recommended)
2. Download the `chess_alpha_beta.py` file
3. Open terminal/command prompt and navigate to the file directory
4. Run the command: `python chess_alpha_beta.py`

## Prerequisites
- **Python 3.x** (No additional libraries required - uses only built-in Python modules)
- **Unicode support** in terminal for proper chess piece display

## How to Play
1. The game starts with a standard chess board setup
2. You play as WHITE and the AI plays as BLACK
3. On your turn, enter moves in algebraic notation (e.g., "e2 e4")
4. The AI will automatically respond with its move
5. The game continues until checkmate, stalemate, or resignation

## Game Rules
- Standard chess rules apply
- Pieces move according to traditional chess movement patterns
- Check and checkmate detection is implemented
- Pawn promotion is simplified (always promotes to queen)
- Castling and en passant are not implemented in this version

## Algorithm Used
**Minimax with Alpha-Beta Pruning**
- **Type**: Adversarial search algorithm
- **Purpose**: Optimal decision-making in zero-sum games
- **How it works**: 
  - Explores the game tree to a specified depth
  - Uses Alpha-Beta pruning to eliminate branches that cannot affect the final decision
  - Evaluates board positions using a heuristic function
- **Evaluation Function**: Based on material count and positional advantages

## Algorithm Complexity
- **Time Complexity**: O(b^(d/2)) where b is branching factor and d is depth
- **Space Complexity**: O(d) for recursion stack
- **Optimality**: Finds the best move given the search depth and evaluation function

## AI Features
- Configurable search depth (default: 3 ply)
- Material-based evaluation with positional bonuses
- Legal move generation with check validation
- Alpha-Beta pruning for efficient search

## Piece Values Used for Evaluation
- Pawn: 1 point
- Knight: 3 points
- Bishop: 3 points
- Rook: 5 points
- Queen: 9 points
- King: 100 points

## Applications of Alpha-Beta Algorithm in Chess
- Computer chess engines
- Game theory research
- Decision-making in competitive environments
- AI research and development

## File Structure
- `chess_alpha_beta.py` - Main game file containing all implementation
- `README.md` - This documentation file

## Limitations
- Does not implement castling or en passant
- Pawn always promotes to queen
- No opening book or endgame tablebase
- Basic evaluation function (strong players can exploit weaknesses)

## Sample Game Input
<img width="1920" height="1020" alt="tictactoe py - algorithms implemention - Visual Studio Code 10_26_2025 9_16_10 PM" src="https://github.com/user-attachments/assets/199d83be-6af2-4106-b779-324806a77427" />
