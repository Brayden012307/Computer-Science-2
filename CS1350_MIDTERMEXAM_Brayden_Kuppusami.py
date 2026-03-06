print("====================================")
print("MIDTERM EXAM PART II:")
print("====================================")
print("====================================")
print("PROBLEM 1")
print("====================================")
class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email):
        
        self.contacts[name] = {"phone": phone, "email": email}

    def search(self, query):
        query = query.lower()
        results = []
        for name, info in self.contacts.items():
            
            if (query in name.lower() or 
                query in info["phone"].lower() or 
                query in info["email"].lower()):
                results.append(name)
        return results

    def merge(self, other_book):
        
        self.contacts.update(other_book.contacts)

    def export_csv(self):
        lines = []
        for name in sorted(self.contacts.keys()):
            phone = self.contacts[name]["phone"]
            email = self.contacts[name]["email"]
            lines.append(f"{name},{phone},{email}")
        return "\n".join(lines)


book1 = ContactBook()
book1.add_contact("Alice Smith", "555-1234", "alice@mail.com")
book1.add_contact("Bob Jones", "555-5678", "bob@work.com")
book1.add_contact("Carol White", "555-9999", "carol@mail.com")

print(book1.search("alice")) 
print(book1.search("555"))   
print(book1.search("mail.com")) 

book2 = ContactBook()
book2.add_contact("Alice Smith", "555-0000", "alice@new.com") 
book2.add_contact("Dave Brown", "555-4444", "dave@mail.com")   
book1.merge(book2)

print(book1.export_csv())
print("====================================")
print("====================================")
print("PROBLEM 2")
print("====================================")
class Event:
    def __init__(self, name):
        self.name = name
        self.volunteers = set()

    def add_volunteer(self, name):
        self.volunteers.add(name)

    def remove_volunteer(self, name):
        self.volunteers.discard(name) 

    def volunteer_count(self):
        return len(self.volunteers)

def find_overcommitted(events, max_events):
    counts = {}
    for event in events:
        for person in event.volunteers:
            counts[person] = counts.get(person, 0) + 1
    
    return {person for person, count in counts.items() if count > max_events}

def find_available(all_volunteers, events):
    busy = set()
    for event in events:
        busy.update(event.volunteers)
    return all_volunteers - busy

def schedule_conflict(event1, event2):
    return event1.volunteers & event2.volunteers


setup = Event("Setup")
for v in ["Alice", "Bob", "Carol", "Dave"]:
    setup.add_volunteer(v)

ceremony = Event("Ceremony")
for v in ["Carol", "Dave", "Eve", "Frank"]:
    ceremony.add_volunteer(v)

cleanup = Event("Cleanup")
for v in ["Alice", "Dave", "Frank", "Grace"]:
    cleanup.add_volunteer(v)

print(f"Setup: {setup.volunteer_count()} volunteers")
print(f"Ceremony: {ceremony.volunteer_count()} volunteers")
print(schedule_conflict(setup, ceremony)) 

events = [setup, ceremony, cleanup]
print(find_overcommitted(events, 2)) 

everyone = {"Alice", "Bob", "Carol", "Dave", "Eve", "Frank", "Grace", "Hank"}
print(find_available(everyone, events)) 
print("====================================")
print("====================================")
print("PROBLEM 3")
print("====================================")
import numpy as np

def weather_analysis(temps_2d):
    
    city_avgs = temps_2d.mean(axis=1)
    
    
    daily_avgs = temps_2d.mean(axis=0)
    
    
    hottest_day = np.argmax(daily_avgs)
    
    
    coldest_city = np.argmin(city_avgs)
    
    
    above_80 = temps_2d > 80
    
    
    city_min = temps_2d.min(axis=1, keepdims=True)
    city_max = temps_2d.max(axis=1, keepdims=True)
    normalized = (temps_2d - city_min) / (city_max - city_min)

    return {
        "city_averages": city_avgs,
        "daily_averages": daily_avgs,
        "hottest_day": hottest_day,
        "coldest_city": coldest_city,
        "above_80": above_80,
        "normalized": normalized
    }


temps = np.array([
    [72, 75, 78, 82, 85, 80, 74],
    [88, 91, 93, 95, 90, 87, 85], 
    [55, 58, 60, 62, 59, 56, 53]  
])

report = weather_analysis(temps)
print("City averages:", report["city_averages"])
print("Daily averages:", report["daily_averages"])
print("Hottest day index:", report["hottest_day"])
print("Coldest city index:", report["coldest_city"])
print("Above 80 (City 0):", report["above_80"][0])
print("Normalized (City 2):", np.round(report["normalized"][2], 2))
print("====================================")
print("====================================")   
print("PROBLEM 4") 
print("====================================")
from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name, base_price):
        self.validate_price(base_price)
        self.name = name
        self.base_price = base_price

    @abstractmethod
    def final_price(self):
        pass

    def label(self):
        
        return f"{self.name} - ${self.final_price():.2f}"

    @staticmethod
    def validate_price(price):
        if price <= 0:
            raise ValueError("Price must be greater than 0")

class DigitalProduct(Product):
    def __init__(self, name, base_price, discount_pct=0.0):
        super().__init__(name, base_price)
        self.discount_pct = discount_pct

    def final_price(self):
        
        return round(self.base_price * (1 - self.discount_pct), 2)

class PhysicalProduct(Product):
    def __init__(self, name, base_price, weight_lbs, shipping_rate=0.50):
        super().__init__(name, base_price)
        self.weight_lbs = weight_lbs
        self.shipping_rate = shipping_rate

    def final_price(self):
        return round(self.base_price + (self.weight_lbs * self.shipping_rate), 2)

class SubscriptionProduct(Product):
    def __init__(self, name, base_price, months, monthly_discount=0.10):
        super().__init__(name, base_price)
        self.months = months
        self.monthly_discount = monthly_discount

    def final_price(self):
        
        total_before_discount = self.base_price * self.months
        total_discount = self.base_price * self.monthly_discount * (self.months - 1)
        return round(total_before_discount - total_discount, 2)

def checkout(cart):
    running_total = 0.0
    for item in cart:
        price = item.final_price()
        print(item.label())
        running_total += price
    
    print(f"Total: ${running_total:.2f}")
    return running_total


cart = [
    DigitalProduct("E-book: Python 101", 29.99, discount_pct=0.20),
    PhysicalProduct("Mechanical Keyboard", 89.99, weight_lbs=2.5),
    SubscriptionProduct("Cloud Storage", 9.99, months=12)
]

total = checkout(cart)
print("====================================")
print("====================================")   
print("PROBLEM 5")
print("====================================")   
import copy

class Matrix:
    def __init__(self, rows):
        
        self.data = copy.deepcopy(rows)
        self.rows = len(rows)
        self.cols = len(rows[0]) if self.rows > 0 else 0

    def __str__(self):
        lines = []
        for row in self.data:
            lines.append(" ".join(f"{val:4}" for val in row))
        return "\n".join(lines)

    def __repr__(self):
        return f"Matrix({self.data})"

    def __getitem__(self, pos):
        r, c = pos
        return self.data[r][c]

    def __setitem__(self, pos, value):
        r, c = pos
        self.data[r][c] = value

    def __len__(self):
        return self.rows * self.cols

    def __contains__(self, value):
        return any(value in row for row in self.data)

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same shape")
        new_data = [[self.data[r][c] + other.data[r][c] for c in range(self.cols)] for r in range(self.rows)]
        return Matrix(new_data)

    def __mul__(self, scalar):
        new_data = [[val * scalar for val in row] for row in self.data]
        return Matrix(new_data)

    def _total_sum(self):
        return sum(sum(row) for row in self.data)

    def __eq__(self, other):
        return self._total_sum() == other._total_sum()

    def __lt__(self, other):
        return self._total_sum() < other._total_sum()

# --- Test Cases ---
m1 = Matrix([[1, 2, 3], [4, 5, 6]])
m2 = Matrix([[10, 20, 30], [40, 50, 60]])

print(m1)
print(repr(m1))
print(m1[0, 1]) 
m1[1, 2] = 99
print(m1[1, 2]) 
m1[1, 2] = 6    
print(len(m1))  
print(5 in m1) 
print(100 in m1) 

m3 = m1 + m2
print(m3)

m4 = m1 * 10
print(m4)

print(m1 == m2) 
print(m1 < m2)  

try:
    bad = m1 + Matrix([[1, 2]])
except ValueError as e:
    print(f"Caught: {e}")
print("====================================") 
print("====================================") 

