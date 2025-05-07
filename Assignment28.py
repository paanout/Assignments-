import matplotlib.pyplot as plt

# Generate numbers from 1 to 1000
numbers = list(range(1, 1001))

# Compute the squares of the numbers
squares = [x**2 for x in numbers]

# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(numbers, squares, color='blue', linewidth=2)
plt.title('Squares of Numbers from 1 to 1000')
plt.xlabel('Number')
plt.ylabel('Square of Number')
plt.grid(True)
plt.tight_layout()
plt.show()
