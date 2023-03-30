#Добавить в класс Animal методы двигаться(toGo), летать(fly), плавать(swim). Создать по два класса наследника Animal, умеющих летать, плавать, бегать. В файле readme.md в репозитории github (или ему подобных) описать какие проблемы в таком проектировании Вы увидели, там же написать возникшие при выполнении дз вопросы (если они есть). P.S. Подумать и сделать так, чтобы классы, не умеющие летать, в итоговом коде летать не должны, не плавающие - не плавать, итд

#Класс Animal:
class Animal:
    def toGo(self):
        pass

    def fly(self):
        pass

    def swim(self):
        pass

#Класс наследника, умеющий летать, бегать и плавать:
class FlyingAnimal(Animal):
    def toGo(self):
        print("Крыльями махать")

    def fly(self):
        print("Умеет летать")

    def swim(self):
        print("Умеет плавать")

#class RunningAnimal(Animal):
    def toGo(self):
        print("Бежать")

    def fly(self):
        pass

    def swim(self):
        print("Умеет плавать")