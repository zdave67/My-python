BOLD = "\033[1m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"
import random, time
#dungeon crawler
#tutorial
savecode = 0
print("\nWelcome to Iron Dungeon, the game where you fight futuristic enemies, find rare loot and gamble it all to try win the jackpot!")
player_health = 100
jungle_relic = 5
player_money = 100
time.sleep(3)
print("Here are all the things you can do:")
time.sleep(2)
while True:
    print(f"\n Your health: {player_health}, Your money: {player_money}\nType '1' to Gamble, '2' to start a dungeon and '3' to generate a save code. \n\nYou can also press '4' to enter a save code to play with your account.  \nPress '5' to open the shop.")
    #start game now
    time.sleep(0)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        #finished
        print(f"\nYou have chosen to Gamble. Your money is {player_money}.")
        time.sleep(1.3)
        gamble_choice = int(input("Enter your game: 1 to use the slot machines and 2 to play the number guesser: "))
        if gamble_choice == 2:
            gamble_amount = int(input("How much do you want to gamble?  "))
            if gamble_amount == player_money or gamble_amount < player_money:
                player_money = player_money - gamble_amount

                guess = int(input(f"Guess a number between 1 and {jungle_relic}:   "))
                if guess == random.randint(1,int(jungle_relic)):
                    player_money = player_money + gamble_amount * 3
                    print(f"You have won and tripled the money you gambled! Your money is now {player_money}.")
                else:
                    print(f"Unlucky, you have just lost {gamble_amount} money.")
            else:
                print("You do not have enough money to bet that much.")
        elif gamble_choice == 1:
            symbols = ["🍒", "🍋", "🍊", "💎"]
            from time import sleep

            player_money = 100


            def print_slow(txt):
                for x in txt:
                    print(x, end='', flush=True)  # not my code (lines 48-52)
                    sleep(0.3)
                print()  # go to new line


            while True:
                sleep(0)
                slot = random.choice(symbols)
                slot2 = random.choice(symbols)
                slot3 = random.choice(symbols)
                choice = int(input(f"Enter '1' when you are ready, 2 to go back - your money is {player_money} and it costs 4 to play. "))
                if choice == 1:
                    if player_money < 0:
                        print("get outta my casino, brokie")

                    else:
                        player_money = player_money - 4
                        print_slow(f"{slot} {slot2} {slot3}")
                        result = slot + slot2 + slot3
                        match result:
                            case "💎💎💎":
                                print("YOU WON!!!")
                                player_money = player_money + 100
                            case "🍊🍊🍊":
                                print("You got a prize")
                                player_money = player_money + 50
                            case"🍋🍋🍋":
                                print("You got a prize")

                                player_money = player_money + 50
                            case "🍒🍒🍒":
                                print("You got a prize")
                                player_money = player_money + 50
                            case _:
                                print("Unlucky, you didn't win anything.")
                elif choice == 2:
                    break
    elif choice == 2:
        #start a dungeon now
        enemies = ["Robot Fly", "Cyborg", "Mega Tron", "Droid", "Laser Bot"]
        bosses = ["UFO", "Giant Laser Bot"]
        enemy_health_options = [30, 40, 50, 60, 70, 80]
        print("Dungeon is starting...")
        time.sleep(3)

        for i in range(3):
            enemy_health = random.choice(enemy_health_options)
            print(f"You have encountered a {random.choice(enemies)} which has {enemy_health} health! You have 3 attack options. \n1. 'Blast': 30 damage. \n2. 'Guarding Strike': 15 damage but you heal 15 health. \n3. 'Heal': heal 30 health.")
            time.sleep(0.5)

            while enemy_health > 0 and player_health > 0:
                attack_choice = int(input("Enter your choice: "))
                time.sleep(1)

                if attack_choice == 1:
                    enemy_health = enemy_health - 30
                    if enemy_health < 1:
                        print("\nYou have killed the enemy.")
                        time.sleep(1.3)
                        player_money = player_money + random.randint(10,40)
                        print(f"You now have {player_money} money.")
                    else:
                        print(f"\nYou have used Blast. The enemy has {enemy_health} health remaining.")
                elif attack_choice == 2:
                    enemy_health = enemy_health - 15
                    player_health = player_health + 15
                    if enemy_health < 1:
                        print("\nYou have killed the enemy.")
                        player_money = player_money + random.randint(10,40)
                        print(f"You now have {player_money} money.")
                    else:
                        print(f"\nYou have used Guarding Strike. The enemy has {enemy_health} health remaining. You have {player_health} health remaining.")
                elif attack_choice == 3:
                    player_health = player_health + 30
                    print(f"\nYou have used Heal. You have {player_health} health remaining.")
                if enemy_health > 0:
                    player_health = player_health - random.randint(1,30)
                    print(f"The enemy has attacked you. You have {player_health} health remaining.")
            if player_health < 1:
                print("You died :(")
                break
        enemy_health = random.choice(enemy_health_options)*4
        print(f"You have encountered a {random.choice(bosses)} which has {enemy_health} health!")
        time.sleep(3)
        while enemy_health > 0 and player_health > 0:
            attack_choice = int(input("Enter your choice: "))
            time.sleep(1)

            if attack_choice == 1:
                enemy_health = enemy_health - 30
                if enemy_health < 1:
                    print("\nYou have killed the enemy.")
                    time.sleep(1.3)
                    player_money = player_money + random.randint(10,40)
                    print(f"You now have {player_money} money.")
                else:
                    print(f"\nYou have used Blast. The enemy has {enemy_health} health remaining.")
            elif attack_choice == 2:
                enemy_health = enemy_health - 15
                player_health = player_health + 15
                if enemy_health < 1:
                    print("\nYou have killed the enemy.")
                    player_money = player_money + random.randint(10,40)
                    print(f"You now have {player_money} money.")
                else:
                    print(
                        f"\nYou have used Guarding Strike. The enemy has {enemy_health} health remaining. You have {player_health} health remaining.")
            elif attack_choice == 3:
                player_health = player_health + 30
                print(f"\nYou have used Heal. You have {player_health} health remaining.")
            if enemy_health > 0:
                player_health = player_health - random.randint(1,30)
                print(f"The enemy has attacked you. You have {player_health} health remaining.")

        if player_health > 0:
            print("You have beat the boss!")
            time.sleep(3)
            relics = ["Diamond Relic", "Gold Relic", "Ancient Relic"]
            relic_acquired = random.choice(relics)
            if relic_acquired == "Diamond Relic":
                print("\nYou have acquired the diamond relic which you sell for 200 money")
                player_money = player_money + 200
                print(f"You now have {player_money} money.")
                time.sleep(3)
            elif relic_acquired == "Gold Relic":
                print("You have acquired the gold relic which you sell for 150 money")
                player_money = player_money + 150
                print(f"You now have {player_money} money.")

                time.sleep(3)
            else:
                print("You have acquired the ancient relic which gives you +100 health.")
                player_health = player_health + 100
                print(f"You now have {player_health} health.")
                time.sleep(3)
        else:
            print("You died :(")
            break
    elif choice == 3:
        savecode = str(player_money) + " " + str(player_health) + " " + str(jungle_relic)
        print(savecode)

    elif choice == 4:

        savecode_ent = input("Enter your savecode: ")
        char_num = 0
        char = ""
        full_word1 = ""
        full_word2 = ""
        while char != " ":
            char = savecode_ent[char_num]
            full_word1 = full_word1 + char
            char_num = char_num + 1
        player_money = int(full_word1)
        print(f"Account Updated - You now have {player_money} money.")
        char_num = char_num + 0
        char = savecode_ent[char_num]
        while char != " ":
            char = savecode_ent[char_num]
            full_word2 = full_word2 + char
            char_num = char_num + 1

        player_health = int(full_word2)
        print(f"Account Updated - You now have {player_health} health.")

        char = savecode_ent[char_num]
        jungle_relic = char
        print("Your Gambling odds have been updated.")

    elif choice == 5:
        print("You have chosen to open the shop.")
        time.sleep(1)
        print("\nHi, I'm Carl the shopkeeper! What would you like to buy?")
        print("\n Item 1: Ancient Relic - 200 money. \nItem 2: Jungle Relic - 350 money. \nItem 3: Upgraded Jungle Relic - 500 money.\nItem 4: ??? - 1000 money.")
        shop_choice = int(input("Enter your choice: "))
        if shop_choice == 1:
            if player_money > 199:
                player_money = player_money - 200
                player_health = player_health  + 150
                print(f"You have successfully bought the ancient relic! Your money is now {player_money} money and your health is now {player_health} health.")
            else:
                print("You do not have enough money to buy the ancient relic.")
        elif shop_choice == 2:
            if player_money > 349:
                player_money = player_money - 350
                jungle_relic = 3
                print(f"You have successfully bought the ancient relic! Your money is now {player_money} money and and now when you gamble, your odds of winning are now 1 in 3!")
            else:
                print("You do not have enough money to buy the jungle relic.")
        elif shop_choice == 3:
            if player_money > 499:
                player_money = player_money - 500
                jungle_relic = 2
                print(f"You have successfully bought the Upgraded Jungle Relic Your money is now {player_money} money and and now when you gamble, your odds of winning are now 1 in 2!")
            else:
                print("You do not have enough money to buy the Upgraded Jungle Relic.")
        elif shop_choice == 4:
                if player_money > 999:
                    player_money = player_money - 1000
                    jungle_relic = 2
                    print(f"You have successfully bought the ???. Your money is now {player_money}.")
                else:
                    print("You do not have enough money to buy the ???")
                print(f"\n{RED}A mysterious force has appeared...")
                time.sleep(4)
                print("\n--The ground begins to open-- ")
                time.sleep(4)
                print("\nYou hear a loud growl coming from underground: Thank you for freeing me...")
                time.sleep(4)
                print(f"\n{GREEN}Carl: What have you done?!")
                time.sleep(4)
                print("\nCarl: Before you entered our world, there was an epic fight with the monster you just freed.\nThe monster is called 'Vulgoroth'.\nThere was a war which lasted for decades and after we made a trap, we captured him and sent him to the center of the earth.")
                time.sleep(7)
                #boss fight time
                print(f"\n{RED}Vulgoroth: The world as you know it will be destroyed! ")
                time.sleep(4)
                print(f"\n{GREEN}Carl: Not on my watch!\nHero, you fight him! If not for me, do it for the safety of the world!")
                time.sleep(4)
                print(f"\n{RESET}You will now fight Vulgoroth. Bossfight starting... ")
                time.sleep(4)
                enemy_health = 500
                while enemy_health > 0 and player_health > 0:
                    attack_choice = int(input("\nEnter your choice: "))
                    time.sleep(1)

                    if attack_choice == 1:
                        enemy_health = enemy_health - 30
                        if enemy_health < 1:
                            print("\nYou have killed Vulgoroth!")
                            time.sleep(1.3)
                            player_money = player_money + random.randint(100, 500)
                            print(f"You now have {player_money} money.")
                        else:
                            print(f"\nYou have used Blast. Vulgoroth has {enemy_health} health remaining.")
                    elif attack_choice == 2:
                        enemy_health = enemy_health - 15
                        player_health = player_health + 15
                        if enemy_health < 1:
                            print("\nYou have killed Vulgoroth!")
                            player_money = player_money + random.randint(100, 500)
                            print(f"You now have {player_money} money.")
                        else:
                            print(f"\nYou have used Guarding Strike. Vulgoroth has {enemy_health} health remaining. You have {player_health} health remaining.")
                    elif attack_choice == 3:
                        player_health = player_health + 30
                        print(f"\nYou have used Heal. You have {player_health} health remaining.")
                    if enemy_health > 0:
                        player_health = player_health - random.randint(10, 50)
                        print(f"Vulgoroth has attacked you. You have {player_health} health remaining.")
                if player_health > 0:
                    print("\nYou have killed Vulgoroth!")
                else:
                    print("\nYou have Died. The world will end if you don't try again. Remember, buy relics before fighting Vulgoroth.")
                    break
                print(f"\n{UNDERLINE}{BOLD}The world will forever owe you!{RESET}")