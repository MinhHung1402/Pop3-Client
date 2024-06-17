def top(server, message_number, num_lines):
    
    print(f'Retrieving headers and first {num_lines} lines of message {message_number}')

    response, lines, octets = server.top(message_number, num_lines)

    print(f"Server response: {response.decode()}")

    #print message content lines
    
    print("Message content:")
    for line in lines:
        print(line.decode())

    # Print octets (size of the message)
    print(f"Octets: {octets} bytes")
    print()