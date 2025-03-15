from komponen import Komponen

class PowerSupply(Komponen):
    def __init__(self, merk: str, nama: str, wattage: int):
        super().__init__(merk, nama)
        self.wattage = wattage

    def get_wattage(self):
        return self.wattage
