public class Harddrive extends Komponen {
    private String tipeDrive;
    private int kapasitasGB;

    public Harddrive(String merk, String nama, String tipeDrive, int kapasitasGB) {
        super(merk, nama);
        this.tipeDrive = tipeDrive;
        this.kapasitasGB = kapasitasGB;
    }

    public String getTipeDrive() {
        return tipeDrive;
    }

    public int getKapasitasGB() {
        return kapasitasGB;
    }

    public void setTipeDrive(String tipeDrive) {
        this.tipeDrive = tipeDrive;
    }

    public void setKapasitasGB(int kapasitasGB) {
        this.kapasitasGB = kapasitasGB;
    }

    @Override
    public String toString() {
        return super.toString() + " | " + tipeDrive + " | " + kapasitasGB + " GB";
    }
}
