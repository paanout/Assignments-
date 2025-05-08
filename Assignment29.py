import matplotlib.pyplot as plt

# Initial Parameters
P0 = 1000       # Initial population
r = 0.05        # Growth rate (5%)
years = 20      # Time duration

# Using FOR loop
population_for = []
P = P0
for t in range(years + 1):
    population_for.append(P)
    P = P * (1 + r)

# Using WHILE loop
population_while = []
P = P0
t = 0
while t <= years:
    population_while.append(P)
    P = P * (1 + r)
    t += 1

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(range(years + 1), population_for, label='For Loop', marker='o')
plt.plot(range(years + 1), population_while, label='While Loop', marker='x', linestyle='--')
plt.title('Population Growth Over Time')
plt.xlabel('Years')
plt.ylabel('Population')
plt.legend()
plt.grid(True)
plt.show()
