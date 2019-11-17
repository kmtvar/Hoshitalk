from websocket_server import WebsocketServer
import server_funs

port = 12345
ip_addr = '192.168.0.12'

server = WebsocketServer(port,host=ip_addr)
server.set_fn_new_client(server_funs.new_client_welcome)
server.set_fn_message_received(server_funs.send_messages)
server.run_forever()
