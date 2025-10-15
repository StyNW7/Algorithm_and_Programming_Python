import os
import random

# Membaca atau membuat file car_list.txt

file_name = 'car_list.txt'
car_list = []

# Read File

if os.path.exists(file_name): # if we want to create a new file

# if (file_name):
    with open(file_name, 'r') as file:

        # Read all lines

        lines = file.readlines()

        # Append each line

        for line in lines:

            line = line.strip()

            if line:

                name, car_type, year, brand, price = line.split('#')
                car_list.append({
                    "name": name,
                    "type": car_type,
                    "year": int(year),
                    "brand": brand,
                    "price": int(price)
                })

else:

    with open(file_name, 'w') as file:
        pass  # Creating new file


# Function to display or printing menu


def display_menu():

    print("\nLamburgher Showroom")
    print("1. Add Car")
    print("2. View Cars")
    print("3. Delete Car")
    print("4. Exit")


# Function to add new caar


def add_car():

    # Name

    while True:
        name = input("Enter car name (5–12 characters): ").strip()
        if 5 <= len(name) <= 12:
            break
        print("Invalid name. Must be between 5–12 characters.")

    # Car Type
    
    while True:
        car_type = input("Enter car type (SUV, Sedan, Sport): ").strip()
        if car_type in ["SUV", "Sedan", "Sport"]:
            break
        print("Invalid car type. Must be 'SUV', 'Sedan', or 'Sport'.")
    
    # Year

    while True:
        try:
            year = int(input("Enter car year (1800–2024): ").strip())
            if 1800 <= year <= 2024:
                break
        except ValueError:
            pass
        print("Invalid year. Must be between 1800–2024.")
    
    # Car Brand

    while True:
        brand = input("Enter car brand (≥3 alphabetic characters): ").strip()
        if len(brand) >= 3 and brand.isalpha():
            break
        print("Invalid brand. Must be at least 3 alphabetic characters.")
    
    # Determine the car constant

    type_constants = {"SUV": 300, "Sedan": 500, "Sport": 600}
    damage = random.randint(500, 1000)
    price = damage * type_constants[car_type]
    
    car_list.append({
        "name": name,
        "type": car_type,
        "year": year,
        "brand": brand,
        "price": price
    })

    print(f"Car '{name}' added successfully!")



# Function to display cars


def view_cars():

    if not car_list:
        print("There's no car available.")
        return
    
    # sorted_cars = sorted(car_list, key=lambda x: x["year"])
    sorted_cars = car_list.sort(key=lambda x: x["year"])
    print("\nList of Cars:")

    # for idx, car in enumerate(sorted_cars, 1):
    #     print(f"{idx}. {car['name']} ({car['type']}, {car['year']}, {car['brand']}) - ${car['price']}")

    index = 1
    for car in sorted_cars:
        print(f"{index}. {car['name']} ({car['type']}, {car['year']}, {car['brand']}) - ${car['price']}")
        index += 1


# Function to delete car


def delete_car():

    if not car_list:
        print("There's no car available.")
        return
    
    view_cars()

    while True:
        try:
            car_idx = int(input("Enter car number to delete: ").strip())
            if 1 <= car_idx <= len(car_list):
                break
        except ValueError:
            pass
        print("Invalid input. Please enter a valid car number.")
    
    removed_car = car_list.pop(car_idx - 1)
    print(f"Car '{removed_car['name']}' has been removed.")


# Function to save and exit


def save_and_exit():

    with open(file_name, 'w') as file:
        for car in car_list:
            line = f"{car['name']}#{car['type']}#{car['year']}#{car['brand']}#{car['price']}\n"
            file.write(line)
    print("Data saved. Exiting program.")

    exit()


# Main Program


while True:

    display_menu()

    choice = input("Choose a menu (1–4): ").strip()

    if choice == "1":
        add_car()
    elif choice == "2":
        view_cars()
    elif choice == "3":
        delete_car()
    elif choice == "4":
        save_and_exit()
    else:
        print("Invalid choice. Please choose between 1–4.")
