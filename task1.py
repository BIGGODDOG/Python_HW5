# Задание 1
# Реализуйте класс «Автомобиль». Необходимо хранить
# в полях класса: название модели, год выпуска, производителя, объем двигателя, цвет машины, цену. Реализуйте
# методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса. 

class Car:
    def __init__(self, model, year, manufacturer, engine_volume, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_volume = engine_volume
        self.color = color
        self.price = price

    def input_data(self):
        self.model = input("Введите название модели: ")
        self.year = int(input("Введите год выпуска: "))
        self.manufacturer = input("Введите производителя: ")
        self.engine_volume = float(input("Введите объем двигателя: "))
        self.color = input("Введите цвет машины: ")
        self.price = float(input("Введите цену: "))

    def display_data(self):
        print(f"Модель: {self.model}")
        print(f"Год выпуска: {self.year}")
        print(f"Производитель: {self.manufacturer}")
        print(f"Объем двигателя: {self.engine_volume} л")
        print(f"Цвет: {self.color}")
        print(f"Цена: {self.price} у.е.")

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_manufacturer(self):
        return self.manufacturer

    def get_engine_volume(self):
        return self.engine_volume

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price

car = Car("Car", 2023, "Toyota", 1.6, "Black", 1243)
print("\nДанные об автомобиле:")
car.display_data()
car.input_data()
print("\nИзменённые данные об автомобиле:")
car.display_data()

print(f"Название: {car.get_model()}")
print(f"Год выпуска: {car.get_year()}")
print(f"Производитель: {car.get_manufacturer()}")
print(f"Объем двигателя: {car.get_engine_volume()}")
print(f"Цвет: {car.get_color()}")
print(f"Цена: {car.get_price()}")