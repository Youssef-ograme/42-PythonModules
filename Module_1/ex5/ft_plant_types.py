class Graden:
    def __init__(self,name:str ,Height:int ,Age:int):
        self.name = name
        self.Height = Height
        self.Age = Age
        
class Flower(Graden):
    def __init__(self, name:str, Height:int, Age:int , color:str):
        super().__init__(name, Height, Age)
        self.color = color
        
    def print_self (self):
        print(f"{self.name} (Flower): {self.Height}cm, {self.Age} days, {self.color} color")
        
    def bloom (self):
        print(f"{self.name} is blooming beautifully !")
        
class Tree(Graden):
    def __init__(self, name:str, Height:int, Age:int ,trunk_diameter:int):
        super().__init__(name, Height, Age)
        self.trunk_diameter = trunk_diameter
        
    def print_self (self):
        print (f"{self.name} (Tree): {self.Height}cm, {self.Age} days, {self.trunk_diameter}cm diameter")
        
    def produce_shade(self):
        som = (self.trunk_diameter * 3.14) / 2
        print(f"{self.name} provides {int (som)} square meters of shade")
        
class Vegetable(Graden):
    def __init__(self, name:str, Height:int, Age:int , harvest_season:str ,nutritional_value:str):
        super().__init__(name, Height, Age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
    def print_self (self):
        print(f"{self.name} (Vegetable): {self.Height}cm, {self.Age} days,{self.harvest_season} harvest")
        print (f"{self.name} is rich in {self.nutritional_value}")
        
def main ():
    info = [
            Flower("Rose",25,30,"red"),
            Tree("Oak",500,1825,50),
            Vegetable("Tomato",80,90,"summer","vitamin C")
    ]
    print ("=== Garden Plant Types ===\n")
    for x in range(len(info)):
        info[x].print_self()
        if isinstance(info[x],Flower):
            info[x].bloom()
            print()
        elif isinstance(info[x],Tree):
            info[x].produce_shade()
            print()
            
if __name__ == "__main__":
    main()