class FruitBasket:

    def __init__(self):

        """Konstruktor untuk membuat objek FruitBasket dengan daftar buah kosong."""

        self.fruits = []

    def add_fruit(self, fruit):

        """
        Menambahkan buah ke dalam keranjang.
        :param fruit: Nama buah yang akan ditambahkan (str)
        """

        if not isinstance(fruit, str) or not fruit.strip():
            print("Nama buah harus berupa string yang valid!")
            return
        self.fruits.append(fruit.strip().capitalize())
        print(f"'{fruit}' berhasil ditambahkan ke keranjang.")

    def remove_fruit(self, fruit):

        """
        Menghapus buah dari keranjang.
        :param fruit: Nama buah yang akan dihapus (str)
        """

        fruit = fruit.strip().capitalize()
        if fruit in self.fruits:
            self.fruits.remove(fruit)
            print(f"'{fruit}' berhasil dihapus dari keranjang.")
        else:
            print(f"'{fruit}' tidak ditemukan di keranjang.")

    def display_fruits(self):

        """Menampilkan semua buah yang ada di keranjang."""

        if not self.fruits:
            print("Keranjang kosong.")

        else:
            print("Buah-buahan dalam keranjang:")

            i = 1
            for fruit in self.fruits:
                print(f"{i}. {fruit}")
                i+=1
            
            # for i, fruit in enumerate(self.fruits, 1):
            #     print(f"{i}. {fruit}")

    def find_fruit(self, fruit):

        fruit = fruit.strip().capitalize()
        if fruit in self.fruits:
            print(f"Find '{fruit}': True")
        else:
            print(f"Find '{fruit}': False")
    

    def total_fruits(self):

        self.display_fruits()
        print (f"Total buah: {len(self.fruits)}")


# Implementasi program untuk mengelola keranjang buah

def continueFunc():
    
    print("Press enter to continue...", end="")
    input()

# if __name__ == "__main__":

basket = FruitBasket()

while True:

    print("\n=== Fruit Basket Menu ===")
    print("1. Tambah Buah")
    print("2. Hapus Buah")
    print("3. Cari Buah")
    print("4. Tampilkan Total Buah")
    print("5. Tampilkan Semua Buah")
    print("6. Keluar")
    
    choice = input("Pilih menu (1-6): ")
    
    if choice == "1":
        fruit_name = input("Masukkan nama buah yang ingin ditambahkan: ")
        basket.add_fruit(fruit_name)
        continueFunc()

    elif choice == "2":
        fruit_name = input("Masukkan nama buah yang ingin dihapus: ")
        basket.remove_fruit(fruit_name)
        continueFunc()

    elif choice == "3":
        fruit_name = input("Masukkan nama buah yang ingin dicari: ")
        basket.find_fruit(fruit_name)
        continueFunc()

    elif choice == "4":
        basket.total_fruits()
        continueFunc()

    elif choice == "5":
        basket.display_fruits()
        continueFunc()

    elif choice == "6":
        print("Terima kasih telah menggunakan sistem Fruit Basket!")
        break

    else:
        print("Pilihan tidak valid, coba lagi.")
