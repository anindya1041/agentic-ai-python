class Chaicup:
    size = 150

    def describe(self):
        return f"A {self.size}ml cup chai"

cup = Chaicup()
print(cup.describe())
print(Chaicup.describe(cup))

cup_two = Chaicup()
cup_two.size = 100  # Correct: modifying the 'size' attribute of the object
print(Chaicup.describe(cup_two))