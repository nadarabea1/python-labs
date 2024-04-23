import math
# Problem 1
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print("Hello, " + last_name + " " + first_name + "!")

# Problem 2
number = input("Enter a number: ")
double_number = int(number + number)
triple_number = int(number + number + number)
number = int(number)

print("The sum of the number is: " + str(number + double_number + triple_number))

# Problem 3
print(f'a string that you \'don\'t\' have to escape is\n This\n is a ........ multi-time\n heredoc string --------> example')

# Problem 4
redius = 6
valume = (4 / 3) * math.pi * (redius**3)
print(f'The valume of the sphere is: {valume}')

# Problem 5
base = input("Enter the base of the triangle: ")
height = input("Enter the height of the triangle: ")
base = int(base)
height = int(height)
area = (1 / 2) * base * height
print(f'The area of the triangle is: {area}')

# Problem 6

for i in range(0, 5):
    for j in range(0, i + 1):
        print("*", end=" ")
    print("\r")

for i in range(5, 0, -1):
    for j in range(0, i - 1):
        print("*", end=" ")
    print("\r")

# Problem 7
word = input("Enter a word: ")
reversed_word = word[::-1]
print(f'The reversed word is: {reversed_word}')

# Problem 8
for i in range(0, 6):
    if (i == 3):
        continue
    print(i, end=" ")

# Problem 9
num1 = 0
num2 = 1
while num1 < 50:
    print(num1, end=" ")
    num1, num2 = num2, num1 + num2
# Problem 10
text = input("Enter a text: ")
digits = 0
letters = 0
for i in text:
    if (i.isalpha()):
        letters += 1
    elif (i.isdigit()):
        digits += 1
print(f'The number of letters in the text is: {letters}')
print(f'The number of digits in the text is: {digits}')
