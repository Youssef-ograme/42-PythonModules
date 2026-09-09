class GradenError(Exception):
    def __init__(self, Message):
        super().__init__(Message)
        self.Message = Message
        
class GardenManager:
    def __init__(self, plant_name, water_level , sunlight_hours, tank_water):
        self.plant_name = plant_name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours
        self.tank_water = tank_water
        self.added = False
        
    def add_plant (self):
        if len(self.plant_name) == 0:
            self.added = False
            raise GradenError("Error adding plant: Plant name cannot be empty!")
        self.added = True
        print(f"Added {self.plant_name} successfully")
            
    def water_plants (self):
        print (f"watring {self.plant_name} - success")
        
    def check_plant_health (self):
        if (self.sunlight_hours < 2 or self.sunlight_hours > 12) or (self.water_level < 1 or self.water_level > 10) or len(self.plant_name) == 0:
            raise GradenError(f"Error checking {self.plant_name}:" f"Water level {self.water_level} is too high (max 10)")
        else:
            print (f"{self.plant_name} health (water: {self.water_level} , sun:{self.sunlight_hours})")
    def check_water_tank(self):
        if (self.tank_water < self.water_level):
            raise GradenError ("Not enough water in tank")
        
def main ():
    info = [
        GardenManager("tomato", 5, 8 , 10),
        GardenManager("lettuce", 6, 9,1),
        GardenManager("carrot", 7, 10,19)
    ]
    try:
        print("Adding plants to garden...")
        for x in info:
            x.add_plant()
    except GradenError as e:
        print(e)
        
    try:
        print("\nWatering plants...")
        for x in info:
            if x.added:
                try:
                    x.check_water_tank()
                    x.water_plants()
                except GradenError as e:
                    print(f"Caught GardenError: {e}")
    except GradenError as e:
        print(e)
    finally:
        print("Closing watering system (cleanup)")
        
    try:
        print("\nChecking plant health...")
        for x in info:
            x.check_plant_health()
    except GradenError as e:
        print(e)
    
    finally:
        print("\nTesting error recovery...")
        print("System recovered and continuing...")
        print("Garden management system test complete!")
    

if __name__ == "__main__":
    main()