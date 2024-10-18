# Задание 3
# Реализуйте класс «Стадион». Необходимо хранить в
# полях класса: название стадиона, дату открытия, страну,
# город, вместимость. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.

class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def input_data(self):
        self.name = input("Введите название стадиона: ")
        self.opening_date = input("Введите дату открытия: ")
        self.country = input("Введите страну: ")
        self.city = input("Введите город: ")
        self.capacity = int(input("Введите вместимость: "))

    def display_data(self):
        print(f"Название стадиона: {self.name}")
        print(f"Дата открытия: {self.opening_date}")
        print(f"Страна: {self.country}")
        print(f"Город: {self.city}")
        print(f"Вместимость: {self.capacity}")

    def get_name(self):
        return self.name

    def get_opening_date(self):
        return self.opening_date

    def get_country(self):
        return self.country

    def get_city(self):
        return self.city

    def get_capacity(self):
        return self.capacity

stadium = Stadium("Great Stadium", "16.03.2002", "Kazakhstan", "Astana", 15000)
print("\nДанные о стадионе:")
stadium.display_data()
stadium.input_data() 
print("\nИзменённые данные о стадионе:")
stadium.display_data()

print("\nДоступ к отдельным полям:")
print(f"Название стадиона: {stadium.get_name()}")
print(f"Дата открытия: {stadium.get_opening_date()}")
print(f"Страна: {stadium.get_country()}")
print(f"Город: {stadium.get_city()}")
print(f"Вместимость: {stadium.get_capacity()}")