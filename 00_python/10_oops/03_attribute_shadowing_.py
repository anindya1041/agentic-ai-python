class Chai:
    temperature = "hot"
    strength = "Strong"

cutting = Chai()
print(cutting.temperature)
cutting.temperature = "Mild"
print(cutting.temperature)
print("Direct look in to the class",Chai.temperature)
del cutting.temperature
print(cutting.temperature)