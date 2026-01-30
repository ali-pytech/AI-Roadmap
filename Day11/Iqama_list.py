def iqama_fee_cal(years, iqama_fee=6500):
    return iqama_fee * years

if __name__ == "__main__":
    try:
        user_input=input("Enter Number of Years with spaces between them: ")
        years_list= [int(y) for y in user_input.split()]
        for years in years_list:
            total_fee = iqama_fee_cal(years)
            print(f"Iqama Fee for {years} Years is {total_fee} SAR")

    except:
        print("Invalid Input. Enter Numbers Only!!")
