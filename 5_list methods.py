#List Methods

subjects = ["Python", "Java", "Python", "C++", "SQL", "Python"]

print("Original Subjects:", subjects)

#count() method
print("\n--- count() Method ---")
print("Python appears:", subjects.count("Python"), "times")
print("Java appears:", subjects.count("Java"), "time")

#index() method
print("\n--- index() Method ---")
print("First occurrence of Python:", subjects.index("Python"))
print("Position of Java:", subjects.index("Java"))
print("Position of SQL:", subjects.index("SQL"))

#append() method
print("\n--- append() Method ---")
subjects.append("HTML")
print("After append:", subjects)

#insert() method
print("\n--- insert() Method ---")
subjects.insert(1, "CSS")
print("After insert:", subjects)

#extend() method
print("\n--- extend() Method ---")
subjects.extend(["JavaScript", "PHP"])
print("After extend:", subjects)

#remove() method
print("\n--- remove() Method ---")
subjects.remove("PHP")
print("After remove:", subjects)

#pop() method
print("\n--- pop() Method ---")
removed_subject = subjects.pop()
print("Removed subject:", removed_subject)
print("After pop:", subjects)

#sort() method
print("\n--- sort() Method ---")
subjects.sort()
print("After sort:", subjects)

#reverse() method
print("\n--- reverse() Method ---")
subjects.reverse()
print("After reverse:", subjects)

#clear() method
print("\n--- clear() Method ---")
subjects.clear()
print("After clear:", subjects)
