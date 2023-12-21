# Task 1
class Dish:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price}$: {self.description}"

class MenuCategory:
    def __init__(self, name, dishes):
        self.name = name
        self.dishes = dishes

    def __str__(self):
        category_content = "\n".join([str(dish) for dish in self.dishes])
        return f"Категория {self.name}:\n{category_content}"

dish1 = Dish("Паста", "Спагетти с соусом болоньезе", 12)
dish2 = Dish("Салат", "Свежий овощной салат", 8)
dish3 = Dish("Десерт", "Тирамису", 6)

category1 = MenuCategory("Горячие блюда", [dish1])
category2 = MenuCategory("Салаты", [dish2])
category3 = MenuCategory("Десерты", [dish3])

print(category1)
print(category2)
print(category3)

# Task 2

class MenuCategory:
    def __init__(self, name, dishes):
        self.name = name
        self.dishes = dishes

    def __str__(self):
        category_content = "\n".join([str(dish) for dish in self.dishes])
        return f"Категория {self.name}:\n{category_content}"

if __name__ == "__main__":
    dish1 = Dish("Паста", "Спагетти с соусом болоньезе", 12)
    dish2 = Dish("Салат", "Свежий овощной салат", 8)
    dish3 = Dish("Десерт", "Тирамису", 6)

    category1 = MenuCategory("Горячие блюда", [dish1, dish2, dish3])

    print(category1)
