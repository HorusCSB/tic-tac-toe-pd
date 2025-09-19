import xmlrpc.client

if __name__ == '__main__':
    client  = xmlrpc.client.ServerProxy("http://localhost:8080")
    num = int(input('Digite um numero:'))
    snum = client.sucessor(num)
    print('sucessor de ',num,' = ',snum)