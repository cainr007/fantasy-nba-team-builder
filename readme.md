The NBA Fantasy League project will allow
a user to create, add, view, and manage their
custom fantasy team. This application uses MySQL as
the database, with Python as the interface.

The 3 layer architecture is composed of the
GUI, BLL, and DAL. The DAL interacts with the database,
the BLL handles the business layer, connecting the DAL to
the GUI. And the GUI is the graphical user interface
that the user interacts with.

For setup and running, the first step will be running
the SQL file in MySQL Workbench to create the tables,
stored procedures, functions and views.

The second step will be running the pip installs from
what's in the requirements.txt file.

After all that is finished, you can begin by accessing the GUI.py
file and running it. You'll be prompted to enter your
MySQL username, password, host and port. The host and port
will be defaulted as "localhost" and "3306".

The domain I chose for this project is NBA fantasy basketball.
I chose this domain because I have an interest in the NBA and
wanted to create a project that combines my interest in
basketball with the database concepts learned throughout
this course.

The advanced feature for this project is the interactive
NBA player cards. Each player card displays the player's
image, name, team, position, and statistics. The user can
also interact with the cards to add players to their fantasy
team.

I chose this feature because I wanted the application to
be more interactive and visually appealing than simply
displaying database records. To create this feature, I
learned how to use the Pillow library to load and display
images within Tkinter, as well as how to dynamically create
the player cards based on the data retrieved from the database.

The advanced feature is primarily contained within GUI.py,
with the player data being retrieved through BLL.py and DAL.py.
The player images are contained within the Images folder.

Finally, a general note that the View Players page may 
take a little while to load because the application is 
loading and displaying all of the player cards and images.
At times, upwards of 60 seconds.