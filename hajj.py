i = 0
name = [1000]
Name = [1000]
while True:
    Name = str(input())

    if Name == "*":
        break
    else:
        name.insert(i, Name)
        i += 1

nameConversion = {
    'Hajj': 'Hajj-e-Akbar',
    'Umrah': 'Hajj-e-Asghar',
}
j = 0
while j < i:
    Name = name[j]
    print("Case " + str(j + 1) + ": " + nameConversion[Name])
    j += 1
