def annual_rent_cal(monthly_rent):
    annual_rent=monthly_rent*12
    return annual_rent 

if __name__ == "__main__":
    try:
        monthly_rent=input("Enter Monthly Rents With Space Between Them: ")
        rents_list=[int(r) for r in monthly_rent.split()]
        for monthly_rent in rents_list:
            annual_rent=annual_rent_cal(monthly_rent)
            print(f"your Monthly Rent is {monthly_rent} SAR so Annual Rent Willl be {annual_rent} SAR")

    except ValueError:
        print("Invalid Input. Try Only Numbers!!!")
