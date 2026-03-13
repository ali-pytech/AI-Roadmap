"""Housing Record JSON"""

import json


housing = [
    {"Apartment":"Apartment A" , "monthly_rent": 2500 , "Location":"Riyadh" , "Annual_rent": 30000},
    {"Apartment":"Apartment b" , "monthly_rent": 2000 , "Location":"Jeddah" , "Annual_rent": 24000}

]

#write to json
with open("housing.json","w") as file:
    json.dump(housing , file, indent=4)


#Read Back
with open("housing.json", "r") as file:
    data = json.load(file)
    print("Housing File Content:\n", data)
