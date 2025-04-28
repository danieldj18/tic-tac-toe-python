# 1) Define winning combinations at the top
WIN_COMBOS = [
    (0,1,2), (3,4,5), (6,7,8),  # rows
    (0,3,6), (1,4,7), (2,5,8),  # columns
    (0,4,8), (2,4,6)            # diagonals
]


def draw_board(b):
    """Prints the current board state."""
    print(f"""
     {b[0]} | {b[1]} | {b[2]}
    ---+---+---
     {b[3]} | {b[4]} | {b[5]}
    ---+---+---
     {b[6]} | {b[7]} | {b[8]}
    """)

def get_player_move(b):

    while True:
        move = input("Choose position (1-9): ").strip()
        if move.isdigit():
            idx = int(move) - 1
            if 0 <= idx < 9 and b[idx] == ' ':
                return idx
        print("Invalid choice; that square is taken or out of range.")


def check_winner(b):
    """Return 'X' or 'O' if there’s a winner, 'Draw' if full, or None otherwise."""
    for a, c, d in WIN_COMBOS:
        if b[a] == b[c] == b[d] != ' ':
            return b[a]
    if ' ' not in b:
            return "Draw"
    return None



def main():
    board = [' '] * 9
    current = 'X'

    while True:
        draw_board(board)
        idx = get_player_move(board)
        board[idx] = current

        winner = check_winner(board)
        if winner:
            if winner == "Draw":
                print("Draw!")
            else:
                print (f"Winner is {winner}")
            break

        current = 'O' if current == 'X' else 'X'


if __name__ == "__main__":
    main()


