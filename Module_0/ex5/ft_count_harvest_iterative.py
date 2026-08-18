
def count_days (days) -> None:
    i = 1
    for i in range(days):
        print("Day ",i + 1)
        
def ft_count_harvest_iterative():
    day = int(input ("Days until harvest: "))
    count_days(day)
    print("Harvest time!")
ft_count_harvest_iterative()