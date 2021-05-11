import socket
import sys
import time

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.connect((HOST, PORT))

    i = 0
    while i < 10:
        f1 = open("pages/form.html",'r')
        f2 = open("pages/form2.html", 'r')

        html = (f1.read() + f2.read()).encode()

        time1 = time.perf_counter() # metodo que retorna o tempo em segundos
        s.send(html)
        data = s.recv(2048)

        time2 = time.perf_counter()

        print("Bandwidth = {}".format(sys.getsizeof(data)/(time2 - time1)))

        i = i + 1
        f1.close()
        f2.close()
