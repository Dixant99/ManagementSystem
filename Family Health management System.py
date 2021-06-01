def getdate():
    import datetime
    return datetime.datetime.now()


def take(t):
    if t == 0:
        c = int(input("press 0 for food & press 1 for exercise\n"))
        if c == 0:
            value = input("what food have eaten\n")
            with open("father_food.txt", "a") as f:
                f = f.write(str([str(getdate())]) + ":" + value + "\n")
                print("Successfully Updated")
        elif c == 1:
            value = input("what exercise you have done\n")
            with open("father_exercise.txt", "a") as f:
                f = f.write(str([str(getdate())]) + ":" + value + "\n")
                print("Successfully Updated")
    elif t == 1:
        c = int(input("press 0 for food & press 1 for exercise\n"))
        if c == 0:
            value = input("what food have eaten\n")
            with open("mother_food.txt", "a") as f:
                f = f.write(str([str(getdate())]) + ":" + value + "\n")
                print("Successfully Updated")
        elif c == 1:
            value = input("what exercise you have done\n")
            with open("mother_exercise.txt", "a") as f:
                f = f.write(str([str(getdate())]) + ":" + value + "\n")
                print("Successfully Updated")
    elif t == 2:
        c = int(input("press 0 for food & press 1 for exercise\n"))
        if c == 0:
            value = input("what food have eaten\n")
            with open("elder_son_food.txt", "a") as f:
                f = f.write(str([str(getdate())]) + ":" + value + "\n")
                print("Successfully Updated")
        elif c == 1:
            value = input("what exercise you have done\n")
            with open("elder_son_exercise.txt", "a") as f:
                f = f.write(str([str(getdate())]) + ":" + value + "\n")
                print("Successfully Updated")
    elif t == 3:
        c = int(input("press 0 for food & press 1 for exercise\n"))
        if c == 0:
            value = input("what food have eaten\n")
            with open("younger_son_food.txt", "a") as f:
                f = f.write(str([str(getdate())]) + ":" + value + "\n")
                print("Successfully Updated")
        elif c == 1:
            value = input("what exercise you have done\n")
            with open("younger_son_exercise.txt", "a") as f:
                f = f.write(str([str(getdate())]) + ":" + value + "\n")
                print("Successfully Updated")


def retrieve(r):
    if r == 0:
        c = int(input("press 0 for food & press 1 for exercise\n"))
        if c == 0:
            with open("father_food.txt") as f:
                for i in f:
                    print(i, end=" ")
        elif c == 1:
            with open("father_exercise.txt") as f:
                for i in f:
                    print(i, end=" ")
    if r == 1:
        c = int(input("press 0 for food & press 1 for exercise\n"))
        if c == 0:
            with open("mother_food.txt") as f:
                for i in f:
                    print(i, end=" ")
        elif c == 1:
            with open("mother_exercise.txt") as f:
                for i in f:
                    print(i, end=" ")
    if r == 2:
        c = int(input("press 0 for food & press 1 for exercise\n"))
        if c == 0:
            with open("elder_son_food.txt") as f:
                for i in f:
                    print(i, end=" ")
        elif c == 1:
            with open("elder_son_exercise.txt") as f:
                for i in f:
                    print(i, end=" ")
    if r == 3:
        c = int(input("press 0 for food & press 1 for exercise\n"))
        if c == 0:
            with open("younger_son_food.txt") as f:
                for i in f:
                    print(i, end=" ")
        elif c == 1:
            with open("younger_son_exercise.txt") as f:
                for i in f:
                    print(i, end=" ")


while True:
    access = int(input("Enter 0 to add data & Enter 1 to retrieve data\n"))
    if access == 0:
        t = int(input("Press 0 for father, Press 1 for mother, Press 2 for elder son , Press 3 for younger son\n"))
        take(t)
    elif access == 1:
        r = int(input("Press 0 for father, Press 1 for mother, Press 2 for elder son , Press 3 for younger son\n"))
        retrieve(r)
