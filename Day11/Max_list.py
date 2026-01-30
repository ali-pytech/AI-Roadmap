def min_in_list(numbers):
    return max(numbers)

if __name__ == "__main__":
    try:
        user_input = input("Enter Numbers With Spaces Between Them: ")
        numbers_list = [int(n) for n in user_input.split()]
        maximum_num = min_in_list(numbers_list)
        print(f"Maximum Number is {maximum_num}")

    except ValueError:
        print("Invalid Input. Try Numbers Only!!!")
