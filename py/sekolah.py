from komputer import Komputer

class Sekolah:
    def __init__(self, nama: str):
        self.nama = nama
        self.komputer_list = []

    def get_nama(self):
        return self.nama

    def tambah_komputer(self, komputer: Komputer):
        self.komputer_list.append(komputer)

    def get_komputer_list(self):
        return self.komputer_list
