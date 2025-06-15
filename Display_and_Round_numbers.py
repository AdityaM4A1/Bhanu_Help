def round_numbers(source_file, destination_file):
    try:
        with open(source_file, 'r') as src_file:
            lines = src_file.readlines()
        
        with open(destination_file, 'w') as dest_file:
            for line in lines:
                decimal_number = float(line.strip())
                rounded_number = round(decimal_number)
                dest_file.write(f"{rounded_number}\n")
        
        print(f"Rounded numbers have been copied from {source_file} to {destination_file}.")
    except FileNotFoundError:
        print(f"The file {source_file} does not exist.")
    except ValueError:
        print("The file contains non-numeric values.")
    except Exception as e:
        print(f"An error occurred: {e}")

def read(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

source_file = 'decimalNumbers.txt'
destination_file = 'roundednumbers.txt'
round_numbers(source_file, destination_file)
print("\nReading roundednumbers.txt:")
read(destination_file)