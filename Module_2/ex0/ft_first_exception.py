def  check_temperature(temp_str):    
    try:
        if int(temp_str) >= 0 and int(temp_str) <= 40:
            print (f"Temperature {temp_str}°C is perfect for plants!\n")
        elif int(temp_str) > 40:
            print (f"Error: {temp_str}°C is too hot for plants (max 40°C)\n")
        elif int(temp_str) < 0:
            print (f"Error: {temp_str}°C is too cold for plants (min 0°C) \n")
            
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")
        
def main ():
    info = ["25","abc","100","-50"]
    
    print ("=== Garden Temperature Checker ===\n")
    for x in info:
        print (f"Testing temperature: {x}")
        check_temperature(x)
    print("All tests completed- program didn't crash!")
if __name__ == "__main__":
    main()
ft_different_errors