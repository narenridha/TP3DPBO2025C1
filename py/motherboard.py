from komponen import Komponen

class Motherboard(Komponen):
    def __init__(self, merk: str, nama: str, chipset: str, slot_ram: int):
        super().__init__(merk, nama)
        self.chipset = chipset
        self.slot_ram = slot_ram

    def get_chipset(self):
        return self.chipset

    def get_slot_ram(self):
        return self.slot_ram
