from komputer import Komputer

class Orang:
    def __init__(self, nama: str, komputer: Komputer):
        self.nama = nama
        self.komputer = komputer

    def get_nama(self):
        return self.nama

    def get_komputer(self):
        return self.komputer
