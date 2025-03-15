public class Orang {
    private String nama;
    private Komputer komputer;

    public Orang(String nama, Komputer komputer) {
        this.nama = nama;
        this.komputer = komputer;
    }

    public String getNama() {
        return nama;
    }

    public Komputer getKomputer() {
        return komputer;
    }

    public void setNama(String nama) {
        this.nama = nama;
    }

    public void setKomputer(Komputer komputer) {
        this.komputer = komputer;
    }

    public void tampilkanInfo() {
        System.out.println("=== Info Orang ===");
        System.out.println("Nama: " + nama);
        System.out.println(komputer);
    }
}
