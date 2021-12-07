import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 6999))
while True:
    res = input("请输入需要发送的信息:")
    client.send(res.encode("utf-8"))
client.close()
