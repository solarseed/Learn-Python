
student = {"name":"Mark", "ID":13313, "feedback":None}

allStudents =[
    {"name":"Mark", "ID":13313, "feedback":None},
    {"name":"Katarina", "ID":15515, "feedback":None},
    {"name":"Jessica", "ID":16616, "feedback":None},
]

print(student['name']) # Mark
print(student.get("lastName", "Unknow1")) # Unknow since lastName does not exist, if it exists, return the value of lastName
print(student.keys())
print(student.values())