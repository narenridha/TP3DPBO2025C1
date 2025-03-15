from komponen import Komponen

class Harddrive(Komponen):
    def __init__(self, merk: str, nama: str, tipe_drive: str, kapasitas_gb: int):
        super().__init__(merk, nama)
        self.tipe_drive = tipe_drive
        self.kapasitas_gb = kapasitas_gb

    def get_tipe_drive(self):
        return self.tipe_drive

    def get_kapasitas_gb(self):
        return self.kapasitas_gb
