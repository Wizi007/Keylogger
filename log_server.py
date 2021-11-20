import socket
Host = '192.168.8.104'
port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((Host, port))
s.listen()
c, a = s.accept()
print(a)
while True:
    f = open("log_new.txt", "a")
    data = c.recv(1024).decode("UTF-8")
    print(data)
    f.write(data)
    f.close()
