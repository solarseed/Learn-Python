def LoopCase(StudentNames):
    for name in StudentNames:
        print(f"Student's Name is {name}")

    x = 0
    for index in range(10): # [0, 1,2,...,9]
        x += 10
        print
        print(f"1. index = {index} X = {x}")

    for index in range(5, 10): #[5, 6, 7,...,9]
        x += 10
        print(f"2. index = {index} X = {x}")

    for index in range(5, 10, 2): #[5, 7, 9]
        x += 10
        print(f"3. index = {index} X = {x}")

def BreakCase(students):
    for name in students:
        if name == "Mark":
            print("Found!!")
            break
        print("Searching")

def continueCase(students):
    for name in students:
        if name == "Mark":
            continue
            print("Found!!")
        print("Searching")


def WhileCase(StudentNames):
    i = 0
    while True:
        print(StudentNames[i])
        if (StudentNames[i] == "Jessica"):
            break
    # todo.

#run
StudentNames = ["Mark", "Katarina", "Jessica", "Tom", "Derek"]
LoopCase(StudentNames)

