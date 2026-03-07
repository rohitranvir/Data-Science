stno = int(input("Enter Student Number: "))
sname = input("Enter Student Name: ")

# validation of C marks
while True:
    cm = int(input("Enter Marks in C: "))
    if cm >= 0 and cm <= 100:
        break

# validation of CPP marks
while True:
    cppm = int(input("Enter Marks in CPP: "))
    if cppm >= 0 and cppm <= 100:
        break

# validation of PYTHON marks
while True:
    pym = int(input("Enter Marks in PYTHON: "))
    if pym >= 0 and pym <= 100:
        break

# calculate total and percentage
totmarks = cm + cppm + pym
permarks = (totmarks / 300) * 100

# decide grade
if cm < 40 or cppm < 40 or pym < 40:
    grade = "FAIL"
else:
    if 250 <= totmarks <= 300:
        grade = "DISTINCTION"
    elif 200 <= totmarks <= 249:
        grade = "FIRST"
    elif 150 <= totmarks <= 199:
        grade = "SECOND"
    elif 120 <= totmarks <= 149:
        grade = "THIRD"
    else:
        grade = "PASS"

# Display Marks Memo
print("=" * 70)
print("\tStudent Marks Report")
print("=" * 70)
print("\tStudent Number:", stno)
print("\tStudent Name:", sname)
print("\tMarks in C:", cm)
print("\tMarks in CPP:", cppm)
print("\tMarks in PYTHON:", pym)
print("-" * 70)
print("\tTotal Marks:", totmarks)
print("\tPercentage:", permarks)
print("-" * 70)
print("\tGrade:", grade)
print("=" * 70)