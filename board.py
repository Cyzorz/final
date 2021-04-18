from termcolor import colored

class Style:
    def createColor(board, number, color):
        return colored(board[number], color)

class Board:
    def __init__(self, playerCharacter, opponentCharacter, board):
        self.playerCharacter = playerCharacter
        self.opponentCharacter = opponentCharacter
        self.board = board

    def generateBoard(self, board):
        if not len(board) > 1:
            for i in range(0, 10):
                board.append(' ')
        
        return f"\n {colored('TIC-TAC-TOE', 'magenta')}\n-------------\n| {Style.createColor(board, 1, 'red')} | {Style.createColor(board, 2, 'red')} | {Style.createColor(board, 3, 'red')} |\n-------------\n| {Style.createColor(board, 4, 'red')} | {Style.createColor(board, 5, 'red')} | {Style.createColor(board, 6, 'red')} |\n-------------\n| {Style.createColor(board, 7, 'red')} | {Style.createColor(board, 8, 'red')} | {Style.createColor(board, 9, 'red')} |\n-------------\n"
    
    def playerMove(self, board):
        boardNumber = input(colored("Player One's turn!", "yellow") + "\nPlease enter a number: ")
        if board[int(boardNumber)] != ' ':
            print("Invalid move! Slot is already taken!")
            return False

        board[int(boardNumber)] = self.playerCharacter
    
    def opponentMove(self, board):
        boardNumber = input(colored("Player Two's turn!", "cyan") + "\nPlease enter a number: ")
        if board[int(boardNumber)] != ' ':
            print("Invalid move! Slot is already taken!")
            return False

        board[int(boardNumber)] = self.opponentCharacter        
