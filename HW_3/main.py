# Создать сет компонентов, и сделать так, чтобы в нем не было 2 одинаковых. (Специально создать два одинаковых компонента в Main и попытаться их добавить в сет)

class Component:
    def __init__(self, name, power):
        self.name = name
        self.power = power
        
    def __eq__(self, other):
        if isinstance(other, Component):
            return self.name == other.name and self.power == other.power
        return False

    def __hash__(self):
        return hash((self.name, self.power))
    
# * Set<Component> result = new HashSet<>(components); (подсказка переопределить методы equals и hashCode).

component1 = Component("component1", 10)
component2 = Component("component2", 20)
component3 = Component("component1", 10)

components = {component1, component2, component3}

print(len(components))

# Переписать compareTo так, чтобы если power лекарств равны, сравнение шло еще и по названиям компонентов лекарства

class Medication:
    def __init__(self, name, components):
        self.name = name
        self.components = components

    def get_power(self):
        return sum([component.power for component in self.components])

    def __lt__(self, other):
        power1 = self.get_power()
        power2 = other.get_power()
        if power1 == power2:
            return self.name < other.name
        return power1 < power2

    def __eq__(self, other):
        return self.name == other.name and self.components == other.components
    
medication1 = Medication('medication1', [component1, component2])
medication2 = Medication('medication2', [component3, component2])
medication3 = Medication('medication3', [component1, component2])

print(medication1 < medication2)  
print(medication1 == medication3)

medications = [medication1, medication2, medication3]
medications_sorted = sorted(medications)

print([medication.name for medication in medications_sorted])  
