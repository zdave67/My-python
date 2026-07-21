import random
symbols = ["🍒", "🍋", "🍊", "💎"]
from time import sleep
money = 100
def print_slow(txt):
    for x in txt:
        print(x, end='', flush=True)  #not my code (lines 5-9)
        sleep(0.3)
    print() # go to new line
while True:
    sleep(0)
    slot = random.choice(symbols)
    slot2 = random.choice(symbols)
    slot3 = random.choice(symbols)
    choice = int(input(f"Enter '1' when you are ready - your money is {money} and it costs 3 to play. "))
    if money < 0:
        print("get outta my casino, brokie")

    else:
        money = money -3
        print_slow(f"{slot} {slot2} {slot3}")
        result = slot + slot2 + slot3
        match result:
            case "💎💎💎":
                print("YOU WON!!!")
                money = money + 100
            case "🍊🍊🍊":
                print("You got a prize")

                money = money + 50
            case "🍋🍋🍋":
                print("You got a prize")

                money = money + 50
            case "🍒🍒🍒":
                print("You got a prize")
                money = money + 50
            case _:
                print("Unlucky, you didn't win anything.")
