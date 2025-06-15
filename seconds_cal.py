def convert_seconds(seconds):

    SECONDS_IN_A_MINUTE = 60
    SECONDS_IN_AN_HOUR = 3600
    SECONDS_IN_A_DAY = 86400

    days = seconds // SECONDS_IN_A_DAY
    seconds_remaining_after_days = seconds % SECONDS_IN_A_DAY
    
    hours = seconds_remaining_after_days // SECONDS_IN_AN_HOUR
    seconds_remaining_after_hours = seconds_remaining_after_days % SECONDS_IN_AN_HOUR
    
    minutes = seconds_remaining_after_hours // SECONDS_IN_A_MINUTE
    remaining_seconds = seconds_remaining_after_hours % SECONDS_IN_A_MINUTE
    
    return days, hours, minutes, remaining_seconds

def main():

    seconds = int(input(""))
    
    days, hours, minutes, remaining_seconds = convert_seconds(seconds)

    if seconds >= 60:
        minutes_only = seconds // 60
        seconds_remaining_after_minutes_only = seconds % 60
        print(f"{seconds} seconds are equal to:")
        print(f"{minutes_only} full minute(s) and {seconds_remaining_after_minutes_only} seconds.")
    else:
        print("The number of seconds is less than one minute.")    
    if seconds >= 3600:
        hours_only = seconds // 3600
        seconds_remaining_after_hours_only = seconds % 3600
        print(f"{hours_only} full hour(s) and {seconds_remaining_after_hours_only} seconds.")
    
    if seconds >= 86400:
        days_only = seconds // 86400
        seconds_remaining_after_days_only = seconds % 86400
        print(f"{days_only} full day(s) and {seconds_remaining_after_days_only} seconds.")

if __name__ == "__main__":
    main()
