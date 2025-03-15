public class Cpu extends Komponen {
    private int jumlahCore;
    private double kecepatanGHz;

    public Cpu(String merk, String nama, int jumlahCore, double kecepatanGHz) {
        super(merk, nama);
        this.jumlahCore = jumlahCore;
        this.kecepatanGHz = kecepatanGHz;
    }

    public int getJumlahCore() {
        return jumlahCore;
    }

    public double getKecepatanGHz() {
        return kecepatanGHz;
    }

    public void setJumlahCore(int jumlahCore) {
        this.jumlahCore = jumlahCore;
    }

    public void setKecepatanGHz(double kecepatanGHz) {
        this.kecepatanGHz = kecepatanGHz;
    }

    @Override
    public String toString() {
        return super.toString() + " | " + jumlahCore + " core | " + kecepatanGHz + " GHz";
    }
}
