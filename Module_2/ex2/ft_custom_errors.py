class GradenError(Exception):
   def __init__(self, Message):
      super().__init__(Message)

class PlantError:
    def __init__(self, Plant , color , age , height):
        self.Plant = Plant
        self.color = color
        self.age = age
        self.height = height
    def check_plant (self):
        if (self.color == "brown" and ((self.age < 10 or self.age > 12) and (self.height < 100 or self.height > 300))):
            raise GradenError(f"Caught PlantError: The {self.Plant} plant is wilting!")
        elif (self.color == "green"):
            print ("plant is good \n")
            
class WaterError(PlantError):
    def __init__(self, Plant, color, age, height , water):
        super().__init__(Plant, color, age, height)
        self.water = water
    def check_water(self):
        if (self.color == "brown" and ((self.age < 10 or self.age > 12) and (self.height < 100 or self.height > 300))):
            raise GradenError(f"Caught WaterError: Not enough {self.water} in the tank!")
        else:
            print("water is good \n")
            
def main ():
    print ("=== Custom Garden Errors Demo ===")
    plant = PlantError("tomat","brown",6,80)
    water = WaterError("tomat","brown",6,80,"water")
    
    try:
        print("\nTesting PlantError...")
        plant.check_plant()
    except GradenError as e:
        print(e)
        
    try:
        print ("\nTesting WaterError...")
        water.check_water()
    except GradenError as e:
        print(e)
    
    
    print("\nTesting catching all garden errors...")
    try:
        plant.check_plant()
    except GradenError as e:
        print(e)
    try:
        water.check_water()
    except GradenError as e:
        print(e)
        
    finally:
        print("\nAll custom error types work correctly!")
        
if __name__ == "__main__":
    main()