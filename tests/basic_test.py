#!/usr/bin/env python3

from random import randint
from time import sleep

class CANFrame:
    def __init__(self, header: str, payload: str, interface: str='can0', dlc: int=8):
        self.interface = interface
        self.header = header
        self.dlc = dlc
        self.payload = payload

    def candump_print(self):
        formatted_header = "{:03X}".format(self.header)
        print(f'{self.interface}  {formatted_header}   [{self.dlc}]  {" ".join("{:02X}".format(byte) for byte in self.payload)}', flush=True)
    

def generate_random_frame(dlc=8) -> CANFrame:
    header = randint(0x000, 0xFFF)
    payload = []
    for i in range(0, dlc):
        payload.append(randint(0x00, 0xFF))

    return CANFrame(header=header, payload=payload)

if __name__ == "__main__":
    while True:
        generate_random_frame().candump_print()
        sleep(0.1)
