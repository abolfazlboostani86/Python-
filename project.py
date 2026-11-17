name = input("Enter student name: ")
count = int(input("Enter number of lessons: "))
lessons = []
grades = []
for i in range(count):
    lesson = input("Enter lesson name and grade: ")
    parts = lesson.split()
    lessons.append(parts[0])
    grade = float(parts[1])
    while grade < 0 or grade > 20:
        print("Invalid grade!")
        grade = float(input("Enter grade again: "))
    grades.append(grade)
average = sum(grades) / count
print("REPORT CARD")
print("Student Name:", name)
for i in range(count):
    print("Lesson:", lessons[i])
    print("Grade:", grades[i])
    if grades[i] >= 10:
        print("PASS")
    else:
        print("FAIL")
print("Average:", average)


