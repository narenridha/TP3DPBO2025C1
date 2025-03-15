# TP3DPBO2025C1
#** Desain Program **
![image](https://github.com/user-attachments/assets/9a28096f-db01-4a4a-8bf6-1d025a3cc2ff)
## **Desain Sistem Komputer di Sekolah**  

Proyek ini merupakan implementasi dari sistem yang merepresentasikan hubungan antara berbagai entitas dalam sebuah lingkungan sekolah, terutama dalam hal kepemilikan dan struktur perangkat komputer. Desain ini menggunakan konsep **Object-Oriented Programming (OOP)** dengan pendekatan **inheritance (pewarisan)** dan **composition (komposisi)** untuk membangun sistem yang fleksibel dan modular.  

---

## 🏛 **Struktur Desain**  

Sistem ini terdiri dari beberapa kelas utama:  

### 1️⃣ **Sekolah** 🏫  
   - Memiliki banyak **komputer** yang digunakan oleh siswa dan staf.  
   - Mengelola daftar komputer yang tersedia di sekolah.  
   - Tidak memiliki hubungan langsung dengan **Orang** dalam desain ini.  

### 2️⃣ **Orang** 👤  
   - Setiap orang (misalnya siswa atau staf) memiliki **satu** komputer pribadi.  
   - Bisa mengatur atau mendapatkan komputer yang dimilikinya.  

### 3️⃣ **Komputer** 🖥  
   - Sebuah komputer terdiri dari beberapa komponen utama:  
     - **CPU** ⚙️  
     - **RAM** 💾 (bisa lebih dari satu)  
     - **Harddrive** 💽  
     - **Motherboard** 🖧  
     - **PowerSupply** 🔋  

### 4️⃣ **Komponen (Abstract Class)** 🔩  
   - Merupakan kelas induk untuk semua jenis komponen perangkat keras (hardware).  
   - Kelas ini tidak bisa diinstansiasi secara langsung, tetapi menyediakan atribut dasar seperti **merek** dan **nama produk** untuk semua komponen yang diwarisi darinya.  
   - Kelas turunannya adalah:
     - **CPU**  
     - **RAM**  
     - **Harddrive**  
     - **Motherboard**  
     - **PowerSupply**  

---

## **Konsep Inheritance (Pewarisan) & Composition (Komposisi)**  

### **1. Inheritance (Pewarisan)**  

Konsep **inheritance (pewarisan)** digunakan untuk membangun hubungan **"is-a"** antara kelas. Dalam desain ini, **Komponen** berperan sebagai **kelas induk (parent class)** yang diwarisi oleh beberapa **kelas anak (subclass)** yang lebih spesifik, yaitu **CPU, RAM, Harddrive, Motherboard, dan PowerSupply**.  

**Mengapa menggunakan inheritance?**  
✔️ Menghindari duplikasi kode dengan menyimpan atribut dasar di kelas induk.  
✔️ Memudahkan pengembangan jika di masa depan ada tambahan komponen lain.  
✔️ Memungkinkan polimorfisme jika diperlukan di tahap pengembangan lebih lanjut.  

**Contoh dalam kode:**
```cpp
class Komponen {
protected:
    string merk;
    string nama;
public:
    Komponen(string merk, string nama) : merk(merk), nama(nama) {}
    string getMerk() { return merk; }
    string getNama() { return nama; }
};
```
Kemudian, kelas seperti **CPU, RAM, Harddrive, Motherboard, dan PowerSupply** akan **mewarisi** atribut dari `Komponen`:

```cpp
class Cpu : public Komponen {
private:
    int jumlahCore;
    float kecepatanGHz;
public:
    Cpu(string merk, string nama, int jumlahCore, float kecepatanGHz)
        : Komponen(merk, nama), jumlahCore(jumlahCore), kecepatanGHz(kecepatanGHz) {}
};
```
👉 Dari contoh di atas, `Cpu` **"is-a"** `Komponen`, sehingga tidak perlu mendeklarasikan kembali atribut `merk` dan `nama`, karena sudah diwarisi dari `Komponen`.

---

### **2. Composition (Komposisi)**  

Konsep **composition (komposisi)** digunakan untuk membangun hubungan **"has-a"** antara kelas, yaitu ketika suatu objek **terdiri dari** objek lain. Dalam desain ini, beberapa contoh **komposisi** adalah:  

✅ **Sekolah memiliki banyak komputer**  
✅ **Orang memiliki satu komputer**  
✅ **Komputer memiliki CPU, RAM (bisa lebih dari satu), Harddrive, Motherboard, dan PowerSupply**  

**Mengapa menggunakan composition?**  
✔️ Memastikan bahwa objek yang lebih kompleks (misalnya Komputer) tidak bisa ada tanpa komponen-komponennya.  
✔️ Memungkinkan hubungan yang lebih realistis, misalnya **CPU bukanlah subclass dari Komputer, melainkan bagian dari Komputer**.  
✔️ Membantu dalam pengelolaan memori, karena objek yang lebih besar dapat dikelola melalui agregasi dari objek-objek kecil.  

**Contoh dalam kode:**
```cpp
class Komputer {
private:
    string nama;
    Cpu cpu;
    vector<Ram> ramList;
    Harddrive harddrive;
    Motherboard motherboard;
    PowerSupply powerSupply;
public:
    Komputer(string nama, Cpu cpu, vector<Ram> ramList, Harddrive harddrive, Motherboard motherboard, PowerSupply powerSupply)
        : nama(nama), cpu(cpu), ramList(ramList), harddrive(harddrive), motherboard(motherboard), powerSupply(powerSupply) {}
};
```
👉 Dari contoh di atas:  
- **Komputer memiliki** (`has-a`) `Cpu`, `Ram`, `Harddrive`, `Motherboard`, dan `PowerSupply`.  
- **Komputer tidak mewarisi Komponen**, karena **bukan** bagian dari hierarki inheritance `Komponen`.  
- **RAM diwakili sebagai `vector<Ram>`**, karena sebuah komputer dapat memiliki lebih dari satu RAM.  

---

## **Kesimpulan**  

- **Inheritance** digunakan untuk membangun hubungan **"is-a"**, di mana `CPU, RAM, Harddrive, Motherboard, dan PowerSupply` adalah bagian dari `Komponen`.  
- **Composition** digunakan untuk membangun hubungan **"has-a"**, seperti `Komputer memiliki CPU, RAM, Harddrive, Motherboard, dan PowerSupply`.  
- Desain ini fleksibel untuk dikembangkan lebih lanjut, seperti menambahkan jenis komponen baru atau memperluas fitur sekolah dan orang.  
