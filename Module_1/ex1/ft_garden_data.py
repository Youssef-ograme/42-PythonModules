#!/usr/bin/env python3
class Graden:
    def __init__(self,name:str ,Height:int ,Age:int):
        self.name = name
        self.Height = Height
        self.Age = Age
    def print_self(self):
        print(f"{self.name}: {self.Height}cm {self.Age} days old")
        
        
def main():
    print("=== Garden Plant Registry ===")
    inof = [
            Graden("Rose",25,30),
            Graden("Sunflower",80,45),
            Graden("Cactus",15,120)
        ]
    for x in range(len(inof)):
        inof[x].print_self()
if __name__ == "__main__":
    main()