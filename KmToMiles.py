def convert_kilometers_to_miles(kilometers):
    miles = kilometers * 0.6214
    return miles

kilometers = float(input("Enter the distance in kilometers: "))
miles = convert_kilometers_to_miles(kilometers)
print(f"{kilometers} kilometers is equal to {miles:.2f} miles.")
