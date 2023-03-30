# Создать класс Doctor. Создайте интерфейсы Runnable, Flyable, Swimable. У интерфейсов должны быть
# методы получения скорости заданного действия.
# Добавьте наследников этим интерфейсам, но таким образом,
# чтобы у каждого интерфейса было минимум по два наследника (при необходимости, добавьте в приложение новые классы)
# У ветеринарной клиники добавьте методы получения всех бегающих, всех плавающих, всех говорящих и всех летающих и вообще всех животных.
# Постарайтесь максимально логично переписать архитектуру проекта.

class Animal:
    def __init__(self, name):
        self.name = name

class Runnable:
    def get_speed(self):
        pass

class Quadruped(Animal, Runnable):
    def get_speed(self):
        pass

class Bipeds(Animal, Runnable):
    def get_speed(self):
        pass

class Swimable:
    def get_speed(self):
        pass

class Fish(Animal, Swimable):
    def get_speed(self):
        pass

class Dolphin(Animal, Swimable):
    def get_speed(self):
        pass

class Flyable:
    def get_speed(self):
        pass

class Bird(Animal, Flyable):
    def get_speed(self):
        pass

class Insect(Animal, Flyable):
    def get_speed(self):
        pass

class Talkable:
    def talk(self):
        pass

class Cat(Animal, Talkable):
    def talk(self):    
        pass

class Dog(Animal, Talkable):
    def talk(self):
        pass

class Doctor:
    def __init__(self):
        self.animals = []

    def getAllRunners(self):
        runners = []
        for animal in self.animals:
            if isinstance(animal, Runnable):
                runners.append(animal)
        return runners

    def getAllSwimmers(self):
        swimmers = []
        for animal in self.animals:
            if isinstance(animal, Swimable):
                swimmers.append(animal)
        return swimmers

    def getAllFlying(self):
        flying = []
        for animal in self.animals:
            if isinstance(animal, Flyable):
                flying.append(animal)
        return flying

    def getAllTalking(self):
        talking = []
        for animal in self.animals:
            if isinstance(animal, Talkable):
                talking.append(animal)
        return talking

    def getAllAnimals(self):
        return self.animals