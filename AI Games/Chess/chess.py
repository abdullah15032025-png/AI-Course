import copy
import math

class ChessGame:
    def __init__(self):
        self.board = self.initialize_board()
        self.current_player = 'white'
        self.move_history = []
        
    def initialize_board(self):
        # Initialize an 8x8 chess board
        board = [['' for _ in range(8)] for _ in range(8)]
        
        # Set up pawns
        for col in range(8):
            board[1][col] = 'bp'  # Black pawns
            board[6][col] = 'wp'  # White pawns
            
        # Set up other pieces
        pieces = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
        for col, piece in enumerate(pieces):
            board[0][col] = 'b' + piece  # Black pieces
            board[7][col] = 'w' + piece  # White pieces
            
        # Fill empty squares
        for row in range(2, 6):
            for col in range(8):
                if not board[row][col]:
                    board[row][col] = '--'
                    
        return board
    
    def print_board(self):
        print("  a b c d e f g h")
        print("  ----------------")
        for row in range(8):
            print(f"{8-row}|", end="")
            for col in range(8):
                piece = self.board[row][col]
                if piece == '--':
                    print('. ', end="")
                else:
                    # Convert to chess symbols for better visualization
                    color = piece[0]
                    piece_type = piece[1]
                    symbols = {
                        'p': '♟', 'r': '♜', 'n': '♞', 'b': '♝',
                        'q': '♛', 'k': '♚',
                        'P': '♙', 'R': '♖', 'N': '♘', 'B': '♗',
                        'Q': '♕', 'K': '♔'
                    }
                    if color == 'w':
                        symbol = symbols.get(piece_type.upper(), piece_type)
                    else:
                        symbol = symbols.get(piece_type, piece_type)
                    print(symbol + ' ', end="")
            print(f"|{8-row}")
        print("  ----------------")
        print("  a b c d e f g h")
    
    def get_piece_moves(self, row, col):
        """Get all possible moves for a piece at given position"""
        piece = self.board[row][col]
        if piece == '--':
            return []
            
        color = piece[0]
        piece_type = piece[1]
        moves = []
        
        if piece_type == 'p':  # Pawn
            direction = 1 if color == 'b' else -1
            start_row = 1 if color == 'b' else 6
            
            # Move forward
            if 0 <= row + direction < 8 and self.board[row + direction][col] == '--':
                moves.append((row + direction, col))
                # Double move from starting position
                if row == start_row and self.board[row + 2 * direction][col] == '--':
                    moves.append((row + 2 * direction, col))
            
            # Captures
            for dc in [-1, 1]:
                if 0 <= col + dc < 8 and 0 <= row + direction < 8:
                    target = self.board[row + direction][col + dc]
                    if target != '--' and target[0] != color:
                        moves.append((row + direction, col + dc))
        
        elif piece_type == 'r':  # Rook
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            moves.extend(self.get_sliding_moves(row, col, directions, color))
        
        elif piece_type == 'b':  # Bishop
            directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
            moves.extend(self.get_sliding_moves(row, col, directions, color))
        
        elif piece_type == 'q':  # Queen
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1), 
                         (1, 1), (1, -1), (-1, 1), (-1, -1)]
            moves.extend(self.get_sliding_moves(row, col, directions, color))
        
        elif piece_type == 'n':  # Knight
            knight_moves = [
                (2, 1), (2, -1), (-2, 1), (-2, -1),
                (1, 2), (1, -2), (-1, 2), (-1, -2)
            ]
            for dr, dc in knight_moves:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    target = self.board[new_row][new_col]
                    if target == '--' or target[0] != color:
                        moves.append((new_row, new_col))
        
        elif piece_type == 'k':  # King
            king_moves = [
                (1, 0), (-1, 0), (0, 1), (0, -1),
                (1, 1), (1, -1), (-1, 1), (-1, -1)
            ]
            for dr, dc in king_moves:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    target = self.board[new_row][new_col]
                    if target == '--' or target[0] != color:
                        moves.append((new_row, new_col))
        
        return moves
    
    def get_sliding_moves(self, row, col, directions, color):
        """Get moves for sliding pieces (rook, bishop, queen)"""
        moves = []
        for dr, dc in directions:
            for i in range(1, 8):
                new_row, new_col = row + i * dr, col + i * dc
                if not (0 <= new_row < 8 and 0 <= new_col < 8):
                    break
                    
                target = self.board[new_row][new_col]
                if target == '--':
                    moves.append((new_row, new_col))
                elif target[0] != color:
                    moves.append((new_row, new_col))
                    break
                else:
                    break
        return moves
    
    def is_valid_move(self, start_row, start_col, end_row, end_col):
        """Check if a move is valid"""
        moves = self.get_piece_moves(start_row, start_col)
        return (end_row, end_col) in moves
    
    def make_move(self, start_row, start_col, end_row, end_col):
        """Make a move on the board"""
        if not self.is_valid_move(start_row, start_col, end_row, end_col):
            return False
            
        piece = self.board[start_row][start_col]
        self.board[end_row][end_col] = piece
        self.board[start_row][start_col] = '--'
        
        # Pawn promotion (simplified - always promote to queen)
        if piece[1] == 'p' and (end_row == 0 or end_row == 7):
            self.board[end_row][end_col] = piece[0] + 'q'
        
        self.move_history.append(((start_row, start_col), (end_row, end_col)))
        self.current_player = 'black' if self.current_player == 'white' else 'white'
        return True
    
    def get_all_moves(self, color):
        """Get all possible moves for a color"""
        moves = []
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece != '--' and piece[0] == color[0]:
                    piece_moves = self.get_piece_moves(row, col)
                    for move in piece_moves:
                        moves.append(((row, col), move))
        return moves
    
    def is_check(self, color):
        """Check if the king of given color is in check"""
        # Find the king
        king_pos = None
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece != '--' and piece[0] == color[0] and piece[1] == 'k':
                    king_pos = (row, col)
                    break
            if king_pos:
                break
        
        if not king_pos:
            return False
        
        # Check if any opponent piece can attack the king
        opponent_color = 'b' if color[0] == 'w' else 'w'
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece != '--' and piece[0] == opponent_color:
                    if king_pos in self.get_piece_moves(row, col):
                        return True
        return False
    
    def is_checkmate(self, color):
        """Check if it's checkmate for the given color"""
        if not self.is_check(color):
            return False
        
        # If in check and no legal moves, it's checkmate
        return len(self.get_legal_moves(color)) == 0
    
    def is_stalemate(self, color):
        """Check if it's stalemate for the given color"""
        if self.is_check(color):
            return False
        
        # If not in check but no legal moves, it's stalemate
        return len(self.get_legal_moves(color)) == 0
    
    def get_legal_moves(self, color):
        """Get all legal moves for a color (considering check)"""
        legal_moves = []
        all_moves = self.get_all_moves(color)
        
        for start, end in all_moves:
            # Create a copy of the game state to test the move
            test_game = copy.deepcopy(self)
            test_game.make_move(start[0], start[1], end[0], end[1])
            
            # If after the move, the king is not in check, it's legal
            if not test_game.is_check(color):
                legal_moves.append((start, end))
                
        return legal_moves

class ChessAI:
    def __init__(self, depth=3):
        self.depth = depth
        
    def evaluate_board(self, game, color):
        """Simple evaluation function based on material count"""
        piece_values = {
            'p': 1, 'n': 3, 'b': 3, 'r': 5, 'q': 9, 'k': 100
        }
        
        score = 0
        for row in range(8):
            for col in range(8):
                piece = game.board[row][col]
                if piece != '--':
                    value = piece_values.get(piece[1], 0)
                    if piece[0] == color[0]:
                        score += value
                    else:
                        score -= value
        
        # Add small bonuses for control of center and piece development
        center_squares = [(3, 3), (3, 4), (4, 3), (4, 4)]
        for row, col in center_squares:
            piece = game.board[row][col]
            if piece != '--' and piece[0] == color[0]:
                score += 0.1
        
        return score
    
    def alpha_beta(self, game, depth, alpha, beta, maximizing_player, ai_color):
        """Alpha-Beta pruning algorithm for chess"""
        if depth == 0 or game.is_checkmate(ai_color) or game.is_checkmate(self.get_opponent_color(ai_color)) or game.is_stalemate(ai_color):
            return self.evaluate_board(game, ai_color)
        
        if maximizing_player:
            max_eval = -math.inf
            legal_moves = game.get_legal_moves(ai_color)
            
            for start, end in legal_moves:
                # Make move on a copy
                new_game = copy.deepcopy(game)
                new_game.make_move(start[0], start[1], end[0], end[1])
                
                eval = self.alpha_beta(new_game, depth - 1, alpha, beta, False, ai_color)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                
                if beta <= alpha:
                    break  # Beta cutoff
                    
            return max_eval
        else:
            min_eval = math.inf
            opponent_color = self.get_opponent_color(ai_color)
            legal_moves = game.get_legal_moves(opponent_color)
            
            for start, end in legal_moves:
                # Make move on a copy
                new_game = copy.deepcopy(game)
                new_game.make_move(start[0], start[1], end[0], end[1])
                
                eval = self.alpha_beta(new_game, depth - 1, alpha, beta, True, ai_color)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                
                if beta <= alpha:
                    break  # Alpha cutoff
                    
            return min_eval
    
    def get_opponent_color(self, color):
        return 'black' if color == 'white' else 'white'
    
    def get_best_move(self, game, ai_color):
        """Get the best move for the AI using Alpha-Beta pruning"""
        best_move = None
        best_value = -math.inf
        legal_moves = game.get_legal_moves(ai_color)
        
        for start, end in legal_moves:
            # Make move on a copy
            new_game = copy.deepcopy(game)
            new_game.make_move(start[0], start[1], end[0], end[1])
            
            move_value = self.alpha_beta(new_game, self.depth - 1, -math.inf, math.inf, False, ai_color)
            
            if move_value > best_value:
                best_value = move_value
                best_move = (start, end)
        
        return best_move

def position_to_coords(position):
    """Convert chess notation (e.g., 'e2') to board coordinates"""
    if len(position) != 2:
        return None
    col_char, row_char = position[0], position[1]
    col = ord(col_char) - ord('a')
    row = 8 - int(row_char)
    return (row, col)

def coords_to_position(coords):
    """Convert board coordinates to chess notation"""
    row, col = coords
    col_char = chr(ord('a') + col)
    row_char = str(8 - row)
    return col_char + row_char

def main():
    game = ChessGame()
    ai = ChessAI(depth=3)  # Increase depth for stronger AI
    
    print("Welcome to Chess with Alpha-Beta AI!")
    print("You are playing as WHITE")
    print("Enter moves in format: e2 e4")
    print()
    
    while True:
        game.print_board()
        print()
        
        # Check game state
        if game.is_checkmate(game.current_player):
            winner = 'BLACK' if game.current_player == 'white' else 'WHITE'
            print(f"Checkmate! {winner} wins!")
            break
        elif game.is_stalemate(game.current_player):
            print("Stalemate! Game is a draw!")
            break
        elif game.is_check(game.current_player):
            print(f"{game.current_player.capitalize()} is in CHECK!")
        
        if game.current_player == 'white':
            # Human player's turn
            while True:
                try:
                    move_input = input("Your move (e.g., 'e2 e4' or 'quit'): ").strip().lower()
                    if move_input == 'quit':
                        print("Thanks for playing!")
                        return
                    
                    start_pos, end_pos = move_input.split()
                    start = position_to_coords(start_pos)
                    end = position_to_coords(end_pos)
                    
                    if start and end:
                        if game.make_move(start[0], start[1], end[0], end[1]):
                            break
                        else:
                            print("Invalid move! Try again.")
                    else:
                        print("Invalid input format! Use format like 'e2 e4'")
                except ValueError:
                    print("Invalid input! Enter two positions separated by space.")
        else:
            # AI's turn
            print("AI is thinking...")
            best_move = ai.get_best_move(game, 'black')
            
            if best_move:
                start, end = best_move
                start_pos = coords_to_position(start)
                end_pos = coords_to_position(end)
                game.make_move(start[0], start[1], end[0], end[1])
                print(f"AI moves: {start_pos} {end_pos}")
            else:
                print("AI has no legal moves!")
                break

if __name__ == "__main__":
    main()
