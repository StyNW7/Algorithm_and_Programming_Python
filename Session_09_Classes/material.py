class Mahasiswa:
    def __init__(self, nama, usia, jurusan):
        self.nama = nama
        self.usia = usia
        self.jurusan = jurusan

    def perkenalan(self):
        print(f"Halo, nama saya {self.nama}, saya berusia {self.usia} tahun, dan saya jurusan {self.jurusan}.")


class BankAccount:
    def __init__(self, nama, saldo):
        self.nama = nama
        self.__saldo = saldo  # Atribut private

    def tambah_saldo(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"{jumlah} telah ditambahkan ke akun {self.nama}.")
        else:
            print("Jumlah harus positif!")

    def cek_saldo(self):
        return self.__saldo


# Membuat objek Mahasiswa
mhs1 = Mahasiswa("Alice", 20, "Informatika")
mhs1.perkenalan()

# Membuat objek BankAccount
akun = BankAccount("Alice", 1000)
akun.tambah_saldo(500)
print(f"Saldo saat ini: {akun.cek_saldo()}")
