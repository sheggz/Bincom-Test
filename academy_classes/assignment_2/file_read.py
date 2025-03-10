'''
Create a text file that has your full name, and write code to read it and extract first name, middle name and last name
'''
with open("name.txt", "r") as file:
    names = file.readline().split(" ")
    print(names)
    print(f"firstname: {names[0]}")
    print(f"Middlename: {names[1]}")
    print(f"Lastname: {names[2]}")

