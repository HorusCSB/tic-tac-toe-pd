import xmlrpc.server

def sucessor(x):
    return x+1

if __name__ == '__main__':
    server = xmlrpc.server.SimpleXMLRPCServer(('localhost',8080))
    
    server.register_function(sucessor)
    
    server.serve_forever()
