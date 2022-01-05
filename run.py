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
noxx_lair = Location("a pond of silver, the large water lilies glowing pink")
sphinx_lair = Location("golden sand swirls as the wind rises")
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
