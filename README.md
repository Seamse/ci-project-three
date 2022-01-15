
# Mythos Maze
[Mythos Maze](https://mythos-maze.herokuapp.com/) is a Python terminal adventure game, which runs on the Code Institute mock terminal on Heroku.

Users can go on an adventure in the Mythos Maze filled with Mythological creatures from different cultures all over the world.  
Depending on their choices they will either find their way out, or become a victim of one of the many creatures the maze houses.  
<br>
![Sphinx, the mythological creature variety](images/sphinx.jpg)  
*The Sphinx is one of the creatures you might encounter inside the Mythos Maze*  
  
## UX Design  
### User stories
* As a user I feel an adventure game should be as intuitive as possible:  
    * The game's introduction asks the user whether they wish to play or not. If they answer yes they will be given a hint on how to conquer the Maze.
    * Throughout the Maze the user will be asked questions: 'What will you do?', 'What will you say?' etc. Their input can be freely given, the game  
      will react differently depending on their feedback. Though this is riskier, I hope it will make the game more immersive.  
    * The game contains a lot of descriptive text, both to bring life to the maze and to inform the user of everything they can potentially interact with.
    * The user can request to see the contents of their inventory, or quit the game, at any time. They need to discover this themselves however.  
      Like the player character, they are 'dropped' into an unfamiliar world and have to figure things out as they go.
    * If the player reaches the official end of the game (there is also a way to leave the maze earlier, if a user manages to find it),  
      they can ask for more information on the creatures they've encountered.
    * Should the player die, they will be asked whether they wish to 'try again' (from the part where they died), 'start over' (from the beginning) or 'stop playing'.

### Site goals
* Create a fun adventure which is easy to navigate.
* Spark some interest in the many mythological creatures that exist in (ancient) folklore.
* Teach the user more about the creatures they've encountered when they reach the end of the game.  

### Flowchart
![Origina Flowchart](images/flowchart.png)  

* Differences to original design  
   * In the original design, there is an option to offer the milk to the Chupacabra in an attempt to placate it.  
     However this meant coming face to face with him and as the milk wasn't going to work on him this would mean the player couldn't  
     realistically get away from him at that point. This part of the story was removed.  
     Instead, the user can choose to drink the milk, which would still create the desired effect of removing the milk from the user's inventory.  
     *Which is a bad idea, but the player needs to find this out for themselves*  
   * In the original design, the bloodstained boots and rusted sword are in the same area. As there was only one area that contained two items  
     and all other areas only contained a maximum of one item, it seemed more frugal to place the rusted sword elsewhere and give the location  
     class only one item attribute.
