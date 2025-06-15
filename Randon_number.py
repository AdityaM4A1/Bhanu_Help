import random

def main():
    even_count = 0
    odd_count = 0
    for _ in range(100):
        number = random.randint(1, 100)
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
            
    print(f"Number of even numbers: {even_count}")
    print(f"Number of odd numbers: {odd_count}")

if __name__ == "__main__":
    main()