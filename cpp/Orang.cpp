#pragma once
#include <iostream>
#include "Komputer.cpp"

using namespace std;

class Orang {
private:
    string nama;
    Komputer* komputer;
public:
    Orang(string nama, Komputer* komputer) {
        this->nama = nama;
        this->komputer = komputer;
    }

    void tampilkanInfo() {
        cout << "\nInformasi Pemilik Komputer:\n";
        cout << "Nama Pemilik: " << nama << endl;
        cout << "Komputer yang dimiliki:\n";
        komputer->tampilkanKomponen();
    }

    ~Orang() {
        delete komputer; // Hapus komputer saat orang dihapus
    }
};
