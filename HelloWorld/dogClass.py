class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof!")

    def introduce(self):
        print(f"Hi! I'm {self.name}, a {self.age}-year-old {self.breed}.")

    def sit(self):
        print(f"{self.name} is now sitting.")

    def run(self):
        print(f"{self.name} is running around!")

    def sleep(self):
        print(f"{self.name} is sleeping... Zzz 😴")

    def eat(self, food):
        print(f"{self.name} is eating {food}. Yum!")

dog1 = Dog("Max", 2, "Belgian")
dog2 = Dog("Nilou", 4, "Maltese")
dog3 = Dog("Luna", 4, "Aspin")



dog2.introduce()
dog2.bark()
dogfood = input("What did your dog eat? ")
dog2.eat(dogfood)
