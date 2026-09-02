#!/usr/bin/env python3

class Graden:
    count = 0
    def __init__(self ,name:str):
        self.name = name
        self.plants = []
        Graden.count += 1
    def add_plants (self , plant):
        self.plants.append(plant)
        print(f"added {plant.name} to {self.name}'s garden")
        
    @classmethod
    def Plants_added(cls):
        print(f"\nPlants added: {cls.count}" ,end=",")
        
class Plant:
    count = 0
    def __init__(self , name:str , height:int):
        self.name = name
        self.height = height
        Plant.count += 1
        
    def grew(self):
        print(f"{self.name} grew 1cm")
    def __str__(self):
        self.height += 1
        return f"-{self.name}: {self.height}cm"
    
    @classmethod
    def Plants_added(cls):
        print(f"Total growth: {cls.count}cm")
        
class FloweringPlant(Plant):
    def __init__(self, name:str , height:int , color:str):
        super().__init__(name, height)
        self.color = color
        self.blooming = True
    def __str__(self):
        if self.blooming:
            return f"-{self.name}: {self.height} ,{self.color} flowers (blooming)"
        else:
            return f"-{self.name}: {self.height}cm"
    
class PrizePlant(FloweringPlant):
    
    def __init__(self, name:str, height:int, color:str , point:int):
        super().__init__(name, height, color)
        self.point = point
        self.blooming = True
    def __str__ (self):
        if self.blooming:
            return f"-{self.name}: {self.height} ,{self.color} flowers (blooming) , Prize points: {self.point}"
        else:
            return f"-{self.name}: {self.height}cm"
    

def main ():
        print("=== Garden Management System Demo ===\n")
        alice_garden = Graden("Alice")
        alice_garden.add_plants(Plant("Oak Tree" , 100))
        alice_garden.add_plants(FloweringPlant("Rose" , 25 , "red"))
        alice_garden.add_plants(PrizePlant("Sunflower" , 15 , "yellow" , 10))

        print (f"\n{alice_garden.name} is helping all plants grow...")
        for plant in alice_garden.plants:
            plant.grew()
        print (f"\n=== {alice_garden.name}'s Garden Report ===")  
        for plant in alice_garden.plants:
            print(f"{plant}")
            
        Graden.Plants_added()
        Plant.Plants_added()
        
if __name__ == "__main__":
    main()