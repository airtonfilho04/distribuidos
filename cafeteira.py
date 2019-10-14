import socket
import sys
import time
from random import randint

status_cafeteira = ["EM ESPERA", "PREPARANDO", "CAFÉ PRONTO"]

def main():
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = "127.0.0.1"
    port = 2323
    addr = (host, port)
    init_msg = "TIPO: CAFETEIRA"
    try:
        soc.sendto(init_msg.encode(), addr)
    except:
        print("Erro ao enviar mensagem")
    
    while(True):
        status = status_cafeteira[randint(0, 2)]
        
        try:
            soc.sendto(status.encode(), addr)
        except:
            print("Erro ao enviar mensagem")

        time.sleep(60)

sys.exit()