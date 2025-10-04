import xmlrpc.server

##### ----------- variáveis globais do jogo (jogadores, jogador atual, status do jogo, espaços em branco, tabuleiro, quantidade de jogadores conectados, jogadas permitidas no terminal)
player = ['', '']
currentPlayerIndex = 0
win = False
emptySpaces = 9
board = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]
playersConnected = 0

allowedPlays = [0, 1, 2]

##### ----------- regras do jogo da velha
def getBoard():
    return board

def getCurrentTurn():
    if playersConnected < 2:
        return "aguardando o segundo jogador..."
    if win:
        return "fim"
    return player[currentPlayerIndex]

def checkWin():
    global win, emptySpaces

    if emptySpaces == 0 and not win:
        win = 'tie'
        print("empate!")
        return

    # diagonal 1
    if (board[0][0] == board[1][1] == board[2][2]) and board[0][0] is not None:
        win = True
        print(f"vitória: {board[0][0]}")
        return

    # diagonal 2
    if (board[0][2] == board[1][1] == board[2][0]) and board[0][2] is not None:
        win = True
        print(f"vitória: {board[0][2]}")
        return

    # linhas
    for x in board:
        if (x[0] == x[1] == x[2]) and x[0] is not None:
            win = True
            print(f"vitória: {x[0]}")
            return

    # colunas
    for y in range(3):
        if (board[0][y] == board[1][y] == board[2][y]) and board[0][y] is not None:
            win = True
            print(f"vitória: {board[0][y]}")
            return


def playerTurn(linha, coluna, playerId):
    global board, emptySpaces, currentPlayerIndex, player, playersConnected, allowedPlays

    print(f"jogada: {player[playerId]}, ({linha}, {coluna})")

    if linha not in allowedPlays or coluna not in allowedPlays:
        print("fora do tabuleiro.")
        return "jgoda inválida! valores permitidos: [0, 1, 2]."

    if board[linha][coluna] is not None:
        print("posição ocupada")
        return "jogada inválida, casa preenchida"

    board[linha][coluna] = player[playerId]
    emptySpaces -= 1
    checkWin()

    if not win:
        currentPlayerIndex = 1 - currentPlayerIndex
        print(f"turno de: {player[currentPlayerIndex]}.")
    else:
        print("----------------")
        print("fim de jogo")

    return "sucesso"

def checkWinStatus():
    if win == 'tie':
        return "empate!"
    elif win:
        return f"{player[currentPlayerIndex]} venceu!"
    return False

##### ----------- operações de servidor
def connect(name):
    global playersConnected
    if playersConnected < 2:
        playerId = playersConnected
        playersConnected += 1
        player[playerId] = name
        print(f"jogador conectado: {player[playerId]}, id: {playerId}")
        return playerId, f"{player[playerId]}"
    return -1, "sala cheia"

if __name__ == '__main__':
    # Inicializa os nomes dos jogadores para exibição
    server = xmlrpc.server.SimpleXMLRPCServer(('localhost', 8080), allow_none=True)

    print("rodando")

    server.register_function(connect)
    server.register_function(getBoard)
    server.register_function(getCurrentTurn)
    server.register_function(playerTurn)
    server.register_function(checkWinStatus)

    server.serve_forever()
