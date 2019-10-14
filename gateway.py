from socket import *

def main():
    host = ''
    port = 2323
    soc = socket(AF_INET, SOCK_DGRAM)
    soc.bind((host, port))

    while(True):
        msg, addrCliente = soc.recvfrom(2048)
        msg = msg.decode()
        print(msg, addrCliente)

if __name__ == '__main__':
    main()

