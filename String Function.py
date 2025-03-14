s = "Welcome to Python programming"
z = "Abubakar"
n = '12345'
v = "abubakar123"

# Print the original string
print("Original String:", s)

# Convert string to lower case
print("\nString in lower form:")
a = s.lower()
print(a)

# Convert string to upper case
print("\nString in upper form:")
b = s.upper()
print(b)

# Convert string to title case
print("\nString in title form:")
c = s.title()
print(c)

# Capitalize the first character of the string
print("\nString in capitalize form:")
d = s.capitalize()
print(d)

# Find function: Returns the index of the first occurrence of the substring, or -1 if not found
print("\nFind Function:")
print("It will print the index value of the first occurrence of 'e' [1]:")
print(s.find("e"))

# Find function with a starting index: Counts after the given index
print("\nHere I give the starting index value 2, now it counts after 2:")
print(s.find("e", 2))

# Find function: If the character is not present in the string, it will return -1
print("\nIf the character is not present in the string, it will return -1:")
print(s.find("z"))

# Index function: Similar to find but raises an error if the substring is not found
print("\nIndex Function:")
print("It will print the index value of the first occurrence of 'e' [1]:")
print(s.index("e"))

# Index function: Raises an error if the character is not present in the string
print("\nIf the character is not present, it will raise an error:")
try:
    print(s.index("z"))
except ValueError as e:
    print(f"Error: {e}")

# Isalpha function: Checks if all characters in the string are alphabetic
print("\nIsalpha Function:")
print(f"'{z}' contains only alphabetic characters:")
print(z.isalpha())

# Isdigit function: Checks if all characters in the string are digits
print("\nIsdigit Function:")
print(f"'{n}' contains only digits:")
print(n.isdigit())
print(f"'{z}' contains only digits:")
print(z.isdigit())

# Isalnum function: Checks if all characters in the string are alphanumeric (letters or digits)
print("\nIsalnum Function:")
print(f"'{v}' contains only alphanumeric characters:")
print(v.isalnum())
