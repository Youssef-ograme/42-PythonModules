def ft_water_reminder():
    nb = int (input ("Days since last watering: "))
    if nb > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
ft_water_reminder()