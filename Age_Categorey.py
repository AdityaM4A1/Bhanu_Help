def Category(age):
    if age < 0:
        return "Invalid age"
    elif age <= 1:
        return "Infant"
    elif age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    else:
        return "Adult"

def main():
    age = int(input("Enter the person's age: "))
    category = Category(age)
    print(f"The person is {category}.")

if __name__ == "__main__":
    main()