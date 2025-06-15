def sum_of_integers_1_to_n_using_sum():
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

    n = get_positive_integer("Enter a positive integer n: ")
    sum_result = sum(range(1, n + 1))

    print(f"The sum of integers from 1 to {n} using sum() function is:", sum_result)

sum_of_integers_1_to_n_using_sum()