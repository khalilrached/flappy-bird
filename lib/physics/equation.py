class Equation:

    def __init__(self, a, b, c, x0=0):
        self.a = a
        self.b = b
        self.c = c
        self.x0 = x0

    def __str__(self):
        return f"<a:{self.a},b:{self.b},c:{self.c},x0:{self.x0}>"

    def call(self, x):
        return self.a * (x - self.x0) * (x - self.x0) + self.b * (x - self.x0) + self.c
