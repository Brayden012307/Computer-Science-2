print("CS1350 FINAL EXAM PART II:")
print("================================")
print("PROBLEM 1:")
print("================================")

def gradebook_summary(grades):
    student_avgs = {}
    course_totals = {}  
    top_per_course = {} 

    for student, courses in grades.items():
        all_scores = []
        for course, scores in courses.items():
            avg = sum(scores) / len(scores)
            all_scores.extend(scores)
            
            
            stats = course_totals.get(course, [0, 0])
            stats[0] += sum(scores)
            stats[1] += len(scores)
            course_totals[course] = stats
            
            
            current_top = top_per_course.get(course)
            if current_top is None or avg > current_top[1] or (avg == current_top[1] and student < current_top[0]):
                top_per_course[course] = (student, avg)
        
        student_avgs[student] = sum(all_scores) / len(all_scores)

    return {
        "student_averages": student_avgs,
        "course_averages": {c: s[0]/s[1] for c, s in course_totals.items()},
        "top_per_course": {c: v[0] for c, v in top_per_course.items()}
    }

print("\n--- Problem 1 Output ---")
grades_data = {
    "alice": {"CS1350": [85, 92, 78], "MATH201": [90, 88]},
    "bob": {"CS1350": [72, 75, 80], "PHYS100": [65, 70]},
    "carol": {"CS1350": [95, 98, 92], "MATH201": [85, 90]},
}
print(gradebook_summary(grades_data))

print("================================")
print("PROBLEM 2:")
print("================================")
def skill_analysis(candidates, required):
    req_set = set(required)
    fully_qualified = []
    
    
    for name, skills in candidates.items():
        if req_set <= skills: 
            fully_qualified.append(name)
    
    
    def match_score(name):
        return (len(candidates[name] & req_set), [-ord(c) for c in name])
    best_match = max(candidates.keys(), key=match_score)

    
    unique_skills = {}
    for name, skills in candidates.items():
        others = set().union(*(s for n, s in candidates.items() if n != name))
        unique = sorted(list(skills - others))
        if unique:
            unique_skills[name] = unique

    return {
        "fully_qualified": sorted(fully_qualified),
        "best_match": best_match,
        "unique_skills": unique_skills
    }

print("\n--- Problem 2 Output ---")
candidates = {
    "alice": {"python", "sql", "git", "docker"},
    "bob": {"python", "java", "git"},
    "carol": {"python", "sql", "git", "docker", "kubernetes"},
    "dave": {"java", "c++"},
    "eve": {"python", "sql"},
}
required = {"python", "sql", "git"}
print(skill_analysis(candidates, required))

print("================================")
print("PROBLEM 3:")
print("================================")
import re


HASHTAG_RE = re.compile(r'#(\w+)')
MENTION_RE = re.compile(r'@(\w+)')
URL_RE = re.compile(r'(https?://\S+)')

def parse_post(text):
    def get_unique(pattern, string):
        seen = set()
        results = []
        for item in pattern.findall(string):
            if item not in seen:
                results.append(item)
                seen.add(item)
        return results

    return {
        "hashtags": get_unique(HASHTAG_RE, text),
        "mentions": get_unique(MENTION_RE, text),
        "urls": get_unique(URL_RE, text)
    }

print("\n--- Problem 3 Output ---")
sample_text = """
Check out #Python and #python tips by @alice_dev and @Bob!
Links: https://example.com/path?q=1 and http://foo.org.
Re-ping @alice_dev and share #Python again.
"""
print(parse_post(sample_text))

print("================================")
print("PROBLEM 4:")
print("================================")
class CartItem:
    def __init__(self, name: str, price: float, quantity: int = 1):
        
        if price < 0 or quantity <= 0:
            raise ValueError("Price must be >= 0 and quantity must be > 0")
        
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def subtotal(self):
        """Returns price * quantity"""
        return self.price * self.quantity

    def __repr__(self):
        """Returns a string like CartItem('apple', 1.50, 3)"""
        return f"CartItem({self.name!r}, {self.price:.2f}, {self.quantity})"


class ShoppingCart:
    def __init__(self):
        
        self.items = []

    def add(self, item: CartItem):
        """Appends an item to the cart"""
        self.items.append(item)

    def remove(self, name: str):
        """Removes the first item whose name matches; raises KeyError if not found"""
        for i, item in enumerate(self.items):
            if item.name == name:
                return self.items.pop(i)
        raise KeyError(f"Item '{name}' not found in cart")

    def total_before_tax(self):
        """Returns the sum of all item subtotals"""
        return sum(item.subtotal for item in self.items)

    def total_with_tax(self, tax_rate=0.08):
        """Returns the total with tax applied"""
        before_tax = self.total_before_tax()
        return before_tax * (1 + tax_rate)

    def __len__(self):
        """Number of items (list length, counting each CartItem once)"""
        return len(self.items)

    def __contains__(self, name):
        """Returns True if any item with that name is in the cart"""
        return any(item.name == name for item in self.items)

    def __iter__(self):
        """Iterates over the cart's CartItems"""
        return iter(self.items)

    def __repr__(self):
        """Returns ShoppingCart(items=[...]) using each item's __repr__"""
        return f"ShoppingCart(items={self.items!r})"


cart = ShoppingCart()
cart.add(CartItem("apple", 1.50, 3))
cart.add(CartItem("bread", 4.00))
cart.add(CartItem("milk", 3.25, 2))


print(len(cart))                       
print("apple" in cart)                 
print("butter" in cart)                
print(cart.total_before_tax())         


print(round(cart.total_with_tax(), 2)) 

for item in cart:
    print(item.name, item.subtotal)    

cart.remove("bread")                   
try:
    cart.remove("butter")              
except KeyError as e:
    print(f"Caught expected error: {e}")

try:
    CartItem("lemon", -1)              
except ValueError as e:
    print(f"Caught expected error: {e}")

print("===============================")
print("PROBLEM 5:")
print("===============================")
def subset_sum(nums, target):
    
    if target == 0:
        return True
    
    
    if not nums:
        return False

    
    
    first = nums[0]
    remaining = nums[1:]
    
    
    include = subset_sum(remaining, target - first)
    
    
    exclude = subset_sum(remaining, target)
    
    
    return include or exclude


test_data = [
    ([3, 34, 4, 12, 5, 2], 9, True),   
    ([3, 34, 4, 12, 5, 2], 30, False), 
    ([1, 2, 3], 0, True),              
    ([], 0, True),
    ([], 5, False),
    ([-2, 3, 5], 1, True),             
    ([1, 2, 3], 7, False)
]

print(f"{'Input':<30} | {'Target':<7} | {'Expected':<8} | {'Result'}")
print("-" * 65)

for nums, target, expected in test_data:
    actual = subset_sum(nums, target)
    status = " PASS" if actual == expected else " FAIL"
    print(f"{str(nums):<30} | {target:<7} | {str(expected):<8} | {status}")