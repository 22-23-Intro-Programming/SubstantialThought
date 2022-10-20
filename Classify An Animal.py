class Plesiasaur: #Sorry if I spelled that wrong.


    def __init__(self):
        self.coat = "slimey probably"
        self.fins = 4
        self.neck = "long"
        self.name = "Nessie"
        self.age = 20000000

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getFins(self):
        return self.fins

def main():

    p = Plesiasaur()

    print("Hi random dinosaur! Who are you?")

    print(p.getName())

    print("Nessie huh, I've heard of you. How old are you?")

    print(p.getAge())

    print("Wow! you are old! How many fins do you have?")

    print(p.getFins())

    print("That is cool. Nice to meet you Nessie.")

if __name__ == "__main__":
    main()

