from time import sleep
import random


def intro(beast):
    sleep(2)
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a {} is somewhere around here, "
                "and has been terrifying the nearby village.".format(beast))
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty"
                "(but not very effective) dagger. \n \n")


def print_pause(message_to_print):
    print(message_to_print)
    sleep(2)


def adventure_field(beast):
    sleep(3)
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    decision = input("What would you like to do? \n(Please enter 1 or 2).\n")
    if decision == '1':
        house_knock(beast)
    elif decision == '2':
        cave_peer(beast)
    else:
        print_pause("Please enter a valid choice! 1 or 2!")
        adventure_field(beast)


def house_knock(beast):
    sleep(2)
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door "
                "opens and out steps a {}.".format(beast))
    print_pause("Eep! This is the {}'s house! \nThe {} "
                "attacks you!".format(beast, beast))

    decision = input("Would you like to (1) fight or (2) run away?\n")

    if decision == '1':
        if 'Sword of Ogoroth' in item_list:
            adventure_win(beast)
        else:
            crazy_clutch_win(beast)
    elif decision == '2':
        sleep(2)
        print("You run back into the field. Luckily, you "
              "don't seem to have been followed.\n \n")
        adventure_field(beast)
    else:
        print("Please choose a valid response. 1 or 2!")
        house_knock(beast)


def cave_peer(beast):
    if 'Sword of Ogoroth' in item_list:
        sleep(2)
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten "
                    "all the good stuff. It's just an empty cave now.")
        print_pause("You walk back out to the field.")
        adventure_field(beast)
    else:
        sleep(2)
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        item_list.append('Sword of Ogoroth')
        print_pause("You discard your silly old dagger and take "
                    "the sword with you.")
        print_pause("You walk back out to the field.\n \n")
        adventure_field(beast)


def adventure_win(beast):
    sleep(2)
    print_pause("As the {} moves to attack, you unsheath your "
                "new sword.".format(beast))
    print_pause("The Sword of Ogoroth shines brightly in your "
                "hand as you brace yourself for the attack.")
    print_pause("But the {} takes one look at your shiny new toy "
                "and runs away!".format(beast))
    print_pause("You have rid the town of the {}. You are "
                "victorious!".format(beast))
    play_again()


def adventure_defeat(beast):
    sleep(2)
    print_pause("You do your best...")
    print_pause("But your dagger is no match for the {}".format(beast))
    print_pause("You have been defeated")
    play_again()


def play_game():
    beast = random.choice(['Wicked Fairy', 'Troll', 'Dragon', 'Witch'])
    intro(beast)
    adventure_field(beast)


def play_again():
    decision = input("Would you like to play again? (Y/N)\n").lower()
    if decision == "y":
        item_list.remove("Sword of Ogoroth")
        play_game()
    elif decision == 'n':
        sleep(2)
        print_pause("Thanks for playing! See you next time.")
    else:
        sleep(2)
        print_pause("Please enter a valid choice. Y or N!")
        play_again()


# crazy_clutch_win is not a good function name but made sense
# when its a RANDOM win that I have added to modify with random,int

def crazy_clutch_win(beast):
    clutch = random.randint(0, 50)
    if clutch > 30:
        print_pause("As the {} moves to attack, you unsheath your "
                    "trusty dagger.".format(beast))
        print_pause("Luck shifts in your favor. As you hack and slash......")
        print_pause("You get a great deep jab in and cause severe bleeding...")
        print_pause("Congratulations!! The {} quit while it was ahead "
                    "and fled never to be seen again.".format(beast))
        print_pause("You have rid the town of the {}. You are "
                    "victorious!".format(beast))
        play_again()
    else:
        adventure_defeat(beast)


if __name__ == '__main__':
    item_list = []
    play_game()
