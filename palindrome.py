def palindrome(ch):
    return ch == ch[::-1]

user_string = input("Enter a character string: ")
if palindrome(user_string):
    print(f"The string '{user_string}' is a palindrome.")
else:
    print(f"The string '{user_string}' is not a palindrome.")