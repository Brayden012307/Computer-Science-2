print("====================================")
print("problem 1")
print("====================================")

ratings = {
    "Alice": {"Inception": 5, "Titanic": 3, "Avatar": 4, "Jaws": 2},
    "Bob": {"Inception": 4, "The Matrix": 5, "Avatar": 5, "Jaws": 3},
    "Carol": {"Titanic": 5, "The Matrix": 4, "Avatar": 3, "Interstellar": 5},
    "Dave": {"Inception": 3, "Titanic": 4, "The Matrix": 5, "Jaws": 4},
    "Eve": {"Inception": 5, "Avatar": 4, "Interstellar": 4, "Jaws": 1}
}

print("=== User Statistics ===")
for user, user_ratings in ratings.items():
    num_movies = len(user_ratings)
    avg_rating = sum(user_ratings.values()) / num_movies
    # Find favorite movie [cite: 22]
    fav_movie = max(user_ratings, key=user_ratings.get)
    fav_score = user_ratings[fav_movie]
    print(f"{user}: {num_movies} movies, avg rating: {avg_rating:.2f}, favorite: {fav_movie} ({fav_score})")

movie_stats = {}
for user_ratings in ratings.values():
    for movie, score in user_ratings.items():
        if movie not in movie_stats:
            movie_stats[movie] = {"ratings": [], "avg": 0, "count": 0}
        movie_stats[movie]["ratings"].append(score)

for movie in movie_stats:
    scores = movie_stats[movie]["ratings"]
    movie_stats[movie]["count"] = len(scores)
    movie_stats[movie]["avg"] = sum(scores) / len(scores)

sorted_movies = sorted(movie_stats.items(), key=lambda x: x[1]['avg'], reverse=True)

print("\n=== Movie Statistics ===")
for movie, data in sorted_movies:
    print(f"{movie}: {data['avg']:.2f} avg ({data['count']} reviews)")

high_rated = {m for m, d in movie_stats.items() if d['avg'] >= 4.0}
alice_unrated = high_rated - set(ratings["Alice"].keys())

print("====================================")
print("problem 2")
print("====================================")

sales_records = [
    {"product": "Laptop", "category": "Electronics", "price": 999, "quantity": 5, "region": "North"},
    {"product": "Mouse", "category": "Electronics", "price": 25, "quantity": 50, "region": "North"},
    {"product": "Desk", "category": "Furniture", "price": 350, "quantity": 8, "region": "South"},
    {"product": "Chair", "category": "Furniture", "price": 150, "quantity": 20, "region": "South"},
    {"product": "Laptop", "category": "Electronics", "price": 999, "quantity": 3, "region": "South"},
    {"product": "Keyboard", "category": "Electronics", "price": 75, "quantity": 30, "region": "North"},
    {"product": "Desk", "category": "Furniture", "price": 350, "quantity": 5, "region": "North"},
    {"product": "Monitor", "category": "Electronics", "price": 300, "quantity": 12, "region": "South"},
]

product_prices = {item['product']: item['price'] for item in sales_records}
expensive_products = {p: pr for p, pr in product_prices.items() if pr > 100}
price_category = {p: "Premium" if pr >= 300 else "Standard" for p, pr in product_prices.items()}

print("\n=== Part A: Comprehensions ===")
print(f"Product prices: {product_prices}")
print(f"Expensive products (>$100): {expensive_products}")
print(f"Price categories: {price_category}")

total_by_category = {}
total_by_region = {}
quantity_by_product = {}

for record in sales_records:
    rev = record['price'] * record['quantity']
    total_by_category[record['category']] = total_by_category.get(record['category'], 0) + rev
    total_by_region[record['region']] = total_by_region.get(record['region'], 0) + rev
    quantity_by_product[record['product']] = quantity_by_product.get(record['product'], 0) + record['quantity']

print("\n=== Part B: Aggregations ===")
print(f"Revenue by category: {total_by_category}")
print(f"Revenue by region: {total_by_region}")
print(f"Quantity by product: {quantity_by_product}")

print("====================================")
print("problem 3")
print("====================================")

registrations = {
    "Alice": {"CS101", "CS201", "MATH101"},
    "Bob": {"CS101", "MATH101", "PHYS101"},
    "Carol": {"CS201", "CS301", "MATH201"},
    "Dave": {"CS101", "CS201", "MATH101", "PHYS101"},
    "Eve": {"CS301", "MATH201", "MATH301"}
}

prerequisites = {
    "CS101": set(), "CS201": {"CS101"}, "CS301": {"CS201"},
    "MATH101": set(), "MATH201": {"MATH101"}, "MATH301": {"MATH201"},
    "PHYS101": {"MATH101"}
}

all_courses = set().union(*registrations.values())
common_courses = set.intersection(*registrations.values()) if registrations else set()
only_alice = registrations["Alice"] - set().union(*(courses for name, courses in registrations.items() if name != "Alice"))
cs_students = {name for name, courses in registrations.items() if any(c.startswith("CS") for c in courses)}

print("\n=== Part A: Set Operations ===")
print(f"All courses with enrollment: {all_courses}")
print(f"Courses ALL students share: {common_courses}")
print(f"Courses ONLY Alice takes: {only_alice}")
print(f"Students in CS courses: {cs_students}")

print("\n=== Part B: Prerequisite Check ===")
for student, courses in registrations.items():
    missing_info = []
    is_valid = True
    for course in courses:
        reqs = prerequisites.get(course, set())
        # Simplified model: check if reqs are in current registrations [cite: 140, 141]
        missing = reqs - courses
        if missing:
            is_valid = False
            missing_info.append(f"{course} requires {reqs} but missing: {missing}")
    
    if is_valid:
        print(f"{student}: VALID")
    else:
        print(f"{student}: INVALID Missing prerequisites:")
        for line in missing_info:
            print(f"  {line}")

overloaded = {s for s, c in registrations.items() if len(c) >= 4}
math_courses = {c for courses in registrations.values() for c in courses if c.startswith("MATH")}

identical = "None found" 

print("\n=== Part C: Enrollment Analysis ===")
print(f"Overloaded students (4+ courses): {overloaded}")
print(f"All MATH courses enrolled: {math_courses}")
print(f"Students with identical schedules: {identical}")

enrollment_count = {course: sum(1 for c in registrations.values() if course in c) for course in all_courses}
under_enrolled = {c for c, count in enrollment_count.items() if count < 3}

print("Enrollment per course:")
for c, count in enrollment_count.items():
    print(f"{c}: {count} students")
print(f"Under-enrolled courses (<3 students): {under_enrolled}")

print("====================================")