class Dog:
    # you can create vars inside the class at the top
    dogs = []

    def __init__(self, name) -> None:
        self.name = name
        self.dogs.append(self)

    # a class method is a method that allows you to not create an instance
    # but you use just by calling the class, that's why you dont see self
    @classmethod
    def num_dogs(cls):
        return len(cls.dogs)
    
    # a static method is just a normal function that you put in a class
    # but it cannot call the other function, so here i cannot call num_dogs
    # you use staticmethods when you want to create classes with methods (like a storage)
    @staticmethod
    def bark(n):
        # barks n times
        for _ in range(n):
            print("Bark!")

tim = Dog("Tim")
john = Dog("John")

Dog.bark(5)
print(Dog.num_dogs())
