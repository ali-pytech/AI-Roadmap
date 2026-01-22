def annual_rent(monthly_rent):
    return monthly_rent * 12

if __name__ == "__main__":
    try:
        monthly_rent = int(input("Enter your monthly rent: "))
        total_rent = annual_rent(monthly_rent)
        print(f"Annual rent for {monthly_rent} SAR per month will be {total_rent} SAR")
    except ValueError:
        print("Invalid input. Please enter numbers only!")
