
# Mythos Maze
[Mythos Maze](https://mythos-maze.herokuapp.com/) is a Python terminal adventure game, which runs on the Code Institute mock terminal on Heroku.

Users can go on an adventure in the Mythos Maze filled with Mythological creatures from different cultures all over the world. Depending on their choices they will either find their way out, or become a victim of one of the many creatures the maze houses.  
<br>
![Sphinx, the mythological creature variety](images/sphinx.jpg)  
*The Sphinx is one of the creatures you might encounter inside the Mythos Maze*  
  
## UX Design  
### User stories
* As a user I feel an adventure game should be as intuitive as possible:  
    * The game's introduction asks the user whether they wish to play or not. If they answer yes they will be given a hint on how to conquer the Maze.
    * Throughout the Maze the user will be asked questions: 'What will you do?', 'What will you say?' etc. Their input can be freely given, the game will react differently depending on their feedback. Though this is riskier, I hope it will make the game more immersive.  
    * The game contains a lot of descriptive text, both to bring life to the maze and to inform the user of everything they can potentially interact with.
    * The user can request to see the contents of their inventory, or quit the game, at any time. They need to discover this themselves however. Like the player character, they are 'dropped' into an unfamiliar world and have to figure things out as they go.
    * If the player reaches the official end of the game (there is also a way to leave the maze earlier, if a user manages to find it), they can ask for more information on the creatures they've encountered.
    * Should the player die, they will be asked whether they wish to 'try again' (from the part where they died), 'start over' (from the beginning) or 'stop playing'.

### Site goals
* Create a fun adventure which is easy to navigate.
* Spark some interest in the many mythological creatures that exist in (ancient) folklore.
* Teach the user more about the creatures they've encountered when they reach the end of the game.  

### Flowchart
![Origina Flowchart](images/flowchart.png)  

* Differences to original design  
   * In the original design, there is an option to offer the milk to the Chupacabra in an attempt to placate it.  
     However this meant coming face to face with him and as the milk wasn't going to work on him this would mean the player couldn't realistically get away from him at that point. This part of the story was removed.  
     Instead, the user can choose to drink the milk, which would still create the desired effect of removing the milk from the user's inventory.  
     *Which is a bad idea, but the player needs to find this out for themselves*  
   * In the original design, the bloodstained boots and rusted sword are in the same area. As there was only one area that contained two items and all other areas only contained a maximum of one item, it seemed more frugal to place the rusted sword elsewhere and give the location class only one item attribute.  

## Features  
### Existing features
* Game introduction:  
  The game first asks the user whether they wish to play or not, from the very beginning the responses a user gets depend completely on their choice of input.  
  Aside from yes or no, uncertain answers will receive a different response as well.  
![Image of the game intro](images/maze_start.jpg)  

* Obtain items:  
  The user can obtain different items which will be necessary to win the game.  
  These can be either found / obtained by the user or given to them by benevolent creatures (though the user must get on their good side first).  
  The user can check what's inside their inventory at any time during the game, the correct input in response to the "What will you do?" question will reveal the current contents.  
![Image of the user obtaining an item](images/obtain_item.jpg)

* Game over:  
  To prevent the game simply ending when the user dies, the user is given the option to try again, start over or stop playing.  
![Image of achieving game over in game](images/game_over.jpg)  

* Unknown input:  
  Unfortunately it was impossible to account for all possible inputs a user might give the game. In case something is entered which has no known response, the following output will be returned, and the game will once again ask the user what they want to do.  
![Image of the computer not understanding input](images/unknown_input.jpg)  

* Different colours:  
  Since the game contains a lot of story / text, different colours have been added to make it easier for the user to keep an overview. Narration is purple, spoken text is cyan, items are yellow etc.  

* Game won:  
  When the user wins the game, they will be informed which creatures they encountered along their route (different routes will lead to different outcomes here). The user is then asked if they would like to know more about any of these creatures, should they choose yes they can specify which creature they would like to learn more about. After the information is given they will be asked again if they would like to know more and, if yes, about which one etc.  
  All informative text is kept short and to the point, to keep the game light and fun rather than turn it into an encyclopedia at the end. When the user inputs that they don't wish to know more, the game will end with a short ending sequence and the user will be told they won the game.  

### Potential future features  
* The game can be expanded upon endlessly by offering more varied responses to different kinds of user input. Gaining feedback from many users would help a game like this evolve and become easier and more fun to play over time.  
* Aside from that more creatures could be added, more paths / directions could be added etc.  
* A help or hint command could be added, in case the game is too hard to beat for the user.

## Technologies used  
* Python3
* [GitHub](https://www.github.com)
* [Gitpod](https://www.gitpod.io)
* [Heroku](https://www.heroku.com)
* [Lucidchart](https://www.lucidchart.com)  

## Testing  
I have manually tested this project by doing the following:  
* Passed the code through a [Pep8](http://pep8online.com/) linter and confirmed there are no problems.
* Played through the game many times to rout out errors or bugs.  
* Tested in my local terminal and the Code Institute Heroku terminal.  

### User testing:
The game's introduction asks the user whether they wish to play or not. If they answer yes they will be given a hint on how to conquer the Maze.  
* When asked if they want to play:
  * Choosing 'no' will give the user the output that they made a wise decision and to come back anytime.
  * Choosing 'yes' will give the user the output 'are you sure?'
  * Choosing anything other than yes or no will give the user the output that they're lacking in confidence.  
  <br>
* When asked if the user is sure they want to play:  
  * Choosing 'yes' will give the user a hint on how to win and start the game.
  * Choosing anything other than yes will give the user the output that they are indecisive.  
  The cycle will keep repeating until the user chooses yes (or a variant thereof) twice.
<br>

Throughout the Maze the user will be asked questions: 'What will you do?', 'What will you say?' etc. Their input can be freely given, the game will react differently depending on their feedback. Though this is riskier, I hope it will make the game more immersive.  
* Different inputs have been tested and verified, "take item", "follow spider", "forward", "continue", "hide", "attack" etc. etc. any command that is not known will result in the user gaining feedback that the computer doesn't understand, after which they will be asked the same question again. This was tested by playing through the game, choosing to attack something at random moments, trying to pick up things at random locations, giving strange answers to questions etc.
  * When items are picked up, a message is shown that the item was added to the user's inventory.
  * When the user dies, a message is shown that they have died. After which they are asked if they want to try again, start over or stop playing.  
<br>

The game contains a lot of descriptive text, both to bring life to the maze and to inform the user of everything they can potentially interact with.
* Playing through the game requires a lot of attentive reading, each phrase might contain important information about potential items the user can pick up or a different direction the user can take. Playing through the game many times should have taken care of text errors and certain sections were shortened to spare the user from having to read too much.  
<br>

The user can request to see the contents of their inventory, or quit the game, at any time. They need to discover this themselves however. Like the player character, they are 'dropped' into an unfamiliar world and have to figure things out as they go.
* The inventory function works properly when typing in words such as "inventory", "contents", "show inventory", "what's in my inventory" etc.
  Whether the user would intuitively find out that this function exists is to be seen, either way the function is not vital to winning the game.  
<br>

If the player reaches the official end of the game (there is also a way to leave the maze earlier, if a user manages to find it), they can ask for more information on the creatures they've encountered.  
* This function was tested by running through different routes of the game. Each route informs the user of which creatures they encountered and they are asked if they want to know more about them as expected.  
<br>

Should the player die, they will be asked whether they wish to 'try again' (from the part where they died), 'start over' (from the beginning) or 'stop playing'.  
* This function was tested multiple times in multiple locations, it works as expected every time and any where. Though try again is not always the best option for a user as you might redo a scene for which you require a specific item, which means the user will simply die again. On the next run it is best to choose start over in that scenario as turning back will also result in getting killed by the creature which is hunting the user through the maze.  

### Bugs
I ran into many 'bugs' or errors while playing through the game and had to tweak the code regularly.  
Some of the more prominent bugs were: 
* Solved bugs 
  * Get an AttributError when trying to move towards a new area that's not available:  
    This was fixed by adding the function: Validate Location.  
  * While loop would not allow the user to quit game after having died:  
    This was solved by adding Break in appropriate places.  
  * Dragon would kill the user even if they had the required item in their inventory:  
    This turned out to be a case of using the wrong variable, player_talk had to be player_talk2.  
  * The Nøkk would still kill the user after they had managed to escape:  
    This required reorganization of the if/else statement within the nokk encounter function.  
  * The user can quit the game at any time, however if the user decided to 'start over' after having died, they were forced to input the quit command multiple times before the game would actually stop:  
  This turned out to be due to calling the location_arrival function inside both the monster encounter function and outside of it, thus causing an unintended cycle. Removing the calling of this function from the monster encounter functions has fixed the issue.  
<br>

* Unsolved bugs
  * To my knowledge, no unsolved bugs remain in the game.

## Deployment
This project was deployed using Code Institute's mock terminal for Heroku.  
* Steps for deployment:
   * Sign into Heroku
   * Choose New.
   * Choose Create new app.
   * Type in a name for your new app.
   * Select your region from the dropdown menu.
   * Choose Create App.
   * In the settings tab choose config vars.
   * Add the key: PORT with value: 8000.
   * Add buildpack Python followed by buildpack NodeJS.
   * In the deploy tab, select GitHub as the deployment method and connect your GitHub profile.
   * Search for the repository that you wish to deploy to Heroku and click "connect".
   * Choose to automatically deploy and update your app.
   * Click on Deploy

The deployed version can be found here: [Mythos Maze](https://mythos-maze.herokuapp.com/)  

## Credits
[Code Institute](https://www.codeinstitute.net) for the deployment terminal  
The image used in the ReadMe was taken from [Pexels](https://www.pexels.com)

Useful pages were:  
[How to create a text based adventure game](https://www.derekshidler.com/how-to-create-a-text-based-adventure-and-quiz-game-in-python/)  
[Youtube](https://www.youtube.com/watch?v=xWzUHRIgYCc)  
[StackOverflow on hassatr](https://stackoverflow.com/questions/903130/hasattr-vs-try-except-block-to-deal-with-non-existent-attributes)  
[StackOverflow on emptying lists](https://stackoverflow.com/questions/1400608/how-to-empty-a-list)  
[How to remove brackets when printing a list](https://www.delftstack.com/howto/python/list-without-brackets-python/)  

* Inspiration for the choice of what kind of project to make was given to me by the lovely Code Institute community on [Slack](https//:www.slack.com)
