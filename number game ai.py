import random
ma = 0
dif = int(input("choose the ai difficulty from 1 (ez) to 2 (hard): "))
tot_sum = 0
while tot_sum < 21:
    choice = int(input(f"enter a number from 1-3 to add on to the {tot_sum} already there: "))
    match choice:
        case 1: tot_sum = tot_sum + 1
        case 2: tot_sum = tot_sum + 2
        case 3: tot_sum = tot_sum + 3
        case _: print("you cheated so the computer will")
    if (21 - tot_sum) == 1:
        print("You win!")
        break
    elif tot_sum > 20:
        print("You lose!")
        break
    if dif == 2:

        print(f"the computer added {4-tot_sum%4} to the total making it {tot_sum + 4-tot_sum%4}!")
        tot_sum = tot_sum + 4 - tot_sum % 4
        if 21 - tot_sum < 2:
            print("You lose!")
            break
    elif dif == 1:
        ma = random.randint(1, 3)
        print(f"the computer added {ma} to the total making it {tot_sum + ma}!")
        tot_sum = tot_sum + ma
        if (21 - tot_sum) ==20:
            print("You lose!")
            break
        elif tot_sum > 20:
            print("You win!")