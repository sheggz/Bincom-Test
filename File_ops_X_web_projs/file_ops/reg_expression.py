import re

pattern = re.compile(r"<td>\d{1,4}</td><td>(\w+)</td><td>(\w+)</td>")
with open("baby2008.html", mode ="r") as file:
    #print(file.readlines()) # gives a list of strings with each line being a html element
    #print("-----------------------------\n", file.read(),"\n", type(file.read()))
    #file.read() # return the entire content of the file as a string
    matches = pattern.findall(file.read()).
    for match in matches:
        print(match)
