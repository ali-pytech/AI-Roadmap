"""Students Gardes Text File"""

students = [
    {"name":"Ali" , "Score":93 , "Status":"Excellent"},
    {"name":"Ahmed" , "Score":78 , "Status":"Good"}
]

try:
    with open("grades.txt","w") as file:
        for s in students:
            file.write(f"{s['name']} -  {s['Score']} -  {s['Status']}\n")


    with open("grades.txt", "r") as file:
        print("Gardes File Content:\n",file.read())

except FileNotFoundError:
    print("Error grades.txt Not Found!!!")
