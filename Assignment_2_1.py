# Student Record Manager
students = {}
n = int(input("How many students do you want to add : "))

for i in range(n):
    print("Student", i + 1)
    roll = int(input("Enter roll number :"))
    name = input("Enter name: ")

    marks = []
    subjects = int(input("How many subjects : "))
    for j in range(subjects):
        m = float(input("Enter mark " + str(j + 1) + ": "))
        while m < 0 or m > 100:
            print("Invalid mark! Please enter a value between 0 and 100.")
            m = float(input("Enter mark " + str(j + 1) + ": "))
        marks.append(m)

    students[roll] = (name, marks)

print("All student records added successfully!")
print(students)

# Average marks above 80

print("Students with average marks above 80:")
is_average = False
for roll in students:
    name = students[roll][0]
    marks = students[roll][1]

    total = 0
    for m in marks:
        total = total + m

    average = total / len(marks)

    if average > 80:
        is_average = True
        print(name, "(Roll No:", roll,") -> Average:", average)

if is_average == False:
    print("No student has average above 80.")

# Update marks

update_roll = int(input("Enter roll number to update marks :"))
if update_roll in students:
    name = students[update_roll][0]
    old_marks = students[update_roll][1]
    print("Current marks of", name, ":", old_marks)

    new_marks = []
    subjects = int(input("How many subjects now? "))
    for j in range(subjects):
        m = float(input("Enter mark " + str(j + 1) + ": "))
        new_marks.append(m)

    students[update_roll] = (name, new_marks)
    print("Marks updated successfully!")
else:
    print("Roll number not found.")

print("Final Student Records:")
print(students)
