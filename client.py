import xmlrpc.client

def printBoard(board):
    print()
    for row in board:
        print(row)
    print()

if __name__ == '__main__':
    client = xmlrpc.client.ServerProxy("http://localhost:8080")
    name = input("Insira seu nome: ")
    playerId, playerName = client.connect(name)
    
    if playerId == -1:
        print(playerName)
        exit()
        
    print(f"Você é: {playerName}")

    while True:
        estado = client.getGameState()
        board = estado['board']
        currentPlayer = estado['currentTurn']
        vencedor = estado['status']

        printBoard(board)

        if vencedor:
            print(f"fim: {vencedor}")
            break
        
        print(f"Vez de: {currentPlayer}")
        
        if currentPlayer == playerName:
            while True:
                try:
                    jogada = input("Digite linha,coluna (ex: 0,2): ")
                    linha, coluna = map(int, jogada.split(","))

                    playResponse = client.playerTurn(linha, coluna, playerId)
                    print(playResponse)

                    if "sucesso" in playResponse:
                        break
                except Exception as e:
                    print(e)
                    exit()
