class Graden:
    def __init__(self , name:str ,heghit:int , age:int):
        self.name = name
        self.set_heghit(heghit)
        self.set_age(age)
        
    def set_heghit (self , __heghit:int) -> None:
        if int (__heghit) < 0:
            print(f"Invalid operation attempted: height {__heghit} [REJECTED]")
            print("Security: Negative height rejected")
            self.heghit = 0
        else:
            self.heghit = __heghit
            print(f"Height updated: {__heghit}cm [OK]")
        
    def set_age(self , __age:int) -> None:
        if int(__age) < 0:
            print(f"Invalid operation attempted: age {__age} [REJECTED]")
            print("Security: Negative height rejected")
            self.age = 0
        else:
            self.age = __age
            print(f"Age updated: {__age} days [OK]")
        
    def get_heghit (self) -> int:
        return self.heghit
    
    def get_age (self) -> int:
        return self.age
    
    def print_self(self):
            print(f"Current plant: {self.name} ({self.get_heghit()}cm, {self.get_age()} days)")
def main():
    info = [
            Graden("Rose",25,30),
            Graden("oak",200,365),
            Graden("cactus",-5,90),
            Graden("sunflower",80,45),
            Graden("fern",15,120),
        ]
    print("=== Garden Security System ===")
    for x in range(len(info)):
        info[x].print_self()
        
if __name__ == "__main__":
    main()