def main():
    
    user_string = input("Enter a character string: ")
    string_list = list(user_string)
    
    while True:
        
        index = input("Enter an index to replace with '?', or 'done' to finish: ")
        if index.lower() == 'done':
            break
        if index.isdigit():
            index = int(index)
            if 0 <= index < len(string_list):
                string_list[index] = '?'
            else:
                print(f"Index {index} is out of range. Please enter a valid index.")
        else:
            print("Invalid input. Please enter a valid integer index or 'done' to finish.")
            
    new_string = ''.join(string_list)
    print(f"The new string is: {new_string}")

if __name__ == "__main__":
    main()