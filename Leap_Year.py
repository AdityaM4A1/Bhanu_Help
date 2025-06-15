def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def main():
    year = int(input("Enter a year in four digits: "))
    if is_leap_year(year):
        print("That is a leap year. February has 29 days.")
    else:
        print("That is not a leap year. February has 28 days.")

if __name__ == "__main__":
    main()