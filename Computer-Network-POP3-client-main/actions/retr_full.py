def retrieve_full_message(server, message_number):
    print(f'Retrieving full message {message_number}')

    response, lines, octets = server.retr(message_number)

    print(f"Server response: {response.decode()}")

    print("Message content:")
    for line in lines:
        print(line.decode())

    # message_content = '\n'.join(line.decode() for line in lines)
    
    # print(message_content)
