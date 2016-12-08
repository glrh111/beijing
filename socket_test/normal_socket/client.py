import socket

def recieve_message():
    conn = socket.create_connection(('123.56.250.233', 80))
    conn.send(b'GET / HTTP1.1\r\n')
    conn.close()

if __name__ == '__main__':

    recieve_message()