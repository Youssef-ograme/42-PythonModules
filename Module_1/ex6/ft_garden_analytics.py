class GardenManager:
    countGraden = 0
    count = 0
    def __init__(self , name:str):
        self.plants = []
        self.name = name
        GardenManager.countGraden += 1
    def add_plant (self , plant):
        self.plants.append(plant)
        GardenManager.count += 1
        print (f"added {plant.plant} to {self.name}'s garden")
    @classmethod
    def count_add(cls):
        print(f"Plants added: {cls.count}",end=", ")
        
class Plant:
    growth = 0
    def __init__(self, plant , height):
        self.plant = plant
        self.height = height
        
    def grow(self):
        Plant.growth += 1
        self.height += 1
        print(f"{self.plant} grew 1cm")
        
    @classmethod
    def Total_growth (cls):
        print(f"Total growth: {cls.growth}cm")
    
    
    def __str__ (self):
        return f"- {self.plant}: {self.height}cm"
    
class FloweringPlant(Plant):
    def __init__(self,plant , height ,color:str):
        super().__init__(plant,height)
        self.color = color
        
    def grow(self):
        Plant.growth += 1
        self.height += 1
        print(f"{self.plant} grew 1cm")
        
    def __str__(self):
        return f"- {self.plant}: {self.height}cm ,{self.color} flowers (blooming)"
    
class PrizeFlower(FloweringPlant):
    count = 0
    def __init__(self,plant , height , color , points):
        super().__init__(plant,height,color)
        self.points = points
        
    def grow(self):
        self.height += 1
        Plant.growth += 1
        print(f"{self.plant} grew 1cm")
        
    def __str__(self):
        return f"- {self.plant}: {self.height}cm ,{self.color} flowers (blooming), Prize points: {self.points}"

def main():
    print ("=== Garden Management System Demo ===\n")
    info = GardenManager("youssef")
    info.add_plant(Plant("Oak Tree",12))
    info.add_plant(FloweringPlant("Rose",26,"red"))
    info.add_plant(PrizeFlower("Sunflower",51,"yellow",10))
    
    bob = GardenManager("Bob")          
    bob.add_plant(Plant("Cactus",30))
    bob.add_plant(FloweringPlant("Tulip",20,"pink"))
    bob.add_plant(PrizeFlower("Sunflower",51,"yellow",10))
    print()
    
    Plant_ = 0
    Flowering = 0
    Prize = 0
    __bool:bool = True
    
    for x in info.plants:
        if isinstance(x,PrizeFlower):
            Prize += 1
        elif isinstance(x,FloweringPlant):
            Flowering += 1
        else:
            Plant_ += 1
    
    for x in info.plants:
        x.grow()
        
    for x in info.plants:
        print(x)
        
    GardenManager.count_add()
    Plant.Total_growth()
    print (f"Plant types: {Plant_} regular, {Flowering} flowering, {Prize} prize flowers")
    
    for x in info.plants:
        if x.height < 0:
            __bool = False
            break
        
    print(f"Height validation test: {__bool}")
    res = 0
    for x in info.plants:
        if isinstance(x,PrizeFlower):
            res += x.points
            res += x.height
        else:
            res += x.height
    
    res_bob = 0                          
    for x in bob.plants:
        if isinstance(x,PrizeFlower):
            res_bob += x.points
            res_bob += x.height
        else:
            res_bob += x.height
    
    print(f"Garden scores - {info.name}: {res}, {bob.name}: {res_bob}")
    print(f"Total gardens managed: {GardenManager.countGraden}")   
if __name__ == "__main__":
    main()
