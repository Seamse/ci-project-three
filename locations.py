"""
Locations class, details about
locations that can be visited and
the connection between the locations
"""

from colorama import Fore
from colorama import Style


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


entrance = Location(f"{Fore.LIGHTMAGENTA_EX}Darkness...\nThe sensation\
 of falling jerks you awake, your eyes opening\nto a sea of stars as your\
 erratic heartbeat tries to stabilize.\nA sliver of a crescent moon\
 shines down on you like an unnatural, mocking grin.\nIts weak silvery\
 light glints off the edge of a rusted sword\nlying in the grass beside\
 you.\nYou sit up slowly, craning your neck to take in the\ntall\
 black hedges rising ominously on either side of you.\nStanding\
 up, you notice your feet are bare.\nAhead, you see a large stone\
 archway, weathered by time,\nleading the way deeper\
 into the darkness of the maze.\nAs you turn your head to look at what's\
 behind you, you hear a twig snap loudly.\nYou freeze before you can\
 see what lies in that direction,\na shiver running down your\
 spine..{Style.RESET_ALL}\n")
entrance.item = "rusted sword"
passage_one = Location(f"{Fore.LIGHTMAGENTA_EX}The hedges feel as if\
 they're closing in on you, the path is dark.\nIn your haste to get away\
 your foot catches on something and you trip,\nyour knees and hands breaking\
 your fall awkwardly on the uneven ground.\nAs you look back to see what\
 tripped you, you stifle a gasp.\nA skeleton in ragged clothing is staring\
 at you with hollow eyesockets.\nIn the pocket of its worn-away vest you see\
 something emit an eerie glow.\nYour hand reaches for it involuntarily,\nbut\
 you quickly jerk it back when a shadow scuttles out from behind the\
 skeleton.\nA spider as large as your hand crawls up the poor man's\
 remains.\nIt hesitates when it notices you,\nits small head twisting\
 as if puzzled by your presence.\nYou stare at it in bafflement when it\
 raises a hairy leg,\nalmost as if in greeting.\nBut before you can think\
 it through a low growl emits from the direction of\nthe archway you just\
 passed and the spider scurries away through\na medium-sized hole in the\
 hedge you hadn't noticed earlier.{Style.RESET_ALL}\n")
passage_one.item = "hoshi no tama"
passage_two = Location(f"{Fore.LIGHTMAGENTA_EX}You're greeted by a brighter\
 path,\nfilled with pieces of old looking, crumbled masonry.\nYou notice\
 something glinting in the moonlight.\nThough you fear what that might be,\
 you fear whatever's chasing you even more.\nSo you keep going, the breeze\
 raising goosebumps on your skin.\nAs you get closer you realize it's a pair\
 of spurred boots,\nthe dark stains on them do not inspire much\
 confidence.\nA bone chilling howl sounds from somewhere behind you in\
 the maze...{Style.RESET_ALL}\n")
passage_two.item = "bloodstained spurred boots"
passage_three = Location(f"{Fore.LIGHTMAGENTA_EX}Panic hits you like a wave\
 as you raise your arms to block the fire.\nYour eyes close tightly as you\
 feel the force of the flames lift your feet off the ground making your\
 world spin.\nYou barely register that your arms aren't getting\
 burned.\nWhen the roaring sound leaves your ears, you slowly open your\
 eyes again.\nYou're surrounded by a muddy swamp,\ntwinkling lights are\
 luring you forward onto the overgrown path.\nAs you take a step forward\
 something heavy lands on your shoulder.\nYou jump and quickly bat at\
 yourself in a frantic attempt to get it off you.\nIt lands on the ground\
 by your feet\nand you immediately recognize the spider, or maybe it's a\
 different spider?\nThe creature raises both its front legs in affront\
 at your rough treatment,\nthen casually makes its way through the shallow\
 mud on your left,\naway from the main path...{Style.RESET_ALL}\n")
passage_three.gift = "nature's blessing"
passage_four = Location(f"{Fore.LIGHTMAGENTA_EX}You run until you're out\
 of breath and find yourself in a dry area,\nthe maze's hedges here are\
 little more than thorns.\nYou notice another breach in the hedge to your\
 right,\nperhaps it's better to veer off the beaten path after all?\nAs if\
 he heard you, that big spider peeks out from that very direction.\nOr\
 maybe it's another spider?\nEither way, he looks at you a moment,\nbefore\
 once again scurrying off through the hole in the hedge.{Style.RESET_ALL}\n")
passage_five = Location(f"{Fore.LIGHTMAGENTA_EX}You don't need to think\
 twice, and though your legs quiver and your feet feel like lead,\nyou rush\
 past the massive creature as quickly as possible.\nThe blackened, steaming\
 rocks soon give way to trees which\ngive way to a forest until the smell\
 of pine surrounds you.\nSomething rustles in the needles coating the forest\
 floor and you tense up,\nonly to exhale in relief when a certain spider\
 reveals itself to you yet again.\nYou have the strangest urge to wave in\
 greeting at\nthe only creature you've encountered so far that didn't appear\
 to be trying to kill you.\nThe spider hops, you'd think he was happy to see\
 you...\nBefore you can decide whether to pass by him, he scurries off again\
 to your left.\nThe moonlight up ahead seems to indicate a glade of some\
 sort,\nthe open air inviting and perhaps leading to an exit.\nBut you notice\
 the spider stops and turns,\nalmost as if checking wether you're following\
 him onto the darker path or not...{Style.RESET_ALL}\n")
kitsune_lair = Location(f"{Fore.LIGHTMAGENTA_EX}You emerge to see a twisting\
 path leading to a beautiful inari shrine.\nDusting off your knees and\
 pulling twigs and leaves out of your clothes,\nyou look up as you hear\
 a strange sound.\nAt first you think you might be hearing things,\nbut\
 when you hear it again it's unmistakably the sound of a child\
 crying.\nHaving no choice but to move forward, you follow the torchlit\
 path.\nAs the shrine comes fully into view you notice a frail looking\
 little girl,\nprobably no older than six, hiding her face in her hands\
 as she sobs.\nHer hands are dirty but her kimono looks clean.\nSomething\
 in the girl's shadow draws your eyes,\nbut the flickering torchlight is\
 fickle and dances this way and that.\nBefore you can scrutinize it\
 further\nthe little girl hiccups and looks up as she notices you.\nsniffling,\
 she speaks in a barely audible\
 voice:\n{Fore.LIGHTCYAN_EX}'hello'.{Style.RESET_ALL}\n")
kitsune_lair.gift = "milk"
naga_lair = Location(f"{Fore.LIGHTMAGENTA_EX}A temporary cloud has cast your\
 surroudings in total darkness.\nWhen the sky clears, the weak moonlight\
 reflects off a shallow stream\nand you notice a tall dark cave on its\
 opposite bank.\nA creature slithers out of the cave.\nIts upper body is\
 human, but his lower body is that of a snake.\nSo far, the being hasn't\
 noticed you yet...{Style.RESET_ALL}\n")
naga_lair.gift = "a large bloodred ruby"
dragon_lair = Location(f"{Fore.LIGHTMAGENTA_EX}You run onwards, following\
 the main path\nwhich changes from grass, to sand, to gravel to rock.\nYou\
 fervently hope to find the exit just around the next corner.\nHeat\
 surrounds you, and when you round the corner,\nvolcanic rock glows in the\
 darkness.\nNo exit seems in sight and you fear you've hit a dead end,\nwhen\
 suddenly the large rock blocking your path starts moving.\nTalons\
 the size of your arm, scales gleaming in the orange light\nand a huge\
 muscular tail which nearly sweeps you off balance.\nYour heart freezes\
 in your throat when eyes the size of your head open to observe you.\nThe\
 gigantic creature huffs out a puff of air so hot you fear your skin might\
 burn.\nThen the creature sniffs the air so strongly,\nyou move an\
 involuntary step forward to keep your balance.\nFear slithers down your\
 spine and a shiver wracks your frame\nas you instinctively know that you\
 are facing an apex predator.{Style.RESET_ALL}\n")
surale_lair = Location(f"{Fore.LIGHTMAGENTA_EX}Massive pine trees obscure\
 the moonlight,\nthe promise of an open glade seems to have vanished into\
 thin air.\nThe idea of ever finding a way out of\nthis mess seems further\
 and further from your grasp.\nYou sit down on a large boulder in dejection,\
 unsure what to do next.\nThe sound of footsteps nears you, you look up\
 to see a woolly\nbipedal creature with long thin fingers and a horn on its\
 head.\nIn your haste to get away you stumble clumsily off the boulder and\
 fall backwards.\nIn a flash the creature is squatting on top of the\
 boulder,\nlooking down on you with a mischievous\
 grin.\n{Fore.LIGHTCYAN_EX}'Clumsy are we?, you entered my forest, so now\
 you must pay the tithe.\nI see the Fairies have taken a liking to you, so\
 for their sake\nI will not punish you for trespassing without a test.\nWill\
 you take my test human?'{Style.RESET_ALL}\n")
puca_lair = Location(f"{Fore.LIGHTMAGENTA_EX}Ancient ruins lie broken and\
 forgotten around you.\nTheir majesty belying glorious times long past.\nThe\
 magnificent horse you see roaming among them however, grabs your full\
 attention.\nThough its coat is black as night,\nthe pale moonlight appears\
 to shimmer off the creature in an enigmatic blue glow.\nHis eyes are two\
 ovals of liquid gold, lending him an almost demonic appearance.\nIt is then\
 you notice that those eyes\nare studying you as much as you were studying\
 him.\nThe creature approaches you,\nand though his advance makes you take\
 a hesitant step back,\nyou know heading back to whatever let loose that\
 howl is probably a worse idea.{Style.RESET_ALL}\n")
puca_lair.item = "Púca"
nokk_lair = Location(f"{Fore.LIGHTMAGENTA_EX}A massive pond of silver reveals\
 itself to you, water lilies glowing a magical pink.\nA violin can be heard\
 over the soft trickling of water from a nearby waterfall.\nTheir combined\
 music making for an enchanting melody.{Style.RESET_ALL}\n")
sphinx_lair = Location(f"{Fore.LIGHTMAGENTA_EX}The path appears to be getting\
 dryer and the air hotter.\nYour clothes have almost dried from the incident\
 at the lake.\nSuddenly the dead looking hedges make way for an\
 enormous\nclearing filled with hills of sand.\nGlittering kernels swirl as\
 the wind rises.\nThe creature you see at the center is beyond anything you've\
 ever imagined.\nA lion the size of a house, though instead of a\
 normal lion's head,\nshe has the upper torso and head of a human\
 woman.\nThe creature is casually playing with a mouse, letting it\
 escape,\nthen catching it again right before it can reach\
 freedom.\nSuddenly, her tail jerks excitedly and her head lifts up\
 as her\ncatlike gaze narrows in on you, like a hunter zoning in\
 on its prey.{Style.RESET_ALL}\n")
leave_maze = Location(f"{Fore.LIGHTMAGENTA_EX}The air clears, the world\
 around you disintegrates\nand suddenly you find yourself in a\
 meadow.\nMorning dew glints in the first rays of the rising sun,\nthe\
 grass blades bending from the water's weight.\nFor the first time that\
 night, you feel as if you can breathe again.\nYour spider friend sits\
 waiting for you amongst an array of sweet smelling flowers.\nHe grows\
 larger as you approach, yet for some reason, you do not feel fear.\nBy\
 the time you stand before him, he stands slightly taller than\
 yourself.\nHis head has morphed into that of a human male and he smiles\
 at you mysteriously.\n{Fore.LIGHTCYAN_EX}'Hello young\
 one.'{Style.RESET_ALL}\n")

entrance.path = passage_one
passage_one.path = passage_two
passage_one.follow_spider = kitsune_lair
passage_two.path = puca_lair
passage_three.path = naga_lair
passage_three.follow_spider = naga_lair
passage_four.path = sphinx_lair
passage_four.follow_spider = kitsune_lair
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
                     surale_lair, puca_lair, nokk_lair, sphinx_lair,
                     leave_maze]
confrontation_locations = [entrance, kitsune_lair, naga_lair,
                           dragon_lair, surale_lair, puca_lair, sphinx_lair,
                           leave_maze]
