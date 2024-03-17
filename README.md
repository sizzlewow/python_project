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



h2. Project Scope:

h3. Goals:
*Accept user input to provide movement through the game world and interact with it.
*Generate output to the user based on interactions with the game.
*Require decision making from the user to determine outcomes in the game.
*Save game state to file so user can stop the game and pick up where they left off 
\\ (I was unable to implement this due to time constraint)

h3. Must perform the following actions:
*Take user input via input menu
*Output
*Logging
*Error handling

h3. Must contain:
*Functions
*Boolean conditions
*List(s)
*Dictionaries
*Modules
*Documentation (code comments and on confluence.)

h3. Time constraints:
*Due 18 Mar 2024 at 1:00PM CST
**Started 10 Mar 2024

h3. Software Requirements:
*OS: Windows 10 or later, Ubuntu workstation or Server 22.04.
*VSCode (other text editors could be used, but VSCode may be preferable)
*Python 3
**PIP
*Modules (not including my own):
*logging
*random
*numpy
*time



h3. Installation and Configuration:
*Install Python 3.12.2 Get it [here|https://www.python.org/downloads/release/python-3122/]
*Unpack the zip file containing my project to a directory of your choice.
*In your terminal of choice, change directory to the project directory.
*Run "pip install -r requirements.txt" (This installs any dependancies required to run this package)
*Run "python main.py" to start the script.
*RECONFIGURATION OF THIS PACKAGE WILL BE COVERED IN "Code Documentation"

h3. Code Documentation:

h4. main.py:
**Starts the game:
***Prints 300 newlines to clear screen, then calls GameMenu.new_char function from game module.
***Once this is complete, GameMenu.main_menu is called from game module.

h4. world.py
**Defines the world the player moves around in.  
\\ Contains classes for each tile type, defining the behaviors and attributes of each,
\\ including flavor text and menu/decision loops.
**Generates a 2D array or matrix which is referenced during player movement within the world.
**Assigns values to each index of the array.
\\ each element matches a key in the dictionary in "tile_dict"
\\ The value assigned to each key is the associated class in the module.
\\ The array is built using numpy.array because it allows for some helpful functions,
\\ such as assigning the data type of elements in the array.
***You can modify the game map by adding rows or columns to tile_map in buildMap
\\ and editing the key/value pairs in tile_types in buildMap
\\ (ensure that the key exists in the map array, and the value aligns to an existing class)

h4. game.py
*Player controls live here.
*Contains: 
**GameMenu.new_char function (for naming character), 
**GameMenu.main_menu function (simply prints out a few stats at start), 
**Movement.where_to function which facilitates player movement through the world and prevents leaving the map.
**(There is nothing to edit in this module)

h4. npc.py
*Currently only holds one class and function: 
**BarTender.choice
\\ Facilitates user interaction with the tavern tile.

h4. player.py
*Contains the User class.  
**Three functions provide a way to update the player's location during movement,
\\ player name, and one state variable set by interaction with the game.
***playerstate changes depending on your actions in the tavern, 
\\will result in different flavor text from one of the tiles.
***player_name is called when the game starts to set the player's name in the game world.
** To change default player start location edit "y" and "x" atributes to valid indices from the map in world.py
\\ index 0,0 is top left, y axis is virtical (indexing down increases the number)
\\ x axis is horizontal (indexing right increases the number)

h4. helper.py
*Currently only holds one class and function: utilities.slowPrint.
\\ the function within takes the text the game would print to the user and outputs it 
\\ a character at a time as though it were being typed.
\\ It just provides a more interesting experience.

h4. Logging
*Logging is facilitated via the logging module.
\\ At various stages within game.py, if the user attempts to perform an illegal move
\\ or provides an invalid input, the event is logged to a file called pylog.log in the script directory.

h4. DISCLAIMER
*No AI or LLM was utilized during the creation of this game.
\\ Any similarities might suggest that I am, in fact, SkyNet
\\ ...and should reflect poorly on AI in general.


