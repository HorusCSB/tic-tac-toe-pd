player = ['','']

currentPlayer = 'name'
win = False
emptySpaces = 9

board = []

allowedPlays = [0,1,2]

def createEmptyTicTacToe():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]

def start():
    global player
    global currentPlayer
    global board
    global emptySpaces
    global win

    player[0] = input("insira o nome do jogador 1:")
    player[1] = input("insira o nome do jogador 2:")
    currentPlayer = player[0]
    emptySpaces = 9
    win = False

    board = createEmptyTicTacToe()

def checkWin():
    global board
    global win
    global emptySpaces
    global currentPlayer
    global player
    if (board[0][0] == board[1][1] == board[2][2]) and board[0][0] != None:
        win = True
        return
    for n in board:
        if (n[0] == n[1] == n[2]) and n[0] != None:
            win = True
            return
    if emptySpaces == 0: 
        win = 'tie'
        return
    currentPlayer = player[1] if currentPlayer == player[0] else player[0]

def playerTurn():
    global currentPlayer
    global emptySpaces
    global board
    while True:
        linha = input("digite a linha (0,1,2):")
        coluna = input("digite a coluna (0,1,2):")
        if int(linha) not in allowedPlays or int(coluna) not in allowedPlays:
            print("Por favor, escolha um valor válido!")
        if (board[int(linha)][int(coluna)] != None):
            print("Esta posição já foi preenchida, tente novamente!")
        else:
            break
    board[int(linha)][int(coluna)] = currentPlayer
    emptySpaces -= 1
    checkWin()
    print(board)


def main():
    start()
    while win == False and win != 'tie':
        playerTurn()
    if(win == 'tie'):
        print("Empate!")
    print(currentPlayer,"venceu!")
if __name__ == "__main__":
    main()

