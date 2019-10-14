import socket
import sys

status_lampada = "APAGADA"

def acender_lampada():
    status_lampada = "ACESA"

def apagar_lampada():
    status_lampada = "APAGADA"

def main():
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = "127.0.0.1"
    port = 2323
    addr = (host, port)
    init_msg = "TIPO: LAMPADA"
    try:
        soc.sendto(init_msg.encode(), addr)
    except:
        print("Erro ao enviar mensagem")
    while(True):
        try:
            solicitacao, addrServidor = soc.recvfrom(2048)
            solicitacao = solicitacao.decode()
        except:
            print("Mensagem não recebida")

        if(solicitacao == "APAGAR"):
            apagar_lampada()
        elif(solicitacao == "ACENDER"):
            acender_lampada()

        soc.sendto(status_lampada.encode(), addr)

sys.exit()