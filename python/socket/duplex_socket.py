"""
socket全双工实现
"""
import sys
import threading
import socket
import time


class Mysocket(object):
    def __init__(self, ip='127.0.0.1', port=6666):
        self.bind_ip = ip
        self.bind_port = port
        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((self.bind_ip, self.bind_port))
            s.listen(10)
        except socket.error as msg:
            print(msg)
            sys.exit(1)
        print('Waiting connection...')

        while 1:
            conn, addr = s.accept()
            '''
            <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 6666), raddr=('127.0.0.1', 64871)> 
            ('127.0.0.1', 64871)
            '''
            print("one client joined")

            tr = threading.Thread(target=self.deal_data, args=(conn, addr))
            ts = threading.Thread(target=self.send_msg, args=(conn,))
            tr.start()
            ts.start()
            ts.join()

    def deal_data(self, conn,addr):
        # print(conn, addr)
        print('Accept new connection from {0}'.format(addr))
        conn.send("Hi, Welcome to the server".encode())
        while 1:
            data = conn.recv(1024)
            print('{0} client send data is {1}'.format(addr, data.decode()))
            time.sleep(1)
            if data.decode() == 'exit' or not data:
                print('{0} connection close'.format(addr))
                conn.send(bytes('Connection closed', 'UTF-8'))
                break
            # conn.send(bytes('Hello, {0}'.format(data), 'UTF-8'))
        conn.close()

    def send_msg(self,conn):
        while 1:
            data = input('please input work: ').encode()
            conn.send(data)
            if data == 'exit':
                break
        conn.close()

if __name__ == '__main__':
    test = Mysocket()
