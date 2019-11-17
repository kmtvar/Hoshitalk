def new_client_welcome(client, server) :
    server.send_message(client,"Welcome to HoshiTalk.")

def send_messages(client, server, message) :
    server.send_message_to_all_except(message, client)

