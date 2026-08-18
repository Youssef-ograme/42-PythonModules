def count_days (age) -> None:
    if age > 1:
        count_days(age - 1)
    print("Day ",age)
def ft_count_harvest_recursive() -> None:
    days = int (input("Days until harvest: "))
    count_days(days)
    print("Harvest time!")
ft_count_harvest_recursive()