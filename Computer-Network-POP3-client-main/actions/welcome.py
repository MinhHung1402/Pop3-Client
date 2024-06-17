def welcome(server):
    respone = server.getwelcome()
    print(respone.decode())
    