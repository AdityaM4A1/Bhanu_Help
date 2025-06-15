def TabProduct(T):
    product = 1
    for number in T:
        product *= number
    return product
    
numbers = [3, 2, 5, 0.5, 20]
product = TabProduct(numbers)
print("The product of the elements in the list [3, 2, 5, 0.5, 20] is:", product)