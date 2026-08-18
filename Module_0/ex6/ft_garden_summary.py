def ft_garden_summary () -> None:
    name: str = input("Enter garden name: ")
    nbr: int = int(input ("Enter number of plants: "))
    print(f"Garden: {name}\nPlants: {nbr}\nStatus: Growing well!")

ft_garden_summary()