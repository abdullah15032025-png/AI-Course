import copy
import math
import random

class ConnectFour:
    def __init__(self):
        self.rows = 6
        self.cols = 7
        self.board = [[' ' for _ in range(self.cols)] for _ in range(self.rows)]
        self.current_player = 'X'  # Human is 'X', AI is 'O'
        
    def print_board(self):
        print("\n  " + "   ".join(str(i) for i in range(self.cols)))
        print("  " + "---" * self.cols)
        for row in self.board:
            print("| " + " | ".join(row) + " |")
            print("  " + "---" * self.cols)
        print()
    
    def is_valid_move(self, col):
        return 0 <= col < self.cols and self.board[0][col] == ' '
    
    def get_valid_moves(self):
        return [col for col in range(self.cols) if self.is_valid_move(col)]
    
    def make_move(self, col, player):
        for row in range(self.rows-1, -1, -1):
            if self.board[row][col] == ' ':
                self.board[row][col] = player
                return True
        return False
    
    def undo_move(self, col):
        for row in range(self.rows):
            if self.board[row][col] != ' ':
                self.board[row][col] = ' '
                return True
        return False
    
    def check_winner(self):
        # Check horizontal
        for row in range(self.rows):
            for col in range(self.cols - 3):
                if (self.board[row][col] != ' ' and
                    self.board[row][col] == self.board[row][col+1] == 
                    self.board[row][col+2] == self.board[row][col+3]):
                    return self.board[row][col]
        
        # Check vertical
        for row in range(self.rows - 3):
            for col in range(self.cols):
                if (self.board[row][col] != ' ' and
                    self.board[row][col] == self.board[row+1][col] == 
                    self.board[row+2][col] == self.board[row+3][col]):
                    return self.board[row][col]
        
        # Check diagonal (positive slope)
        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                if (self.board[row][col] != ' ' and
                    self.board[row][col] == self.board[row+1][col+1] == 
                    self.board[row+2][col+2] == self.board[row+3][col+3]):
                    return self.board[row][col]
        
        # Check diagonal (negative slope)
        for row in range(3, self.rows):
            for col in range(self.cols - 3):
                if (self.board[row][col] != ' ' and
                    self.board[row][col] == self.board[row-1][col+1] == 
                    self.board[row-2][col+2] == self.board[row-3][col+3]):
                    return self.board[row][col]
        
        return None
    
    def is_board_full(self):
        return all(self.board[0][col] != ' ' for col in range(self.cols))
    
    def is_game_over(self):
        return self.check_winner() is not None or self.is_board_full()

class ConnectFourAI:
    def __init__(self, depth=5):
        self.depth = depth
        
    def evaluate_window(self, window, player):
        score = 0
        opponent = 'X' if player == 'O' else 'O'
        
        if window.count(player) == 4:
            score += 100
        elif window.count(player) == 3 and window.count(' ') == 1:
            score += 5
        elif window.count(player) == 2 and window.count(' ') == 2:
            score += 2
            
        if window.count(opponent) == 3 and window.count(' ') == 1:
            score -= 4
            
        return score
    
    def evaluate_position(self, game, player):
        score = 0
        
        # Prefer center column
        center_array = [game.board[row][3] for row in range(game.rows)]
        center_count = center_array.count(player)
        score += center_count * 3
        
        # Evaluate horizontal
        for row in range(game.rows):
            row_array = game.board[row]
            for col in range(game.cols - 3):
                window = row_array[col:col+4]
                score += self.evaluate_window(window, player)
        
        # Evaluate vertical
        for col in range(game.cols):
            col_array = [game.board[row][col] for row in range(game.rows)]
            for row in range(game.rows - 3):
                window = col_array[row:row+4]
                score += self.evaluate_window(window, player)
        
        # Evaluate positive diagonal
        for row in range(game.rows - 3):
            for col in range(game.cols - 3):
                window = [game.board[row+i][col+i] for i in range(4)]
                score += self.evaluate_window(window, player)
        
        # Evaluate negative diagonal
        for row in range(3, game.rows):
            for col in range(game.cols - 3):
                window = [game.board[row-i][col+i] for i in range(4)]
                score += self.evaluate_window(window, player)
        
        return score
    
    def alpha_beta(self, game, depth, alpha, beta, maximizing_player, ai_player):
        human_player = 'X' if ai_player == 'O' else 'O'
        
        valid_moves = game.get_valid_moves()
        is_terminal = game.is_game_over()
        
        if depth == 0 or is_terminal:
            if is_terminal:
                winner = game.check_winner()
                if winner == ai_player:
                    return (None, 100000000000000)
                elif winner == human_player:
                    return (None, -10000000000000)
                else:  # Game is over, no winner - it's a tie
                    return (None, 0)
            else:  # Depth is zero
                return (None, self.evaluate_position(game, ai_player))
        
        if maximizing_player:
            value = -math.inf
            column = random.choice(valid_moves)
            
            for col in valid_moves:
                game_copy = copy.deepcopy(game)
                game_copy.make_move(col, ai_player)
                new_score = self.alpha_beta(game_copy, depth-1, alpha, beta, False, ai_player)[1]
                
                if new_score > value:
                    value = new_score
                    column = col
                
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            
            return column, value
        
        else:  # Minimizing player
            value = math.inf
            column = random.choice(valid_moves)
            
            for col in valid_moves:
                game_copy = copy.deepcopy(game)
                game_copy.make_move(col, human_player)
                new_score = self.alpha_beta(game_copy, depth-1, alpha, beta, True, ai_player)[1]
                
                if new_score < value:
                    value = new_score
                    column = col
                
                beta = min(beta, value)
                if alpha >= beta:
                    break
            
            return column, value
    
    def get_best_move(self, game, ai_player):
        return self.alpha_beta(game, self.depth, -math.inf, math.inf, True, ai_player)[0]

def main():
    game = ConnectFour()
    ai = ConnectFourAI(depth=5)  # Adjust depth for difficulty
    
    print("Welcome to Connect Four with Alpha-Beta AI!")
    print("You are playing as X, AI is O")
    print("Enter column numbers (0-6) to make your move")
    
    while True:
        game.print_board()
        
        # Check game state
        winner = game.check_winner()
        if winner:
            if winner == 'X':
                print("Congratulations! You win!")
            else:
                print("AI wins!")
            break
        elif game.is_board_full():
            print("It's a tie!")
            break
        
        if game.current_player == 'X':
            # Human player's turn
            while True:
                try:
                    col = int(input("Your move (0-6): "))
                    if game.is_valid_move(col):
                        game.make_move(col, 'X')
                        game.current_player = 'O'
                        break
                    else:
                        print("Invalid move! Column is full or out of range.")
                except ValueError:
                    print("Please enter a valid number (0-6).")
        else:
            # AI's turn
            print("AI is thinking...")
            ai_move = ai.get_best_move(game, 'O')
            game.make_move(ai_move, 'O')
            print(f"AI placed a piece in column {ai_move}")
            game.current_player = 'X'

if __name__ == "__main__":
    main()
