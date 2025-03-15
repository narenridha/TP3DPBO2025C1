#pragma once
#include "Komponen.cpp"

class Motherboard : public Komponen {
private:
    string chipset;
    int slotRam;
public:
    Motherboard() {}

    Motherboard(string merk, string nama, string chipset, int slotRam) 
        : Komponen(merk, nama), chipset(chipset), slotRam(slotRam) {}

    void setChipset(string chipset) {
        this->chipset = chipset;
    }

    void setSlotRam(int slotRam) {
        this->slotRam = slotRam;
    }

    string getChipset() {
        return chipset;
    }

    int getSlotRam() {
        return slotRam;
    }

    ~Motherboard() {}
};