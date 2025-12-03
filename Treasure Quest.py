print(" Welcome to the Ultimate Treasure Quest! ")
name = input("Enter your name: ").capitalize()
print(f"Let's begin the game, {name}!")

# Choose weapon
print("Choose your weapon: Sword / Shield / Bow")
weapon = input("Enter your weapon choice: ").lower()
print(f"You have chosen the {weapon}. Good luck!\n")

# First crossroad
direction = input("You are at a crossroad. Do you want to go 'left' into the forest or 'right' towards the mountains? ").lower()

if direction == "left":
    print("\nYou enter the dark forest. Strange sounds surround you!")
    action = input("You see a river. Do you 'swim' across or 'walk' along the bank? ").lower()
    if action == "swim":
        print("\nThe current is strong! You struggle but survive.")
        treasure = input("You find a glowing chest in the river. Do you 'open' it or 'ignore' it? ").lower()
        if treasure == "open":
            print("You find a magical sword! With it, you feel unstoppable. You win! 🏆")
        else:
            print("You leave the chest. Suddenly, a monster appears and you have no weapon to fight. Game over! 💀")
    elif action == "walk":
        print("\nWalking along the bank, you find a friendly elf who gives you a potion.")
        choice = input("Do you 'drink' the potion or 'save' it for later? ").lower()
        if choice == "drink":
            print("You feel super strong! You defeat all monsters ahead. You win! 🎉")
        else:
            print("You save the potion, but get lost in the forest. Game over! 💀")
    else:
        print("You stand still and get attacked by wild animals. Game over! 💀")

elif direction == "right":
    print("\nYou start climbing the mountains. The path is steep and cold.")
    action = input("You see a cave. Do you 'enter' the cave or 'climb' over the peak? ").lower()
    if action == "enter":
        print("\nInside the cave, you meet a dragon guarding treasure!")
        fight = input("Do you 'fight' the dragon or 'sneak' past it? ").lower()
        if fight == "fight":
            if weapon == "sword":
                print("You fight bravely with your sword and defeat the dragon! Treasure is yours. You win! 🏆")
            elif weapon == "bow":
                print("You shoot arrows from afar and hit the dragon. It flees. You win! 🎉")
            else:
                print("Your shield can't harm the dragon. You get burned. Game over! 💀")
        elif fight == "sneak":
            print("You sneak past the dragon and find a hidden treasure behind it. You win! 🎉")
        else:
            print("You hesitate and the dragon notices you. Game over! 💀")
    elif action == "climb":
        print("\nYou climb to the peak and find a snowy plateau.")
        choice = input("Do you 'rest' or 'explore' the plateau? ").lower()
        if choice == "rest":
            print("While resting, an avalanche hits! You survive but lose your way. Game over! 💀")
        else:
            print("Exploring carefully, you find a secret entrance to a treasure cave. You win! 🏆")
    else:
        print("You slip while climbing and fall. Game over! 💀")

else:
    print("You hesitate too long. Night falls and wild animals surround you. Game over! 💀")
