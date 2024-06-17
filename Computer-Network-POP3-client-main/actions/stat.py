def stat(server):
    print('Fetching mailbox status')

    response = server.stat()
    #The number of messages in the mailbox
    print(f"Number of messages: {response[0]}")
    
    #The total size of the mailbox in bytes.
    print(f"Total size: {response[1]} bytes")