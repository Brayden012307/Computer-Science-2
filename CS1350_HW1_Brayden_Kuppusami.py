print("================================")
print("Problem 1: Contact Manager")
print("================================")

contacts = {}
contacts["Mom"] = "555-1234" 
contacts["Dad"] = "555-5678" 
contacts["Best Friend"] = "555-8888" 
contacts["Pizza Place"] = "555-9999" 
contacts["Work"] = "555-0000" 

print("=== Initial Contacts ===")
print(contacts)

print("\n=== Access and Modify ===")
print(f"Mom's number: {contacts['Mom']}")
contacts["Dad"] = "555-4321"
contacts["Dentist"] = "555-2222"
grandma_lookup = contacts.get("Grandma", "Contact not found")
print(f"Looking up Grandma: {grandma_lookup}")
print("Updated contacts:", contacts)
print("\n=== Delete and Analyze ===")
del contacts["Pizza Place"]
old_work = contacts.pop("Work")
print(f"Removed work number: {old_work}")
print(f"Contacts remaining: {len(contacts)}")
print(f"Contact names: {contacts.keys()}")
print(f"Phone numbers: {contacts.values()}")

print("================================")
print("Problem 2: Grade Book Analyzer")
print("================================")

grades = { 
    "Alice": 87, 
    "Bob": 65, 
    "Carol": 92, 
    "Dave": 78, 
    "Eve": 55, 
    "Frank": 88, 
    "Grace": 71, 
    "Henry": 95, 
    "Ivy": 60, 
    "Jack": 83 
}

print("\n=== Basic Statistics ===")
print(f"Students: {grades.keys()}")
print(f"Grades: {grades.values()}")

total_students = len(grades) 
sum_grades = sum(grades.values()) 
average = sum_grades / total_students 

print(f"Total students: {total_students}") 
print(f"Sum of grades: {sum_grades}") 
print(f"Class average: {average:.2f}") 
print(f"Highest grade: {max(grades.values())}") 
print(f"Lowest grade: {min(grades.values())}") 

def get_letter(score): 
    if score >= 90: 
        return "A" 
    elif score >= 80: 
        return "B" 
    elif score >= 70: 
        return "C" 
    elif score >= 60: 
        return "D" 
    else: 
        return "F" 
    
print("\n=== Grade Report ===")
for name, grade in grades.items(): 
    letter = get_letter(grade) 
    print(f"{name}: {grade} ({letter})") 

print("\n=== Grade Distribution ===")
passed = 0 
failed = 0 
count_a = 0 
count_b = 0 
count_c = 0 
count_d = 0 
count_f = 0

for name, grade in grades.items():
    if grade >= 60: 
        passed += 1
    else: 
        failed += 1

    letter = get_letter(grade) 
    if letter == "A": 
        count_a += 1
    elif letter == "B":
        count_b += 1
    elif letter == "C":
        count_c += 1
    elif letter == "D":
        count_d += 1
    elif letter == "F":
        count_f += 1

print(f"Passed: {passed}") 
print(f"Failed: {failed}") 
print(f"A grades: {count_a}") 
print(f"B grades: {count_b}") 
print(f"C grades: {count_c}") 
print(f"D grades: {count_d}") 
print(f"F grades: {count_f}") 

print("\n=== Top and Bottom Performers ===")

top_name = "" 
top_grade = 0 
for name, grade in grades.items(): 
    if grade > top_grade:
        top_grade = grade
        top_name = name

print(f"Highest scorer: {top_name} ({top_grade})")

bottom_name = "" 
bottom_grade = 100 
for name, grade in grades.items(): 
    if grade < bottom_grade:
        bottom_grade = grade
        bottom_name = name

print(f"Lowest scorer: {bottom_name} ({bottom_grade})") 

print("\n=== Above Average Students ===")
for name, grade in grades.items(): 
    if grade > average: 
        print(f"{name}: {grade}") 

print("==================================")