def rset(server):
    print('Resetting the session')
    response = server.rset()

    print(response.decode())