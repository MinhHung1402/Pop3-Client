def list(server):
    response, listings, octets = server.list()

    print(response.decode())

    for listings in listings:
        msg_num, size = listings.decode('utf-8').split()
        print(f'Message {msg_num} is {size} octets')
    print(f'Total size: {octets} octets')