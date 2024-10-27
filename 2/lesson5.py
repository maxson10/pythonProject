"""
class Cat():
    def __init__(self,breed,color,age):



        self.breed = breed
        self.color = color
        self.age = age

    def say_meow(self):

        return'МЯУ'

    def say_mur(self):
        return'Мур'

cat1 = Cat("Дворовая", "Белый", 5)

cat2 = Cat("Британская", "Серый", 3)

cat1.say_meow()
cat1.say_mur()

class HomCat(Cat):
    def __init__(self,breed,color,age, owner, name):

        super().__init__(breed,color,age)
        self.owner = owner
        self.name = name

    def Breed(self):
        return self.breed
    def Color(self):
        return self.color
    def Owner(self):
        return self.owner
    def Name(self):
        return self.name

h_cat1 = HomCat("Сиамская", "Рыжий", 4, "Хозяин1", "Васька")
h_cat2 = HomCat("Мейн-кун", "Чёрный", 1, "Хозяин2", "Царь")
print (h_cat1.Breed())
print(h_cat1.Color())
print(h_cat1.Owner())
print(h_cat1.Name())
print()
print (h_cat2.Breed())
print(h_cat2.Color())
print(h_cat2.Owner())
print(h_cat2.Name())

print(h_cat1.say_meow())
print(h_cat2.say_mur())

"""

class Posyda():
    def __init__(self,type,color):
        self.color = color
        self.type = type

class HomPosyda(Posyda):
    def __init__(self,color,type,firma):
        super().__init__(type,color)
        self.firma = firma

    def type(self):
        return self.type

    def firma(self):
        return self.firma

posyda1 = Posyda("Чистая", "Белый")
posyda2 = HomPosyda("Черная","Грязная", "Фирма1")

print(posyda1.color)
print(posyda2.firma)