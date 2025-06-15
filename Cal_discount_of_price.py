def cal_discount(quantity):
    if 10 <= quantity <= 19:
        return 0.20
    elif 20 <= quantity <= 49:
        return 0.30
    elif 50 <= quantity <= 99:
        return 0.40
    elif quantity >= 100:
        return 0.50
    else:
        return 0.0

def main():

    PACKAGE_PRICE = 99
    
    quantity = int(input("Enter the number of packages purchased: "))
    discount_rate = cal_discount(quantity)
    discount_amount = PACKAGE_PRICE * quantity * discount_rate
    total_amount = PACKAGE_PRICE * quantity - discount_amount
    print(f"Discount amount: ${discount_amount:,.2f}")
    print(f"Total amount: ${total_amount:,.2f}")

if __name__ == "__main__":
    main()