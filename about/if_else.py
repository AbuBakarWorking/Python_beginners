# language = str(input("Please Enter Your Favorite Language::"))


# if language == 'Python':
#     print("Correct! Of course it is Python!")




# Get the user input
# user_input = input("Enter a string: ")

# # Check if the input is "hello"
# if user_input == "Hello":
#     print("Hello back to you!")
# # Check if the input is "goodbye"
# elif user_input == "goodbye":
#     print("See you later!")
# # Check if the input is "yes" or "no"
# elif user_input.lower() == "yes" or user_input.lower() == "no":
#     print("You answered:", user_input)
# # If none of the above conditions are true, print a default message
# else:
#     print("I didn't understand that. Try again!")





# More programs
# Define a function to calculate the grade of a subject
def calculate_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"

# Get the marks of 5 subjects from the user
subject1 = float(input("Enter mark of subject 1: "))
subject2 = float(input("Enter mark of subject 2: "))
subject3 = float(input("Enter mark of subject 3: "))
subject4 = float(input("Enter mark of subject 4: "))
subject5 = float(input("Enter mark of subject 5: "))

# Calculate the total
total = subject1 + subject2 + subject3 + subject4 + subject5

# Calculate the average
average = total / 5

# Calculate the percentage
percentage = (total / 500) * 100

# Calculate the grade of each subject
grade1 = calculate_grade(subject1)
grade2 = calculate_grade(subject2)
grade3 = calculate_grade(subject3)
grade4 = calculate_grade(subject4)
grade5 = calculate_grade(subject5)

# Print the results
print("Subject 1: Mark =", subject1, ", Grade =", grade1)
print("Subject 2: Mark =", subject2, ", Grade =", grade2)
print("Subject 3: Mark =", subject3, ", Grade =", grade3)
print("Subject 4: Mark =", subject4, ", Grade =", grade4)
print("Subject 5: Mark =", subject5, ", Grade =", grade5)
print("Total: ", total)
print("Average: ", average)
print("Percentage: ", percentage)









