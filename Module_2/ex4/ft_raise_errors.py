def check_plant_health(plant_name, water_level, sunlight_hours):
        if len(plant_name) == 0:
            raise ValueError ("Error: Plant name cannot be empty!")
        elif (water_level < 1 or water_level > 10):
            raise ValueError ("Error: Water level 15 is too high (max 10)")
        elif (sunlight_hours < 2 or sunlight_hours > 12):
            raise ValueError ("Error: Sunlight hours 0 is too low (min 2)")
        else :
            return (f"Plant {plant_name} is healthy!")


def test_plant_checks():
    print("=== Garden Plant Health Checker ===")

    print("Testing good values...")
    try:
        print(check_plant_health("tomato", 5, 8))
    except ValueError as e:
        print(f"Error: {e}")

    print("Testing empty plant name...")
    try:
        check_plant_health("", 1, 10)
    except ValueError as e:
        print(f"Error: {e}") 

    print("Testing bad water level...")
    try:
        check_plant_health("tomato", 15, 8)
    except ValueError as e:
        print(f"Error: {e}")

    print("Testing bad sunlight hours...")
    try:
        check_plant_health("tomato", 5, 0)
    except ValueError as e:
        print(f"Error: {e}")

    finally:
        print("All error raising tests completed!")


def main():
    test_plant_checks()
if __name__ == "__main__":
    main()