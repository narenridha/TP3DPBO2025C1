import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        // Membuat komputer untuk Lab1 di sekolah
        Komputer lab1 = new Komputer("Lab1",
                new Cpu("Intel", "Core i7", 8, 3.4),
                Arrays.asList(new Ram("Corsair", "Vengeance", 16, "DDR5")),
                new Harddrive("Samsung", "Evo", "SSD", 1024),
                new Motherboard("ASRock", "Z390", "ATX", 16),
                new PowerSupply("Corsair", "RM750x", 750)
        );

        // Membuat komputer untuk Lab2 di sekolah
        Komputer lab2 = new Komputer("Lab2",
                new Cpu("AMD", "Ryzen 7", 8, 3.6),
                Arrays.asList(new Ram("Kingston", "Fury", 32, "DDR4")),
                new Harddrive("Seagate", "Barracuda", "HDD", 2048),
                new Motherboard("MSI", "B450M", "Micro-ATX", 4),
                new PowerSupply("Cooler Master", "MWE 650", 650)
        );

        // Membuat sekolah dan menambahkan komputer
        Sekolah sekolah = new Sekolah("SMK Teknologi");
        sekolah.tambahKomputer(lab1);
        sekolah.tambahKomputer(lab2);

        // Membuat komputer pribadi untuk seorang individu
        Komputer pcAlex = new Komputer("PC Alex",
                new Cpu("AMD", "Ryzen 5", 6, 3.6),
                Arrays.asList(new Ram("G.Skill", "Trident Z", 16, "DDR4")),
                new Harddrive("WD", "Blue", "HDD", 2048),
                new Motherboard("Gigabyte", "B560", "ATX", 4),
                new PowerSupply("EVGA", "600W", 600)
        );

        Orang alex = new Orang("Alex", pcAlex);

        // Menampilkan informasi
        sekolah.tampilkanInfo();
        alex.tampilkanInfo();
    }
}
