def ListCases():
    StudentNames = ["Mark", "Katarina", "Jessica"]
    print(StudentNames[1])
    #                  -3        -2         -1
    # StudentNames = ["Mark", "Katarina", "Jessica"]
    print(StudentNames[-1]) # Jessica

    # set value
    StudentNames[0] = 'James'
    print(StudentNames);

    # Add element
    StudentNames.append('Homer')
    print(f'len of the students:{len(StudentNames)}')
    print(StudentNames)
    res = 'Mark' in StudentNames    
    print(f"Mark in students? {res}")

    #remove element
    del StudentNames[0]
    print(StudentNames);

    #Slicing
    StudentNames = ["Mark", "Katarina", "Jessica", "Homer"]
    print(StudentNames)

    print(StudentNames[1:]) # right of the element 1 (remove first element)
    print(StudentNames[1:-1]) # remove the 1st and the last element, print the rest

#run 
ListCases()