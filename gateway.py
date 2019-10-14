from socket import *

def main():
    host = ''
    port = 2323
    soc = socket(AF_INET, SOCK_DGRAM)
    soc.bind((host, port))

    while(True):
        print('oi')


