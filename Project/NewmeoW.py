# List of Dictionary - Global Variable

meow_list = []


# Continue Function


def continueFunc():
    print("Press enter to continue...", end="")
    input()


# Generate Meow ID


def generate_meow_id():
    index = len(meow_list) + 1
    return f"NW{index:03}"


# Function to add new meow


def add_new_meow():
    
    # Name Validation

    name = input("Masukkan Nama Meow (5-30 karakter): ")
    while len(name) < 5 or len(name) > 30:
        print("Nama harus antara 5 dan 30 karakter.")
        name = input("Masukkan Nama Meow (5-30 karakter): ")

    # Meow Type Validation
    
    meow_type = input("Masukkan Tipe Meow (S, N, W): ").upper()
    while meow_type not in ["S", "N", "W"]:
        print("Tipe harus S, N, atau W.")
        meow_type = input("Masukkan Tipe Meow (S, N, W): ").upper()

    # Age Validation

    age = int(input("Masukkan Umur Meow (bulan, minimal 2 bulan): "))
    while age < 2:
        print("Umur harus lebih dari 1 bulan.")
        age = int(input("Masukkan Umur Meow (bulan, minimal 2 bulan): "))

    # Weight Validationn

    weight = float(input("Masukkan Berat Meow (gram, minimal 100 gram): "))
    while weight < 100:
        print("Berat harus lebih dari 99 gram.")
        weight = float(input("Masukkan Berat Meow (gram, minimal 100 gram): "))

    # Description Validation

    description = input("Masukkan Deskripsi Meow (minimal 2 kata): ")
    while len(description.split()) < 2:
        print("Deskripsi harus lebih dari 2 kata.")
        description = input("Masukkan Deskripsi Meow (minimal 2 kata): ")

    # Twin Meow Validation

    is_twin = input("Apakah Meow Kembar? (Yes/No): ").capitalize()
    while is_twin not in ["Yes", "No"]:
        print("Jawaban hanya bisa Yes atau No.")
        is_twin = input("Apakah Meow Kembar? (Yes/No): ").capitalize()

    # Add Data to List

    if is_twin == "Yes":
        for _ in range(2):
            meow_id = generate_meow_id()
            meow_list.append({
                "id": meow_id,
                "name": name,
                "type": meow_type,
                "age": age,
                "weight": weight,
                "description": description
            })
            print(f"Meow baru dengan ID {meow_id} berhasil ditambahkan!")

    else:
        meow_id = generate_meow_id()
        meow_list.append({
            "id": meow_id,
            "name": name,
            "type": meow_type,
            "age": age,
            "weight": weight,
            "description": description
        })
        print(f"Meow baru dengan ID {meow_id} berhasil ditambahkan!")

    continueFunc()


# Function to update Meow


def update_meow():

    meow_id = input("Masukkan Meow ID yang ingin diupdate: ")

    # meow = next((m for m in meow_list if m["id"] == meow_id), None)

    meow = None
    for m in meow_list:
        if m["id"] == meow_id:
            meow = m
            break

    if not meow:
        print("Meow ID tidak ditemukan.")
        return

    # Validate new age

    new_age = int(input("Masukkan Umur baru (bulan, lebih dari 2 bulan dan berbeda dari sebelumnya): "))
    while new_age <= 2 or new_age == meow["age"]:
        print("Umur harus lebih dari 2 bulan dan berbeda dari sebelumnya.")
        new_age = int(input("Masukkan Umur baru (bulan): "))

    # Validate new weight

    new_weight = float(input("Masukkan Berat baru (gram, lebih dari 100 gram dan berbeda dari sebelumnya): "))
    while new_weight <= 100 or new_weight == meow["weight"]:
        print("Berat harus lebih dari 100 gram dan berbeda dari sebelumnya.")
        new_weight = float(input("Masukkan Berat baru (gram): "))

    # Validate new description

    new_description = input("Masukkan Deskripsi baru (minimal 2 kata dan berbeda dari sebelumnya): ")
    while len(new_description.split()) < 2 or new_description == meow["description"]:
        print("Deskripsi harus lebih dari 2 kata dan berbeda dari sebelumnya.")
        new_description = input("Masukkan Deskripsi baru (minimal 2 kata): ")

    # Update data

    meow["age"] = new_age
    meow["weight"] = new_weight
    meow["description"] = new_description

    print(f"Data Meow dengan ID {meow_id} berhasil diupdate!")

    continueFunc()


# Function to delete meow


def delete_meow():

    meow_id = input("Masukkan Meow ID yang ingin dihapus: ")
    
    # meow = next((m for m in meow_list if m["id"] == meow_id), None)

    meow = None
    for m in meow_list:
        if m["id"] == meow_id:
            meow = m
            break

    if not meow:
        print("Meow ID tidak ditemukan.")
        return

    confirm = input(f"Apakah Anda yakin ingin menghapus Meow {meow_id}? (Yes/No): ").capitalize()

    if confirm == "Yes":
        meow_list.remove(meow)
        print(f"Meow dengan ID {meow_id} berhasil dihapus.")
    else:
        print("Penghapusan dibatalkan.")

    continueFunc()


# Function to show the list of Meow


def show_list_of_meows():

    if not meow_list:
        print("No Meow :(")
    else:
        print("Daftar Meow:")
        for meow in meow_list:
            print(f"ID: {meow['id']}, Nama: {meow['name']}, Tipe: {meow['type']}, Umur: {meow['age']} bulan, Berat: {meow['weight']} gram, Deskripsi: {meow['description']}")

    continueFunc()


# Main Function


def main():

    while True:

        print("\n  _   _                                __          __")
        print(" | \ | |                               \ \        / /")
        print(" |  \| | _____      ___ __ ___   ___  __\ \  /\  / / ")
        print(" | . ` |/ _ \ \ /\ / / '_ ` _ \ / _ \/ _ \ \/  \/ /  ")
        print(" | |\  |  __/\ V  V /| | | | | |  __/ (_) \  /\  /   ")
        print(" |_| \_|\___| \_/\_/ |_| |_| |_|\___|\___/ \/  \/    ")

        print ("\n\n=================================================\n\n")

        print("1. Add New Meow")
        print("2. Update Meow")
        print("3. Delete Meow")
        print("4. Show List of Meows")
        print("5. Exit")
        choice = input("Pilih operasi (1-5): ")

        if choice == "1":
            add_new_meow()
        elif choice == "2":
            update_meow()
        elif choice == "3":
            delete_meow()
        elif choice == "4":
            show_list_of_meows()
        elif choice == "5":
            print("Thank you MeowMeow :D\n")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Run the main Function

main()