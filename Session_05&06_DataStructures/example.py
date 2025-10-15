students = []

def show_menu():
    print("\n===== MENU =====")
    print("1. Tambah Mahasiswa")
    print("2. Tampilkan Semua")
    print("3. Update Mahasiswa")
    print("4. Hapus Mahasiswa")
    print("5. Keluar")

def insert_student():
    name = input("Nama: ")
    age = int(input("Umur: "))
    major = input("Jurusan: ")
    student = {'name': name, 'age': age, 'major': major}
    students.append(student)
    print("Data berhasil ditambahkan!")

def show_students():
    for i, s in enumerate(students):
        print(f"{i+1}. {s['name']} ({s['age']} tahun) - {s['major']}")

def update_student():
    show_students()
    idx = int(input("Pilih nomor mahasiswa yang ingin diupdate: ")) - 1
    if 0 <= idx < len(students):
        students[idx]['name'] = input("Nama baru: ")
        students[idx]['age'] = int(input("Umur baru: "))
        students[idx]['major'] = input("Jurusan baru: ")
        print("Data berhasil diupdate!")
    else:
        print("Nomor tidak valid!")

def delete_student():
    show_students()
    idx = int(input("Pilih nomor mahasiswa yang ingin dihapus: ")) - 1
    if 0 <= idx < len(students):
        students.pop(idx)
        print("Data berhasil dihapus!")
    else:
        print("Nomor tidak valid!")

while True:
    show_menu()
    choice = input("Pilih menu: ")
    if choice == '1': insert_student()
    elif choice == '2': show_students()
    elif choice == '3': update_student()
    elif choice == '4': delete_student()
    elif choice == '5': break
    else: print("Pilihan tidak valid!")
