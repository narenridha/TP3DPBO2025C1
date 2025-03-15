from komponen import Komponen

class Ram(Komponen):
    def __init__(self, merk: str, nama: str, kapasitas_gb: int, ddr: str):
        super().__init__(merk, nama)
        self.kapasitas_gb = kapasitas_gb
        self.ddr = ddr

    def get_kapasitas_gb(self):
        return self.kapasitas_gb

    def get_ddr(self):
        return self.ddr
