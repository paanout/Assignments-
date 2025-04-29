# Sample data representing smart meter readings (timestamp, energy usage in kWh)
readings = [
    "2025-04-29 08:00, 1.23\n",
    "2025-04-29 09:00, 1.45\n",
    "2025-04-29 10:00, 1.67\n"
]

# 1. open() with 'w' mode to create a new file and write the readings
with open("smart_meter.txt", "w") as fh:
    fh.writelines(readings)  # 8. fh.writelines(S)

# 2. open() with 'a' mode to append a new reading
with open("smart_meter.txt", "a") as fh:
    fh.write("2025-04-29 11:00, 1.89\n")  # 7. fh.write(s)

# 3. open() with 'r' mode to read the file
with open("smart_meter.txt", "r") as fh:
    content = fh.read()  # 4. fh.read()
    print("Full content using fh.read():\n", content)

# Reopen to demonstrate fh.readline() and fh.readlines()
with open("smart_meter.txt", "r") as fh:
    line1 = fh.readline()  # 5. fh.readline()
    print("First line using fh.readline():", line1.strip())

    # Reading remaining lines
    remaining_lines = fh.readlines()  # 6. fh.readlines()
    print("Remaining lines using fh.readlines():")
    for line in remaining_lines:
        print(line.strip())

# 9. fh.close() is automatically handled with 'with' blocks (best practice),
# but shown explicitly below for reference:

fh = open("smart_meter.txt", "r")
# perform some reading
fh.close()  # 9. fh.close()
