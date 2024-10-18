def calculate_average_marks(students):
    
    average_marks = {}
    
    
    for student, subjects in students.items():
        
        marks_total = sum(subjects.values())
        
        num_of_subjects = len(subjects)
        
        average = marks_total / num_of_subjects
        
        average_marks[student] = average
    
    return average_marks
students = {
    "Alice": {"Math": 80, "English": 75, "Science": 90},
    "Bob": {"Math": 70, "English": 85, "Science": 75},
    "Charlie": {"Math": 95, "English": 60, "Science": 85}
}


averages = calculate_average_marks(students)
print(averages)

print(max(averages.values()))