"""In this project will learn how about inheritance in python
    obb by building a animal sound making thingy
"""
class animal():
    def __init__(self):
        pass

    def make_sound(self):
        sound = "ruble_ruble_ruble!"
        return f"this animal goes:{sound}"

class Dog(animal):
    def __init__(self, name):
        self.name = name
        animal.__init__(self)
    
    def make_sound(self):
        sound = "bark_bark_bark!"
        return sound

dog = Dog("sibi")
print(dog.make_sound())