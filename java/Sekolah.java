import java.util.ArrayList;
import java.util.List;

public class Sekolah {
    private String nama;
    private List<Komputer> komputerList;

    public Sekolah(String nama) {
        this.nama = nama;
        this.komputerList = new ArrayList<>();
    }

    public void tambahKomputer(Komputer komputer) {
        komputerList.add(komputer);
    }

    public String getNama() {
        return nama;
    }

    public List<Komputer> getKomputerList() {
        return komputerList;
    }

    public void setNama(String nama) {
        this.nama = nama;
    }

    public void setKomputerList(List<Komputer> komputerList) {
        this.komputerList = komputerList;
    }

    public void tampilkanInfo() {
        System.out.println("=== Info Sekolah ===");
        System.out.println("Nama Sekolah: " + nama);
        System.out.println("Jumlah Komputer: " + komputerList.size());
        for (Komputer komputer : komputerList) {
            System.out.println(komputer);
        }
    }
}
