"""
Mythos Maze: an adventure game
"""
import time


class Location:
    """
    class used for the different locations within the Maze
    """
    def __init__(self, description):
        self.description = description
        self.path = None
        self.follow_spider = None
        self.item = None
        self.item2 = None


entrance = Location("a large stone archway looms before you.")
passage_one = Location("hedges confine you on both sides, the path is dark")
passage_one.item = "hoshi no tama"
passage_two = Location("a brighter path, filled with pieces of old masonry")
passage_two.item = "bloodstained spurred boots"
passage_two.item2 = "rusted sword"
passage_three = Location("a muddy swamp, twinkling lights lure you forward")
passage_three.item = "nature's blessing"
passage_four = Location("a dry area, the hedges are little more than thorns")
passage_five = Location("a forest, the smell of pine surrounds you")
kitsune_lair = Location("a twisting path leading to a beautiful inari shrine")
kitsune_lair.item = "milk"
naga_lair = Location("a stream with a tall dark cave on its opposite bank")
naga_lair.item = "gem"
dragon_lair = Location("volcanic rock seems to glow in the darkness")
surale_lair = Location("massive pine trees obscure the moonlight")
puca_lair = Location("ancient ruins lie in pieces around you")
nokk_lair = Location("a pond of silver, the large water lilies glowing pink")
sphinx_lair = Location("glittering sand swirls as the wind rises")
leave_maze = Location("the air clears, the maze's hedges disintegrate")

entrance.path = passage_one
passage_one.path = passage_two
passage_one.follow_spider = kitsune_lair
passage_two.path = puca_lair
passage_three.path = naga_lair
passage_three.follow_spider = naga_lair
passage_four.path = sphinx_lair
passage_five.path = surale_lair
passage_five.follow_spider = leave_maze


class Monster:
    """
    class to define the mythical creatures
    you can run into in the Maze
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
chupacabra = Monster("Chupacabra", "Latin-American", "The chupacabra is a monstrous\
 creature that attacks animals and consumes their blood.\nPhysical\
 descriptions of the Chupacabra vary, with some describing it as more dog-like\
 while most others describe it as reptilian and alien-like.\nSome report\
 it as being a heavy creature the size of a small bear, with a row of spines\
 reaching from the neck to the base of the tail")
anansi = Monster("Anansi", "West-African", "Anansi is most well known\
 for his ability to outsmart and triumph over more powerful opponents through\
 his use of cunning, creativity and wit.\nHe often takes the shape of a spider\
 and is sometimes considered to be a god of all knowledge of stories")


Location = entrance


def display_intro():
    """
    Displays the opening / introductory text of the game
    """
    intro_done = False
    while intro_done is False:
        player_input = input("Welcome to the Mythos Maze, would you like to try and traverse\
 its perils?\n")
        affirmative = ["yes", "y", "definitely", "let's go", "bring it",
                       "hell yes", "absolutely"]
        negative = ["no", "n", "no way", "hell no", "absolutely not", "never",
                    "nope"]
        if player_input.lower().strip() in affirmative:
            player_input2 = input("Are you sure?\n")
            if player_input2.lower().strip() in affirmative:
                print("Very well then, it's your funeral. Good luck mortal...")
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


def main():
    """
    Fires up all active functions, in correct order, that make the game run
    """
    display_intro()


main()
