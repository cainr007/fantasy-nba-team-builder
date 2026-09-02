**NBA Fantasy League**

The NBA Fantasy League project allows a user to create, add, view, and
manage their custom fantasy team. This application uses MySQL as the
database and Python as the interface.

**Architecture**

The application uses a three-layer architecture consisting of the GUI,
BLL, and DAL.

- GUI (Graphical User Interface): The interface that the user interacts with.
- BLL (Business Logic Layer): Handles the application's business logic
  and connects the GUI to the DAL.
- DAL (Data Access Layer): Handles communication with the MySQL database.

**Setup and Running**

1. Set Up the Database
Run the SQL file in MySQL Workbench. This will create the required tables,
stored procedures, functions, and views.

2. Install Requirements
Install the Python packages listed in `requirements.txt`.

3. Run the Application
Run `GUI.py` to launch the application.

You will be prompted to enter your MySQL:
- Username
- Password
- Host
- Port

The host and port default to:
- Host: `localhost`
- Port: `3306`********
