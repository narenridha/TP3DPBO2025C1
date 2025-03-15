#pragma once
#include <vector>
#include "Komputer.cpp"

class Sekolah {
private:
    string namaSekolah;
    vector<Komputer*> daftarKomputer;
public:
    Sekolah(string nama) {
        this->namaSekolah = nama;
    }

    void tambahKomputer(Komputer* komputer) {
        daftarKomputer.push_back(komputer);
    }

    void tampilkanKomputer() {
        cout << "\nSekolah: " << namaSekolah << " memiliki komputer:\n";
        for (Komputer* k : daftarKomputer) {
            k->tampilkanKomponen();
            cout << "-----------------\n";
        }
    }

    ~Sekolah() {
        for (Komputer* k : daftarKomputer) {
            delete k;
        }
        daftarKomputer.clear();
    }
};
