#include <bits/stdc++.h>
#include "Cpu.cpp"
#include "Ram.cpp"
#include "Harddrive.cpp"
#include "Motherboard.cpp"
#include "PowerSupply.cpp"
#include "Komputer.cpp"
#include "Orang.cpp"
#include "Sekolah.cpp"

using namespace std;

int main() {
    ios::sync_with_stdio(0); cin.tie(0);

    // Membuat komputer untuk seorang individu
    Komputer* pc1 = new Komputer("PC Abdul", 
        Cpu(8, 3.4, "Intel", "Core i7"), 
        { Ram(16, "DDR5", "Corsair", "Vengeance"), Ram(8, "DDR4", "Corsair", "Vengeance") },
        Harddrive(1024, "SSD", "Samsung", "Evo"),
        Motherboard("ASRock", "Z390", "ATX", 16),
        PowerSupply("Corsair", "RM750x", 750)
    );

    Orang orang1("Budi", pc1);
    orang1.tampilkanInfo();

    // Membuat sekolah dan menambahkan komputer
    Sekolah sekolah("SMA Negeri 1");

    Komputer* pc2 = new Komputer("PC Lab 1", 
        Cpu(6, 2.9, "AMD", "Ryzen 5"), 
        { Ram(8, "DDR4", "Kingston", "HyperX") },
        Harddrive(512, "SSD", "Crucial", "MX500"),
        Motherboard("MSI", "B450M", "Micro-ATX", 16),
        PowerSupply("EVGA", "600W Bronze", 600)

    );

    Komputer* pc3 = new Komputer("PC Lab 2", 
        Cpu(4, 3.0, "Intel", "Core i5"), 
        { Ram(16, "DDR5", "G.Skill", "Ripjaws") },
        Harddrive(2048, "HDD", "WD", "Blue"),
        Motherboard("Gigabyte", "B560", "ATX", 32),
        PowerSupply("Seasonic", "Focus GX", 650)
    );

    sekolah.tambahKomputer(pc2);
    sekolah.tambahKomputer(pc3);

    sekolah.tampilkanKomputer();

    return 0;
}
