import serial
import os


#cecip est un code correcteur 2 bits sur 16

class rs232_bus:

    def __init__(self) -> None:
        self.rs232 = serial.Serial('/dev/ttyUSB0', 19200, timeout=1)
        self.rs232.open()
        self.test()

    def send(self, data):
        self.rs232.write(data)
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
            self.send("Hello")
            rcv = self.receive()
            print(rcv)
            os.sleep(1)


#class corrector_code:


if __name__ == '__main__':
    uart = rs232_bus()

