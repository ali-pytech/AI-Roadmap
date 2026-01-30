def vat_cal(prices):
    vat_rate = 0.15
    vat = prices * vat_rate
    total_price = prices + vat
    return vat, total_price

if __name__ == "__main__":
    try:
        user_input = input("Enter Prices of Items With Spaces Between Them: ")
        price_list = [int(p) for p in user_input.split()]

        for prices in price_list:
            vat, total_price = vat_cal(prices)
            print(f"VAT on {prices} SAR is {vat} SAR and total price will be {total_price} SAR")

    except ValueError:
        print("Invalid Input! Try only numbers.")
