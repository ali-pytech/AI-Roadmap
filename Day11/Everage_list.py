def everage_finder(numbers):
    return sum(numbers) / len(numbers)

if __name__ == "__main__":
    try:
        user_input = input("Enter Numbers With space between them :")
        numbers_list = [int(n) for n in user_input.split()]
        Everage = everage_finder(numbers_list)
        print(f"Everage of All Numbers will be {Everage}")
    except ValueError:
        print("Invalid Input. Try Only Numbers!!!")
