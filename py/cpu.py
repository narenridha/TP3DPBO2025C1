from komponen import Komponen

class Cpu(Komponen):
    def __init__(self, merk: str, nama: str, jumlah_core: int, kecepatan_ghz: float):
        super().__init__(merk, nama)
        self.jumlah_core = jumlah_core
        self.kecepatan_ghz = kecepatan_ghz

    def get_jumlah_core(self):
        return self.jumlah_core

    def get_kecepatan_ghz(self):
        return self.kecepatan_ghz
