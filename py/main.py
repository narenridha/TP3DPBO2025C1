from cpu import Cpu
from ram import Ram
from harddrive import Harddrive
from motherboard import Motherboard
from powersupply import PowerSupply
from komputer import Komputer
from orang import Orang
from sekolah import Sekolah

def main():
    # Membuat komputer untuk Lab1 di sekolah
    cpu1 = Cpu("Intel", "Core i7", 8, 3.4)
    ram1 = Ram("Corsair", "Vengeance", 16, "DDR5")
    harddrive1 = Harddrive("Samsung", "Evo", "SSD", 1024)
    motherboard1 = Motherboard("ASRock", "Z390", "ATX", 16)
    power_supply1 = PowerSupply("Corsair", "RM750x", 750)
    komputer1 = Komputer("Lab1", cpu1, [ram1, Ram("Corsair", "Vengeance", 8, "DDR4")], harddrive1, motherboard1, power_supply1)

    # Membuat komputer untuk Lab2 di sekolah
    cpu2 = Cpu("AMD", "Ryzen 5", 6, 3.6)
    ram2 = Ram("G.Skill", "Trident Z", 16, "DDR4")
    harddrive2 = Harddrive("WD", "Blue", "HDD", 2048)
    motherboard2 = Motherboard("MSI", "B450M", "Micro-ATX", 4)
    power_supply2 = PowerSupply("EVGA", "600W", 600)
    komputer2 = Komputer("Lab2", cpu2, [ram2, Ram("G.Skill", "Trident Z", 16, "DDR4")], harddrive2, motherboard2, power_supply2)

    # Membuat sekolah dan menambahkan komputer ke dalamnya
    sekolah = Sekolah("SMK Informatika")
    sekolah.tambah_komputer(komputer1)
    sekolah.tambah_komputer(komputer2)

    # Membuat komputer pribadi untuk orang pertama
    cpu3 = Cpu("Intel", "Core i5", 6, 3.2)
    ram3 = Ram("Kingston", "HyperX", 16, "DDR4")
    harddrive3 = Harddrive("Crucial", "MX500", "SSD", 512)
    motherboard3 = Motherboard("Gigabyte", "B560", "ATX", 32)
    power_supply3 = PowerSupply("Seasonic", "Focus GX", 650)
    komputer3 = Komputer("PC Alex", cpu3, [ram3], harddrive3, motherboard3, power_supply3)

    # Membuat komputer pribadi untuk orang kedua
    cpu4 = Cpu("AMD", "Ryzen 7", 8, 4.0)
    ram4 = Ram("Corsair", "Dominator", 32, "DDR5")
    harddrive4 = Harddrive("Samsung", "Evo", "SSD", 2048)
    motherboard4 = Motherboard("ASUS", "ROG STRIX", "ATX", 64)
    power_supply4 = PowerSupply("EVGA", "SuperNOVA", 750)
    komputer4 = Komputer("PC Brian", cpu4, [ram4, Ram("Corsair", "Dominator", 32, "DDR5")], harddrive4, motherboard4, power_supply4)

    # Membuat dua orang dengan masing-masing satu komputer
    orang1 = Orang("Alex", komputer3)
    orang2 = Orang("Brian", komputer4)

    # Menampilkan informasi sekolah
    print(f"\nSekolah: {sekolah.get_nama()} memiliki {len(sekolah.get_komputer_list())} komputer.")
    for i, komputer in enumerate(sekolah.get_komputer_list(), start=1):
        print(f"\nKomputer {i}: {komputer.get_nama()}")
        print(f"  CPU        : {komputer.get_cpu().get_merk()} {komputer.get_cpu().get_nama()} ({komputer.get_cpu().get_jumlah_core()} Core) ~{komputer.get_cpu().get_kecepatan_ghz()}GHz")
        for ram in komputer.get_ram_list():
            print(f"  RAM        : {ram.get_merk()} {ram.get_nama()} ({ram.get_kapasitas_gb()} GB) {ram.get_ddr()}")
        print(f"  Harddrive  : {komputer.get_harddrive().get_tipe_drive()} {komputer.get_harddrive().get_merk()} {komputer.get_harddrive().get_nama()} ({komputer.get_harddrive().get_kapasitas_gb()} GB)")
        print(f"  Motherboard: {komputer.get_motherboard().get_chipset()} {komputer.get_motherboard().get_merk()} {komputer.get_motherboard().get_nama()} ({komputer.get_motherboard().get_slot_ram()} Slot)")
        print(f"  PowerSupply: {komputer.get_power_supply().get_merk()} {komputer.get_power_supply().get_nama()} ({komputer.get_power_supply().get_wattage()} Watt)")

    # Menampilkan informasi setiap orang dan komputer pribadi mereka
    print(f"\nOrang dan komputer pribadi mereka:")
    for orang in [orang1, orang2]:
        print(f"\nNama: {orang.get_nama()}")
        komputer = orang.get_komputer()
        print(f"  Komputer   : {komputer.get_nama()}")
        print(f"  CPU        : {komputer.get_cpu().get_merk()} {komputer.get_cpu().get_nama()} ({komputer.get_cpu().get_jumlah_core()} Core) ~{komputer.get_cpu().get_kecepatan_ghz()}GHz")
        for ram in komputer.get_ram_list():
            print(f"  RAM        : {ram.get_merk()} {ram.get_nama()} ({ram.get_kapasitas_gb()} GB) {ram.get_ddr()}")
        print(f"  Harddrive  : {komputer.get_harddrive().get_tipe_drive()} {komputer.get_harddrive().get_merk()} {komputer.get_harddrive().get_nama()} ({komputer.get_harddrive().get_kapasitas_gb()} GB)")
        print(f"  Motherboard: {komputer.get_motherboard().get_chipset()} {komputer.get_motherboard().get_merk()} {komputer.get_motherboard().get_nama()} ({komputer.get_motherboard().get_slot_ram()} Slot)")
        print(f"  PowerSupply: {komputer.get_power_supply().get_merk()} {komputer.get_power_supply().get_nama()} ({komputer.get_power_supply().get_wattage()} Watt)")

if __name__ == "__main__":
    main()
