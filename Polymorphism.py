class transport:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print(self.brand, self.model)
  
#==================================
class Car(transport):
  def __init__(self, brand, model):
    super().__init__(brand, model)

  def move(self):
    print("Drive!")
#==================================
class Boat(transport):
  def __init__(self, brand, model):
    super().__init__(brand, model)

  def move(self):
    print("Sail!")
#==================================
class Plane(transport):
  def __init__(self, brand, model):
    super().__init__(brand, model)

  def move(self):
    print("Fly!")

#=============== main ===================
if __name__ == "__main__":
  print("------- polymorphism example -------")

car1 = Car("Ford", "Mustang")       
boat1 = Boat("Ibiza", "Touring 20") 
plane1 = Plane("Boeing", "747")     

for x in (car1, boat1, plane1):
  x.move()

