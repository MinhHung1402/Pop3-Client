def quit(server):
    print('Trying to shut down the connection')

    response = server.quit()

    print(response.decode())