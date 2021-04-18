from board import Board

board = [' ']
bd = Board("x", "o", board)
print(bd.generateBoard(board))
while True:
    bd.playerMove(board)
    print(bd.generateBoard(board))
    bd.opponentMove(board)
    print(bd.generateBoard(board))