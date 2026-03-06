print("===================================")
print("PART 1:SECTION A")
print("===================================")
print("QUESTION 1=C")
print("QUESTION 2=C")
print("QUESTION 3=A")
print("QUESTION 4=B")
print("QUESTION 5=B")
print("QUESTION 6=D")
print("QUESTION 7=D")
print("QUESTION 8=B")
print("QUESTION 9=B")
print("QUESTION 10=B")
print("QUESTION 11=C")
print("QUESTION 12=C")
print("QUESTION 13=D")
print("QUESTION 14=B")
print("QUESTION 15=B")
print("QUESTION 16=C")
print("QUESTION 17=B")
print("QUESTION 18=B")
print("QUESTION 19=B")
print("QUESTION 20=B")
print("===================================")
print("PART 1:SECTION B")
print("===================================")
print("QUESTION 21=F")
print("QUESTION 22=T")
print("QUESTION 23=F")
print("QUESTION 24=T")
print("QUESTION 25=F")
print("QUESTION 26=T")
print("QUESTION 27=F")
print("QUESTION 28=T")
print("QUESTION 29=F")
print("QUESTION 30=F")
print("===================================")
print("PART 1:SECTION C")
print("===================================")
print("QUESTION 31=expensive = {k: v for k, v in menu.items() if v > 15}")
print("QUESTION 32=\n a)enrolled & submitted \n b)enrolled - submitted")
print("QUESTION 33=\n arr[0:2, 1:] → [[20, 30], [50, 60]] \n np.mean(arr, axis=1) → [20., 50., 80.]")
print("QUESTION 34=\nPolymorphism \nPolymorphism allows different classes to be treated as instances of a same parent class through a uniform interface. Each object execution uses its own specific implementation of that method")
print("QUESTION 35=\nBug 1: total += 1 should be Counter.total += 1 \nBug 2: @staticmethod should be @classmethod")
print("QUESTION 36=\na)Instance Method\nb)Class Method\nc)Static Method\nd)Class Method\ne)Instance Method")
print("===================================")
print("PART 2:SECTION A")
print("===================================")
print("PROBLEM 1:")
print("===================================")
def analyze_text(text):
    
    clean_text = "".join(char.lower() for char in text if char.isalpha() or char.isspace())
    words = clean_text.split()
    
    
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    
    if not counts:
        return {"word_counts": {}, "most_common": None, "unique_count": 0}

    
    most_common_word = max(counts, key=counts.get)
    
    
    unique_count = sum(1 for word in counts if counts[word] == 1)
    
    return {
        "word_counts": counts,
        "most_common": most_common_word,
        "unique_count": unique_count
    }
print("===================================")
print("PROBLEM 2:")
print("===================================")
class Roster:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = set() 

    def enroll(self, name):
        self.students.add(name) 
    def drop(self, name):
        self.students.discard(name) 

    def is_enrolled(self, name):
        return name in self.students 

def common_students(roster1, roster2):
    
    return roster1.students & roster2.students

def exclusive_students(roster1, roster2):
    
    return roster1.students ^ roster2.students

def print_report(rosters):
    if not rosters: return
    
    
    for r in rosters:
        print(f"{r.course_name}: {len(r.students)} students")
    
   
    all_enrolled = rosters[0].students
    for r in rosters[1:]:
        all_enrolled &= r.students
    print(f"Enrolled in all courses: {all_enrolled}")
print("===================================")
print("PROBLEM 3:")
print("===================================")
import numpy as np

def grade_report(grades_2d):
   
    student_avgs = np.mean(grades_2d, axis=1)
    
    
    assignment_avgs = np.mean(grades_2d, axis=0)
    
    
    highest_idx = np.argmax(student_avgs)
    
    
    max_avg = np.max(student_avgs)
    curved = grades_2d * (100 / max_avg)
    
    
    passing_mask = grades_2d >= 60
    
    return {
        "student_averages": student_avgs,
        "assignment_averages": assignment_avgs,
        "highest_student": highest_idx,
        "curved_grades": curved,
        "passing": passing_mask
    }
print("===================================")
print("PROBLEM 4:")
print("===================================")
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, make, model, year):
        self.make, self.model, self.year = make, model, year

    @abstractmethod
    def fuel_cost(self, distance): pass 

    def info(self):
        return f"{self.year} {self.make} {self.model}" 

    @staticmethod
    def validate_year(year):
        return 1900 <= year <= 2026 

class GasCar(Vehicle):
    def __init__(self, make, model, year, mpg, gas_price=3.50):
        super().__init__(make, model, year)
        self.mpg, self.gas_price = mpg, gas_price

    def fuel_cost(self, distance):
        return (distance / self.mpg) * self.gas_price 

class ElectricCar(Vehicle):
    def __init__(self, make, model, year, kwh_per_mile, electricity_price=0.13):
        super().__init__(make, model, year)
        self.kwh_per_mile, self.electricity_price = kwh_per_mile, electricity_price

    def fuel_cost(self, distance):
        return distance * self.kwh_per_mile * self.electricity_price 

class HybridCar(GasCar):
    def __init__(self, make, model, year, mpg, gas_price=3.50, electric_fraction=0.4):
        super().__init__(make, model, year, mpg, gas_price)
        self.electric_fraction = electric_fraction

    def fuel_cost(self, distance):
        
        return super().fuel_cost(distance) * (1 - self.electric_fraction)

def trip_cost(vehicles, distance):
    costs = []
    for v in vehicles:
        cost = v.fuel_cost(distance)
        print(f"{v.info()}: ${cost:.2f}")
        costs.append((cost, v.info()))
    print(f"Cheapest: {min(costs)[1]}")
print("===================================")
print("PROBLEM 5:")
print("===================================")
class Wallet:
    def __init__(self, owner):
        self.owner = owner
        self.balances = {} 

    
    def __getitem__(self, currency):
        return self.balances.get(currency, 0.0)

    def __setitem__(self, currency, amount):
        if amount < 0: raise ValueError("Balance cannot be negative")
        self.balances[currency] = float(amount)

    def __contains__(self, currency):
        return self.balances.get(currency, 0) > 0

    def __len__(self):
        return sum(1 for amt in self.balances.values() if amt > 0)

    def __iter__(self):
        return iter(self.balances.keys())

    
    def __str__(self):
        return f"{self.owner}'s Wallet ({len(self)} currencies)"

    def __repr__(self):
        return f"Wallet('{self.owner}')"

    
    def __add__(self, other):
        new_wallet = Wallet(f"{self.owner} & {other.owner}")
        all_currencies = set(self.balances.keys()) | set(other.balances.keys())
        for curr in all_currencies:
            new_wallet[curr] = self[curr] + other[curr]
        return new_wallet

    def __mul__(self, factor):
        new_wallet = Wallet(self.owner)
        for curr, amt in self.balances.items():
            new_wallet[curr] = amt * factor
        return new_wallet

    
    def _total_value(self):
        return sum(self.balances.values())

    def __eq__(self, other):
        return self._total_value() == other._total_value()

    def __lt__(self, other):
        return self._total_value() < other._total_value()
print("===================================")
print("TEST CASES")
print("===================================")
print("PROBLEM 1:")
sample = "The cat sat on the mat. The cat liked the mat!"
result = analyze_text(sample)
print(result["word_counts"])   
print(result["most_common"])  
print(result["unique_count"]) 
print("===================================")
print("PROBLEM 2:")
cs101 = Roster("CS 101")
for name in ["Alice", "Bob", "Carol", "Dave"]: cs101.enroll(name)

cs201 = Roster("CS 201")
for name in ["Carol", "Dave", "Eve", "Frank"]: cs201.enroll(name)

cs301 = Roster("CS 301")
for name in ["Dave", "Eve", "Grace"]: cs301.enroll(name)

print(common_students(cs101, cs201))    
print(exclusive_students(cs101, cs201)) 
print_report([cs101, cs201, cs301])     
print("===================================")
print("PROBLEM 3:")
grades = np.array([
    [85, 90, 78, 92], 
    [70, 65, 80, 75], 
    [95, 88, 92, 97], 
    [60, 72, 68, 55]  
])

report = grade_report(grades)
print("Student averages:", report["student_averages"])      
print("Highest student index:", report["highest_student"])
print("Curved grades (Student 0):", report["curved_grades"][0]) 
print("Passing (Student 3):", report["passing"][3])        
print("===================================")
print("PROBLEM 4:")
cars = [
    GasCar("Toyota", "Camry", 2024, mpg=32),
    ElectricCar("Tesla", "Model 3", 2025, kwh_per_mile=0.25),
    HybridCar("Toyota", "Prius", 2024, mpg=50, electric_fraction=0.4)
]

trip_cost(cars, 300) 
print("===================================")
print("PROBLEM 5:")
w1 = Wallet("Alice")
w1["USD"] = 100.0
w1["EUR"] = 50.0
w2 = Wallet("Bob")
w2["USD"] = 75.0
w2["GBP"] = 30.0
print(w1) 
print(repr(w1)) 
print(w1["USD"]) 
print(w1["JPY"]) 
print("EUR" in w1) 
print(len(w1)) 

w3 = w1 + w2
print(w3) 
print(w3["USD"]) 
print(w3["EUR"]) 
print(w3["GBP"]) 
w4 = w1 * 2
print(w4["USD"]) 
print(w4["EUR"]) 

print(w1 == w2) 
print(w2 < w1) 

for currency in w1:
 print(f" {currency}: {w1[currency]}")

try:
 w1["USD"] = -10
except ValueError as e:
 print(f"Caught: {e}")   
print("===================================")

