import random

print("================================")
print("      TREASURE ADVENTURE")
print("================================")

name = input("Enter your name: ")

health = 100
gold = 0

print("\nWelcome,", name, "!")
print("You are an adventurer searching for hidden treasure.")

while health > 0:

    print("\n------ GAME MENU ------")
    print("1. Explore the forest")
    print("2. Fight a monster")
    print("3. Search for treasure")
    print("4. Check status")
    print("5. Exit game")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        print("\nYou entered a mysterious forest.")
        event = random.choice(["health", "gold", "monster"])

        if event == "health":
            health += 10
            print("You found a health potion! +10 health.")

        elif event == "gold":
            gold += 20
            print("You found 20 gold coins!")

        else:
            health -= 20
            print("A wild monster attacked you! -20 health.")

    elif choice == "2":
        print("\nA monster appeared!")
        player_attack = random.randint(10, 30)
        monster_attack = random.randint(5, 20)

        print("You attacked the monster for", player_attack, "damage.")
        print("The monster attacked you for", monster_attack, "damage.")

        if player_attack >= 20:
            gold += 15
            print("You defeated the monster! +15 gold.")
        else:
            health -= monster_attack
            print("You escaped, but lost some health.")

    elif choice == "3":
        treasure = random.randint(10, 50)
        gold += treasure
        print("\nCongratulations! You found", treasure, "gold coins.")

    elif choice == "4":
        print("\n------ YOUR STATUS ------")
        print("Player:", name)
        print("Health:", health)
        print("Gold:", gold)

    elif choice == "5":
        print("\nThanks for playing!")
        break

    else:
        print("\nInvalid choice! Please try again.")

    if health <= 0:
        print("\nGAME OVER!")
        print("You have run out of health.")

print("\nFinal Gold:", gold)
print("Thanks for playing", name + "!")