print("===== STUDENT PERFORMANCE ANALYZER =====")

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

dstl_marks = int(input("enter dstl mark:"))
coa_marks = int(input("enter coa mark:"))       
tc_marks = int(input("enter tc mark:"))
ms_marks = int(input("enter ms mark:"))
dsa_marks = int(input("enter dsa mark:"))

total = dstl_marks + coa_marks + tc_marks + ms_marks + dsa_marks    

percentage = total / 5

# Subject marks
marks = {
    "DSTL": dstl_marks,
    "COA": coa_marks,
    "tc": tc_marks,
    "ms": ms_marks,
    "dsa": dsa_marks
}

highest = max(marks.values())
lowest = min(marks.values())
average = total / 5

print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Average Marks:", average)

strongest_subject = max(marks, key=marks.get)
weakest_subject = min(marks, key=marks.get)

print("Strongest Subject:", strongest_subject)
print("Weakest Subject:", weakest_subject)

import matplotlib.pyplot as plt

subjects = list(marks.keys())
scores = list(marks.values())

plt.bar(subjects, scores)

plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Student Performance")

plt.show()

# Grade aur Result
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

if percentage >= 40:
    result = "PASS"
else:
    result = "FAIL"


# Result file me save karna
with open("result.txt", "w") as file:
    file.write("===== STUDENT RESULT =====\n")
    file.write(f"Name: {name}\n")
    file.write(f"Roll No: {roll_no}\n")
    file.write(f"Total Marks: {total}\n")
    file.write(f"Percentage: {percentage}\n")
    file.write(f"Grade: {grade}\n")
    file.write(f"Result: {result}\n")

print("Result successfully saved in result.txt")

