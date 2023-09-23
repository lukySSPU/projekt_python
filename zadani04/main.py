class Rectangle:
    # Atributy na úrovni třídy
    count = 0  # Počet vytvořených objektů třídy Rectangle
    total_area = 0  # Celková plocha všech obdélníků

    def __init__(self, width, height):
        # Atributy na úrovni objektu
        self.width = width
        self.height = height
        self.area = width * height

        # Zvýšení počtu objektů třídy Rectangle a celkové plochy
        Rectangle.count += 1
        Rectangle.total_area += self.area

    def __str__(self):
        return f"Obdélník o šířce {self.width} a výšce {self.height}"

    def __eq__(self, other):
        # Porovnání obdélníků podle jejich plochy
        return self.area == other.area

    def __lt__(self, other):
        # Porovnání obdélníků podle jejich plochy
        return self.area < other.area

    def __add__(self, other):
        # Sčítání obdélníků vytvoří nový obdélník se součtem jejich ploch
        new_width = self.width + other.width
        new_height = self.height + other.height
        return Rectangle(new_width, new_height)

    def __mul__(self, scalar):
        # Násobení obdélníku skalárem zvětší jeho plochu
        new_width = self.width * scalar
        new_height = self.height * scalar
        return Rectangle(new_width, new_height)

    @staticmethod
    def print_count():
        # Statická metoda pro výpis počtu vytvořených objektů třídy
        print(f"Celkový počet vytvořených objektů třídy Rectangle: {Rectangle.count}")

    @classmethod
    def average_area(cls):
        # Metoda třídy pro výpočet průměrné plochy obdélníků
        return cls.total_area / cls.count

# Vytvoření několika objektů třídy Rectangle
rect1 = Rectangle(5, 10)
rect2 = Rectangle(3, 7)
rect3 = Rectangle(4, 8)

# Výpis informací o objektech
print(rect1)
print(rect2)
print(rect3)

# Porovnání objektů podle plochy
print("rect1 == rect2:", rect1 == rect2)
print("rect1 < rect2:", rect1 < rect2)
print("rect1 > rect2:", rect1 > rect2)

# Sčítání obdélníků
rect4 = rect1 + rect2
print("Sčítání obdélníků:", rect4)

# Násobení obdélníku skalárem
rect5 = rect1 * 3
print("Násobení obdélníku:", rect5)

# Použití statické metody pro výpis počtu objektů
Rectangle.print_count()

# Použití metody třídy pro výpočet průměrné plochy obdélníků
avg_area = Rectangle.average_area()
print(f"Průměrná plocha obdélníků: {avg_area}")
