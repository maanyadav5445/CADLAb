students = {}

def add_student():
    roll = input()
    name = input()
    marks = list(map(int, input().split()))
    students[roll] = {"name": name, "marks": marks}

def display_students():
    for roll, data in students.items():
        print(roll, data["name"], data["marks"])

def average_marks():
    for roll, data in students.items():
        avg = sum(data["marks"]) / len(data["marks"])
        print(roll, avg)

def highest_marks():
    top = ("", 0)
    for roll, data in students.items():
        total = sum(data["marks"])
        if total > top[1]:
            top = (roll, total)
    print(top)

while True:
    choice = input()
    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        average_marks()
    elif choice == "4":
        highest_marks()
    elif choice == "5":
        break