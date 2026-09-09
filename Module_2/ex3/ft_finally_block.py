def  water_plants(plant_list):
    try:
        i = 0
        while i < len(plant_list):
            
            if isinstance(plant_list[i],str):
                print(f"Watering {plant_list[i]}")
                
            else:
                raise ValueError ("Error: Cannot water None - invalid plant!")
            i += 1
    finally:
        print("Closing watering system (cleanup)")
            
def test_watering_system():
    print("=== Garden Watering System ===\n")
    
    print ("Opening watering system")
    plant_list = ["tomat","lettuce","carrots" , "youssef"]
    
    try:
        water_plants(plant_list)
        
    except ValueError as e:
            print(e)
            
    else:
        print("Watering completed successfully!")
        
    finally:
        print ("\nCleanup always happens, even with errors!")
        
def main ():
    test_watering_system()
if __name__ == "__main__":
    main()
        