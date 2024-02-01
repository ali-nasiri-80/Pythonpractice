def menu():
    print("1: Add tel", end="\t\t")
    print("2: Delete tel", end="\t\t")
    print("3: Search tel")
    print("4: Change tel", end="\t\t")
    print("5: Change name", end="\t\t")
    print("6: Display all")
    print("7:Exit")
    choose = int(input("Select 1 to 7:"))
    return choose


def add(telbook):
    name = input("Enter name:")
    telno = input("Enter tel number:")
    if name not in telbook:
        telbook[name] = telno
    else:
        print("name is alread exists:")
    print()
    return telbook


def delete(telbook):
    name = input("Enter name for deleted:")
    if name in telbook:
        del telbook[name]
    else:
        print(name, "is not found try agin:")
    return telbook


def search(telbook):
    name = input("Enter name for search:")
    if name in telbook:
        print(name, ":", telbook[name])
    else:
        print(name, "is not found.")


def changeTel(telbook):
    name = input("Enter name:")
    telno = input("Enter new tel number:")
    if name in telbook:
        telbook[name] = telno
    else:
        print(name, "not found")
    return telbook


def changeName(telbook):
    oldname = input("Enter the old name:\n")
    newname = input("Enter the new name:")
    if oldname in telbook:
        telbook[newname] = telbook.pop(oldname)
    else:
        print(oldname, "is not found.")
    return telbook


def printAll(telbook):
    for name in telbook:
        print(name,":",telbook[name], end='\t')
    print(" ")


telbook = {}
while 1:
    choose = menu()
    if choose == 7:
        break
    elif choose == 1:
        n = int(input("Enter tel add:"))
        for i in range(1, n+1):
            telbook = add(telbook)
            
    elif choose == 2:
        telbook = delete(telbook)
    elif choose == 3:
        telbook = search(telbook)
    elif choose == 4:
        telbook = changeTel(telbook)
    elif choose == 5:
        telbook = changeName(telbook)
    elif choose == 6:
        printAll(telbook)
print('-'*40)
