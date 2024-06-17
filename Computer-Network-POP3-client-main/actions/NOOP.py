def noop(server):

    response = server.noop().decode('utf-8')
    
    print(f"NOOP response: {response}")
