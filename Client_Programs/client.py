from websocket import create_connection
import threading
import client_funs
import ssl

#print("Set ip address: ")
#server_ip = input("")
server_ip = "127.0.0.1"
server_port = "12345"
server_info = "wss://" + server_ip + ":" + server_port
flag = True

while True :
    try :
        ws = create_connection(server_info,sslopt={"cert_reqs": ssl.CERT_NONE},timeout=0.2)
        break
    except KeyboardInterrupt :
        flag = False
        break
    except :
        pass

if flag == True :
    thread_send = threading.Thread(target=client_funs.client_send, args=(ws,))
    thread_recv = threading.Thread(target=client_funs.client_receive, args=(ws,))
    thread_send.start()
    thread_recv.start()
    while True :
        try :
            thread_send.join(0.5)
            thread_recv.join(0.5)
        except KeyboardInterrupt :
            print("Keyboard Interrupt. Disconnect with the server")
            client_funs.stop = True
            break            
    thread_send.join()
    thread_recv.join()
    ws.close()
else :
    print("Could not connect to the server")
