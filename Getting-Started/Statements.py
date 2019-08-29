
def ifCase():
    num = 5
    if num:
        print('If number is not 0, it will be ture in if statements')

    text = "python"
    if text:
        print('if string is not empty, it will be ture in if statements')

    noneObj = None
    if noneObj:
        print('This will be executed.')

    #Ternary If Statements
    a = 1
    b = 2
    print("Bigger") if a > b else print("smaller")



# Run def
ifCase()