Internship Python project\
\
Create a Python script with at least 4 functions.\
Must contain:\
  input menu\
  output\
  logging\
  error handling\
  exit and return codes\
Must use 2 of the following:\
  Functions\
  if/else statements\
  case statements



Project requirements:

Must perform the following actions:
Take user input via input menu
Output
Logging
Error handling

Must contain:
Functions
Boolean conditions
List(s)
Dictionaries
Modules
Documentation (code comments and on confluence.)

Software requirements:
VSCode (other text editors could be used, but VSCode made it simpler to debug my code)
Python 3
Modules (not including my own):
logging
random
numpy
time

Goals:

Accept user input to provide movement through the game world and interact with it.
Generate output to the user based on interactions with the game.
Require decision making from the user to determine outcomes in the game.
Save game state to file so user can stop the game and pick up where they left off (was unable to implement this).

Code Documentation:

main.py:
Effectively starts the game.
Prints 300 newlines to clear screen, then calls GameMenu.new_char function from game module.
Once this is complete, GameMenu.main_menu is called from game module.

world.py
Defines the world the player moves around in.  Contains classes for each tile type
defining the behaviors and attributes of each, including flavor text and menu/decision loops.
Generates a 2D array or matrix which is referenced during player movement within the world.
Assigns values to each index of the array and assigns it as a key in a dictionary to reference the associated class in the module.
The array is built using numpy.array because it allows for some helpful functions later on.

game.py
Player controls live here.
Contains GameMenu.new_char function (for naming character), GameMenu.main_menu function (simply prints out a few stats at start), 
and Movement.where_to function which facilitates player movement through the world and prevents leaving the map.

npc.py
Currently only holds one class: BarTender, and one function: choice.
Facilitates user interaction with the tavern tile.

player.py
Contains the User class.  Three functions therein provide a way to update the player's
location during movement, player name, and one state variable set by interaction with the game.

helper.py
Currently only holds one class and function: utilities.slowPrint.
the function within takes the text the game would print to the user and outputs it 
a character at a time as though it were being typed.  Just provides a more interesting experience.

Logging is facilitated via the logging module.  At various stages within game.py, 
if the user attempts to perform an illegal move or provides an invalid input, the event is logged to a file called pylog.log in the script directory.

No AI or LLM was utilized during the creation of this game.  Any similarities might suggest that I am, in fact, SkyNet..and should reflect poorly on AI in general.


