from socket import *
HOST = 'localhost'
PORT = 9999

client = socket(AF_INET, SOCK_STREAM)
client.bind((HOST,PORT))

client.listen()
c,addr = client.accept()
while True:
    try:
        text = input('>')
        if text == "quit":
            break
        c.send((text+'\n').encode('utf-8'))
    except BrokenPipeError:
        print('Connection closed...')
        break

client.close()
