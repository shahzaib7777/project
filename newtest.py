data = [''] 

while True:
    Name = input("enter the name : ")
    data.append(Name)

    choice = input("enter another name ?? (y / n : ")
    if choice.casefold() == 'n':
        break 

for element in data:
    print(element)