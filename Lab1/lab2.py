# Problem 1

import random
numbers = [1, 2, 3, 3]
result = [numbers[0]]
for i in range(1, len(numbers)):
    if numbers[i] != numbers[i - 1]:
        result.append(numbers[i])
print(result)

# Problem 2

text1 = "ABCDE"
text2 = "TUVWXYZ"

if (len(text1) % 2 == 0):
    half1 = text1[:len(text1)//2]
    half2 = text1[len(text1)//2:]
else:
    half1 = text1[:len(text1)//2+1]
    half2 = text1[len(text1)//2+1:]

if (len(text2) % 2 == 0):
    half3 = text2[:len(text2)//2]
    half4 = text2[len(text2)//2:]
else:
    half3 = text2[:len(text2)//2+1]
    half4 = text2[len(text2)//2+1:]

print(half1 + half3 + half2 + half4)


# Problem 3
list1 = [1, 5, 7, 9]
list2 = [1, 5, 5]
print(len(list1) == len(set(list1)))
print(len(list2) == len(set(list2)))

# Problem 4
arr = [64, 34, 25, 12, 22, 11, 90]
n = len(arr)
for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print("Sorted array is:", arr)


# Guessing Game
random_number = random.randint(1, 100)
tries = 10
guessed_numbers = set()

while tries > 0:
    user_input = input("Enter your guess: ")
    guess = int(user_input)
    if guess < 1 or guess > 100:
        print("Your guess is out of range (1-100). Try again.")
        continue

    if guess in guessed_numbers:
        print("You've already guessed that number. Try a different one.")
        continue

    guessed_numbers.add(guess)
    tries -= 1

    if guess == random_number:
        print(
            f"Congratulations! You guessed the correct number ({random_number})!")
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() == 'yes':
            random_number = random.randint(1, 100)
            tries = 10
            guessed_numbers = set()
            print("I've selected a new random number. You have 10 tries to guess it.")
        else:
            print("Thanks for playing!")
        continue

    if guess < random_number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")
