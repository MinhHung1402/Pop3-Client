import poplib
from email.parser import Parser

def get_msg_content(server, message_number):
    response, message_lines, octets = server.retr(message_number)
        
    # Convert message lines from bytes to a list of strings
    message_lines = [line.decode('utf-8') for line in message_lines]
        
    # Join the message lines into a single string
    message_data = '\n'.join(message_lines)
    
    # Parse the email message
    email_parser = Parser()
    msg = email_parser.parsestr(message_data)
    
    # Extract the content of the email (plaintext part)
    content = ""
    for part in msg.walk():
        content_type = part.get_content_type()
        if "text/plain" in content_type:
            content += part.get_payload()
    
    print(f"Content of message {message_number}:")
    print(content)