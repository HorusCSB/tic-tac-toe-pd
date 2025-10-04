import xmlrpc.client

def printBoard(board):
    print()
    for row in board:
        print(row)
    print()

if __name__ == '__main__':
    client = xmlrpc.client.ServerProxy("http://localhost:8080")
    name = input("insira seu nome:")
    playerId, playerName = client.connect(name)
    
    if playerId == -1:
        print(playerName)
        exit()
        
    print(f"Você é: {playerName}")

    while True:
        vencedor = client.checkWinStatus()
        if vencedor:
            print(vencedor)
            printBoard(client.getBoard())
            break
        
        currentPlayer = client.getCurrentTurn()
        printBoard(client.getBoard())
        print(f"Vez de: {currentPlayer}")
        
        if currentPlayer == playerName:
            while True:
                try:
                    jogada = input("Digite linha,coluna (ex: 0,2): ")
                    linha, coluna = map(int, jogada.split(","))

                    playResponse = client.playerTurn(linha, coluna, playerId)

                    if "sucesso" in playResponse:
                        break
                except:
                    exit()


