from cpu import Cpu
from ram import Ram
from harddrive import Harddrive
from motherboard import Motherboard
from powersupply import PowerSupply

class Komputer:
    def __init__(self, nama: str, cpu: Cpu, ram_list: list, harddrive: Harddrive, motherboard: Motherboard, power_supply: PowerSupply):
        self.nama = nama
        self.cpu = cpu
        self.ram_list = ram_list
        self.harddrive = harddrive
        self.motherboard = motherboard
        self.power_supply = power_supply

    def get_nama(self):
        return self.nama

    def get_cpu(self):
        return self.cpu

    def get_ram_list(self):
        return self.ram_list

    def get_harddrive(self):
        return self.harddrive

    def get_motherboard(self):
        return self.motherboard

    def get_power_supply(self):
        return self.power_supply

    def add_ram(self, ram: Ram):
        self.ram_list.append(ram)
