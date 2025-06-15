def calculate_monthly_averages(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            steps = [int(line.strip()) for line in lines]
            days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            monthly_averages = []
            start_day = 0
            for days in days_in_month:
                end_day = start_day + days
                monthly_steps = steps[start_day:end_day]
                monthly_average = sum(monthly_steps) / days
                monthly_averages.append(monthly_average)
                start_day = end_day
            
            return monthly_averages
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
        return None
    except ValueError:
        print("The file contains non-integer values.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def display_monthly_averages(monthly_averages):
    if monthly_averages is not None:
        months = ["January", "February", "March", "April", "May", "June",
                  "July", "August", "September", "October", "November", "December"]
        
        for month, average in zip(months, monthly_averages):
            print(f"The average number of steps taken in {month} is: {average:.2f}")

filename = 'steps.txt'
monthly_averages = calculate_monthly_averages(filename)
display_monthly_averages(monthly_averages)
