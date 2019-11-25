def new_client_welcome(client, server) :
    with open("new_client_message.txt", "rb") as f :
        server.send_message(client,f.read())

def send_messages(client, server, message) :
    if message == "--help" :
        with open("options.txt", "rb") as f :
            server.send_message(client,f.read())
    else :
        server.send_message_to_all_except(message, client)

