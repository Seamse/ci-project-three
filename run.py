"""
Mythos Maze: an adventure game.
"""

import time
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
entrance.item = f"{Fore.LIGHTYELLOW_EX}rusted sword{Style.RESET_ALL}"
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
passage_one.item = f"{Fore.LIGHTYELLOW_EX}hoshi no tama{Style.RESET_ALL}"
passage_two = Location(f"{Fore.LIGHTMAGENTA_EX}You're greeted by a brighter\
 path,\nfilled with pieces of old looking, crumbled masonry.\nYou notice\
 something glinting in the moonlight.\nThough you fear what that might be,\
 you fear whatever's chasing you even more.\nSo you keep going, the breeze\
 raising goosebumps on your skin.\nAs you get closer you realize it's a pair\
 of spurred boots,\nthe dark stains on them do not inspire much\
 confidence.\nA bone chilling howl sounds from somewhere behind you in\
 the maze...{Style.RESET_ALL}\n")
passage_two.item = f"{Fore.LIGHTRED_EX}bloodstained\
 {Fore.LIGHTYELLOW_EX}spurred boots{Style.RESET_ALL}"
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
passage_three.gift = f"{Fore.LIGHTGREEN_EX}nature's blessing{Style.RESET_ALL}"
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
kitsune_lair.gift = f"{Fore.LIGHTYELLOW_EX}milk{Style.RESET_ALL}"
naga_lair = Location(f"{Fore.LIGHTMAGENTA_EX}A temporary cloud has cast your\
 surroudings in total darkness.\nWhen the sky clears, the weak moonlight\
 reflects off a shallow stream\nand you notice a tall dark cave on its\
 opposite bank.\nA creature slithers out of the cave.\nIts upper body is\
 human, but his lower body is that of a snake.\nSo far, the being hasn't\
 noticed you yet...{Style.RESET_ALL}\n")
naga_lair.gift = f"{Fore.LIGHTYELLOW_EX}a large\
 {Fore.LIGHTRED_EX}bloodred ruby{Style.RESET_ALL}"
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
puca_lair.item = f"{Fore.LIGHTYELLOW_EX}Púca{Style.RESET_ALL}"
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


class Monster:
    """
    class to define the mythical creatures
    you can run into in the Maze.
    """

    definition = "a mythical creature is a legendary being that is\
 unverifiable but popularly accepted as possibly factual.\nThey are\
 described in folklore and fall in the category of the supernatural\
 and paranormal.\n"

    def __init__(self, name, origin, characteristics):
        self.name = name
        self.origin = origin
        self.characteristics = characteristics

    def description(self):
        """
        describe the creature
        """
        return f"The {self.name} has {self.origin}\
 origins.\n{self.characteristics}"


kitsune = Monster("Kitsune", "Japanese", "Kitsune is the Japanese word\
 for 'Fox',\nthey are extremely intelligent and very powerful\
 shape-shifters.\nKitsune are specially known for their charm abilities,\
 illusions,\npossession, and mind manipulation.\nThe more tails a kitsune\
 has (they may have as many as nine)\nthe older, wiser,and more powerful it\
 is.\nBecause of their potential power and influence,\nsome people make\
 sacrifices to them as to a deity.\n")
naga = Monster("Naga", "Hindu", "The Naga is a semidivine being,\
 they are a strong\nhandsome species who are half human and half\
 cobra.\nNaga bite only the truly evil, or those destined to die\
 prematurely.\nThey are also associated with waters (rivers, lakes,\
 seas, and wells)\nand are guardians of treasure.\n")
dragon = Monster("Dragon", "European", "European dragons are\
 typically depicted as a large,\nfire-breathing, scaly, horned,\
 lizard-like creature.\nDragon's blood often contains unique powers,\
 keeping them alive\nfor longer or giving them poisonous or acidic\
 properties.\nClassical European dragons are often described as\
 illuminating the air,\nmost protect a cavern or castle filled\
 with gold and treasure.\n")
surale = Monster("Şüräle", "Tatar and Bashkir", "The Şüräle are\
 forest spirits, bogeymen and shapeshifters.\nThey have a humanoid figure\
 with long bony fingers,\nthick fur and a single horn in their forehead.\nThe\
 Şüräle is a trickster\nwho likes to lead travelers astray and\
 enjoys tickling its victims to death.\nIn human form\
 they have their shoes on backwards.\n")
puca = Monster("Púca", "Celtic", "The Púcai are considered\
 to be bringers of both good and bad fortune.\nThough shapeshifters,\
 they often come in the shape of wild colts.\nNo matter what shape the púca\
 takes, its fur is almost always dark.\nPúca are commonly said to entice\
 humans to take a ride on their back,\ngiving the rider a wild\
 and terrifying journey.\n")
nokk = Monster("Nøkk", "Scandinavian", "The Nøkken are fair male water spirits\
 who play enchanted songs on their violins.\nLegend has it they lured women\
 and children to drown in lakes or streams.\nThough many stories indicate they\
 were mostly harmless and attracted\nnot only women and children, but men as\
 well with their sweet songs.\nThey could be defeated by calling their name\
 which was believed to cause their death.\nIf a person brought the nøkk three\
 drops of blood, a black animal,\nscandivanian vodka or wet snuff, he would\
 teach them his enchanting music.\n")
sphinx = Monster("Sphinx", "Greek", "The Sphinx is a female monster\
 with the body of a lion, the head\nand breast of a woman, eagle's wings\
 and a serpent's tail.\nShe devours all who fail to solve her riddle.\n")
chupacabra = Monster("Chupacabra", "Latin-American", "The chupacabra is a\
 monstrous creature that attacks animals and consumes their blood.\nPhysical\
 descriptions of the Chupacabra vary, with some describing it as\
 more\ndog-like while most others describe it as reptilian and\
 alien-like.\nSome report it as being a heavy creature the size of a small\
 bear,\nwith a row of spines reaching from the neck to the base of the\
 tail.\n")
anansi = Monster("Anansi", "West-African", "I am most well known\
 for my ability to outsmart and triumph\nover more powerful opponents through\
 my use of cunning, creativity and wit.\nI often take the shape of a spider\
 and am sometimes\nconsidered to be a god of all knowledge of stories.\n")
fairies = Monster("Fairies", "many", "Fairies are feared as dangerous and\
 powerful beings\nwho are sometimes friendly to humans but can also be cruel\
 or mischievous.\nPeople believed that these fairies lived underground,\nin\
 deep forests or near water areas.\nThe civilians avoided crossing such\
 paths\nthat were notorious as fairy residences.\nPeople even had the corners\
 of their homes removed\nto avoid interfering in the fairy pathway.\n")

who_is_where = {kitsune_lair: kitsune, naga_lair: naga, dragon_lair: dragon,
                surale_lair: surale, puca_lair: puca, nokk_lair: nokk,
                sphinx_lair: sphinx, passage_three: fairies,
                leave_maze: anansi}

kitsune_conversation = [f"{Fore.LIGHTCYAN_EX}'Are you certain? It's easy to\
 spot, it glows and it's very pretty.'{Style.RESET_ALL}", f"\
 {Fore.LIGHTMAGENTA_EX}Tentatively she holds her shaking hands out\
 towards you.\nThe girl appears almost nervous, as if you might change your\
 mind at the last second.\nWhen you drop the small glowing orb into her\
 outstretched hands,\na ripple of relief seems to wash over her.\nShe clasps\
 the little ball tightly to her chest\nand beneath her lowered bangs you see\
 a grin unfurl.\n{Fore.LIGHTCYAN_EX}'Thank you, human.\
 '\n{Fore.LIGHTMAGENTA_EX}She looks up suddenly, her slit pupils\
 belying her human disguise.\n{Fore.LIGHTCYAN_EX}'A favour for a favour is in\
 order I suppose..'\n{Fore.LIGHTMAGENTA_EX}You barely have time to notice the\
 five fox tails unfurl\nbehind the girl's body before a gulf of flame consumes\
 you.{Style.RESET_ALL}\n", f"{Fore.LIGHTMAGENTA_EX}The girl's face morphs in\
 anger and her voice\ntakes on a menacing timbre as she stalks towards\
 you.\nHer form shimmering and slowly changing shape.\n{Fore.LIGHTCYAN_EX}'You\
 dare steal what is mine?'\n{Fore.LIGHTMAGENTA_EX}As the girl\
 grows in size she simultaneously seems to become transparent.\nThe\
 last visible part of her are her slit eyes burning with a deep\
 hatred.\n{Fore.LIGHTCYAN_EX}'Despicable creature.\
 '\n{Fore.LIGHTMAGENTA_EX}You're rooted to the spot as she lunges\
 towards you in a formless kind of smoke.\nLifting your hands in a last\
 attempt at defense\nyou scream in horror as you see the smoke force its\
 way beneath your fingernails...{Style.RESET_ALL}\n", f"{Fore.LIGHTCYAN_EX}'Do\
 you have it? Will you give it back to me?'{Style.RESET_ALL}", f"\
 {Fore.LIGHTCYAN_EX}'Hm, you don't have it with you though...\nBut if you've\
 seen it, it must not be far.\nI suppose I'll track back in the direction\
 you came from.'\n{Fore.LIGHTMAGENTA_EX}The girl's eyes suddenly take on a\
 ruthless sheen.\n{Fore.LIGHTCYAN_EX}'I'm afraid that means you are no longer\
 of use to me human.\nNo hard feelings.'{Style.RESET_ALL}\n", f"\
 {Fore.LIGHTCYAN_EX}'No?'{Fore.LIGHTMAGENTA_EX}The girl sighs, suddenly all\
 measure of sadness seems to have left her.\nHer pupils slit as she regards\
 you in a kind of measured boredom.\n{Fore.LIGHTCYAN_EX}'I'm afraid you've\
 outstayed your usefulness, human.'{Style.RESET_ALL}\n", f"\
 {Fore.LIGHTCYAN_EX}'I'm afraid I don't have time for\
 this'{Style.RESET_ALL}\n"]
naga_conversation = [f"{Fore.LIGHTMAGENTA_EX}You tentatively approach the\
 creature, halting by the bank of the small stream.\nIts body tenses when\
 it notices your scent, he looks up sharply,\nonly to relax as it catches\
 sight of you.\n{Fore.LIGHTCYAN_EX}'Well well, a human? How did you get lossst\
 in here little mouse?\nDid you come to be my dinner?'{Style.RESET_ALL}\n", f"\
 {Fore.LIGHTCYAN_EX}'No? a ssshame.'\n{Fore.LIGHTMAGENTA_EX}The creature's\
 tongue darts out, tasting the air,\nits regard turning speculative as it\
 assesses you.\n{Fore.LIGHTCYAN_EX}'I see you have received the Fairies'\
 blessing.\nI suppossse I can gift you sssome of my preciousss time\
 human.\nWhat have you brought me in offering?'{Style.RESET_ALL}\n", f"\
 {Fore.LIGHTMAGENTA_EX}The creature's gaze lights\
 up.\n{Fore.LIGHTCYAN_EX}'where did you obtain thisss?\
 I have not feasted on sssuch a treat for many a\
 moon.'\n{Fore.LIGHTMAGENTA_EX}He looks up from\
 his new prize, regarding you almost with kindness.\n{Fore.LIGHTCYAN_EX}'\
 Here, take thisss and hurry along now, or it is not MY dinner you will\
 become.'{Style.RESET_ALL}\n", f"{Fore.LIGHTMAGENTA_EX}The creature\
 blinks, then bursts out laughing.\nIt shows off its large, elongated\
 canines and\nflexes its claws in a semi-threatening\
 display.\n{Fore.LIGHTCYAN_EX}'What ussse\
 do you imagine I could have for that rusted piece of former glory?\nUnless\
 you plan to ssstrike me down human?'\n{Fore.LIGHTMAGENTA_EX}He slithers\
 closer on his long tail,\nlooming over you in a way that makes you shift\
 uncomfortably in place.\n{Fore.LIGHTCYAN_EX}'Let me advissse you againssst\
 the latter'{Style.RESET_ALL}\n", f"{Fore.LIGHTMAGENTA_EX}The creature's tongue\
 darts out, its brow furrows in annoyance.\n{Fore.LIGHTCYAN_EX}'Fortunately\
 for you I do not eat junk food.\nThough I might dispose of you in other\
 ways.\nBegone lowly creature, before I change my mind and give you a taste\
 of my claws.'{Style.RESET_ALL}\n"]
dragon_conversation = ["'Who dares enter my lair?'\n", "The beast makes a sound\
 reminiscent of a chuckle,\nbut it's so powerful it makes the ground\
 shake.\nYou dare lie to me human?.\nNo matter, I suppose you'll do as a\
 snack.'\n", "'Do not lie to me human! Were it not for the precious stone\
 you carry\nI would've eaten you for your insolence.\nGive it to me and I\
 might find myself in a more benevolent mood.'\n", "'A wise decision, such\
 a precious item belongs in a Dragon's hoard.\nI shall let you pass, this\
 time.'\n", "'Hmm, humans make tiny snacks.\nThough I would've eaten you\
 already regardless,\nwere it not for the precious cargo you carry.\nGive me\
 the ruby, child of man.'\n", "'You are either very brave, or very\
 foolish.\nWhichever it may be, this is the end of the line for you\
 child of man'\n"]
surale_conversation = ["The creature seems to think a moment\
 and then it snaps its lengthy fingers.\n'You shall either dance with me\
 or we can hold a tickling competition.'\nIt leaned further forward, his\
 nose almost touching yours.\n'Which shall it be human?'\n", "The creature\
 claps its hands.\n'Delightful!'\nbefore\
 you have the chance to do anything\nhe already lifted you up by your arms and\
 placed you on your feet.\nHe regards your bare feet in puzzlement for a\
 moment,\nbut then shrugs and drags you into a spinning motion with one strong\
 jerk.\nYou could swear you hear faint music from somewhere accompanying your\
 awkward\nmovements,but the creature hops around and seems utterly pleased\
 with himself,\nso you decide to focus on keeping things that way.\nSoon\
 however you grow dizzy and tired,\nyou fall to your knees on the soft\
 pine bedding.\nThe creature regards you thoughtfully, then smiles.\n'I\
 suppose you'll be wanting to go home now? This is no place for a\
 human after all.\nThank you for the dance, child of man who received\
 the Fairies' blessing.'\n", "'The mischievous grin slowly turns\
 malicious.\n'You should not enter in games you are sure to lose\
 human.'\nThe last thing you see is the creature cracking its knuckles\nbefore\
 your sides seethe with a tickling sensation so fierce,\nall your\
 other senses seem to disappear and the world goes blank.\n", "The creature\
 cocks his head.\n'You tresspass in my forest, I offer you a chance at mercy,\
 yet you refuse?'\n'Tis a wonder how long your species has\
 survived.'\nScratching his hairy chin he regards you thoughtfully and then\
 shrugs.\n'Ah well, to each their own I guess.'\nHe reaches out to you,\
 you try to scramble away but he drags you back by your ankle.\nBefore\
 you can blink,\nhis long thin fingers have latched onto your sides and\
 started tickling you furiously.\nAt first you laugh and roll\
 around.\nBut soon the sensation becomes overwhelming.\nThe last thing you\
 see through tear-filled eyes\nis the manic grin of moonlight still shining\
 down on you.\n"]
puca_conversation = ["'Well well, are you lost traveler?\n", "'Poor thing,\
 I understand your predicament.\nLuckily for you I know this maze like the\
 back of my hoof, so to speak.\nClimb on my back and I will take you out\
 of here.\nWhat do you say, will you ride me human?'\n", "The creature\
 bends its knees to lower himself to the ground.\nYou walk up to him\
 hesitantly\nand grasp on to his long silky mane before swinging your leg\
 over his back.\nThe spurs flash in the moonlight and the horse neighs in\
 dismay.\nBefore you can properly take your seat\nhe bucks you off\
 angrily and quickly gets back up.\n'You did not mention you have the\
 sharp things on human,\nI won't go near you then. Leave quickly or you\
 will regret having visited me.'\n", "You walk up to him hesitantly and\
 grasp\non to his long silky mane before swinging your leg over his\
 back.\nAs you take your seat he stands back up and you marvel\nat the feel\
 of this powerful animal.\nYou hear him neigh, almost like a snicker, before\
 he suddenly shoots off\nlike a bullet and all you can do is hold on for dear\
 life.\nYour screams get swallowed in the maze's endless depths...\n", "You\
 nod nervously,\nthen hastily make your way past the dark beast to continue on\
 the path.\n", "You swallow nervously, then bravely take a step forwards as you\
 say:\n'I will not use the spurs on you, if you will help me get out of this\
 maze.'\nHe looks at you, mist blowing out of his nostrils before he\
 replies:\n' Perhaps you should remove your boots.'\nYou think it over, but\
 something in the creature's intense gaze\nmakes you too nervous to trust it\
 completely and you shake your head.\n'No, but I can gift them to you once we\
 reach our destination?'\nHe stomps his front hoof as he contemplates your\
 offer.\nThen he bobs his head up and down saying:\n'No one will be able\
 to use the sharp things again then.\nCome human, I will take you along the\
 path.'\n", "An evil, mocking laughter comes from the animal.\n'Are you scared\
 human?\nRun along then, before the Chupa bleeds you dry...'\n"]
nokk_conversation = ["The music lures you forward, it fills your senses\
 until they feel like bursting.\nYour body relaxes, the stress and fear\
 flowing out of you\nsimilar to how the water flows over the\
 waterfall.\nWhat was there to be afraid of again? Surely you have arrived\
 in paradise.\nNear the waterfall, you see a fallen angel half submerged\
 in water.\nHe's the most beautiful man you've ever seen\nand plays the\
 violin with a devotion worthy of a lover.\n", "The man lifts his\
 gaze, acknowledging you standing\nby the edge of the water as if he was\
 aware of your presence all along.\nWhen he sees you, his violin playing\
 comes to an abrupt halt\nas his face morphs in shock and wonder.\nYou\
 hardly notice however, as the spell you were under is abruptly\
 lifted.\nYou feel as if you've been dunked in an ice bath\nand can suddenly\
 no longer appreciate the man's musical voice when he says:\n'Such a\
 magnificent creature!\nI have yet to see a coat so black as to be the envy\
 of the night sky.'\nHe turns his gaze to you and you look back\
 warily.\n'Thank you, human, for bringing this magnificent creature before\
 my eyes.\nAs a reward, I shall free you from this maze, go home child of\
 man.'\nHe waves his hand over the silvery water and\nlike a mirage the\
 world around you seems to ripple...\n", "You don't really register your\
 feet touching the water.\nAll you're aware of is the enchanting\
 music\nand a feeling of complete contentment as you move forward, deeper\
 into the lake...\n", "The water closes over the top of your head,\nyou\
 feel like a babe protectively wrapped in silk.\nSuddenly your peace\
 is disrupted by an awful screech so loud you gasp.\nYour lungs instantly\
 fill with water and panic floods you along with it.\nYou try desperately\
 to swim to the surface.\nSomehow your head finally breaks through and you\
 gasp\nlungfulls of air as you blink the water from your eyes.\nIt takes\
 you a moment to get your bearings.\nThe handsome violinist is now\
 sitting on top of a rock,\nkeeping his legs tucked in as if afraid\
 to touch the water.\nHe looks at you in anger.\n'You DARE bring filthy\
 metal into my waters?!'\nYou look into the water to see the rusted sword\
 you had picked up earlier,\nit must've floated away from you as you\
 walked into the water.\nBarely recovered from the shock, you realize\
 this is your chance to get away.\nAs quickly as your legs can tread\
 the water you make your way back to shore,\nclambering back onto the\
 land and rushing to continue on the maze's path.\n", "The water\
 closes over the top of your head,\nyou feel like a babe protectively\
 wrapped in silk.\nAbsolute bliss fills you as your world goes dark...\n"]
sphinx_conversation = ["The mouse runs off, forgotten in the face of\
 more intriguing prey.\n'Well well, a human, haven't seen one of those\
 in a long, long, looong while.\nI commend you on making it this far into\
 the maze.'\nShe looks you over as she crosses her front paws\nand flicks\
 her tail lazily in the air behind her.\n'I imagine you'll be wanting to\
 leave here yes?'\nShe doesn't bother waiting for your answer as she\
 continues.\n'so I'll make this easy for you, there are really only\
 two ways to end this.\nEither you solve my riddle, and I shall\
 point you in the right direction.\nOr, if you don't solve my riddle,\
 you get a one way ticket into my stomach.'\nShe flexes her paws\
 in anticipation.\n'Though you could try running of course, I haven't\
 enjoyed a good hunt in a while.\nWhat shall it be human? Will you\
 play?'\n", "'Very well, here's my riddle human:\nA monkey has stolen\
 a purse containing two coins,\nwhich together are worth 30\
 groats.\nGiven that one of the coins is not a 10-groat piece,\nand\
 that the only coins that exist are 1, 5, 10 and 20 groats,\ncan you\
 say how much each of the two coins is worth?\n", "'How boring, I\
 suppose I made that one too easy for you.'\nThe creature sighs in\
 exasperation and casually motions her head\nin the general direction\
 to her left.\n'Head in that direction and I reckon Anansi will\
 lead you out.'\nYou do not hesitate to do as she instructs...\n", "She\
 uncrosses her front paws,\nlowers her body\
 and flexes her muscles in preparation to pounce.\n'I'm afraid that\
 is incorrect.'\nYou barely have time to shriek before she leaps and\
 your world becomes dark...\n", "A grin spreads on her face as she\
 gets up to stand on all fours.\n'Goodie, I hope you run fast\
 human.'\nShe leaps through the air as you desperately try to get away.\n"]
anansi_conversation = ["He regards you, slowly breathing\
 in and out in an almost meditative way.\nHis sharp gaze keeps you frozen\
 in place.\n'You did well and kept your wits\
 about you.\nYou have conquered the Mythos Maze.\nCongratulations are in\
 order, as a reward I will send you home in but a moment.\nFirst though,\
 I would like to introduce you\nto the mythical creatures you encountered\
 along your way.'\n", "'I understand, it has been a trying night for\
 you.\nPlease do visit us again sometime.'\nHe waves his leg in a sweeping\
 motion, a wistful smile on his face.\n"]
killed_by_chupa = ["A set of glowing red coals stare at you from the \
 darkness.\nA low growl reverberates through the air\nas whatever they belong\
 to moves closer to you.\nSharp claws scratch the earth and the\
 moonlight reveals a heavily\nprotruding spinal ridge on a creature that\
 looks like an emaciated, hairless dog.\ndrool slowly slides down razor\
 sharp canines as the creature braces itself to pounce...\n"]
win_sequence = ["You startle awake, your head\
 groggy from the aftermath of sleep\nas you try to clumsily free yourself from\
 your tangled sheets.\nYou look around in a disoriented haze, your alarm\
 blaring\nloudly enough in the background to wake the dead.\nFor a moment\
 you think you see two glowing red eyes stare at you from the\
 shadows.\nYou shake your head and rub your eyes,\nthe glowing red coals\
 have vanished by the time you look again.\nYou must've had a bad dream\
 tonight...\n"]

affirmative = ["yes", "y", "definitely", "let's go", "bring it",
               "hell yes", "absolutely", "I might have", "yea", "ye"]
negative = ["no", "n", "no way", "hell no", "absolutely not", "never",
            "nope", "nah"]
follow_path = ["path", "follow path", "straight", "straight ahead",
               "keep going", "go into the maze", "enter maze", "go into maze",
               "head deeper into maze", "run away", "run", "forward", "move",
               "move forward", "onward", "continue", "move on", "keep moving"]
follow_spider = ["follow spider", "spider", "after spider", "side passage",
                 "hole", "move through hole", "move through hedge"]
stop_game = ["quit", "go home", "leave maze", "exit", "i'm done"]
seal_your_doom = ["help!", "investigate noise", "investigate",
                  "investigate sound", "go back", "turn back", "hide", "shout",
                  "scream", "attack", "use sword", "look behind you",
                  "turn around", "look back"]
pickup_items = ["search pocket", "search pockets", "pick up", "pick up item",
                "take", "take item", "take boots", "take sword",
                "pick up boots", "pick up sword", "investigate", "grab sword",
                "grab item", "pickup sword", "pickup item", "search skeleton",
                "search body", "search", "grab boots", "put on boots",
                "wear boots"]
avoid = ["leave", "don't help", "don't listen", "go away", "sneak past",
         "sneak"]
correct_answer = ["10 and 20", "20 and 10", "10 groats and 20 groats",
                  "20 groats and 10 groats", "10, 20", "20, 10", "10 20",
                  "20 10", "ten groats, twenty groats",
                  "twenty groats, ten groats", "ten groats twenty groats",
                  "twenty groats ten groats",
                  "ten and twenty", "twenty and ten",
                  "ten groats and twenty groats",
                  "twenty groats and ten groats",
                  "ten, twenty", "twenty, ten", "ten twenty", "twenty ten"]
contents = ["inventory", "show inventory", "what's in my inventory",
            "what's in my inventory?"]


def display_intro():
    """
    Displays the opening / introductory text of the game.
    """
    intro_done = False
    while intro_done is False:
        player_input = input("Welcome to the Mythos Maze, would you like to\
 try and traverse its perils?\n>")
        if player_input.lower().strip() in affirmative:
            player_input2 = input("Are you sure?\n>")
            if player_input2.lower().strip() in affirmative:
                print("Very well then, it's your funeral.\nLet me give you\
 a piece of advice:\nThe creatures you will encounter can be quite daunting\
 to face.\nYou may not wish to face them empty handed...\nGood luck\
 mortal.\n>")
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
                not in avoid:
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
            print("The delicious milk revitalizes and refreshes you.")
            inventory.remove("milk")
            player_input3 = input("What will you do?\n>")
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
            player_input3 = input("what will you do?\n>")
        elif LOCATION is monster_locations[3] and \
                player_input3.lower().strip() not in avoid:
            dragon_encounter()
            if EXIT_GAME is True:
                break
            else:
                location_arrival()
                break
        elif LOCATION is monster_locations[4] and \
                player_input3.lower().strip() not in avoid and\
                player_input3.lower().strip() not in negative:
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
                player_input3.lower().strip() not in avoid:
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
                player_input3.lower().strip() not in avoid:
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
            print("Though you want to leave, your fear and uncertainty keep\
 you rooted to the spot.")
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
            print(killed_by_chupa[0])
            game_over()
            if EXIT_GAME is True:
                break
            else:
                location_arrival()
                break
        elif player_input3.lower().strip() in contents:
            print(f"Your inventory currently contains: {', '.join(inventory)}")
            player_input3 = input("What will you do?\n>")
        else:
            print("I'm afraid I don't quite catch your meaning")
            player_input3 = input("What will you do?\n>")
    else:
        print("Returning to reality...")


def kitsune_encounter():
    """
    Handles interaction between player and
    the Kitsune (when encountered)
    """
    global LOCATION
    print("'I lost my marble, have you seen it?'")
    player_talk = input("What will you say?\n>")
    if player_talk.lower().strip() in negative and "hoshi no tama" in \
            inventory:
        print(kitsune_conversation[0])
        player_talk2 = input("Will you hand over the hoshi no tama?\n>")
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
        player_talk2 = input("Will you hand over the hoshi no tama?\n>")
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
        print(f"The contents of your inventory is currently:\
            {', '.join(inventory)}")
        player_talk2 = input("What will you offer?\n>")
        while player_talk2.lower().strip() != "milk":
            if player_talk2.lower().strip() == "rusted sword":
                print(naga_conversation[3])
                player_talk2 = input("What will you offer?\n>")
            elif player_talk2.lower().strip() == "nature's blessing":
                print("You cannot gift someone else's blessing of you\
 onto another person.")
                player_talk2 = input("What will you offer?\n>")
            else:
                print("'I have no ussse for sssuch a thing human'")
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
    print(f"'{player_talk}?, you smell.. human. Are you human?'\n>")
    player_talk2 = input("What will you say?\n>")
    if player_talk2.lower().strip() in negative and \
            "a large bloodred ruby" not in inventory:
        print(dragon_conversation[1])
        game_over()
    elif player_talk2.lower().strip() in negative and \
            "a large bloodred ruby" in inventory:
        print(dragon_conversation[2])
        player_talk3 = input("Will you hand over the large bloodred ruby?\n>")
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
        player_talk3 = input("Will you hand over the large bloodred ruby?\n>")
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
            player_talk3 = input("Will you try to convince the Puca to\
 let you ride him? Or will you move on?\n>")
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
        print("CONGRATULATIONS! YOU BEAT THE GAME VIA THE SECRET ROUTE")
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
    print(f"'They are the:\n{', '.join(monsters_met)}\nand finally, myself. I\
 am known as Anansi.\nThe creature that was hunting you is known as a\
 Chupacabra.'\n")
    player_talk = input("'Would you like to know more about any of these\
 beings?\nOr perhaps you do not know what a mythical\
 creature is?\nWould you like to expand your knowledge?\nA simple\
 yes or no will suffice.'\n>")
    while player_talk.lower().strip() not in stop_game and \
            player_talk.lower().strip() not in negative:
        player_talk = input("Which being would you like to know more\
 about?\n>")
        if player_talk.lower().strip() == "mythical creature" or \
                player_talk.lower().strip() == "mythical creatures":
            print(Monster.definition)
            player_talk = input("'Would you like to know more?'\n>")
        elif player_talk.lower().strip() == "kitsune" or \
                player_talk.lower().strip() == "the kitsune":
            print(kitsune.description())
            player_talk = input("'Would you like to know more?'\n>")
        elif player_talk.lower().strip() == "naga" or \
                player_talk.lower().strip() == "the naga":
            print(naga.description())
            player_talk = input("'Would you like to know more?'\n>")
        elif player_talk.lower().strip() == "dragon" or \
                player_talk.lower().strip() == "the dragon":
            print(dragon.description())
            player_talk = input("'Would you like to know more?'\n>")
        elif player_talk.lower().strip() == "surale" or \
                player_talk.lower().strip() == "the surale" or\
                player_talk.lower().strip() == "Şüräle" or \
                player_talk.lower().strip() == "the Şüräle":
            print(surale.description())
            player_talk = input("'Would you like to know more?'\n>")
        elif player_talk.lower().strip() == "puca" or \
                player_talk.lower().strip() == "the puca" or \
                player_talk.lower().strip() == "púca" or \
                player_talk.lower().strip() == "the púca":
            print(puca.description())
            player_talk = input("'Would you like to know more?'\n>")
        elif player_talk.lower().strip() == "nokk" or \
                player_talk.lower().strip() == "the nokk" or \
                player_talk.lower().strip() == "nøkk" or \
                player_talk.lower().strip() == "the nøkk":
            print(nokk.description())
            player_talk = input("'Would you like to know more?'\n>")
        elif player_talk.lower().strip() == "sphinx" or \
                player_talk.lower().strip() == "the sphinx":
            print(sphinx.description())
            player_talk = input("'Would you like to know more?'\n>")
        elif player_talk.lower().strip() == "anansi" or \
                player_talk.lower().strip() == "you":
            print(anansi.description())
            player_talk = input("'Would you like to know more?'\n>")
        elif player_talk.lower().strip() == "chupacabra" or \
                player_talk.lower().strip() == "the chupacabra":
            print(chupacabra.description())
            player_talk = input("Would you like to know more?'\n>")
        else:
            print(f"'I'm sorry, I can only tell you about the:\n\
 {', '.join(monsters_met)}, myself\nor what mythical \
 creatures are in general.'")
    else:
        print(anansi_conversation[1])
        time.sleep(6)
        print(win_sequence[0])
        time.sleep(6)
        print("CONGRATULATIONS! YOU BEAT THE GAME")


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
            print(f"You have added {LOCATION.item} to your inventory\n")
        elif LOCATION.item in inventory:
            print(f"{LOCATION.item} is already in your inventory\n")
        else:
            print("There's nothing here that you can take with you\n")
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
        print("Although the path is ahead,\nyou cannot see\
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
    global EXIT_GAME
    print("you have died\n")
    player_input4 = input("would you like to try again,\
 start over or stop playing?\n")
    if player_input4.lower().strip() == "start over":
        LOCATION = entrance
        inventory.clear()
    elif player_input4.lower().strip() == "stop playing":
        print("We're sorry to see you go...")
        EXIT_GAME = True


def main():
    """
    Fires up all active functions, in correct order, that make the game run
    """
    display_intro()
    location_arrival()


main()
