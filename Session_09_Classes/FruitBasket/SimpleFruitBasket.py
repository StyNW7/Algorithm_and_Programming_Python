class FruitBasket:
    
    def __init__(self):
        self.fruits = []

    def add_fruit(self, fruit):
        self.fruits.append(fruit)

    def remove_fruit(self, fruit):
        if fruit in self.fruits:
            self.fruits.remove(fruit)

    def display_fruits(self):
        return self.fruits

    def find_fruit(self, fruit):
        return fruit in self.fruits

    def total_fruits(self):
        return len(self.fruits)

basket = FruitBasket()
basket.add_fruit("Apple")
basket.add_fruit("Banana")
basket.add_fruit("Mango")
print("Fruits: ", basket.display_fruits())
basket.remove_fruit("Apple")
print("Fruits after deletion: ", basket.display_fruits());
print("Find Banana: ", basket.find_fruit("Banana"))
print("Find Cherry: ", basket.find_fruit("Cherry"))
print("Fruits: ", basket.display_fruits())
print("Total of fruits: ", basket.total_fruits())