#  # Input: positive integer n
# n = int(input("Enter a positive integer: "))

# # Initialize sum variable
# total_sum = 0

# # Use a for loop to add each number from 1 to n
# for i in range(1, n + 1):
#     total_sum += i
# # Print the result
# print("The sum of numbers from 1 to", n, "is:", total_sum)



# CHAT FIRST # Input: integer num
# num = int(input("Enter a number: "))

# # Use a for loop to print the multiplication table
# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")



# CHAT FIRST# list = [1, 2, 3, 4, 5, 6]
# even = 0
# odd = 0
# for i in list:
#     if i%2==0:
#         even += 1
#     elif i%2 != 0:
#         odd += 1

# print(even)
# print(odd)


# CHAT FIRST# str = "Hello"
# new_str = ""
# for i in str:
#     new_str =  str[::-1]
# print(new_str)


# CHAT FIRST# list = [5, 1, 9, 6, 3]
# max = list[0]
# for i in list:
#     if i > max:
#         max = i
# print(max)


# ME # list  = [1, 2, 3, 4, 5, 6]
# count = 0
# for i in list:
#     if i%2 == 0:
#         count += 1
# print(count)


# ME #n = [1, 2, 3, 4, 5]
# new = 0
# for i in n:
#     new = n[::-1]
# print(new)



# ME # n = int(input("Enter the number"))
# sum = 1
# for i in range(1, n+1):
#     sum *= i
# print(sum)



# ME # n = int(input("Enter the number"))
# sum = 0
# for i in range(1,  n+1):
#     if i%2!=0:
#         sum += i
# print(sum)




# ME #str = "Hello, Brother"
# vowels = "AEIOUaeiou"
# str1 = 0
# for i in str:
#     if i in vowels:
#         str1 += 1                  ## To count the value
# print(str1) 



# ME # n = [3, 5, 7, 9, 2]
# sum = 0
# for i in n:
#     sum += i
# print(sum) 


## Medium
# CHAT# Input: Get the value of N from the user
# N = int(input("Enter a number to find prime numbers up to N: "))

# # List to store prime numbers
# primes = []

# # Loop through numbers from 2 to N
# for num in range(2, N + 1):
#     is_prime = True
    
#     # Check if the number is divisible by any of the previously found primes
#     for prime in primes:
#         if num % prime == 0:
#             is_prime = False
#             break  # No need to check further; num is not prime
    
#     # If the number is prime, add it to the list and print it
#     if is_prime:
#         primes.append(num)
#         print(num, end=' ')


#  ME  #str = "hello"
# count = 0
# for i in str:
#     if "l" in i:
#         count += 1
# print(count)



# # CHAT # Input: Get two lists of integers from the user
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]

# # Use a for loop to find common elements
# common_elements = []

# for item in list1:
#     if item in list2:
#         common_elements.append(item)

# # Output the result
# print("Common elements:", common_elements)




# CHAT # Input: Define the list of elements
# input_list = [2, 3, 2, 4, 3, 3, 5]

# # Create an empty dictionary to store the count of each element
# occurrences = {}

# # Use a for loop to iterate through the list
# for element in input_list:
#     if element in occurrences:
#         occurrences[element] += 1  # Increment the count if the element is already in the dictionary
#     else:
#         occurrences[element] = 1   # Initialize the count if it's the first time encountering the element

# # Output the result
# for element, count in occurrences.items():
#     if count == 1:
#         print(f"{element} appears {count} time")
#     else:
#         print(f"{element} appears {count} times")

# Input: Get the value of N from the user
# N = int(input("Enter a number N: "))



# ME # Initialize the sum to 0
# sum_divisible = 0

# # Loop through all numbers from 1 to N
# for num in range(1, N + 1):
#     if num % 3 == 0 or num % 5 == 0:
#         sum_divisible += num  # Add the number to the sum if it is divisible by 3 or 5

# # Output the result
# print("Sum of numbers divisible by 3 or 5:", sum_divisible)



# CHAT # Sample list of numbers
# numbers = [12, 35, 1, 10, 34, 1]

# # Initialize variables to track the largest and second largest numbers
# largest = float('-inf')
# second_largest = float('-inf')

# # Loop through each number in the list
# for num in numbers:
#     if num > largest:
#         # Update second largest before updating largest
#         second_largest = largest
#         largest = num
#     elif num > second_largest and num != largest:
#         # Update second largest only if num is not equal to largest
#         second_largest = num

# # Output the result
# print("The second largest number is:", second_largest)


# n = int(input("ENter the number"))
# sum = 0
# for i in range(3, n):
#     if i%5==0 or i%3==0:
#         sum+= i
# print(sum)


# a = 10
# b = 20
# for i in range(a, b):
#     if i%1==0 and i%i==0:
#         print(i) 


# a = [2, 3, 4, 5]
# mul = 1
# for i in a:
#     mul*= 1
# print(mul)

