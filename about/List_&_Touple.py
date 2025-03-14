my_list =  [1,2,3,4,5,3,4, 'abubakar','List','zayn']
list1 = []
list2 = list((1,2,3,4)) #List in a Touple
random_List = [24,7,5,9,21]


print(my_list)
print(list1)
print(list2)


print()

print("List Indexing")
print(my_list[2]) #Third Element


print()

print("Adding New Element")
my_list.append('Shapatar')
print(my_list)

print()


print("Removing List Element")
list2.pop()
print(list2)

# We Can Also Use Remove build_in function
my_list.remove(2)
print(my_list)

print()
print("This is Random List")
print(random_List)




print()
print("Sorting List")
random_List.sort()
print(random_List)


print()
print("Reversing List")
random_List.reverse()
print(random_List)



print()
print("Index Element")
random_List.index(21)
print(random_List)

print()
print(my_list.count(3)) # 3 is present 2 times in list
print("Counting that which number is multiple_times in list")


print()
print("Nested List") 
nested = [13,5,'shan',['a','b',7,8],'yes',2] #List in List
print(nested)

print()
print()



print("Touple")
t = (1,2,4,3,8,9,7,2,3,4)
print(t)
print("Index of 4 in touple is ", t.index(4))
print("Size of Touple:: ",t.__sizeof__())
print("Length of Touple ",len(t))
print(" Counting that which number is multiple_times in Touple (4 is present 2 time in touple) == ",t.count(4))
print("Is 4 present in touple or not=", t.__contains__(4))

print()

fruits = ("apple", "banana", "orange", "apple", "kiwi", "apple")
print(fruits)
print()
apple_count = fruits.count("apple")
print("Number of times 'apple' appears in the tuple: ", apple_count)










# print("Welcome to the List Program!")

# while True:
#     response = input("Do you want to create a list? (yes/no): ")
#     if response.lower() == "yes":
#         my_list = []
#         print("List created! Here are your options:")
#         while True:
#             print("1. Append an element")
#             print("2. Remove an element")
#             print("3. Pop an element")
#             print("4. Indexing")
#             print("5. Sort the list")
#             print("6. Reverse the list")
#             print("7. Get the length of the list")
#             print("8. Show the list")
#             print("9. Clear the list")
#             print("0. Exit")
#             choice = input("Enter your choice: ")
#             if choice == "1":
#                 element = input("Enter an element to append: ")
#                 my_list.append(element)
#                 print("Element appended!")
#             elif choice == "2":
#                 element = input("Enter an element to remove: ")
#                 if element in my_list:
#                     my_list.remove(element)
#                     print("Element removed!")
#                 else:
#                     print("Element not found in the list!")
#             elif choice == "3":
#                 if len(my_list) > 0:
#                     element = my_list.pop()
#                     print(f"Element {element} popped!")
#                 else:
#                     print("List is empty!")
#             elif choice == "4":
#                 index = int(input("Enter an index: "))
#                 if index < len(my_list):
#                     print(f"Element at index {index}: {my_list[index]}")
#                 else:
#                     print("Index out of range!")
#             elif choice == "5":
#                 my_list.sort()
#                 print("List sorted!")
#             elif choice == "6":
#                 my_list.reverse()
#                 print("List reversed!")
#             elif choice == "7":
#                 print(f"Length of the list: {len(my_list)}")
#             elif choice == "8":
#                 print("Current List!", my_list)
#                 break
#             elif choice == "9":
#                 my_list.clear()
#                 print("List cleared!")
#             elif choice == 0:
#                 print("Exiting the program!")
#             else:
#                 print("Invalid choice! Try again.")
#     elif response.lower() == "no":
#         print("Exiting the program!")
#         break
#     else:
#         print("Invalid response! Try again.")