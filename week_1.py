# Question 1: Write a Python code that prints numbers from 1 to 10 on the screen.

# for i in range(1, 11):
#     print(i)

####################################################################################################

# Question 2: Take a number input from the user and write a Python program that prints even numbers up to this number on the screen. Do this first with 'for' and then with 'while' loops.

# What if the user enters an odd number?

# number = int(input("Enter a number: "))
# for i in range(0, number + 1, 2):
#     print(i)

# i = 0
# while i <= number:
#     print(i)
#     i += 2

####################################################################################################

# Question 3: Write a Python code that receives a start and end value from the user and prints all the numbers between these values ​​(including the end value) on the screen.

# start_number = int(input("Enter the start number: "))
# end_number = int(input("Enter the end number: "))

# for i in range(start_number, end_number + 1):
#     print(i)

####################################################################################################

# Question 4: Get a number from the user and write a Python code that prints whether this number is odd or even.

# number = int(input("Enter a number: "))

# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

####################################################################################################

# Question 5: Write a Python program that takes a positive integer input from the user and calculates its factorial. Factorial is the product of all positive integers between a number itself and 1.

# number = int(input("Enter a number: "))
# factorial = 1

# for i in range(1, number + 1):
#     factorial *= i

# print(factorial)

####################################################################################################

# Question 6: Write a Python code that receives a number from the user and checks whether this number is prime.

# number = int(input("Enter a number: "))
# is_prime = True

# if number == 0 or number == 1:
#     is_prime = False
# elif number == 2:
#     is_prime = True
# else:
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#             break

# if is_prime:
#     print("Prime")
# else:
#     print("Not Prime")

####################################################################################################

# Question 7: How to create a loop that calculates the Fibonacci sequence and returns the result as a list containing numbers up to a certain limit?

# limit = int(input("Enter a limit: "))
# list = [0, 1]

# if limit == 0:
#     list = [0]
# elif limit == 1:
#     list = [0, 1]
# else:
#     for i in range(2, limit + 1):
#         list.append(list[i - 1] + list[i - 2])

# print(list)

####################################################################################################

# Question 8: Write a Python code that takes a word from the user and prints the reverse of this word on the screen.

# word = input("Enter a word: ")
# reverse_word = ""

# for i in range(len(word) - 1, -1, -1):
#     reverse_word += word[i]

# print(reverse_word)

####################################################################################################

# Question 9: How to create a combination of loop and conditional statement that takes a word input from the user and checks whether that word is a palindrome (the same when read backwards)?

# word = input("Enter a word: ")
# is_palindrome = True

# for i in range(len(word) // 2):
#     if word[i] != word[len(word) - 1 - i]:
#         is_palindrome = False
#         break

# if is_palindrome:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

####################################################################################################

# Question 10: Write the code that calculates the person's weight index and returns the result as underweight, overweight or overweight according to the index value. (You can look on the internet for the weight index calculation)
# To do this, ask the user for their weight and height measurements. weight index
# If it is below 25, it is weak,
# Between 25-30 is normal,
# If you are over 30-40, you are overweight.
# If you are over 40, you are overweight.

# weight = float(input("Enter your weight (kg): "))
# height = float(input("Enter your height (m): "))
# weight_index = weight / (height**2)

# if weight_index < 25:
#     print("Underweight")
# elif 25 <= weight_index < 30:
#     print("Normal")
# elif 30 <= weight_index < 40:
#     print("Overweight")
# else:
#     print("Obese")

####################################################################################################

# Question 11: How to write a Python program that finds the largest of three numbers entered by a user?

# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# number3 = int(input("Enter the third number: "))

# if number1 > number2 and number1 > number3:
#     print(number1)
# elif number2 > number1 and number2 > number3:
#     print(number2)
# else:
#     print(number3)

####################################################################################################

# Question 12: Get Midterm and Final grades from a student for any course. The sum of 40% of the midterm exam grade and 60% of the final grade will give the year-end average. If the average is below 50, "FAILED" will appear on the screen, and if it is 50 or above, "SUCCESSFUL" will be displayed on the screen. This printing process is 4 lessons. and the lessons will be written one after the other.

# lessons = []
# midterm = []
# final = []

# for i in range(4):
#     input_lesson = input(f"Enter the lesson {i + 1}: ")
#     lessons.append(input_lesson)
#     input_midterm = int(input(f"Enter the midterm grade for {input_lesson}: "))
#     midterm.append(input_midterm)
#     input_final = int(input(f"Enter the final grade for {input_lesson}: "))
#     final.append(input_final)

# for i in range(4):
#     if midterm[i] * 0.4 + final[i] * 0.6 < 50:
#         print(f"{lessons[i]}: FAILED")
#     else:
#         print(f"{lessons[i]}: SUCCESSFUL")

####################################################################################################
