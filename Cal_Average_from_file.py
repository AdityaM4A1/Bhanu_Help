def calculate_average_from_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            numbers = [int(line.strip()) for line in lines]
            if numbers:
                average = sum(numbers) / len(numbers)
                return average
            else:
                print("The file is empty.")
                return None
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
        return None
    except ValueError:
        print("The file contains non-integer values.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

filename = 'numbers.txt'
average = calculate_average_from_file(filename)
if average is not None:
    print(f"The average of the numbers in the file is: {average:.2f}")
