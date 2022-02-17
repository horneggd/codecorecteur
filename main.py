import serial
from time import sleep 


#cecip est un code correcteur 2 bits sur 16

class rs232_bus:

    def __init__(self) -> None:
        self.rs232 = serial.Serial('/dev/ttyUSB0', 19200)
        # self.rs232.open()
        self.test()

    def send(self, data):
        self.rs232.write(data.encode())
    # todo envoyer data a travers la laison série

    def receive(self):
        rcv = self.rs232.readline()
        return rcv
    # recevoir les données

    def insert_errore_in_byte(self, nberror, byte):
        pass
    # inserer les erreur

    def verify(self, data_send, data_receive):
        pass
    # checker que la donnée recu et la donné envoyé est la meme

    def test(self):
        while(1):
            self.send("Hello\n")
            rcv = self.receive()
            print(rcv)
            sleep(1)
            


class corrector_code:

    def xor(self, byte):
        res = 0
        while(byte != 0):
            res ^= byte & 1
            byte >>= 1
        return (res & 1) 

    def encode(self, data):
        g1 = 0x4f
        g2 = 0x6d
        buff = 0
        encode_out = []
        for i in range(0, len(data)):
            buff_in = data(1)
            buff_out = 0
            for j in data:
                buff += buff_in & 0x01
                buff_out <<= 1
                buff_out += self.xor(buff & g1)
                buff_out <<= 1
                buff_out = ~self.xor(buff_out^(buff & g2)) & 0x01
                buff <<= 1
                buff_in >>= 1
            encode_out.append(buff_out >> 8)
            encode_out.append(buff_out & 0x00ff)
        return encode_out

        #ici la fonction qui encode se que tu veux envoyer

    def decode():
        #ici retourne la le text apres decodage
        pass
        

if __name__ == '__main__':
    uart = rs232_bus()

