Admin panel is comprised of a few menus with options, usually selected via a number.

Main menu:
1.Change stop status
2.remove stop
3.add stop
4.quit

### 1.Change stop status
The user is shown a list of all stops currently in the database, with their ids on the left, and is asked to choose a stop, then choose what should be the new status.
'e' exits back to main menu.

### 2.Remove stop
The user is shown a list of all stops currently in the database, with their ids on the left, and is asked to choose a stop, and then asked to confirm. After a confirmation, the stop is removed from the database.
'e' exits back to main menu.

### 3.Add stop
The user is given two options; add by name or add by coordinates;
#### Add by name
A name to match is requested and then a list of stops with a matching name is returned. The user is asked to pick which stop should be added, asked for the walking distance to the stop, and then asked to confirm.(while the data of the stop is being displayed.). After confirmation the stop is added to the database.
#### Add by coordinates
The user is asked to define a box - the upper and lower bounds of longitude and latitude. In both cases the order (which one is higher and which is lower) doesn't matter. After defining the box, a list of stops within this box is returned. The user is asked to pick which stop should be added, asked for the walking distance to the stop, and then asked to confirm (while the data of the stop is being displayed.). After confirmation the stop is added to the database.

### 4.Quit
Stops the program. Unecessary, since the program can always be stopped with ctrl+c, however added for ease of use.

It's technically very hard to case any problems by exiting the program with ctrl+c because all database transactions are completed right after they are done, which means the only way to break anything is with very precise timing, however, using the Quit option is recommended.