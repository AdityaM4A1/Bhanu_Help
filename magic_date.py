def is_valid_date(month, day, year):
    if month < 1 or month > 12:
        return False
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day < 1 or day > 31:
            return False
    elif month in [4, 6, 9, 11]:
        if day < 1 or day > 30:
            return False
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            if day < 1 or day > 29:
                return False
        else:
            if day < 1 or day > 28:
                return False
    
    return True

def main():
    month,day,year = map(int,input().split('/'))
    if is_valid_date(month, day, year):
        if month * day == year:
            print("This is a magic date.")
        else:
            print("This is not a magic date.")
    else:
        print("The entered date is not valid.")

if __name__ == "__main__":
    main()