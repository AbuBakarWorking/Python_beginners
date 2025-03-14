print("\nFunction")
print("Two types of Functions")
print("1. Built-in Functions")
print("2. User-defined Functions")
print("\nFunction is a block of code which only runs when it is called.")
print("\nYou can pass data, known as parameters, into a function.")
print("\nA function can return data as a result.")
print("\nIn Python, a function is defined using the def keyword:")



# def isgreater():
#     a=int(input("Enter the first number:"))
#     b=int(input("Enter the second number:"))
#     if a>b:
#         print(f"First number {a} is greater")
#     else:
#         print(f"Second number {b} is greater")
# isgreater()

# def mean():
#     a=int(input("\nEnter the first number:"))
#     b=int(input("Enter the second number:"))
#     c=int(input("Enter the third number:"))
#     d=(a+b+c)/3
#     print(f"Mean of the three numbers is {d}")
# mean()



# def square(number):
#       n = int(input("Enter any number to find its square::"))
#       print(f"Square of {n} is", n ** 2)
# square()


# def sum():
#     a = int(input("Enter Number 1::"))
#     b = int(input("Enter Number 2::"))
#     print(f"Sum of {a} and {b} is", a + b)

# sum()

# print()
# def multiply(num1,num2):
#     return num1 * num2

# print(multiply(5,6))
# print(multiply("h",5))

# print(multiply([5,6,7],5))

print()
# one method is this
# import math
# def circle(radius):
#      return math.pi * radius ** 2
# print(circle(5))

# import math
# def circle(radius):
#     area = math.pi * radius ** 2
#     circumference = 2 * math.pi * radius
    
#     print("\nArea of circle is::",area)
#     print("Circumference of circle is::",circumference)

#     print(f"\nArea of circle is::{area:.2f}")
#     print(f"Circumference of circle is::{circumference:.2f}")

# circle(6)


# def greet(name = "Advance"):
#     return "Python " + name + " course "
# print(greet("Language"))
# print(greet())


# print("Lambda Function")  
# # lambda arguments : expression 
# # lambda arguments, arguments : expression
# print("Printing Cube of number")
# cube = lambda x: x ** 3
# y= int(input("Enter any number to find its cube::"))
# print(f"The cube of {y} is ",cube(y))


# def sum_all(*args):
#     # print(*args)
#     # print(args) # touple
#     for i in args:
#         print(i * 2)
#     return sum(args)

# print("Sum is",sum_all(1,2,4))
# print("Sum is",sum_all(1,2,4,5,6))



def print_kwargs(**kwargs):
    for key, values in kwargs.items():
        print(f"{key}: {values}")




print_kwargs(name= "Abubakar", age = 23)
print_kwargs(name= "Abubakar", age = 23, subject = "DBMS")
print_kwargs(name= "Abubakar", age = 23, subject = "DBMS", location = "Karachi")



print("\nEven Generator")
def even_generator(limit):
    for i in range(2,limit+1,2):
        yield i

for num in even_generator(10):
    print(num)




print("\nEven Generator through user input")
def even_generator():
    limit = int(input("\nEnter the number limit::"))
    for i in range(2,limit+1,2):
        yield i

for num in even_generator():
    print(num)


    