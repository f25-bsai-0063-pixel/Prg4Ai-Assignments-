def Cal_Res(python, ai, maths):
    total = python + ai + maths
    percentage = (total / 300) * 100
    if percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"
    return total, percentage, grade
 
 
students = []                   
 
for i in range(5):
    print("\n--- Student", i + 1, "---")
    name = input("Enter name: ")
    roll = input("Enter Roll Number: ")
    python = float(input("Python marks: "))
    ai = float(input("AI marks: "))
    maths = float(input("Maths marks: "))
 
    total, percentage, grade = Cal_Res(python, ai, maths)
 
    student = {                     
        "name": name, "roll": roll,
        "python": python, "ai": ai, "maths": maths,
        "total": total, "percentage": percentage, "grade": grade
    }
    students.append(student)
 
print("\n-----RESULTS-----")
for s in students:
    print(s["name"], "|", s["roll"], "| Total:", s["total"],
          "| %:", round(s["percentage"], 2), "| Grade:", s["grade"])
 
topper = students[0]                
for s in students:
    if s["percentage"] > topper["percentage"]:
        topper = s

print("\nHighest:", topper["name"], "with", round(topper["percentage"], 2), "%")
 
with open("results.txt", "w") as f:
    for s in students:
        f.write(s["name"] + "," + s["roll"] + "," + str(s["total"]) + ","
                + str(round(s["percentage"], 2)) + "," + s["grade"] + "\n")
    f.write("\nTopper: " + topper["name"] + "\n")
