class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def detail(self):
        print(self.name, "is studying")

p = Person(name="Joe", age=34, gender="male")
p.detail()
