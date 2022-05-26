class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.name = age


buddy = Dog("Jack", 3)
pet = Dog("Jesse", 2)

print("my name is " + str(buddy.name) + " I am an " + buddy.species)
