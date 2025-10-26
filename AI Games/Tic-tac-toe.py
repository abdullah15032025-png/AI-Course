def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def alpha_beta(board, depth, alpha, beta, maximizing_player):
    winner = check_winner(board)
    if winner == 'O':  # AI wins
        return 1
    elif winner == 'X':  # Human wins
        return -1
    elif is_board_full(board):  # Tie
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for move in get_available_moves(board):
            i, j = move
            board[i][j] = 'O'
            eval = alpha_beta(board, depth + 1, alpha, beta, False)
            board[i][j] = ' '
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_available_moves(board):
            i, j = move
            board[i][j] = 'X'
            eval = alpha_beta(board, depth + 1, alpha, beta, True)
            board[i][j] = ' '
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def get_best_move(board):
    best_val = float('-inf')
    best_move = None
    for move in get_available_moves(board):
        i, j = move
        board[i][j] = 'O'
        move_val = alpha_beta(board, 0, float('-inf'), float('inf'), False)
        board[i][j] = ' '
        if move_val > best_val:
            best_val = move_val
            best_move = move
    return best_move

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    
    while True:
        # Human move
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    break
                else:
                    print("Cell already occupied!")
            except (ValueError, IndexError):
                print("Invalid input! Enter numbers between 0-2.")
        
        print_board(board)
        if check_winner(board) == 'X':
            print("You win!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

        # AI move
        print("AI's turn...")
        ai_move = get_best_move(board)
        board[ai_move[0]][ai_move[1]] = 'O'
        print_board(board)
        
        if check_winner(board) == 'O':
            print("AI wins!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()
