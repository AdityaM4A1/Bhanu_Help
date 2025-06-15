def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

n = get_positive_integer("Enter the number of integers (n): ")
even_sum = 0
odd_sum = 0
for i in range(n):
    num = get_positive_integer(f"Enter positive integer {i + 1}: ")
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num
if even_sum == odd_sum:
    print("The sum of the even numbers is equal to the sum of the odd numbers.")
else:
    print("The sum of even numbers is not equal to the sum of odd numbers.")

