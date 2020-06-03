


class Person:

    name = ''
    surname = ''
    age = 0

    def __init__(self, _name, _surname, _age):
        self.name = _name
        self.surname = _surname
        self.age = _age

    def print_pretty_name(self):
        print('Sig. %s %s (age: %d)' % (self.name, self.surname, self.age))

    def save(self):
        pass


class Student(Person):

    classroom = ''

    def __init__(self, _name, _surname, _age, _classroom):
        super().__init__(_name, _surname, _age)
        self.classroom = _classroom

    def print_pretty_name(self):
        print('from class: %s' % self.classroom)
        super().print_pretty_name()

    def do_homework(self):
        print('zzzzzzzzzz ...')

    def save(self):
        super().save()
        # notfy via email


class Shape():

    def draw(self):
        raise Exception("to be overridden")

    def hide(self):
        raise Exception("to be overridden")

    def move(self):
        self.hide()
        ...
        self.draw()


class Square(Shape):

    size = 0

    def __init__(self, size):
        self.size = size

    def draw(self):
        print("|--------------|")
        print("|              |")
        print("|              |")
        print("|              |")
        print("|              |")
        print("|              |")
        print("|--------------|")

    def hide(self):
        pass


class Rectangle(Shape):

    width = 0
    height = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        print("|-----------------------|")
        print("|                       |")
        print("|                       |")
        print("|                       |")
        print("|                       |")
        print("|                       |")
        print("|-----------------------|")

    def hide(self):
        pass

my_shapes = [
    Square(10),
    Square(20),
    Rectangle(10, 45),
    ...
]

for shape in my_shapes:
    shape.draw()


for i, shape in enumerate(my_shapes):
    if i % 2 == 0:
        shape.move()



mario = Person('Mario', 'Orlandi', 59)
andrea = Student('Andrea', 'Orlandi', 19, "5A")

# mario.do_homework()
# andrea.do_homework()

mario.print_pretty_name()
andrea.print_pretty_name()



# x = 5
# y = 6

# print("x: %d" % x)
# print("y: %d" % y)

