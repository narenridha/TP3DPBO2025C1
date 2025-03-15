#pragma once
#include <iostream>
#include <string>
#include <vector>
#include "Cpu.cpp"
#include "Harddrive.cpp"
#include "Ram.cpp"
#include "Motherboard.cpp"
#include "PowerSupply.cpp"


using namespace std;


class Komputer
{
private:
    string nama;
    Cpu cpu;
    vector<Ram> ramList;
    Harddrive harddrive;
    Motherboard motherboard;
    PowerSupply powerSupply;
public:
    Komputer()
    {


    }


    Komputer(string nama, Cpu cpu, vector<Ram> ramList, Harddrive harddrive, Motherboard motherboard, PowerSupply powerSupply)
    {
        this->nama = nama;
        this->cpu = cpu;
        this->ramList = ramList;
        this->harddrive = harddrive;
        this->motherboard = motherboard;
        this->powerSupply = powerSupply;
    }


    void setNama(string nama)
    {
        this->nama = nama;
    }

    void setCpu(Cpu cpu)
    {
        this->cpu = cpu;
    }


    void setRam(vector<Ram> ramList)
    {
        this->ramList = ramList;
    }    
   
    void setHarddrive(Harddrive harddrive)
    {
        this->harddrive = harddrive;
    }


    void addRam(Ram ram)
    {
        this->ramList.push_back(ram);
    }

    void setMotherboard(Motherboard motherboard)
    {
        this->motherboard = motherboard;
    }

    void setPowerSupply(PowerSupply powerSupply)
    {
        this->powerSupply = powerSupply;
    }


    string getNama()
    {
        return this->nama;
    }


    Cpu getCpu()
    {
        return this->cpu;
    }


    vector<Ram> getRamList() // return vector
    {
        return this->ramList;
    }


    Harddrive getHarddrive()
    {
        return this->harddrive;
    }

    Motherboard getMotherboard()
    {
        return this->motherboard;
    }

    PowerSupply getPowerSupply()
    {
        return this->powerSupply;
    }

    void tampilkanKomponen() {
        cout << "Nama        : " << nama << endl;
        cout << "Cpu         : " << cpu.getMerk() << ' ' << cpu.getNama() << " (" << cpu.getJumlahCore() << " Core) ~" << cpu.getKecepatanGHz() << "GHz" << endl;
        for (Ram& ram : ramList) {
            cout << "Ram         : " << ram.getMerk() << ' ' << ram.getNama() << " (" << ram.getKapasitasGB() << " GB) " << ram.getDdr() << endl;
        }
        cout << "Harddrive   : " << harddrive.getTipeDrive() << ' ' << harddrive.getMerk() << ' ' << harddrive.getNama() << " (" << harddrive.getKapasitasGB() << " GB) " << endl;
        cout << "Motherboard : " << motherboard.getMerk() << ' ' << motherboard.getNama() << ' ' << motherboard.getNama() << " (" << motherboard.getSlotRam() << " Slot) " << endl;
        cout << "PowerSupply : " << powerSupply.getMerk() << ' ' << powerSupply.getNama() << " (" << powerSupply.getWattage() << " Watt) " << endl;
    }
    

    ~Komputer()
    {


    }
};
