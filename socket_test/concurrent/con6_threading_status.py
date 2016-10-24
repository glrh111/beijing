from socket import socket, AF_INET, SOCK_STREAM
import threading
from functools import partial

class LazyConnection:

    def __init__(self, address, family=AF_INET, ltype=SOCK_STREAM):
        self.address = address
        self.family = family
        self.ltype = ltype
        self.local = threading.local()

    def __enter__(self):
        if hasattr(self.local, 'sock'):
            raise RuntimeError('Already connected')
        self.local.sock = socket(self.family, self.ltype)
        self.local.sock.connect(self.address)
        return self.local.sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.local.sock.close()
        del self.local.sock

def test(conn):
    with conn as s:
        print 'Entering'
        s.send(b'GET / HTTP/1.1\r\n')
        s.send(b'Host: www.glrh11.com\r\n')
        s.send(b'\r\n')
        resp = b''.join(iter(partial(s.recv, 8192), b''))
    print 'Got {} bytes'.format(len(resp))
    print resp

if __name__ == '__main__':
    conn = LazyConnection(('www.glrh11.com', 80))
    t1 = threading.Thread(target=test, args=(conn,))
    t2 = threading.Thread(target=test, args=(conn,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
