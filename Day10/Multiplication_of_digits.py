def mul_of_digits(num):
    total = 1
    for digit in str(num):
        total *= int(digit)
    return total

if __name__ == "__main__":
    try:
        number = int(input("Enter any number: "))
        result = mul_of_digits(number)
        print(f"Multiplication of digits of {number} is {result}")
    except ValueError:
        print("Invalid input. Please enter numbers only!")
