students = {
    "101": {"name": "Aman", "marks": [78, 85, 90]},
    "102": {"name": "Riya", "marks": [88, 79, 92]},
    "103": {"name": "Karan", "marks": [67, 72, 80]}
}

for sid, data in students.items():
    total = sum(data["marks"])
    avg = total / len(data["marks"])
    grade = "A" if avg >= 85 else "B" if avg >= 70 else "C"
    print(sid, data["name"], total, avg, grade)

topper = max(students.items(), key=lambda x: sum(x[1]["marks"]))
print("Topper:", topper[1]["name"])