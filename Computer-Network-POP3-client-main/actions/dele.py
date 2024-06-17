def delete(server, message_number):
    
    print(f'Trying to delete message {message_number}')
    
    response = server.dele(message_number)
    
    print(response.decode())