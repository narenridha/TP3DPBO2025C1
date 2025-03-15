public class Motherboard extends Komponen {
    private String chipset;
    private int slotRam;

    public Motherboard(String merk, String nama, String chipset, int slotRam) {
        super(merk, nama);
        this.chipset = chipset;
        this.slotRam = slotRam;
    }

    public String getChipset() {
        return chipset;
    }

    public int getSlotRam() {
        return slotRam;
    }

    public void setChipset(String chipset) {
        this.chipset = chipset;
    }

    public void setSlotRam(int slotRam) {
        this.slotRam = slotRam;
    }

    @Override
    public String toString() {
        return super.toString() + " | Chipset: " + chipset + " | Slot RAM: " + slotRam;
    }
}
