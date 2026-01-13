tracker = {}

tracker["Alice"] = 85
tracker["Bob"] = 78
tracker["Carol"] = 92
print("After adding:", tracker)

tracker["Bob"] = 82 
print("After update:", tracker)

dropped = tracker.pop("Carol")
print(f"Carol dropped with grade: {dropped}")
print("Final roster:", tracker)


grades_list = [85, 78] 

grades_dict = {"Alice": 85, "Bob": 78} 


shopping_cart = {}


shopping_cart["Apple"] = 0.99
shopping_cart["Bread"] = 2.50
shopping_cart["Milk"] = 3.99


shopping_cart["Bread"] = 2.75


removed_item = "Apple"
removed_price = shopping_cart.pop(removed_item)
print(f"Removed: {removed_item} (Price: ${removed_price})")


print("Final Shopping Cart:", shopping_cart)


total_price = sum(shopping_cart.values())
print(f"Total Price: ${total_price:.2f}")