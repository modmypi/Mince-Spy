from tropi import TroPi
import socket

tropi = TroPi()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(('', 9050))
sock.listen(1)
connection, client_address = sock.accept()
try:
    while True:
        data = connection.recv(128)
        print(data)
        if data:
            if data.decode() == 'True':
                tropi.SetAllColours(255,0,0)
            elif data.decode() == 'False':
                tropi.SetAllColours(0,0,0)
        else:
            break
finally:
    connection.close()
