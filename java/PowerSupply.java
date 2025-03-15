public class PowerSupply extends Komponen {
    private int wattage;

    public PowerSupply(String merk, String nama, int wattage) {
        super(merk, nama);
        this.wattage = wattage;
    }

    public int getWattage() {
        return wattage;
    }

    public void setWattage(int wattage) {
        this.wattage = wattage;
    }

    @Override
    public String toString() {
        return super.toString() + " | " + wattage + "W";
    }
}
