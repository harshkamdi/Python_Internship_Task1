# Program 1: Sum of Two Numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = num1 + num2
print("Sum =", sum)

# Program 2: Odd or Even Checker

num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")

# Program 3: Factorial Calculator

num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print("Factorial of negative number does not exist.")
elif num == 0:
    print("Factorial = 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("Factorial =", factorial)

# Program 4: Fibonacci Sequence

n = int(input("Enter the number of terms: "))
a = 0
b = 1
print("Fibonacci Sequence:")
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
print()

# Program 5: String Reverse

text = input("Enter a string: ")
reverse = text[::-1]
print("Reversed String:", reverse)

# Program 6: Palindrome Checker

text = input("Enter a word: ")
if text == text[::-1]:
    print("It is a Palindrome")
else:
    print("It is Not a Palindrome")

# Program 7: Leap Year Checker

year = int(input("Enter a year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year")
else:
    print(year, "is Not a Leap Year")

# Program 8: Armstrong Number

num = int(input("Enter a number: "))
temp = num
sum = 0
while temp > 0:
    digit = temp % 10
    sum = sum + digit ** 3
    temp = temp // 10
if num == sum:
    print(num, "is an Armstrong Number")
else:
    print(num, "is Not an Armstrong Number")