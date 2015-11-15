import requests
import socket

r = requests.get("https://api.ipify.org?format=json")
data = r.json()
r = requests.post("http://127.0.0.1:8000/ip/", data)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((data["ip"] , 8888))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]

s.listen(1)

while 1:
    conn, addr = s.accept()
    data = conn.recv(1024)

s.close()
