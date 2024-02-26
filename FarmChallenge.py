class Animal:
    def __init__(self, name, age, colour, sound, type, height, health, hunger, stomach, favfood):
        self.name = name
        self.age = age
        self.colour = colour
        self.sound = sound
        self.type = self.__class__.__name__
        self.height = height
        self.health = health
        self.hunger = hunger
        self.stomach = stomach
        self.favfood = favfood
    def description(self):
        print(f"I am %s, a %s that is %s years old and %s. I am %s and make a sound: '%s'. My favourite food is %s" % (self.name, self.type, self.age, self.height, self.colour, self.sound, self.favfood))
    def fullness(self):
        if(self.stomach > 10):
            print("I feel sick")
            if(self.health > 1):
                self.health = self.health-1
            else:
                print("You have died")
        elif(self.stomach < self.hunger):
            print("I am hungry")
            self.stomach = self.stomach-3
        else:
            print("I am neither hungry nor too full")
            self.stomach = self.stomach-2
    def makeSound(self):
        print(self.sound)
    def eat(self):
        print("I am eating my favourite food which is %s" %(self.favfood))
        self.stomach +1

class GroundAnimal(Animal):
    def __init__(self, name, age, colour, sound, type, height, health, hunger, stomach, favfood):
        super().__init__(name, age, colour, sound, type, height, health, hunger, stomach, favfood)
class FlyingAnimal(Animal):
    def __init__(self, name, age, colour, sound, type, height, health, hunger, stomach, wings, favfood):
        self.wings = wings
        super().__init__(name, age, colour, sound, type, height, health, hunger, stomach, favfood)

class Dog(GroundAnimal):
    def __init__(self, name, age, colour, sound, type, height, health, hunger, stomach):
        super().__init__(name, age, colour, sound, type, height, health, hunger, stomach, "bones")

class Sheep(GroundAnimal):
    def __init__(self, name, age, colour, sound, type, height, health, hunger, stomach):
        super().__init__(name, age, colour, sound, type, height, health, hunger, stomach, "grass")

class Pig(GroundAnimal):
    def __init__(self, name, age, colour, sound, type, height, health, hunger, stomach):
        super().__init__(name, age, colour, sound, type, height, health, hunger, stomach, "slop")

class Horse:
    def __init__(self, name, age, colour, sound, type, height, health, hunger, stomach):
        super().__init__(name, age, colour, sound, type, height, health, hunger, stomach, "haybales")

class Duck(FlyingAnimal):
    def __init__(self, name, age, colour, sound, type, height, health, hunger, stomach, wings):
        super().__init__(name, age, colour, sound, type, height, health, hunger, stomach, wings, "crumbs")

class FlyingCow(FlyingAnimal, GroundAnimal):
    def __init__(self, name, age, colour, sound, type, height, health, hunger, stomach, wings):
        super().__init__(name, age, colour, sound, type, height, health, hunger, stomach, wings, "grass")
    def overTheMoon(self):
        print(f"I am using my magnificient cow %s to fly over the moon" % (self.wings))

specialCow = FlyingCow("Ted", 2, "Black and White", "MOOOOOOOOOO", None, "6'5", 100, 11, 10, "high speed wings")
specialCow.description()
print(specialCow.health)
print(specialCow.stomach)
specialCow.fullness()
print(specialCow.health)
print(specialCow.stomach)