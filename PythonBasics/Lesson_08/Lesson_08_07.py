class Complex(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return Complex(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        return Complex(self.a * other.a - self.b * other.b, self.b * other.a + self.a * other.b)

    def __truediv__(self, other):
        return Complex((self.a * other.a + self.b * other.b) / (other.a * other.a + other.b * other.b),
                       (self.b * other.a - self.a * other.b) / (other.a * other.a + other.b * other.b))

    def __str__(self):
        return '(%s+%sj)' % (self.a, self.b)


my_complex = Complex(1, 2)
tru_complex = complex(1, 2)
print(my_complex)
print(tru_complex)

my_complex = my_complex + Complex(1, 2)
tru_complex = tru_complex + complex(1, 2)
print(my_complex)
print(tru_complex)

my_complex = my_complex * Complex(1, 2)
tru_complex = tru_complex * complex(1, 2)
print(my_complex)
print(tru_complex)

my_complex = my_complex / Complex(1, 2)
tru_complex = tru_complex / complex(1, 2)
print(my_complex)
print(tru_complex)
