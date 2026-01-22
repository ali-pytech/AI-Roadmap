def vat_cal(price):
    vat_rate = 0.15
    vat = vat_rate * price
    total = vat + price
    return vat, total

if __name__ == "__main__":
    try:
        price = int(input("Enter the price of item: "))
        vat, total = vat_cal(price)
        print(f"VAT on {price} will be {vat} SAR and total price will be {total} SAR")
    except ValueError:
        print("Invalid input. Please enter a number!")
