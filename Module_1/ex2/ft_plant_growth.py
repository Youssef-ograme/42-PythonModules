#!/usr/bin/env python3

class Graden:
    def __lsinit__(self,name:str , Height:int , age:int):
        self.name = name
        self.Height = Height
        self.Age = age
    def print_self(self):
        print(f"{self.name}: {self.Height}cm {self.Age} days old")
        
    def grow (self):
        self.Height += 1
        
    def age_up (self):
        self.Age += 1
        
    def get_info (self):
        self.print_self()
        
    def check_info(self):
        som = self.Height
        for x in range(1,8):
            print(f"=== Day {x} ===")
            self.get_info()
            self.grow()
            self.age_up()
        som = self.Height - som - 1
        print(f"Growth this week: +{som}cm\n")
            
def main ():
    info = [
        Graden("Rose",25,30),
        Graden("Sunflower",80,45),
        Graden("Cactus",15,120),
        Graden("ikhan",100,230)
    ]
    for x in range(len(info)):
        info[x].check_info()
        
if __name__ == "__main__":
    main()