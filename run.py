"""
Mythos Maze: an adventure game
"""
import time


class Location:
    """
    Class used for the different locations within the Maze
    """
    def __init__(self, description):
        self.description = description
        self.path = None
        self.follow_spider = None
        self.item = None
        self.item2 = None


entrance = Location("a large stone archway looms before you.")
passage_one = Location("")
passage_one.item = "hoshi no tama"
passage_two = Location("")
passage_two.item = "bloodstained spurred boots"
passage_two.item2 = "rusted sword"
passage_three = Location("")
passage_four = Location("")
passage_five = Location("")
kitsune_lair = Location("")
kitsune_lair.item = "milk"
naga_lair = Location("")
naga_lair.item = "gem"
dragon_lair = Location("")
surale_lair = Location("")
puca_lair = Location("")
noxx_lair = Location("")
sphinx_lair = Location("")
leave_maze = Location("")
