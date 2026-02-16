student = {
    "name": "Carlos",
    "age": 22,
    "subjects": ["PNE", "Networks", "Databases"],
    "grades": {"PNE": 8.5, "Networks": 7.0, "Databases": 9.2}
}
#The student's name
print("Name:", student["name"])
#The number of subjects they are enrolled in
print("Number of subjects:", len(student["subjects"]))
#Whether "PNE" is in their subjects list
print("Enrolled in PNE:","PNE" in student["subjects"])
#Their grade in Databases
print("Databases grade:",student["grades"]["Databases"])
#Their average grade across all subjects (rounded to 2 decimals)
count = 0
a = 0
for i in student["grades"]:
    count +=1
    a += student["grades"][i]
av = a/count
av = round(av,2)
print("Average grade:", av)
#All subject-grade pairs, one per line
print("Subject grades:")
for subject, grade in student["grades"].items():
    print(" ", subject, ":", grade)