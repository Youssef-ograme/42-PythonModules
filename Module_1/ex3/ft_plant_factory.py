#!/usr/bin/env python3
class Graden:
    def __init__(self , name:str , Height:int , age:int):
        self.name = name.capitalize()
        self.Height = Height
        self.age = age
    def print_self(self):
        print(f"Created: {self.name} ({self.Height}cm, {self.age} days)")
        
def main():
    info = [
        Graden("Rose",25,30),
        Graden("oak",200,365),
        Graden("cactus",-5,90),
        Graden("sunflower",80,45),
        Graden("fern",15,120),
    ]
    print("=== Plant Factory Output ===")
    for x in range(len(info)):
        info[x].print_self()
    print(f"\nTotal plants created: {len(info)}")

if __name__ == "__main__":