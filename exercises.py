class Game:
    def __init__(self):
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }
    def play_game(self):
        print("Welcome to the game!")
        self.print_board()

        while not self.winner and not self.tie:
            self.print_turn_message()
            move = self.get_valid_move()
            self.play_move(move)
            self.print_board()

            if self.check_winner():
                self.print_winner_message()
            elif self.check_tie():
                self.tie = True
                self.print_winner_message()
            else:
                self.toggle_turn()

    def print_board(self):
        b = self.board
        print(f"""
                A   B   C
            1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
                ----------
            2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
                ----------
            3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

    def play_move(self, spot):
        if spot not in self.board or self.board[spot]:
            return False
        self.board[spot] = self.turn
        return True

    def check_winner(self):
        b = self.board
        win_conditions = [
            ['a1', 'a2', 'a3'], ['b1', 'b2', 'b3'], ['c1', 'c2', 'c3'],  # Rows
            ['a1', 'b1', 'c1'], ['a2', 'b2', 'c2'], ['a3', 'b3', 'c3'],  # Columns
            ['a1', 'b2', 'c3'], ['c1', 'b2', 'a3'] 
        ]
        for condition in win_conditions:
            if b[condition[0]] == b[condition[1]] == b[condition[2]] == self.turn:
                self.winner = self.turn
                return True
        return False

    def check_tie(self):
        return all(self.board[spot] is not None for spot in self.board)

    def toggle_turn(self):
        self.turn = 'O' if self.turn == 'X' else 'X'

    def print_turn_message(self):
        print(f"It's player {self.turn}'s turn!")

    def print_winner_message(self):
        if self.winner:
            print(f"{self.winner} wins the game!")
        elif self.tie:
            print("It's a tie!")

    def get_valid_move(self):
        while True:
            move = input("Enter a valid move (example: A1): ").lower()
            if move in self.board and not self.board[move]:
                return move
            print("Invalid move, please try again.")


game_instance = Game()
game_instance.play_game()


#Note : 
#I have outsourced the question and tried to solve it with the help frindes.