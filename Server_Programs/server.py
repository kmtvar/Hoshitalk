from websocket_server import WebsocketServer
import server_funs

port = 12345
ip_addr = '127.0.0.1'

server = WebsocketServer(port,host=ip_addr)
server.set_fn_new_client(server_funs.new_client_welcome)
server.set_fn_message_received(server_funs.send_messages)
server.set_fn_client_left(server_funs.bye_client)
server.run_forever()
