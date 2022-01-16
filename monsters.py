"""
Monster class, details about
the monsters that can be encountered
and where each monster can be found
"""

from colorama import Fore
from colorama import Style
from locations import kitsune_lair, dragon_lair, naga_lair, surale_lair, \
    puca_lair, nokk_lair, sphinx_lair, passage_three, leave_maze


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
dragon_conversation = [f"{Fore.LIGHTCYAN_EX}'Who dares enter my\
 lair?'{Style.RESET_ALL}\n", f"{Fore.LIGHTMAGENTA_EX}The beast makes a sound\
 reminiscent of a chuckle,\nbut it's so powerful it makes the ground\
 shake.\n{Fore.LIGHTCYAN_EX}'You dare lie to me human?.\nNo matter, I suppose\
 you'll do as a snack.'{Style.RESET_ALL}\n", f"{Fore.LIGHTCYAN_EX}'Do not\
 lie to me human! Were it not for the precious stone you carry\nI would've\
 eaten you for your insolence.\nGive it to me and I might find myself in a\
 more benevolent mood.'{Style.RESET_ALL}\n", f"{Fore.LIGHTCYAN_EX}'A wise\
 decision, such a precious item belongs in a Dragon's hoard.\nI shall let\
 you pass, this time.'{Style.RESET_ALL}\n", f"{Fore.LIGHTCYAN_EX}'Hmm, humans\
 make tiny snacks.\nThough I would've eaten you already regardless,\nwere\
 it not for the precious cargo you carry.\nGive me the ruby, child of\
 man.'{Style.RESET_ALL}\n", f"{Fore.LIGHTCYAN_EX}'You are either very brave,\
 or very foolish.\nWhichever it may be, this is the end of the line for you\
 child of man'{Style.RESET_ALL}\n"]
surale_conversation = [f"{Fore.LIGHTMAGENTA_EX}The creature seems to think a\
 moment and then it snaps its lengthy fingers.\n{Fore.LIGHTCYAN_EX}'You shall\
 either dance with me or we can hold a tickling competition.\
 '\n{Fore.LIGHTMAGENTA_EX}It leaned further forward, his nose almost touching\
 yours.\n{Fore.LIGHTCYAN_EX}'Which shall it be human?'{Style.RESET_ALL}\n", f"\
 {Fore.LIGHTMAGENTA_EX}The creature claps its\
 hands.\n{Fore.LIGHTCYAN_EX}'Delightful!'\n{Fore.LIGHTMAGENTA_EX}before\
 you have the chance to do anything\nhe has already lifted you up by your arms\
 and placed you on your feet.\nHe regards your bare feet in puzzlement for a\
 moment,\nbut then shrugs and drags you into a spinning motion with one strong\
 jerk.\nYou could swear you hear faint music from somewhere accompanying your\
 awkward\nmovements,but the creature hops around and seems utterly pleased\
 with himself,\nso you decide to focus on keeping things that way.\nSoon\
 however you grow dizzy and tired.\nYou fall to your knees on the soft\
 pine bedding.\nThe creature regards you thoughtfully, then\
 smiles.\n{Fore.LIGHTCYAN_EX}'I suppose you'll be wanting to go home now?\
 This is no place for a human after all.\nThank you for the dance, child of\
 man who received the Fairies' blessing.'{Style.RESET_ALL}\n", f"\
 {Fore.LIGHTMAGENTA_EX}The mischievous grin slowly turns\
 malicious.\n{Fore.LIGHTCYAN_EX}'You should not enter in games you are sure to\
 lose human.'\n{Fore.LIGHTMAGENTA_EX}The last thing you see is the creature\
 cracking its knuckles\nbefore your sides burn with a tickling sensation so\
 fierce,\nall your other senses seem to disappear and the world goes\
 blank.{Style.RESET_ALL}\n", f"{Fore.LIGHTMAGENTA_EX}The creature\
 cocks his head.\n{Fore.LIGHTCYAN_EX}'You tresspass in my forest, I offer you\
 a chance at mercy, yet you refuse?'\n'Tis a wonder how long your species has\
 survived.'\n{Fore.LIGHTMAGENTA_EX}Scratching his hairy chin he regards you\
 thoughtfully and then shrugs.\n{Fore.LIGHTCYAN_EX}'Ah well, to each their own\
 I guess.'\n{Fore.LIGHTMAGENTA_EX}He reaches out to you,\
 you try to scramble away but he drags you back by your ankle.\nBefore\
 you can blink,\nhis long thin fingers have latched onto your sides and\
 started tickling you furiously.\nAt first you laugh and roll\
 around.\nBut soon the sensation becomes overwhelming.\nThe last thing you\
 see through tear-filled eyes\nis the manic grin of moonlight still shining\
 down on you.{Style.RESET_ALL}\n"]
puca_conversation = [f"{Fore.LIGHTCYAN_EX}'Well well, are you lost\
 traveler?{Style.RESET_ALL}\n", f"{Fore.LIGHTCYAN_EX}'Poor thing,\
 I understand your predicament.\nLuckily for you I know this maze like the\
 back of my hoof, so to speak.\nClimb on my back and I will take you out\
 of here.\nWhat do you say, will you ride me human?\
 '{Style.RESET_ALL}\n", f"{Fore.LIGHTMAGENTA_EX}The creature\
 bends its knees to lower himself to the ground.\nYou walk up to him\
 hesitantly\nand grasp on to his long silky mane before swinging your leg\
 over his back.\nThe spurs flash in the moonlight and the horse neighs in\
 dismay.\nBefore you can properly take your seat\nhe bucks you off\
 angrily and quickly gets back up.\n{Fore.LIGHTCYAN_EX}'You did not mention\
 you have the sharp things on human,\nI won't go near you then. Leave quickly\
 or you will regret having visited me.'{Style.RESET_ALL}\n", f"\
 {Fore.LIGHTMAGENTA_EX}You walk up to him hesitantly and\
 grasp\non to his long silky mane before swinging your leg over his\
 back.\nAs you take your seat he stands back up and you marvel\nat the feel\
 of this powerful animal.\nYou hear him neigh, almost like a snicker, before\
 he suddenly shoots off\nlike a bullet and all you can do is hold on for dear\
 life.\nYour screams get swallowed in the maze's endless\
 depths...{Style.RESET_ALL}\n", f"{Fore.LIGHTMAGENTA_EX}You\
 nod nervously,\nthen hastily make your way past the dark beast to continue\
 on the path.{Style.RESET_ALL}\n", f"{Fore.LIGHTMAGENTA_EX}You swallow\
 nervously, then bravely take a step forwards as you say\
 :\n{Fore.LIGHTWHITE_EX}'I will not use the spurs on you, if you will help me\
 get out of this maze.'\n{Fore.LIGHTMAGENTA_EX}He looks at you, mist blowing\
 out of his nostrils before he replies:\n{Fore.LIGHTCYAN_EX}'Perhaps you\
 should remove your boots.'\n{Fore.LIGHTMAGENTA_EX}You think it over, but\
 something in the creature's intense gaze\nmakes you too nervous to trust it\
 completely and you shake your head.\n{Fore.LIGHTWHITE_EX}'No, but I can gift\
 them to you once we reach our destination?'\n{Fore.LIGHTMAGENTA_EX}He stomps\
 his front hoof as he contemplates your offer.\nThen he bobs his head up and\
 down saying:\n{Fore.LIGHTCYAN_EX}'No one will be able\
 to use the sharp things again then.\nCome human, I will take you along the\
 path.'{Style.RESET_ALL}\n", f"{Fore.LIGHTMAGENTA_EX}An evil, mocking laughter\
 comes from the animal.\n{Fore.LIGHTCYAN_EX}'Are you scared\
 human?\nRun along then, before the Chupa bleeds you\
 dry...'{Style.RESET_ALL}\n"]
nokk_conversation = [f"{Fore.LIGHTMAGENTA_EX}The music lures you forward,\
 it fills your senses.\nYour body relaxes,\
 the stress and fear flowing out of you\nsimilar to how the water flows over\
 the waterfall.\nSurely you have arrived\
 in paradise.\nNear the waterfall, you see a fallen angel half submerged\
 in water.\nHe's the most beautiful man you've ever seen\nand plays the\
 violin with a devotion worthy of a lover.{Style.RESET_ALL}\n", f"\
 {Fore.LIGHTMAGENTA_EX}The man lifts his gaze, acknowledging you standing\nby\
 the edge of the water as if he was aware of your presence all along.\nWhen\
 he sees you, his violin playing comes to an abrupt halt\nas his face morphs\
 in shock and wonder.\nYou hardly notice however, as the spell you were under\
 is abruptly lifted.\nYou feel as if you've been dunked in an ice bath\nand\
 can suddenly no longer appreciate the man's musical voice when he\
 says:\n{Fore.LIGHTCYAN_EX}'Such a magnificent creature!\nI have yet to see a\
 coat so black as to be the envy of the night sky.'\n{Fore.LIGHTMAGENTA_EX}He\
 turns his gaze to you and you look back warily.\n{Fore.LIGHTCYAN_EX}'Thank\
 you, human, for bringing this magnificent creature before\
 my eyes.\nAs a reward, I shall free you from this maze, go home child of\
 man.'\n{Fore.LIGHTMAGENTA_EX}He waves his hand over the silvery water\
 and\nlike a mirage the world around you seems to ripple\
 ...{Style.RESET_ALL}\n", f"{Fore.LIGHTMAGENTA_EX}You don't really register\
 your feet touching the water.\nAll you're aware of is the enchanting\
 music\nand a feeling of complete contentment as you move forward, deeper\
 into the lake...{Style.RESET_ALL}\n", f"{Fore.LIGHTMAGENTA_EX}The water\
 closes over the top of your head,\nyou feel like a babe protectively wrapped\
 in silk.\nSuddenly your peace is disrupted by an awful screech so loud you\
 gasp.\nYour lungs instantly fill with water and panic floods you along with\
 it.\nYou try desperately to swim to the surface.\nSomehow your head finally\
 breaks through and you gasp\nlungfulls of air as you blink the water from\
 your eyes.\nIt takes you a moment to get your bearings.\nThe handsome\
 violinist is now sitting on top of a rock,\nkeeping his legs tucked in as if\
 afraid to touch the water.\nHe looks at you in anger.\n{Fore.LIGHTCYAN_EX}'\
 You DARE bring filthy metal into my waters?!'\n{Fore.LIGHTMAGENTA_EX}You\
 look into the water to see the rusted sword you had picked up earlier,\nit\
 must've floated away from you as you walked into the water.\nBarely\
 recovered from the shock, you realize this is your chance to get away.\nAs\
 quickly as your legs can tread the water you make your way back to\
 shore,\nclambering back onto the land and rushing to continue on the maze's\
 path.{Style.RESET_ALL}\n", f"{Fore.LIGHTMAGENTA_EX}The water\
 closes over the top of your head,\nyou feel like a babe protectively\
 wrapped in silk.\nAbsolute bliss fills you as your world goes\
 dark...{Style.RESET_ALL}\n"]
sphinx_conversation = [f"{Fore.LIGHTMAGENTA_EX}The mouse runs off,\
 forgotten in the face of more intriguing prey.\n{Fore.LIGHTCYAN_EX}'Well\
 well, a human, haven't seen one of those in a long, long, looong while.\nI\
 commend you on making it this far into the maze.'\n{Fore.LIGHTMAGENTA_EX}She\
 looks you over as she crosses her front paws\nand flicks her tail lazily in\
 the air behind her.\n{Fore.LIGHTCYAN_EX}'I imagine you'll be wanting to\
 leave here yes?'\n{Fore.LIGHTMAGENTA_EX}She doesn't bother waiting for your\
 answer as she continues.\n{Fore.LIGHTCYAN_EX}'so I'll make this easy for you,\
 there are really only two ways to end this.\nEither you solve my riddle, and\
 I shall point you in the right direction.\nOr, if you don't solve my riddle,\
 you get a one way ticket into my stomach.'\n{Fore.LIGHTMAGENTA_EX}She flexes\
 her paws in anticipation.\n{Fore.LIGHTCYAN_EX}'Though you could try running\
 of course, I haven't enjoyed a good hunt in a while.\nWhat shall it be human?\
 Will you play?'{Style.RESET_ALL}\n", f"{Fore.LIGHTCYAN_EX}'Very well, here's\
 my riddle human:\nA monkey has stolen a purse containing two coins,\nwhich\
 together are worth 30 groats.\nGiven that one of the coins is not a 10-groat\
 piece,\nand that the only coins that exist are 1, 5, 10 and 20 groats,\ncan\
 you say how much each of the two coins is worth?'{Style.RESET_ALL}\n", f"\
 {Fore.LIGHTCYAN_EX}'How boring, I suppose I made that one too easy for you.\
 '\n{Fore.LIGHTMAGENTA_EX}The creature sighs in exasperation and casually\
 motions her head\nin the general direction to her left.\n{Fore.LIGHTCYAN_EX}'\
 Head in that direction and I reckon Anansi will lead you out.\
 '\n{Fore.LIGHTMAGENTA_EX}You do not hesitate to do as she instructs...\
 {Style.RESET_ALL}\n", f"{Fore.LIGHTMAGENTA_EX}She uncrosses her front\
 paws,\nlowers her body and flexes her muscles in preparation to pounce\
 .\n{Fore.LIGHTCYAN_EX}'I'm afraid that is incorrect.\
 '\n{Fore.LIGHTMAGENTA_EX}You barely have time to shriek before she leaps and\
 your world becomes dark...{Style.RESET_ALL}\n", f"{Fore.LIGHTMAGENTA_EX}A grin\
 spreads on her face as she gets up to stand on all\
 fours.\n{Fore.LIGHTCYAN_EX}'Goodie, I hope you run fast human.\
 '\n{Fore.LIGHTMAGENTA_EX}She leaps through the air as you desperately try to\
 get away.{Style.RESET_ALL}\n"]
anansi_conversation = [f"{Fore.LIGHTMAGENTA_EX}He regards you, slowly breathing\
 in and out in an almost meditative way.\nHis sharp gaze keeps you frozen\
 in place.\n{Fore.LIGHTCYAN_EX}'You did well and kept your wits\
 about you.\nYou have conquered the Mythos Maze.\nCongratulations are in\
 order, as a reward I will send you home in but a moment.\nFirst though,\
 I would like to introduce you\nto the mythical creatures you encountered\
 along your way.'{Style.RESET_ALL}\n", f"{Fore.LIGHTCYAN_EX}'I understand,\
 it has been a trying night for you.\nPlease do visit us again sometime.\
 '\n{Fore.LIGHTMAGENTA_EX}He waves his hairy leg in a sweeping\
 motion, a wistful smile on his face.{Style.RESET_ALL}\n"]
killed_by_foolishness = [f"{Fore.LIGHTMAGENTA_EX}A set of glowing\
 {Fore.LIGHTRED_EX}red {Fore.LIGHTMAGENTA_EX}coals stare at you from the\
 darkness.\nA low growl reverberates through the air\nas whatever they\
 belong to moves closer to you.\nSharp claws\
 scratch the earth and the moonlight reveals a heavily\nprotruding spinal\
 ridge on a creature that looks like an emaciated, hairless dog.\ndrool\
 slowly slides down razor sharp canines as the creature braces itself to\
 pounce...{Style.RESET_ALL}\n", f"{Fore.LIGHTMAGENTA_EX}You lift the\
 sword in shaking hands.\nWith a battlecry you charge, hoping you'll\
 forget your fear.\nSeeing the creature up close makes you waver for\
 a moment.\nPanic clawing its way up your body like growing\
 vines.\nYet you refuse to go down without a fight.\nWith a single\
 hit, the timeworn sword snaps in two and you know you're in deep\
 trouble...{Style.RESET_ALL}\n", f"{Fore.LIGHTMAGENTA_EX}You ball\
 your hands into fists.\nWhatever else\
 may be said of you, you will not go down without a fight\
 ...{Style.RESET_ALL}\n"]
win_sequence = [f"{Fore.LIGHTMAGENTA_EX}You startle awake, your head\
 groggy from the aftermath of sleep\nas you try to clumsily free yourself from\
 your tangled sheets.\nYou look around in a disoriented haze, your alarm\
 blaring\nloudly enough in the background to wake the dead.\nFor a moment\
 you think you see two glowing {Fore.LIGHTRED_EX}red\
 {Fore.LIGHTMAGENTA_EX}eyes stare at you from the shadows.\nYou shake your\
 head and rub your eyes,\nthe glowing red coals\
 have vanished by the time you look again.\nYou must've had a bad dream\
 tonight...{Style.RESET_ALL}\n"]
