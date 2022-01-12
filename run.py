"""
Mythos Maze: an adventure game.
"""


import time


class Location:
    """
    class used for the different locations within the Maze.
    """

    def __init__(self, description):
        self.description = description
        self.path = None
        self.follow_spider = None
        self.move_on = None
        self.item = None
        self.gift = None


entrance = Location("Darkness...\nA herbal scent assaults your senses,\
 sage? Or maybe thyme?\nThe sensation\
 of falling jerks you awake, your eyes opening to a sea of stars as your\
 erratic heartbeat tries to stabilize.\nA sliver of a crescent moon\
 shines down on you like an unnatural, mocking grin.\nIts weak silvery\
 light glints off the edge of a rusted sword lying in the grass beside\
 you.\nYou sit up slowly, craning your neck to take in the\
 tall black hedges rising ominously on either side of you.\nAhead,\
 you see a large stone archway, weathered by time, leading the way deeper\
 into the darkness of the maze.\nAs you turn your head to look at what's\
 behind you, you hear a twig snap loudly.\nYou freeze before you can\
 see what lies in that direction, a shiver running down your spine..\n")
entrance.item = "rusted sword"
passage_one = Location("The hedges feel as if they're closing in on you,\
 the path is dark.\nIn your haste to get away your foot catches on something\
 and you trip, your knees and hands breaking your fall awkwardly on the uneven\
 ground.\nAs you look back to see what tripped you, you stifle a gasp.\nA\
 skeleton in ragged clothing is staring at you with hollow eyesockets.\nIn\
 the pocket of its worn-away vest you see something emit an eerie\
 glow.\nYour hand reaches for it involuntarily, but you quickly jerk it back\
 when a shadow scuttles out from behind the skeleton.\nA spider as large as\
 your hand crawls up the poor man's remains.\nIt hesitates when it notices\
 you, its small head twisting as if puzzled by your presence.\nYou stare\
 at it in bafflement when it raises a hairy leg, almost as if in\
 greeting.\nBut before you can think it through a low growl emits from the\
 direction of the archway you just passed and the spider scurries away\
 through a medium-sized hole in the hedge you hadn't noticed earlier.\n")
passage_one.item = "hoshi no tama"
passage_two = Location("a brighter path, filled with pieces of old masonry\n")
passage_two.item = "bloodstained spurred boots"
passage_three = Location("Panic hits you like a wave as you raise your arms\
 to block the fire.\nYour eyes close tightly as you feel the force of the\
 flames lift your feet off the ground making your world spin.\nYou barely\
 register that your arms aren't getting burned.\nWhen the roaring sound leaves\
 your ears, you slowly open your eyes again.\nYou're surrounded by a muddy\
 swamp, twinkling lights are luring you forward onto the overgrown path.\nAs\
 you take a step forward something heavy lands on your shoulder.\nYou jump\
 and quickly bat at yourself in a frantic attempt to get it off you.\nIt\
 lands on the ground by your feet and you immediately recognize the spider,\
 or maybe it's a different spider?\nThe creature raises both its front legs\
 in affront at your rough treatment, then casually makes its way through the\
 shallow mud on your left, away from the main path...\n")
passage_three.gift = "nature's blessing"
passage_four = Location("a dry area, the hedges are little more than thorns\n")
passage_five = Location("a forest, the smell of pine surrounds you\n")
kitsune_lair = Location("You emerge to see a twisting path leading to a\
 beautiful inari shrine\nDusting off your knees and pulling twigs and leaves\
 out of your clothes, you look up as you hear a strange sound.\nAt first you\
 think you might be hearing things, but when you hear it again it's\
 unmistakably the sound of a child crying.\nHaving no choice but to move\
 forward, you follow the torchlit path.\nAs the shrine comes fully into view\
 you notice a frail looking little girl, probably no older than six, hiding\
 her face in her hands as she sobs.\nHer hands are dirty but her kimono looks\
 clean.\nSomething in the girl's shadow draws your eyes, but the flickering\
 torchlight is fickle and dances this way and that.\nBefore you can scrutinize\
 it further the little girl hiccups and looks up as she notices\
 you.\nsniffling, she speaks in a barely audible voice:\n'hello'.\n")
kitsune_lair.gift = "milk"
naga_lair = Location("A temporary cloud has cast your surroudings in total\
 darkness.\nWhen the sky clears, the weak moonlight reflects off a shallow\
 stream and you notice a tall dark cave on its opposite bank.\nA creature\
 slithers out of the cave.\nIts upper body is human, but his lower body is\
 that of a snake.\nSo far, the being hasn't noticed you yet...\n")
naga_lair.gift = "a large bloodred ruby"
dragon_lair = Location("volcanic rock seems to glow in the darkness\n")
surale_lair = Location("massive pine trees obscure the moonlight\n")
puca_lair = Location("ancient ruins lie in pieces around you\n")
puca_lair.item = "Púca"
nokk_lair = Location("a pond of silver, the large water lilies glowing pink\n")
sphinx_lair = Location("glittering sand swirls as the wind rises\n")
leave_maze = Location("the air clears, the maze's hedges disintegrate\n")

entrance.path = passage_one
passage_one.path = passage_two
passage_one.follow_spider = kitsune_lair
passage_two.path = puca_lair
passage_three.path = naga_lair
passage_three.follow_spider = naga_lair
passage_four.path = sphinx_lair
passage_five.path = surale_lair
passage_five.follow_spider = leave_maze
kitsune_lair.move_on = passage_three
naga_lair.path = dragon_lair
dragon_lair.move_on = passage_five
surale_lair.move_on = leave_maze
puca_lair.move_on = nokk_lair
nokk_lair.move_on = passage_four
sphinx_lair.move_on = leave_maze

monster_locations = [kitsune_lair, passage_three, naga_lair, dragon_lair,
                     surale_lair, puca_lair, nokk_lair, sphinx_lair]


class Monster:
    """
    class to define the mythical creatures
    you can run into in the Maze.
    """

    definition = "a mythical creature is a monster that is\
 unverifiable but popularly accepted as possibly factual"

    def __init__(self, name, origin, characteristics):
        self.name = name
        self.origin = origin
        self.characteristics = characteristics

    def description(self):
        """
        describe the creature
        """
        return f"A {self.name} has {self.origin}\
 origin.\n{self.characteristics}."


kitsune = Monster("Kitsune", "Japanese", "Kitsune is the Japanese word\
 for 'Fox', they are extremely intelligent and very powerful\
 shape-shifters.\nKitsune are specially known for their charm abilities,\
 illusions, possession, and mind manipulation.\nThe more tails a kitsune\
 has (they may have as many as nine) the older, wiser,and more powerful it\
 is.\nBecause of their potential power and influence, some people make\
 sacrifices to them as to a deity")
naga = Monster("Naga", "Hindu", "The Naga is a semidivine being,\
 they are a strong handsome species who are half human and half\
 cobra.\nNaga bite only the truly evil, or those destined to die\
 prematurely.\nThey are also associated with waters (rivers, lakes,\
 seas, and wells) and are guardians of treasure")
dragon = Monster("Dragon", "European", "European dragons are\
 typically depicted as a large, fire-breathing, scaly, horned,\
 lizard-like creature.\nDragon's blood often contains unique powers,\
 keeping them alive for longer or giving them poisonous or acidic\
 properties.\nClassical European dragons are often described as\
 illuminating the air, most protect a cavern or castle filled\
 with gold and treasure")
surale = Monster("Şüräle", "Tatar and Bashkir", "The Şüräle are\
 forest spirits, bogeymen and shapeshifters.\nThey have a humanoid figure\
 with long bony fingers, thick fur and a single horn in their forehead.\nThe\
 Şüräle is a trickster who likes to lead travelers astray and\
 enjoys tickling its victims to death.\nIn human form\
 they have their shoes on backwards")
puca = Monster("Púca", "Celtic", "The Púcai are considered\
 to be bringers of both good and bad fortune.\nThough shapeshifters,\
 they often come in the shape of wild colts.\nNo matter what shape the púca\
 takes, its fur is almost always dark.\nPúca are commonly said to entice\
 humans to take a ride on their back, giving the rider a wild\
 and terrifying journey")
nokk = Monster("Nøkk", "Scandinavian", "The Nøkken are fair male water spirits\
 who play enchanted songs on their violins.\nLegend has it they lured women\
 and children to drown in lakes or streams.\nThough many stories indicate they\
 were mostly harmless and attracted not only women and children, but men as\
 well with their sweet songs")
sphinx = Monster("Sphinx", "Greek", "The Sphinx is a female monster\
 with the body of a lion, the head and breast of a woman, eagle's wings\
 and a serpent's tail.\nShe devours all who fail to solve her riddle")
chupacabra = Monster("Chupacabra", "Latin-American", "The chupacabra is a\
 monstrous creature that attacks animals and consumes their blood.\nPhysical\
 descriptions of the Chupacabra vary, with some describing it as more dog-like\
 while most others describe it as reptilian and alien-like.\nSome report\
 it as being a heavy creature the size of a small bear, with a row of spines\
 reaching from the neck to the base of the tail")
anansi = Monster("Anansi", "West-African", "Anansi is most well known\
 for his ability to outsmart and triumph over more powerful opponents through\
 his use of cunning, creativity and wit.\nHe often takes the shape of a spider\
 and is sometimes considered to be a god of all knowledge of stories")
fairies = Monster("Fairies", "many", "Fairies are feared as dangerous and\
 powerful beings who are sometimes friendly to humans but can also be cruel\
 or mischievous.\nPeople believed that these fairies lived underground,\
 in deep forests or near water areas.\nThe civilians avoided crossing such\
 paths that were notorious as fairy residences. People even had the corners\
 of their homes removed to avoid interfering in the fairy pathway.\n")

who_is_where = {kitsune_lair: kitsune, naga_lair: naga, dragon_lair: dragon,
                surale_lair: surale, puca_lair: puca, nokk_lair: nokk,
                sphinx_lair: sphinx, passage_three: fairies}

kitsune_conversation = ["'Are you certain? It's easy to spot, it glows and\
 it's very pretty.'", "Tentatively she holds her shaking hands out towards\
 you.\nThe girl appears almost nervous, as if you might change your mind at\
 the last second.\nWhen you drop the small glowing orb into her outstretched\
 hands a ripple of relief seems to wash over her.\nShe clasps the little ball\
 tightly to her chest and beneath her lowered bangs you see a grin\
 unfurl.\n'Thank you, human.'\nShe looks up suddenly, her slit pupils\
 belying her human disguise.\n'A favour for a favour is in order\
 I suppose..'\nYou barely have time to notice the five fox tails\
 unfurl from behind the girl's body before a gulf of flame consumes\
 you.\n", "The girl's face morphs in anger and her voice takes on a\
 menacing timbre as she stalks towards you.\nHer form shimmering and\
 slowly changing shape.\n'You dare steal what is mine?'\nAs the girl\
 grows in size she simultaneously seems to become transparent.\nThe\
 last visible part of her are her slit eyes burning with a deep\
 hatred.\n'Despicable creature.'\nYou're rooted to the spot as she lunges\
 towards you in a formless kind of smoke.\nLifting your hands in a last\
 attempt at defense you scream in horror as you see the smoke force its\
 way beneath your fingernails...\n", "'Do you have it? Will you give it\
 back to me?'", "'Hm, you don't have it with you though...\nBut if you've\
 seen it, it must not be far. I suppose I'll track back in the direction\
 you came from.'\nThe girl's eyes suddenly take on a ruthless sheen.\n'I'm\
 afraid that means you are no longer of use to me human. No hard\
 feelings.'\n", "'No?' The girl sighs, suddenly all measure of sadness\
 seems to have left her.\nHer pupils slit as she regards you in a kind of\
 measured boredom.\n'I'm afraid you've outstayed your usefulness, human.'\n"]
naga_conversation = ["You tentatively approach the creature, halting by the\
 bank of the small stream.\nIts body tenses when it notices your scent,\
 looking up sharply, only to relax as it catches sight of you.\n'Well\
 well, a human? How did you get lossst in here little mouse? Did you come\
 to be my dinner?'\n", "'No? a ssshame.'\nThe creature's tongue darts out,\
 tasting the air, its regard turning speculative as it assesses you.\n'I\
 see you have received the Fairies' blessing.\nI suppossse I can gift\
 you sssome of my preciousss time human.\nWhat have you brought me in\
 offering?'\n", "The creature's gaze lights up.\n'where did you obtain thisss?\
 I have not feasted on sssuch a treat for many a moon.'\n He looks up from\
 his new prize, regarding you almost with kindness.\n'Here, take thisss and\
 hurry along now, or it is not MY dinner you will become.'\n", "The creature\
 blinks, then bursts out laughing.\nIt shows off its large, elongated\
 canines and flexes its claws in a semi-threatening display.\n'What ussse\
 do you imagine I could have for that rusted piece of former glory?\nUnless\
 you plan to ssstrike me down human?'\nHe slithers closer on his long tail,\
 looming over you in a way that makes you shift uncomfortably in place.\n'Let\
 me advissse you againssst the latter'\n", "The creature's tongue darts out,\
 its brow furrows in annoyance.\n'Fortunately for you I do not eat junk\
 food.\nThough I might dispose of you in other ways.\nBegone lowly creature,\
 before I change my mind and give you a taste of my claws.'\n"]
dragon_conversation = [""]


affirmative = ["yes", "y", "definitely", "let's go", "bring it",
               "hell yes", "absolutely", "I might have"]
negative = ["no", "n", "no way", "hell no", "absolutely not", "never",
            "nope"]
follow_path = ["path", "follow path", "straight", "straight ahead",
               "keep going", "go into the maze", "enter maze", "go into maze",
               "head deeper into maze", "run away", "run", "forward", "move",
               "move forward", "onward", "continue"]
follow_spider = ["follow spider", "spider", "after spider", "side passage",
                 "hole", "move through hole", "move through hedge"]
stop_game = ["quit", "go home", "leave maze", "exit"]
seal_your_doom = ["help!", "investigate noise", "investigate",
                  "investigate sound", "go back", "turn back", "hide", "shout",
                  "scream", "attack", "use sword"]
pickup_items = ["search pocket", "search pockets", "pick up", "pick up item",
                "take", "take item", "take boots", "take sword",
                "pick up boots", "pick up sword", "investigate", "grab sword",
                "grab item", "pickup sword", "pickup item", "search skeleton",
                "search body", "search"]
avoid = ["leave", "don't help", "don't listen", "go away", "sneak past",
         "sneak"]


def display_intro():
    """
    Displays the opening / introductory text of the game.
    """
    intro_done = False
    while intro_done is False:
        player_input = input("Welcome to the Mythos Maze, would you like to\
 try and traverse its perils?\n")
        if player_input.lower().strip() in affirmative:
            player_input2 = input("Are you sure?\n")
            if player_input2.lower().strip() in affirmative:
                print("Very well then, it's your funeral. Good luck mortal\n")
                intro_done = True
            else:
                print("Indecision is the thief of opportunity you know...\n")
        elif player_input.lower().strip() in negative:
            print("A wise choice.")
            time.sleep(1)
            print("However, please don't hesitate to visit\
 me again should you change your mind.\n")
        else:
            print("Such confidence, best run back and hide behind your\
 mother's skirts child.\n")


LOCATION = entrance
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
    player_input3 = input("What will you do?\n")
    if player_input3.lower().strip() in stop_game:
        print("")
    while player_input3.lower().strip() not in stop_game:
        if LOCATION is monster_locations[0] and player_input3.lower().strip()\
                not in avoid:
            kitsune_encounter()
            location_arrival()
            break
        elif LOCATION is monster_locations[1] and \
                player_input3.lower().strip() in follow_spider:
            take_items('gift')
            monsters_met.append(which_monster())
            validate_path('spider')
            player_input3 = input("What will you do?\n")
        elif LOCATION is monster_locations[1] and \
                player_input3.lower().strip() == "drink milk":
            print("The delicious milk revitalizes and refreshes you.")
            inventory.remove("milk")
            player_input3 = input("What will you do?\n")
        elif LOCATION is monster_locations[2] and \
                player_input3.lower().strip() not in avoid and \
                player_input3.lower().strip() not in follow_path and\
                player_input3.lower().strip() not in follow_spider:
            naga_encounter()
            location_arrival()
            break
        elif LOCATION is monster_locations[2] and \
                player_input3.lower().strip() in avoid:
            validate_path()
            player_input3 = input("what will you do?\n")
        elif LOCATION is monster_locations[3] and \
                player_input3.lower().strip() not in avoid:
            dragon_encounter()
            location_arrival()
            break
        elif LOCATION in monster_locations and player_input3.lower().strip()\
                in avoid and LOCATION is not monster_locations[2]:
            print("Though you want to leave, your fear and uncertainty keep\
 you rooted to the spot.")
            player_input3 = input("What will you do?\n")
        elif player_input3.lower().strip() in pickup_items:
            take_items()
            player_input3 = input("What will you do?\n")
        elif player_input3.lower().strip() in follow_path:
            validate_path()
            player_input3 = input("What will you do?\n")
        elif player_input3.lower().strip() in follow_spider:
            validate_path('spider')
            player_input3 = input("What will you do?\n")
        elif player_input3.lower().strip() in seal_your_doom:
            game_over()
            break
        else:
            print("I'm afraid I don't quite catch your meaning")
            player_input3 = input("What will you do?\n")


def kitsune_encounter():
    """
    Handles interaction between player and
    the Kitsune (when encountered)
    """
    global LOCATION
    print("'I lost my marble, have you seen it?'")
    player_talk = input("What will you say?\n")
    if player_talk.lower().strip() in negative and "hoshi no tama" in \
            inventory:
        print(kitsune_conversation[0])
        player_talk2 = input("Will you hand over the hoshi no tama?\n")
        if player_talk2.lower().strip() in affirmative:
            print(kitsune_conversation[1])
            time.sleep(10)
            take_items('gift')
            monsters_met.append(which_monster())
            inventory.remove("hoshi no tama")
            LOCATION = LOCATION.move_on
        elif player_talk2.lower().strip() in negative:
            print(kitsune_conversation[2])
            game_over()
    elif player_talk.lower().strip() in affirmative and "hoshi no tama" in \
            inventory:
        print(kitsune_conversation[3])
        player_talk2 = input("Will you hand over the hoshi no tama?\n")
        if player_talk2.lower().strip() in affirmative:
            print(kitsune_conversation[1])
            time.sleep(10)
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
        print("it's not working")


def naga_encounter():
    """
    Handles interaction between player and
    the Naga (when encountered)
    """
    global LOCATION
    print(naga_conversation[0])
    player_talk = input("What will you say?\n")
    if player_talk.lower().strip() in negative and "milk" in \
            inventory and "nature's blessing" in inventory:
        print(naga_conversation[1])
        print("The contents of your inventory is currently: ")
        for i in inventory:
            print(i)
        player_talk2 = input("What will you offer?\n")
        while player_talk2.lower().strip() != "milk":
            if player_talk2.lower().strip() == "rusted sword":
                print(naga_conversation[3])
                player_talk2 = input("What will you offer?\n")
            elif player_talk2.lower().strip() == "nature's blessing":
                print("You cannot gift someone else's blessing of you\
 onto another person.")
                player_talk2 = input("What will you offer?\n")
            else:
                print("'I have no ussse for sssuch a thing human'")
                player_talk2 = input("What will you offer\n")
        else:
            print(naga_conversation[2])
            inventory.remove("milk")
            time.sleep(6)
            take_items('gift')
            LOCATION = LOCATION.path
    elif "nature's blessing" or "milk" not in inventory:
        print(naga_conversation[4])
        LOCATION = LOCATION.path


def dragon_encounter():
    """
    Handles interaction between player and
    the Dragon (when encountered)
    """


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
        if LOCATION.item is not None:
            inventory.append(LOCATION.item)
            print(f"You have added {LOCATION.item} to your inventory\n")
            LOCATION.item = None
        else:
            print("There's nothing to pick up")
    elif thing == 'gift':
        inventory.append(LOCATION.gift)
        print(f"The {which_monster()} added {LOCATION.gift} to\
 your inventory\n")


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
        print("Although the path is ahead, you cannot see\
 a way to pass by the creature without putting yourself in harm's way\n")
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
    print("you have died\n")
    player_input4 = input("would you like to try again,\
 start over or stop playing?\n")
    if player_input4.lower().strip() == "try again":
        location_arrival()
    elif player_input4.lower().strip() == "start over":
        LOCATION = entrance
        main()
    elif player_input4.lower().strip() == "stop playing":
        print("bye bye")


def main():
    """
    Fires up all active functions, in correct order, that make the game run
    """
    display_intro()
    location_arrival()


main()
