
student = {"name":"Mark", "ID":13313, "feedback":None}


print(student['name']) # Mark

try:
    lastName = student["last_name"]
except KeyError:
    print("Error finding last_name")
except TypeError:
    print("this is for type error")
except Exception as error:
    print("Unknow error")
    print(error)

print("Done!")