sequence = input()
countV = 0
countH = 0

for i in list(sequence):
    if i.upper() == "V":
        countV += 1
    elif i.upper() == "H":
        countH += 1
    else:
        print("Invalid Statement")

if (countV % 2 == 0) and (countH % 2 == 0):
    print("1 2\n3 4")
elif (countV % 2 == 0) and (countH % 2 != 0):
    print("2 1\n4 3")
elif (countV % 2 != 0) and (countH % 2 == 0):
    print("3 4\n1 2")
else:
    print("4 3\n2 1")
    
