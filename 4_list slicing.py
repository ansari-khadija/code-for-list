# List Slicing

subjects = ["Python", "Java", "C++", "SQL", "HTML", "CSS"]

print("Subjects:", subjects)

# Basic slicing
print(" Basic Slicing ")
print("First three subjects:", subjects[0:3])
print("Subjects from index 2 to 4:", subjects[2:5])

# Slicing from the beginning
print("Slicing from Beginning ")
print("First four subjects:", subjects[:4])

# Slicing to the end
print(" Slicing to End ")
print("From third subject:", subjects[2:])

# Slicing with negative indexes
print("Negative Slicing")
print("Last three subjects:", subjects[-3:])
print("Except the last two:", subjects[:-2])

# Slicing with a step
print(" Slicing with Step ")
print("Every second subject:", subjects[::2])

# Reverse the list using slicing
print("Reverse list:", subjects[::-1])
