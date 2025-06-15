def calculate_average(notes):
    total_marks = 0
    for student in notes:
        total_marks += student[1]
    average = total_marks / len(notes)
    return average

def classify_students(notes):
    admitted = []
    rejected = []
    for student in notes:
        if student[1] >= 10:
            admitted.append(student[0])
        else:
            rejected.append(student[0])
    return admitted, rejected

notes = [
    ['Florian', 2],
    ['Antoine', 12],
    ['Erwan', 7],
    ['Xavier', 11],
    ['Didier', 20],
    ['Alain', 0],
    ['Hadi', 12]
]

average = calculate_average(notes)
print(f"The average of the exam is: {average:.2f}")
admitted, rejected = classify_students(notes)
print("Admitted students:", admitted)
print("Rejected students:", rejected)
