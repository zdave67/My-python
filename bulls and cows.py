import random
idx = 0
print("you have 6 tries to guess my 4 digit number")
target_number = random.randint(1000,9999)
for i in range(6):
    guess = int(input("Guess a 4 digit number: "))
    if len(str(guess)) != 4:
        print("Guess a 4 digit number")
    elif guess == target_number:
        print("You guessed the number")
        break
    else:
        idx = 0
        for x in range(4):
            if str(guess)[idx] == str(target_number)[idx]:
                print(f"number {idx+1} of your guess is correct")
            elif str(guess)[idx] in str(target_number):
                print(f"number {idx+1} of your guess is in the wrong place")
            elif str(guess)[idx] not in str(target_number):
                print(f"number {idx+1} of your guess is not correct")
            idx = idx + 1