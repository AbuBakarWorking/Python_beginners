#this program will not add two values, but do concatenate,
#for this purpose we use type_casting in the next but same program

print("This will concatenate the two values, not add them")
a=input("Enter number 1::")
b=input("Enter number 2::")
print(a+b)
#this will concatenate the two values, not add them


print()

print("Implicit TypeCasting")

num1 = 5
num2 = 3.5
result = num1 + num2  # Implicitly converts num1 to float, result is 8.5 (float)
print(result)
print(type(result))

print()


#2. Subtraction:
num3 = 8
num4 = 2.0
result = num3 - num4  # Implicitly converts num2 to int, result is 6 (int)
print(result)
print(type(result))

print()

#3. Multiplication:
num5 = 4
num6 = 2.5
result = num5 * num6 # Implicitly converts num1 to float, result is 10.0 (float)
print(result)
print(type(result))

print()

#4. Division:
num7 = 10
num8 = 3
result = num7 / num8  # Implicitly converts both num1 and num2 to float, result is 3.3333333333333335 (float)
print(result)
print(type(result))




print()
#5. Mixed Operations:
num9 = 7
num10 = 2.0
result = num9 / num10  # Implicitly converts num1 to float, result is 3.5 (float)
print(result)
print(type(result))


print()
#6. Concatenation (for strings):
string1 = "Hello, "
string2 = "World!"
result = string1 + string2  # Implicitly converts both strings to a single string, result is "Hello, World!" (string)
print(result)
print(type(result))


print()
#7. Comparison:
num11 = 5
num12 = 3.5
result = num11 > num12  # Implicitly converts num2 to int, result is True (bool)
print(result)
print(type(result))







print()

print("Explicit TypeCasting")

print("This porgram add two numbers. Because we do type casting in it")
a1=int(input("Enter number 1::"))
b1=int(input("Enter number 2::"))
print(a1+b1)

print()

# Addition of String and Integer Using Explicit Conversion
string2 = "56"
number = 44

print("Converting the string into an integer number.")
string_number = int(string2)

sum_of_numbers = number + string_number
print("The Sum of both the numbers is: ", sum_of_numbers)


print()

string3 = "Abubakar"
floating_number = 45.20

print(string3)

print()
# Converting the string as well as integer number into floating point number.
new_str = int(string3)
new_number = int(floating_number)
print("String converted into integer: ", new_str)
print("The floating-point number converted into integer: ", new_number)


