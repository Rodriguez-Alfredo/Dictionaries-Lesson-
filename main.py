#!/bin/python3

#DICTIONARIES - key/values pairs {} 

drinks = {"White Russian": 7, "Old Fashion": 10, "Lemon Drop": 8} #drink is the key, price is the value

print(drinks)

employees = {"Finance": ["Bob", "Linda", "Tina"], "IT": ["Gene", "Louise", "Teddy"], "HR": ["Jimmy", "Mort"]}

print(employees)

employees ["Legal"] = ["Mr. Frond"] #adds new key:value pair 

print(employees)

employees.update({"Sales": ["Andie", "Ollie"]}) #adds new key:value
print (employees)

drinks["White Russian"] = 8 #update the value to a key
print (drinks)

print(drinks.get("White Russian")) #specified value you want to return

#Thank You TCM Security