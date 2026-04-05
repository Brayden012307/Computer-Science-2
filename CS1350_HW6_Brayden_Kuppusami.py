print("==========================")
print("WEEK11 L1-UNIT 1:BEGINNER")
print("==========================")

import re

text = "The price is $49.99 today"
match = re.search(r"\$\d+\.\d{2}", text)

if match:
   
    print(f"Price: {match.group()}")

    
    start = match.start()
    end = match.end()
    print(f"Start: {start}, End: {end}")

    
    s, e = match.span()
    before = text[:s]
    after = text[e:]
    
    print(f"Before: '{before}'")
    print(f"After: '{after}'")
print("==========================")
print("WEEK11 L1-UNIT 1:INTERMEDIATE")
print("==========================")
import re

sentences = [
    "This is is a problem",
    "The the cat sat down",
    "No duplicates here",
    "I really really like Python",
]

for sentence in sentences:
     
    match = re.search(r"\b(\w+)\s+\1\b", sentence, re.IGNORECASE)

    if match:
        print(f"Duplicate '{match.group(1)}' in: {sentence}")
    else:
        print(f"No duplicates in: {sentence}")
print("==========================")
print("WEEK11 L1-UNIT 1:ADVANCED")
print("==========================")
import re

records = [
    "Name: Alice Smith | ID: EMP-001 | Dept: Engineering",
    "Name: Bob Jones | ID: EMP-042 | Dept: Marketing",
    "Name: Carol White | ID: EMP-108 | Dept: Sales",
]

pattern = r"Name: (?P<name>.*?) \| ID: (?P<id>.*?) \| Dept: (?P<dept>.*)"

for record in records:
    match = re.search(pattern, record)
    if match:
        d = match.groupdict()
        
        print(f"Employee: {d['name']} (ID: {d['id']}) works in {d['dept']}")
        
        
        id_span = match.span("id")
        print(f"  ID location: {id_span}")
print("==========================")
print("WEEK11 L1-UNIT 2:BEGINNER")
print("==========================")
import re

texts = [
    "Alice is 20 years old",
    "Bob is 22 years old",
    "Charlie is 19 years old",
]

for text in texts:
    
    match = re.search(r"^(\w+) is (\d+) years old", text)

    if match:
        name = match.group(1)
        age = match.group(2)
        print(f"Name: {name}, Age: {age}")
print("==========================")
print("WEEK11 L1-UNIT 2:INTERMEDIATE")
print("==========================")
import re

dates = ["03-15-2026", "12-25-2025", "01-01-2000"]

for date in dates:
    
    pattern = r"(?P<month>\d{2})-(?P<day>\d{2})-(?P<year>\d{4})"
    match = re.search(pattern, date)
    
    if match:
        
        info = match.groupdict()
        print(f"{info['month']}/{info['day']}/{info['year']}")
print("==========================")
print("WEEK11 L1-UNIT 2:ADVANCED")
print("==========================")
import re

log_entries = [
    "[2026-03-10 14:30:45] Server started",
    "[2026-03-10 09:15:02] User login",
    "[2026-03-11 22:00:00] Backup complete",
]

for entry in log_entries:
   
    pattern = r"\[(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2})\] (?P<message>.*)"
    
    match = re.search(pattern, entry)
    if match:
        d = match.groupdict()
        
        print(f"At {d['time']} on {d['date']}, the log reported: {d['message']}")
print("==========================")
print("WEEK11 L1-UNIT 3:BEGINNER")
print("==========================")    
import re

texts = [
    "Hello there!",
    "Hi everyone.",
    "Hey you!",
    "Goodbye now.",
    "Howdy partner!"
]

for text in texts:
   
    match = re.search(r"^(Hello|Hi|Hey)", text)

    if match:
        print(f"Greeting found: '{match.group(1)}' in '{text}'")
    else:
        print(f"No greeting in: '{text}'")    
print("==========================")
print("WEEK11 L1-UNIT 3:INTERMEDIATE")
print("==========================")
import re

files = ["report.pdf", "photo.jpg", "data.csv", "script.py", "style.css", "image.png"]

for f in files:
    lower_f = f.lower()

    
    is_doc = re.search(r"\.(pdf|doc|txt|csv)$", lower_f)
    is_img = re.search(r"\.(jpg|jpeg|png|gif)$", lower_f)
    is_code = re.search(r"\.(py|js|html|css)$", lower_f)

    if is_doc:
        category = f"Document ({is_doc.group(1)})"
    elif is_img:
        category = f"Image ({is_img.group(1)})"
    elif is_code:
        category = f"Code ({is_code.group(1)})"
    else:
        category = "Other"

    print(f"{f:<15} -> {category}")
print("==========================")
print("WEEK11 L1-UNIT 3:ADVANCED")
print("==========================")
import re

dates = [
    "2026-03-15",   # ISO
    "03/15/2026",   # US
    "15 Mar 2026",  # Text
    "March 15, 2026", # Long
    "not a date",
]

for date in dates:
    
    iso = re.search(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})", date)
    
    
    us = re.search(r"(?P<month>\d{2})/(?P<day>\d{2})/(?P<year>\d{4})", date)
    
    
    text_fmt = re.search(r"(?P<day>\d{1,2}) (?P<month>[A-Z][a-z]{2}) (?P<year>\d{4})", date)
    
    
    long_fmt = re.search(r"(?P<month>[A-Z][a-z]+) (?P<day>\d{1,2}), (?P<year>\d{4})", date)

    matched = iso or us or text_fmt or long_fmt
    
    if matched:
        d = matched.groupdict()
        print(f"'{date}' -> month={d['month']}, day={d['day']}, year={d['year']}")
    else:
        print(f"'{date}' -> no match")
print("==========================")
print("==========================")
print("WEEK12 L2-UNIT 1:BEGINNER")     
print("==========================")
import re

texts = ["Python is great", "I love Python", "PYTHON", "python3"]

for text in texts:
    
    m = re.match(r"Python", text)
    
    
    s = re.search(r"Python", text)
    
    starts = "yes" if m else "no"
    contains = "yes" if s else "no"
    print(f"'{text}' - starts with Python: {starts}, contains Python: {contains}")   
print("==========================")
print("WEEK12 L2-UNIT 1:INTERMEDIATE")
print("==========================")
import re

text = """
Student grades: Alice-92, Bob-78, Charlie-85, Diana-95.
Room numbers: A101, B204, C310.
Emails: alice@school.edu, bob@school.edu.
"""


name_scores = re.findall(r"([A-Z][a-z]+)-(\d+)", text)
print(f"Scores: {name_scores}")


rooms = re.findall(r"[A-Z]\d{3}", text)
print(f"Rooms: {rooms}")


emails = re.findall(r"[a-z]+@[a-z]+\.[a-z]+", text)
print(f"Emails: {emails}")
print("==========================")
print("WEEK12 L2-UNIT 1:ADVANCED")
print("==========================")
import re

csv_lines = [
    "Alice,Smith,25,Engineer,alice@corp.com",
    "Bob,Jones,30,Designer,bob@corp.com",
    "Carol,White,28,Manager,carol@corp.com",
]

for line in csv_lines:
    
    match = re.match(r"(\w+),(\w+),(\d+),(\w+),([\w\.-]+@[\w\.-]+)", line)

    if match:
        first, last, age, role, email = match.groups()
        
        
        age_num = int(age)
        valid_age = 18 <= age_num <= 65
        
       
        status = "✅" if valid_age else "⚠️ age"
        print(f"{status} {first} {last} ({age}), {role}, {email}")
print("==========================")
print("WEEK12 L2-UNIT 2:BEGINNER")     
print("==========================")
import re

text = "The cat sat on the mat near the bat"


result = re.sub(r"\b\wat\b", "___", text)
print(result)


result2 = re.sub(r"\b\wat\b", "___", text, count=1)
print(result2)
print("==========================")
print("WEEK12 L2-UNIT 2:INTERMEDIATE")     
print("==========================")
import re

phones = [
    "555-123-4567",
    "555.123.4567",
    "5551234567",
]

for phone in phones:
    
    digits = re.sub(r"\D", "", phone)
    
    
    formatted = re.sub(r"(\d{3})(\d{3})(\d{4})", r"(\1) \2-\3", digits)
    
    print(f"{phone:<15} -> {formatted}")
print("==========================")
print("WEEK12 L2-UNIT 2:ADVANCED")     
print("==========================")
import re

text = "Python was created in 1991. Version 3.0 came in 2008. Now it's 2026."


for match in re.finditer(r"\d{4}", text):
    start, end = match.span()
    ctx_start = max(0, start - 10)
    ctx_end = min(len(text), end + 10)
    context = text[ctx_start:ctx_end]
    
    
    print(f"Year: {match.group()} at {start}-{end} | Context: '...{context}...'")


def add_100(match):
    return str(int(match.group()) + 100)

result = re.sub(r"\d+", add_100, text)
print(f"\nAfter adding 100: {result}")
print("==========================")
print("WEEK12 L2-UNIT 3:BEGINNER")     
print("==========================")
import re


cap_word = re.compile(r"\b[A-Z]\w*")

texts = [
    "Alice met Bob in Paris",
    "the quick brown Fox",
    "No Capitals at the End except Here",
]

for text in texts:
    
    matches = cap_word.findall(text)
    print(f"Capitalized words: {matches}")
print("==========================")
print("WEEK12 L2-UNIT 3:INTERMEDIATE")
print("==========================")
import re

date_pattern = re.compile(r"""
    ^           
    (\d{2})     
    /           
    (\d{2})     
    /           
    (\d{4})     
    $           
""", re.VERBOSE)

tests = ["03/15/2026", "3/15/2026", "03-15-2026", "12/25/2025"]
for t in tests:
    match = date_pattern.match(t)
    if match:
        print(f"✅ {t} -> month={match.group(1)}, day={match.group(2)}, year={match.group(3)}")
    else:
        print(f"❌ {t}")
print("==========================")
print("WEEK12 L2-UNIT 3:ADVANCED")
print("==========================")
import re

class Validator:
    
    
    _email = re.compile(r"^[\w\.-]+@[\w\.-]+\.[a-z]{2,3}$", re.IGNORECASE)
    _phone = re.compile(r"^\d{3}-\d{3}-\d{4}$")
    _zip   = re.compile(r"^\d{5}(-\d{4})?$")
    _date  = re.compile(r"^\d{4}-\d{2}-\d{2}$")

    @classmethod
    def is_email(cls, text):
        return cls._email.match(text) is not None

    @classmethod
    def is_phone(cls, text):
        
        return cls._phone.match(text) is not None

    @classmethod
    def is_zip(cls, text):
        
        return cls._zip.match(text) is not None

    @classmethod
    def is_date(cls, text):
        
        return cls._date.match(text) is not None

# --- Test Suite ---

tests = {
    "is_email": ["alice@example.com", "not-an-email", "bob@site.org"],
    "is_phone": ["555-123-4567", "5551234567", "55-123-4567"],
    "is_zip":   ["46802", "46802-1234", "4680", "ABCDE"],
    "is_date":  ["2026-03-15", "03/15/2026", "2026-13-01"],
}



for method_name, cases in tests.items():
    
    method = getattr(Validator, method_name)
    
    print(f"\n{method_name}:")
    for case in cases:
        result = method(case)
        icon = "✅" if result else "❌"
        print(f"{icon} {case}")

print("\n============================")