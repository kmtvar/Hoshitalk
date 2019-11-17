import sys
import select

stop = False

def unix_input_with_timeout(prompt='', timeout=10000):
    sys.stdout.write(prompt)
    sys.stdout.flush()
    (ready, _, _) = select.select([sys.stdin], [], [], timeout)
    if ready :
        return sys.stdin.readline().rstrip('\n')
    else :
        raise TimeoutOccurred

def client_send(ws) :
    while not stop :
        try :
            messages = unix_input_with_timeout(prompt="",timeout=0.2)
            ws.send(messages)
        except :
            pass

def client_receive(ws) :
    while not stop :
        try :
            messages = ws.recv()
            print(messages)
        except :
            pass
