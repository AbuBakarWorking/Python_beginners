range(6)
#by-default Start from 0
#by-default condition<6
#increment 1



range(1,5)
#Start from 1
#condition<5
#increment 1

range(1,5,2)
#Start from 1
#condition<5
#define increment by 2

# for loop with range function
for n in range(7):
    print(n)

print()

for n in range(1,9):
    print(n)

print()
#add increment by 2
print("Start from 1 goes up to 9 with increment of 2")
for n in range(1,10,2):
    print(n)


print()
print("Print 3 times shapatar")
for n in range(3):
    print("Shapatar")


print()   
print("Printing table by using for loop")
for n in range(1,11):
    print("2 *",n,"=",2*n)


#user input
# print()
# print("user will give input to print any table") 
# n=int(input(" Enter Number by your choice! "))
# for i in range(1,11):
#     print(n,"*",i,"=",n*i)
print()



# Exercise 1: Print First 10 natural numbers using while loop
count = 1
while count < 10:
    print(count)
    count += 1


# Reverse List
print()
list1 = [1,2,8,9,10]
list = reversed(list1)
for item in list:
   print("Reverse List", item)

print()
# Some of cube from 1 to given Number!
def print_cubes(n): 
 for i in range(1, n+1):
        cube = i ** 3 
        print(f"The Number of {i} is {cube}") # type: ignore

given_number = int(input(" Enter Number "))  
print_cubes(given_number)





