# Example: Creating and modifying a list
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # Add item
fruits[1] = "blueberry"  # Modify item
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'orange']


# Example: Creating a tuple
person = ("Alice", 30, "Engineer")
print(person[0])  # Output: Alice
# Attempting to modify a tuple (will raise an error)
# person[1] = 31  # TypeError: 'tuple' object does not support item assignment

# Example: Using range in a loop
for i in range(5):
    print(i)
# Output: 0 1 2 3 4

# Tuples for fixed data
location = (40.7128, -74.0060)  # Coordinates (immutable, so good for safety)

# Lists for dynamic data
shopping_cart = ["milk", "bread"]
shopping_cart.append("eggs")  # You can keep adding to your cart

# Range for iteration
for step in range(1, 6):
    print(f"Step {step}")  # Used in controlled loops
