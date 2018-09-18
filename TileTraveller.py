

start = (1,1)

i = "You can travel: "

while start != (3,1):
    if start == (1,1):
        print(i + "(N)orth")
        direction = input("Direction: ")
        if direction == 'n':
            start == (1,2)
        else:
            print("invalid direction!")
    if start == (1,2):
        print(i + "(N)orth or (E)ast")
        direction =input("Direction: ")
        if direction == 'n':
            start == (1,3)
        elif direction == 'e':
            start == (2,2)
        else:
            print("invalid direction!")
    if start == (2,2):
        print(i + "(E)ast or (S)outh")
        direction = input("Direction: ")
        if direction == 'e':
            start == (1,2)
        elif direction == 's':
            start == (2,1)
        else:
            print("invalid direction!")
    if start == (2,1):
        print(i + "(N)orth")
        direction = input("Direction: ")
        if direction == 'n':
            start = (2,2)
        else:
            print("invalid direction!")
    if start == (1,3):
        print(i + "(S)outh or (E)ast")
        direction = input("Direction: ")
        if direction == 'e':
            start = (2,3)
        elif direction == 's':
            start = (1,2)
        else: 
            print("invalid direction!")
    if start == (2,3):
        print(i + "(E)ast or (W)est")
        direction = input("Direction: ")
        if direction == 'e':
            start = (3,3)
        elif direction == 'w':
            start = (1,3)
        else:
            print("invalid direction!")
    if start == (3,3):
        print(i + "(E)ast or (S)outh")
        direction = input("Direction: ")
        if direction == 'e':
            start = (2,3)
        elif direction == 's':
            start = (3,2)
        else:
            print("invalid direction!")
    if start == (3,2):
        print(i + "(N)orth or (S)outh")
        direction = input("direction: ")
        if direction == 'n':
            start = (3,3)
        elif direction == 's':
            start = (3,1)
            print("VICTORY")
    




