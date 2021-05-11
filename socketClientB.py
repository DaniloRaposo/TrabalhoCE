import socket

serverMACAddress = '00:E0:4C:23:BC:06'
port = 3
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((serverMACAddress,port))
while i in ["1","2","3","4","5","6","7","8","9","10"]:
    text = i
    s.send(bytes(text, 'UTF-8'))
s.close()