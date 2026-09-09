def test_error_types():
    garden_operations()
def garden_operations ():
        try :
            nb = "a"
            a = int(nb)
            print(a)
        except ValueError as e:
            print("Testing ValueError...")
            print (f"Caught ValueError: invalid literal for {e})\n")
            
        try:
            nb = 10
            nb = nb / 0
        except ZeroDivisionError as e:
            print ("Testing ZeroDivisionError...")
            print(f"Caught ZeroDivisionError: {e}\n")
        
        try:
            with open("hello.txt","r") as file:
                content = file.read()
                print(content)
        except FileNotFoundError as e:
            print ("Testing FileNotFoundError...")
            print(f"Caught FileNotFoundError: {e}\n")
            
        try :
            info = {"name":"youssef", "color":"blue"}
            print (info["bome"])
        except KeyError as e:
            print ("Testing KeyError...")
            print(f"Caught KeyError: {e}\n")

        try:
            nb = "a"
            a = int(nb)
            print(a)            
            info = {"name":"youssef"}
            print(info["bom"])
        except (ValueError , KeyError):
            print ("Testing multiple errors together...")
            print("Caught an error, but program continues!\n")        
        print ("All error types tested successfully!")
def main():
    test_error_types()
if __name__ == "__main__":
    main()