import java.util.List;

public class Komputer {
    private String nama;
    private Cpu cpu;
    private List<Ram> ramList;
    private Harddrive harddrive;
    private Motherboard motherboard;
    private PowerSupply powerSupply;

    public Komputer(String nama, Cpu cpu, List<Ram> ramList, Harddrive harddrive, Motherboard motherboard, PowerSupply powerSupply) {
        this.nama = nama;
        this.cpu = cpu;
        this.ramList = ramList;
        this.harddrive = harddrive;
        this.motherboard = motherboard;
        this.powerSupply = powerSupply;
    }

    public String getNama() {
        return nama;
    }

    public Cpu getCpu() {
        return cpu;
    }

    public List<Ram> getRamList() {
        return ramList;
    }

    public Harddrive getHarddrive() {
        return harddrive;
    }

    public Motherboard getMotherboard() {
        return motherboard;
    }

    public PowerSupply getPowerSupply() {
        return powerSupply;
    }

    public void setNama(String nama) {
        this.nama = nama;
    }

    public void setCpu(Cpu cpu) {
        this.cpu = cpu;
    }

    public void setRamList(List<Ram> ramList) {
        this.ramList = ramList;
    }

    public void setHarddrive(Harddrive harddrive) {
        this.harddrive = harddrive;
    }

    public void setMotherboard(Motherboard motherboard) {
        this.motherboard = motherboard;
    }

    public void setPowerSupply(PowerSupply powerSupply) {
        this.powerSupply = powerSupply;
    }


    @Override
    public String toString() {
        StringBuilder specs = new StringBuilder("Komputer: " + nama + "\n");
        specs.append("  CPU         : ").append(cpu).append("\n");
        specs.append("  RAM         : ");
        for (Ram ram : ramList) {
            specs.append(ram).append(", ");
        }
        specs.append("\n  Harddrive   : ").append(harddrive).append("\n");
        specs.append("  Motherboard : ").append(motherboard).append("\n");
        specs.append("  Power Supply: ").append(powerSupply).append("\n");
        return specs.toString();
    }
}
