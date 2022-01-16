"""
Mythos Maze: an adventure game.
"""

import time
from colorama import Fore
from colorama import Style
from locations import entrance, monster_locations, confrontation_locations
from monsters import surale_conversation, kitsune_conversation, \
    naga_conversation, dragon_conversation, puca_conversation, \
    nokk_conversation, win_sequence, sphinx_conversation, \
    anansi_conversation, Monster, kitsune, naga, surale, dragon, nokk, \
    who_is_where, chupacabra, sphinx, anansi, puca, killed_by_foolishness
from user_answers import affirmative, negative, follow_path, \
    follow_spider, stop_game, seal_your_doom, attack, pickup_items, \
    avoid, correct_answer, contents


def display_intro():
    """
    Displays the opening / introductory text of the game.
    """
    intro_done = False
    while intro_done is False:
        player_input = input(f"{Fore.LIGHTCYAN_EX}Welcome to the Mythos Maze,\
 would you like to try and traverse its perils?{Style.RESET_ALL}\n>")
        if player_input.lower().strip() in affirmative:
            player_input2 = input(f"{Fore.LIGHTCYAN_EX}Are you\
 sure?{Style.RESET_ALL}\n>")
            if player_input2.lower().strip() in affirmative:
                print(f"{Fore.LIGHTCYAN_EX}Very well then, it's your funeral."
                      f"\nLet me give you a piece of advice:\nThe creatures "
                      f"you will encounter can be quite daunting to "
                      f"face.\nYou may not wish to face them empty handed...\n"
                      f"Good luck mortal.{Style.RESET_ALL}\n>")
                intro_done = True
            else:
                print(f"{Fore.LIGHTCYAN_EX}Indecision is the thief of "
                      f"opportunity you know...{Style.RESET_ALL}\n")
        elif player_input.lower().strip() in negative:
            print(f"{Fore.LIGHTCYAN_EX}A wise choice.{Style.RESET_ALL}")
            time.sleep(1)
            print(f"{Fore.LIGHTCYAN_EX}However, please don't hesitate to visit\
 me again should you change your mind.{Style.RESET_ALL}\n")
        else:
            print(f"{Fore.LIGHTCYAN_EX}Such confidence, best run back and hide\
 behind your mother's skirts child.{Style.RESET_ALL}\n")


LOCATION = entrance
EXIT_GAME = False
visited = ["entrance"]
inventory = []
monsters_met = []


def location_arrival():
    """
    Player arrives at a certain location and gets prompted what
    to do next.
    """
    time.sleep(1)
    print(LOCATION.description)
    player_input3 = input("What will you do?\n>")
    while player_input3.lower().strip() not in stop_game:
        if LOCATION is monster_locations[0] and player_input3.lower().strip()\
                not in avoid and player_input3.lower().strip() not in attack:
            kitsune_encounter()
            if EXIT_GAME is True:
                break
            else:
                location_arrival()
                break
        elif LOCATION is monster_locations[1] and \
                player_input3.lower().strip() in follow_spider:
            take_items('gift')
            monsters_met.append(which_monster())
            validate_path('spider')
            player_input3 = input("What will you do?\n>")
        elif LOCATION is monster_locations[1] and \
                player_input3.lower().strip() == "drink milk":
            print(f"{Fore.LIGHTMAGENTA_EX}The delicious milk revitalizes and\
 refreshes you.{Style.RESET_ALL}")
            inventory.remove("milk")
            player_input3 = input("What will you do?\n>")
        elif LOCATION is monster_locations[2] and \
                player_input3.lower().strip() not in avoid and \
                player_input3.lower().strip() not in follow_path and\
                player_input3.lower().strip() not in follow_spider\
                and player_input3.lower().strip() not in attack:
            naga_encounter()
            location_arrival()
            break
        elif LOCATION is monster_locations[2] and \
                player_input3.lower().strip() in avoid:
            validate_path()
            player_input3 = input("what will you do?\n>")
        elif LOCATION is monster_locations[3] and \
                player_input3.lower().strip() not in avoid and\
                player_input3.lower().strip() not in attack:
            dragon_encounter()
            if EXIT_GAME is True:
                break
            else:
                location_arrival()
                break
        elif LOCATION is monster_locations[4] and \
                player_input3.lower().strip() not in avoid and\
                player_input3.lower().strip() not in negative and\
                player_input3.lower().strip() not in attack:
            surale_encounter()
            if EXIT_GAME is True:
                break
            else:
                location_arrival()
                break
        elif LOCATION is monster_locations[4] and \
                player_input3.lower().strip() in negative:
            print(surale_conversation[3])
            game_over()
            break
        elif LOCATION is monster_locations[5] and \
                player_input3.lower().strip() not in avoid and\
                player_input3.lower().strip() not in attack:
            puca_encounter()
            if EXIT_GAME is True:
                break
            else:
                location_arrival()
                break
        elif LOCATION is monster_locations[6] and \
                player_input3.lower().strip() not in avoid:
            nokk_encounter()
            if EXIT_GAME is True:
                break
            else:
                location_arrival()
                break
        elif LOCATION is monster_locations[7] and \
                player_input3.lower().strip() not in avoid and\
                player_input3.lower().strip() not in attack:
            sphinx_encounter()
            if EXIT_GAME is True:
                break
            else:
                location_arrival()
                break
        elif LOCATION is monster_locations[8] and\
                player_input3.lower().strip() not in avoid:
            win()
            break
        elif LOCATION in monster_locations and player_input3.lower().strip()\
                in avoid and LOCATION is not monster_locations[2]:
            print(f"{Fore.LIGHTMAGENTA_EX}Though you want to leave, your fear "
                  f"and uncertainty keep you rooted to the spot"
                  f".{Style.RESET_ALL}")
            player_input3 = input("What will you do?\n>")
        elif player_input3.lower().strip() in pickup_items:
            take_items()
            player_input3 = input("What will you do?\n>")
        elif player_input3.lower().strip() in follow_path:
            validate_path()
            player_input3 = input("What will you do?\n>")
        elif player_input3.lower().strip() in follow_spider:
            validate_path('spider')
            player_input3 = input("What will you do?\n>")
        elif player_input3.lower().strip() in seal_your_doom:
            print(killed_by_foolishness[0])
            game_over()
            if EXIT_GAME is True:
                break
            else:
                location_arrival()
                break
        elif player_input3.lower().strip() in attack and\
                LOCATION in confrontation_locations and\
                "rusted sword" in inventory:
            print(killed_by_foolishness[1])
            game_over()
            if EXIT_GAME is True:
                break
            else:
                location_arrival()
                break
        elif player_input3.lower().strip() in attack and\
                LOCATION in confrontation_locations and\
                "rusted sword" not in inventory:
            print(killed_by_foolishness[2])
            game_over()
            if EXIT_GAME is True:
                break
            else:
                location_arrival()
                break
        elif player_input3.lower().strip() in attack and\
                LOCATION not in confrontation_locations:
            print(f"{Fore.LIGHTMAGENTA_EX}It appears your mind has devolved\
 into madness\nto the point that you're attacking empty air.\nPerhaps a\
 different course of action is more productive?{Style.RESET_ALL}")
            player_input3 = input("What will you do?\n>")
        elif player_input3.lower().strip() in contents:
            print(f"{Fore.LIGHTMAGENTA_EX}Your inventory currently\
 contains:{Fore.LIGHTYELLOW_EX} {', '.join(inventory)}{Style.RESET_ALL}")
            player_input3 = input("What will you do?\n>")
        else:
            print(f"{Fore.LIGHTMAGENTA_EX}I'm afraid I don't quite catch your\
 meaning{Style.RESET_ALL}")
            player_input3 = input("What will you do?\n>")
    else:
        print(f"{Fore.LIGHTGREEN_EX}Returning to reality...{Style.RESET_ALL}")


def kitsune_encounter():
    """
    Handles interaction between player and
    the Kitsune (when encountered)
    """
    global LOCATION
    print(f"{Fore.LIGHTCYAN_EX}'I lost my marble, have you seen\
 it?'{Style.RESET_ALL}")
    player_talk = input("What will you say?\n>")
    if player_talk.lower().strip() in negative and "hoshi no tama" in \
            inventory:
        print(kitsune_conversation[0])
        player_talk2 = input(f"{Fore.LIGHTMAGENTA_EX}Will you hand over the\
 {Fore.LIGHTYELLOW_EX}hoshi no tama?{Style.RESET_ALL}\n>")
        if player_talk2.lower().strip() in affirmative:
            print(kitsune_conversation[1])
            time.sleep(12)
            take_items('gift')
            time.sleep(2)
            monsters_met.append(which_monster())
            inventory.remove("hoshi no tama")
            LOCATION = LOCATION.move_on
        elif player_talk2.lower().strip() in negative:
            print(kitsune_conversation[2])
            game_over()
    elif player_talk.lower().strip() in affirmative and "hoshi no tama" in \
            inventory:
        print(kitsune_conversation[3])
        player_talk2 = input(f"{Fore.LIGHTMAGENTA_EX}Will you hand over the\
 {Fore.LIGHTYELLOW_EX}hoshi no tama?{Style.RESET_ALL}\n>")
        if player_talk2.lower().strip() in affirmative:
            print(kitsune_conversation[1])
            time.sleep(6)
            take_items('gift')
            monsters_met.append(which_monster())
            inventory.remove("hoshi no tama")
            LOCATION = LOCATION.move_on
        elif player_talk2.lower().strip() in negative:
            print(kitsune_conversation[2])
            game_over()
    elif player_talk.lower().strip() in affirmative and "hoshi no tama" not \
            in inventory:
        print(kitsune_conversation[4])
        game_over()
    elif player_talk.lower().strip() in negative and "hoshi no tama" not in \
            inventory:
        print(kitsune_conversation[5])
        game_over()
    else:
        print(kitsune_conversation[6])
        game_over()


def naga_encounter():
    """
    Handles interaction between player and
    the Naga (when encountered)
    """
    global LOCATION
    print(naga_conversation[0])
    player_talk = input("What will you say?\n>")
    if player_talk.lower().strip() in negative and "milk" in \
            inventory and "nature's blessing" in inventory:
        print(naga_conversation[1])
        print(f"{Fore.LIGHTMAGENTA_EX}The contents of your inventory is\
 currently:{Fore.LIGHTYELLOW_EX}{', '.join(inventory)}{Style.RESET_ALL}")
        player_talk2 = input("What will you offer?\n>")
        while player_talk2.lower().strip() != "milk":
            if player_talk2.lower().strip() == "rusted sword":
                print(naga_conversation[3])
                player_talk2 = input("What will you offer?\n>")
            elif player_talk2.lower().strip() == "nature's blessing":
                print(f"{Fore.RED}You cannot gift someone else's blessing of \
 you onto another person.{Style.RESET_ALL}")
                player_talk2 = input("What will you offer?\n>")
            else:
                print(f"{Fore.LIGHTCYAN_EX}'I have no ussse for sssuch a\
 thing human'{Style.RESET_ALL}")
                player_talk2 = input("What will you offer\n>")
        else:
            print(naga_conversation[2])
            inventory.remove("milk")
            time.sleep(6)
            take_items('gift')
            time.sleep(2)
            monsters_met.append(which_monster())
            LOCATION = LOCATION.path
    elif "nature's blessing" or "milk" not in inventory:
        print(naga_conversation[4])
        time.sleep(2)
        LOCATION = LOCATION.path


def dragon_encounter():
    """
    Handles interaction between player and
    the Dragon (when encountered)
    """
    global LOCATION
    print(dragon_conversation[0])
    player_talk = input("What will you say?\n>")
    print(f"{Fore.LIGHTCYAN_EX}'{player_talk}?, you smell.. human. Are you\
 human?'{Style.RESET_ALL}\n>")
    player_talk2 = input("What will you say?\n>")
    if player_talk2.lower().strip() in negative and \
            "a large bloodred ruby" not in inventory:
        print(dragon_conversation[1])
        game_over()
    elif player_talk2.lower().strip() in negative and \
            "a large bloodred ruby" in inventory:
        print(dragon_conversation[2])
        player_talk3 = input(f"{Fore.LIGHTMAGENTA_EX}Will you hand over the\
 {Fore.LIGHTYELLOW_EX}large {Fore.LIGHTRED_EX}bloodred\
 ruby?{Style.RESET_ALL}\n>")
        if player_talk3.lower().strip() in negative:
            game_over()
        elif player_talk3.lower().strip() in affirmative:
            print(dragon_conversation[3])
            inventory.remove("a large bloodred ruby")
            time.sleep(6)
            monsters_met.append(which_monster())
            LOCATION = LOCATION.move_on
    elif player_talk2.lower().strip() in affirmative and \
            "a large bloodred ruby" in inventory:
        print(dragon_conversation[4])
        player_talk3 = input(f"{Fore.LIGHTMAGENTA_EX}Will you hand over the\
 {Fore.LIGHTYELLOW_EX}large {Fore.LIGHTRED_EX}bloodred\
 ruby?{Style.RESET_ALL}\n>")
        if player_talk3.lower().strip() in negative:
            game_over()
        elif player_talk3.lower().strip() in affirmative:
            print(dragon_conversation[3])
            inventory.remove("a large bloodred ruby")
            time.sleep(3)
            monsters_met.append(which_monster())
            LOCATION = LOCATION.move_on
    else:
        print(dragon_conversation[5])
        game_over()


def surale_encounter():
    """
    Handles interaction between player and
    the Surale (when encountered)
    """
    global LOCATION
    print(surale_conversation[0])
    player_talk = input("Which will you choose?\n>")
    if player_talk.lower().strip() == "dance":
        print(surale_conversation[1])
        time.sleep(6)
        monsters_met.append(which_monster())
        LOCATION = LOCATION.move_on
    else:
        print(surale_conversation[2])
        game_over()


def puca_encounter():
    """
    Handles the interaction between player and
    the Puca (when encountered)
    """
    global LOCATION
    print(puca_conversation[0])
    player_talk = input("What will you say?\n>")
    if player_talk.lower().strip() in affirmative:
        print(puca_conversation[1])
        player_talk2 = input("What will you say?\n>")
        if player_talk2.lower().strip() in affirmative and \
                "bloodstained spurred boots" in inventory:
            print(puca_conversation[2])
            player_talk3 = input(f"{Fore.LIGHTMAGENTA_EX}Will you try to "
                                 f"convince the Púca to let you ride him? "
                                 f"Or will you move on?{Style.RESET_ALL}\n>")
            if player_talk3.lower().strip() in follow_path:
                print(puca_conversation[4])
                time.sleep(6)
                monsters_met.append(which_monster())
                LOCATION = LOCATION.move_on
            else:
                print(puca_conversation[5])
                time.sleep(6)
                take_items()
                time.sleep(2)
                monsters_met.append(which_monster())
                LOCATION = LOCATION.move_on
                inventory.remove("bloodstained spurred boots")
        elif player_talk2.lower().strip() in affirmative and \
                "bloodstained spurred boots" not in inventory:
            print(puca_conversation[3])
            game_over()
        else:
            print(puca_conversation[6])
            monsters_met.append(which_monster())
            time.sleep(2)
            LOCATION = LOCATION.move_on
    else:
        print(puca_conversation[6])
        monsters_met.append(which_monster())
        time.sleep(2)
        LOCATION = LOCATION.move_on


def nokk_encounter():
    """
    Handles the interaction between player and
    the Nokk (when encountered)
    """
    global LOCATION
    global EXIT_GAME
    print(nokk_conversation[0])
    time.sleep(6)
    if "Púca" in inventory:
        print(nokk_conversation[1])
        time.sleep(6)
        print(win_sequence[0])
        time.sleep(6)
        print(f"{Fore.LIGHTGREEN_EX}CONGRATULATIONS! YOU BEAT THE GAME VIA THE\
 SECRET ROUTE{Style.RESET_ALL}")
        EXIT_GAME = True
    elif "Púca" not in inventory and "rusted sword" in inventory:
        print(nokk_conversation[2])
        print(nokk_conversation[3])
        monsters_met.append(which_monster())
        inventory.remove("rusted sword")
        time.sleep(12)
        LOCATION = LOCATION.move_on
    else:
        print(nokk_conversation[2])
        time.sleep(6)
        print(nokk_conversation[4])
        game_over()


def sphinx_encounter():
    """
    Handles the interaction between player and
    the Sphinx (when encountered)
    """
    global LOCATION
    print(sphinx_conversation[0])
    player_talk = input("What will you say?\n>")
    if player_talk.lower().strip() in affirmative:
        print(sphinx_conversation[1])
        player_talk2 = input("What is your answer?\n>")
        if player_talk2.lower().strip() in correct_answer:
            print(sphinx_conversation[2])
            monsters_met.append(which_monster())
            time.sleep(6)
            LOCATION = LOCATION.move_on
        else:
            print(sphinx_conversation[3])
            game_over()
    else:
        print(sphinx_conversation[4])
        game_over()


def win():
    """
    Sequence when player wins
    the game.
    """
    print(anansi_conversation[0])
    print(f"{Fore.LIGHTCYAN_EX}'They are the:\n{', '.join(monsters_met)}\nand\
 finally, myself. I am known as Anansi.\nThe creature that was hunting you is\
 known as a Chupacabra.'{Style.RESET_ALL}\n")
    player_talk = input(f"{Fore.LIGHTCYAN_EX}'Would you like to know more\
 about any of these beings?\nOr perhaps you do not know what a mythical\
 creature is?\nWould you like to expand your knowledge?\nA simple\
 yes or no will suffice.'{Style.RESET_ALL}\n>")
    while player_talk.lower().strip() not in stop_game and \
            player_talk.lower().strip() not in negative:
        player_talk = input(f"{Fore.LIGHTCYAN_EX}'Which being would you like\
 to know more about?'{Style.RESET_ALL}\n>")
        if player_talk.lower().strip() == "mythical creature" or \
                player_talk.lower().strip() == "mythical creatures":
            print(Monster.definition)
            player_talk = input(f"{Fore.LIGHTCYAN_EX}'Would you like to know\
 more?'{Style.RESET_ALL}\n>")
        elif player_talk.lower().strip() == "kitsune" or \
                player_talk.lower().strip() == "the kitsune":
            print(kitsune.description())
            player_talk = input(f"{Fore.LIGHTCYAN_EX}'Would you like to know\
 more?'{Style.RESET_ALL}\n>")
        elif player_talk.lower().strip() == "naga" or \
                player_talk.lower().strip() == "the naga":
            print(naga.description())
            player_talk = input(f"{Fore.LIGHTCYAN_EX}'Would you like to know\
 more?'{Style.RESET_ALL}\n>")
        elif player_talk.lower().strip() == "dragon" or \
                player_talk.lower().strip() == "the dragon":
            print(dragon.description())
            player_talk = input(f"{Fore.LIGHTCYAN_EX}'Would you like to know\
 more?'{Style.RESET_ALL}\n>")
        elif player_talk.lower().strip() == "surale" or \
                player_talk.lower().strip() == "the surale" or\
                player_talk.lower().strip() == "Şüräle" or \
                player_talk.lower().strip() == "the Şüräle":
            print(surale.description())
            player_talk = input(f"{Fore.LIGHTCYAN_EX}'Would you like to know\
 more?'{Style.RESET_ALL}\n>")
        elif player_talk.lower().strip() == "puca" or \
                player_talk.lower().strip() == "the puca" or \
                player_talk.lower().strip() == "púca" or \
                player_talk.lower().strip() == "the púca":
            print(puca.description())
            player_talk = input(f"{Fore.LIGHTCYAN_EX}'Would you like to know\
 more?'{Style.RESET_ALL}\n>")
        elif player_talk.lower().strip() == "nokk" or \
                player_talk.lower().strip() == "the nokk" or \
                player_talk.lower().strip() == "nøkk" or \
                player_talk.lower().strip() == "the nøkk":
            print(nokk.description())
            player_talk = input(f"{Fore.LIGHTCYAN_EX}'Would you like to know\
 more?'{Style.RESET_ALL}\n>")
        elif player_talk.lower().strip() == "sphinx" or \
                player_talk.lower().strip() == "the sphinx":
            print(sphinx.description())
            player_talk = input(f"{Fore.LIGHTCYAN_EX}'Would you like to know\
 more?'{Style.RESET_ALL}\n>")
        elif player_talk.lower().strip() == "anansi" or \
                player_talk.lower().strip() == "you":
            print(anansi.description())
            player_talk = input(f"{Fore.LIGHTCYAN_EX}'Would you like to know\
 more?'{Style.RESET_ALL}\n>")
        elif player_talk.lower().strip() == "chupacabra" or \
                player_talk.lower().strip() == "the chupacabra":
            print(chupacabra.description())
            player_talk = input(f"{Fore.LIGHTCYAN_EX}'Would you like to know\
 more?'{Style.RESET_ALL}\n>")
        else:
            print(f"{Fore.LIGHTCYAN_EX}'I'm sorry, I can only tell you about\
 the:\n{', '.join(monsters_met)}, myself\nor what mythical \
 creatures are in general.'{Style.RESET_ALL}")
    else:
        print(anansi_conversation[1])
        time.sleep(6)
        print(win_sequence[0])
        time.sleep(6)
        print(f"{Fore.LIGHTGREEN_EX}CONGRATULATIONS! YOU BEAT THE\
 GAME{Style.RESET_ALL}")


def which_monster():
    """
    Find out which monster is in the player's
    current location.
    """
    if LOCATION in who_is_where:
        value = who_is_where.get(LOCATION).name
        return value


def take_items(thing='item'):
    """
    Checks if there are items in that location and
    allows player to pick up items and add them to
    their inventory.
    """
    if thing == 'item':
        if LOCATION.item not in inventory and LOCATION.item is not None:
            inventory.append(LOCATION.item)
            print(f"{Fore.LIGHTMAGENTA_EX}You have added{Fore.LIGHTYELLOW_EX}\
 {LOCATION.item} {Fore.LIGHTMAGENTA_EX}to your inventory.{Style.RESET_ALL}\n")
        elif LOCATION.item in inventory:
            print(f"{LOCATION.item} {Fore.LIGHTMAGENTA_EX}is already in your\
 inventory{Style.RESET_ALL}\n")
        else:
            print(f"{Fore.LIGHTMAGENTA_EX}There's nothing here that you can\
 take with you.{Style.RESET_ALL}\n")
    elif thing == 'gift':
        inventory.append(LOCATION.gift)
        print(f"{Fore.LIGHTMAGENTA_EX}The {which_monster()} added\
 {Fore.LIGHTYELLOW_EX}{LOCATION.gift} {Fore.LIGHTMAGENTA_EX}to your\
 inventory{Style.RESET_ALL}\n")


def validate_path(follow='path'):
    """
    Checks if player is allowed to leave / move to a new
    location, or if they have to do something here before
    being allowed to move on.
    """
    global LOCATION
    if follow == 'spider':
        LOCATION = LOCATION.follow_spider
    elif follow == 'path':
        LOCATION = LOCATION.path
    if hasattr(LOCATION, "description") is False:
        print(f"{Fore.LIGHTMAGENTA_EX}Although the path is ahead,\n"
              f"you cannot see a way to pass by the creature without "
              f"putting yourself in harm's way.{Style.RESET_ALL}\n")
        LOCATION = visited[-1]
    else:
        visited.append(LOCATION)
        time.sleep(1)
        print(LOCATION.description)


def game_over():
    """
    Game over sequence for when the player dies
    """
    global LOCATION
    global EXIT_GAME
    print(f"{Fore.LIGHTRED_EX}you have died{Style.RESET_ALL}\n")
    player_input4 = input("would you like to try again,\
 start over or stop playing?\n")
    if player_input4.lower().strip() == "start over":
        LOCATION = entrance
        inventory.clear()
        monsters_met.clear()
    elif player_input4.lower().strip() == "stop playing":
        print(f"{Fore.LIGHTCYAN_EX}'We're sorry to see you\
 go...'{Style.RESET_ALL}")
        EXIT_GAME = True


def main():
    """
    Fires up all active functions, in correct order, that make the game run
    """
    display_intro()
    location_arrival()


main()
