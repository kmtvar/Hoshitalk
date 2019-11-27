def new_client_welcome(client, server) :
    with open("new_client_message.txt", "rb") as f :
        server.send_message(client,f.read())

def send_messages(client, server, message) :
    if message == "" :
        pass
    elif message == "--help" :
        with open("options.txt", "rb") as f :
            server.send_message(client,f.read())
    else :
        user_id = f"  <User{client['id']}>"
        server.send_message_to_all_except(message + user_id, client)

def bye_client(client, server) :
    user_left_announcement = f"### User{client['id']} has left ###"
    server.send_message_to_all_except(user_left_announcement, client)
