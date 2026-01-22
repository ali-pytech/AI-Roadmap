def iqama_fee_cal(years, iqama_fee=6500):
    return iqama_fee * years

if __name__ == "__main__":
    try:
        years = int(input("Enter Number of Years: "))
        total_fee = iqama_fee_cal(years)
        print(f"Total Iqama Fee for {years} years will be {total_fee} SAR")
    except ValueError:
        print("Invalid Input. Try Only Numbers!!!!")

