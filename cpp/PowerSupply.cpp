#pragma once
#include "Komponen.cpp"

class PowerSupply : public Komponen {
private:
    int wattage;
public:
    PowerSupply() {}

    PowerSupply(string merk, string nama, int wattage) 
        : Komponen(merk, nama), wattage(wattage) {}

    void setWattage(int wattage) {
        this->wattage = wattage;
    }

    int getWattage() {
        return wattage;
    }

    ~PowerSupply() {}
};
