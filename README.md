Hello!
Welcome to the Habit Tracker. This README file will help outline how to use the Habit Tracker.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  SETUP  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Steps to run compiled code:
---------------------------
- Download and save in the same folder:
	- `Click.exe`
	- `Database.db` (Not extremely necessary, but won't hurt to have it)
- Double click `Click.exe`
- The program should execute in a command terminal.
- ENJOY!

Steps to run code through an interpreter:
- Download and save the following in the same project folder:
	- `Click.exe`
	- `Habits.db` (Not extremely necessary, but won't hurt to have it)
	- `Database.py`
	- `Click.py`
	- `main.py`
	- `Test.py`
- Load up your python interpreter (An example: PyCharm)
- Open the project folder that you created
- Open the `Click.py` file
- Run the file (Alternatively, you can run the file through the python terminal using "python Click.py")
- The program should execute within the terminal

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  USING THE PROGRAM  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The tracker does feature a "help" function and this is explained in the program itself. 

The user can type "home" to receive a bunch of instructions on how to use the program and "exit" to terminate the program.

Typing "home" gives the following list of instructions:
	- help: Display the current list of instructions.
    	- add-habit : Add a habit to your list of Habits. (Requires habit name and periodicity)
    	- delete-habit: Removes a habit from your list of habits. (Requires habit name)
    	- display-habit: Displays all habits onto the console
    	- tick-habit: Use this to complete a habit and to increase your streak! (Requires habit name and periodicity)
    	- display-period-habit: Use this to display all habits within a given periodicity (Requires habit periodicity)
    	- display-high-streak: Use this to display the habit with the highest streak!
    	- display-high-streak-period: Use this to display the habit with the highest streak in a provided period

Please note that the command MUST be type as it is seen. To add a habit, the following must be inputted: "add-habit" without the quotation marks.

Typing "help" brings up a help screen that the user can interact with to learn more about each of the commands that the program provides.
An example of such an input would be the following:
	- Type "help"
	- Type "help display-habit"
	- The following is returned:
		- Displays the DB formatted information to the user :return: N/A. Calls a procedure that does the display.
	- The user is free to type "help", "home" or any other command to continue with the program


A user should be able to type any of the above commands and the program will accept it, unless the user is in the progress of validating an input.
The user should then complete the inputting process, as prompted on the screen, and then retry the command. 

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  GENERAL TIPS  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The program does come with a unit test module that needs to be executed separately.

This can be done in the same way that the `Click.py` file is executed:
	- Load the `Test.py` file in the python interpreter
	- Run the file (Alternatively, execute in the terminal with "python Test.py")

The output of the code is a simple pass/fail of several tests run with the program. All tests should be passed on the program run. 
However, if they are not, it could be a database issue (the database is non existent).
How to Fix:
	- Ensure that the `Habits.db` file is in the correct folder (same folder as all other .py files)
	- Try running the `Click.py` file FIRST, before executing the `Test.py` file

This should fix the problem. 