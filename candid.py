#!/usr/bin/env python3

import sys
import yaml
import importlib

class CandidInstance:
    def __init__(self, filename):
        self.callbacks = {}
        self.filename = filename
        self.mappings = self.load_mappings()
        self.devices = self.mappings.keys()
        self.load_callbacks()

    def load_mappings(self):
        with open(self.filename, 'r') as file:
            return yaml.safe_load(file)
        
    def load_callbacks(self):
        for device in self.devices:
            cb_handle = self.mappings[device]['callback']
            cb_module = importlib.import_module(f'callbacks.{cb_handle}') 
            cb_function = getattr(cb_module, cb_handle)
            self.callbacks[device] = cb_function


class CANFrame:
    def __init__(self, header: str='0', payload: str='0', interface: str='can0', dlc: int=8):
        self.interface = interface
        self.header = header
        self.dlc = dlc
        self.payload = payload

    def from_candump_line(self, buff):
        buff_split = buff.split()
        self.interface = buff_split[0].strip()
        self.header = buff_split[1]                                 # 3 byte header in hex
        self.dlc = int(buff_split[2].strip('[]'), 10)                           # int in dec
        self.payload = [int(byte, 16) for byte in buff_split[3:(self.dlc + 3)]] # dlc number of payload bytes in hex

    def candump_printout(self):
        formatted_header = "{:03X}".format(self.header)
        print(f'{self.interface}  {formatted_header}   [{self.dlc}]  {" ".join("{:02X}".format(byte) for byte in self.payload)}', flush=True)


def main():
    candid = CandidInstance('mappings/user_mappings.yaml')

    while True:
        buff = sys.stdin.readline()
        cdl = CANFrame()
        cdl.from_candump_line(buff)
        if cdl.header in candid.devices:
            candid.callbacks[cdl.header](cdl.payload)

if __name__ == "__main__":
    main()
