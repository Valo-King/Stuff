names = []

while True:
    nameToAppend = input("What is your name? ")
    names.append(nameToAppend)
    yesNo = input("Are there more names to take down? ")
    if yesNo == "no" or yesNo == "No" or yesNo == "n" or yesNo == "N":
        break
    else:
        continue
print(" ".join(names))