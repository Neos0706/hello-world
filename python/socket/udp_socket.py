import sys
import socket
import threading



def recvData(udp_socket):
    while 1:
        recv_data = udp_socket.recvfrom(1024)
        print('\n<<%s:%s>>' % (str(recv_data[1]), recv_data[0].decode('utf-8')))


def sendData(udp_socket,dest_ip, dest_port):
    while 1:
        send_data = input('>>')
        udp_socket.sendto(send_data.encode(), (dest_ip, dest_port))



def main(port=7788):
    try:
        udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        # bind 本地的端口
        udp_socket.bind(('', port))

    except socket.error as msg:
        print(msg)
        sys.exit(1)

    dest_ip = input('请输入对方的ip')
    dest_port = int(input('请输入对方的port'))

    tr = threading.Thread(target=recvData, args=(udp_socket, ))
    ts = threading.Thread(target=sendData, args=(udp_socket, dest_ip,dest_port))
    tr.start()
    ts.start()



if __name__ == '__main__':
    if len(sys.argv) == 2:
        port = sys.argv[1]
        main(int(port))
    else:
        main()


