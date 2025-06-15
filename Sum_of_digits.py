def main():
    
    digits = input("Enter a sequence of digits with nothing separating them: ")
    total = 0
    for digit in digits:
        total += int(digit)
    print(f"The total of the digits in the string you entered is {total}")

if __name__ == "__main__":
    main()