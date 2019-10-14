import socket
import sys
import time
from random import randint

def set_temp(): 
    temp = randint(20, 32)
    return temp

def main():
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = "127.0.0.1"
    port = 2323
    addr = (host, port)
    init_msg = "TIPO: TEMPERATURA"
    try:
        soc.sendto(init_msg.encode(), addr)
    except:
        print("Erro ao enviar mensagem")
    while(True):
        temp = set_temp()
        
        try:
            soc.sendto(temp.encode(), addr)
        except:
            print("Erro ao enviar mensagem")

        time.sleep(60)

sys.exit()
