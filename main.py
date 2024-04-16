from fractions import gcd

class Rational:
    def __init__(self, num, den):
        if den == 0:
            raise ValueError("Denominator cannot be zero")
        common = gcd(num, den)
        self.num = num // common
        self.den = den // common

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self, other):
        if isinstance(other, Rational):
            new_num = self.num * other.den + other.num * self.den
            new_den = self.den * other.den
            return Rational(new_num, new_den)
        elif isinstance(other, int):
            return Rational(self.num + other * self.den, self.den)
        else:
            raise TypeError("Unsupported operand type for +")

class RationalList:
    def __init__(self, elements=[]):
        self.elements = []
        for element in elements:
            if not isinstance(element, Rational):
                raise TypeError("Elements of RationalList must be instances of Rational")
            self.elements.append(element)

    def __str__(self):
        return '[' + ', '.join(map(str, self.elements)) + ']'

    def __getitem__(self, index):
        return self.elements[index]

    def __setitem__(self, index, value):
        if not isinstance(value, Rational):
            raise TypeError("Elements of RationalList must be instances of Rational")
        self.elements[index] = value

    def __len__(self):
        return len(self.elements)

    def __add__(self, other):
        if isinstance(other, RationalList):
            new_elements = self.elements + other.elements
            return RationalList(new_elements)
        elif isinstance(other, (int, Rational)):
            new_elements = self.elements + [other]
            return RationalList(new_elements)
        else:
            raise TypeError("Unsupported operand type for +")

    def __iadd__(self, other):
        if isinstance(other, RationalList):
            self.elements += other.elements
        elif isinstance(other, (int, Rational)):
            self.elements.append(other)
        else:
            raise TypeError("Unsupported operand type for +=")
        return self

# Приклад використання
r1 = Rational(1, 2)
r2 = Rational(3, 4)
r3 = Rational(5, 6)

list1 = RationalList([r1, r2])
list2 = RationalList([r3])

print("List 1:", list1)
print("List 2:", list2)

# Додавання списків
combined_list = list1 + list2
print("Combined list:", combined_list)

# Додавання числа до списку
combined_list += Rational(7, 8)
print("Combined list after addition:", combined_list)

# Зчитування елемента списку за індексом
print("Element at index 0:", combined_list[0])

# Зміна елемента списку за індексом
combined_list[0] = Rational(9, 10)
print("Combined list after modification:", combined_list)

# Визначення кількості елементів у списку
print("Length of combined list:", len(combined_list))

# Знайдіть суму послідовності чисел.
sum_of_list = Rational(0, 1)
for rational in combined_list:
    sum_of_list += rational
print("Sum of the sequence:", sum_of_list)
