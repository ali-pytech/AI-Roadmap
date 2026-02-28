"""Housing file Handler"""
try:
    with open ("housing.txt", "r") as file:
        data = file.read()
        print(data)

except FileNotFoundError:
    print("Housing file Not Found. Please check File Name!")
