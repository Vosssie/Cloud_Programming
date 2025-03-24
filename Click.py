import click  # CLI interface to show hints and instructions to the user
import sys
from click_shell import shell  # Adds instructional prompts and messages to Click layout
from main import Habits  # Import ability to access Habits class instances
from Database import create_db, display_db, create_habit, remove_habit, complete_habit, display_periodicity, \
    display_highest_streak, display_highest_streak_periodicity  # Import all subroutines located in the Database.py file


# Setup of CLI with welcome message and prompts for user assistance
@shell(prompt="Input Habit Command > ", intro="""Welcome to your Habit terminal! \n 
Here you can see to all your habitual needs. Type \"home\" for further instructions. \n
To exit the application: type \"exit\" \n""")
def habitual():
    """
    Procedure to call the create_db() function to create db if not already existing.
    Resets completion of all active habits
    :return:
    """
    click.clear()  # clears the CLI
    all_habits = create_db()
    click.clear()  # clears the CLI as the Completion rest procedure does not need to be exposed to the user
    pass


@habitual.command()  # Adds another command to the CLI
def home():
    """
    Displays a list of instructions for the user to navigate the CLI.
    All instructions correlate to functions below and are given descriptions for the user to understand requirements
    """
    click.clear()
    print("""Here is a list of commands
    
    help: Display the current list of instructions.
    add-habit : Add a habit to your list of Habits. (Requires habit name and periodicity)
    delete-habit: Removes a habit from your list of habits. (Requires habit name)
    display-habit: Displays all habits onto the console
    tick-habit: Use this to complete a habit and to increase your streak! (Requires habit name and periodicity)
    display-period-habit: Use this to display all habits within a given periodicity (Requires habit periodicity)
    display-high-streak: Use this to display the habit with the highest streak!
    display-high-streak-period: Use this to display the habit with the highest streak in a provided period
    """)


@habitual.command()  # Adds another command to the CLI
def add_habit():
    """
    Adds a habit to the database.
    The user is required to enter a habit name and period
    :return: N/A: Calls a function that adds the habit, period and default values to the DB
    """
    verified = False
    while not verified:
        new_habit_name = input("Please input the name of your new habit:  ")
        print("You entered", new_habit_name)
        check = input("Is this correct? Y/N:  ")
        if check.lower() == "y":
            break
    verified = False
    while not verified:
        new_habit_periodicity = input("Please input the periodicity of this habit:  ")
        if new_habit_periodicity.lower() == "daily" or new_habit_periodicity.lower() == "weekly":
            break
        else:
            print("Not a valid period, please retry")
    habit = Habits(new_habit_name.lower(), new_habit_periodicity.lower())  # Default class instance values are sent
    create_habit(habit)


@habitual.command()
def delete_habit():
    """
    Removes a habit from the DB
    The user is required to input the name and period of the habit
    :return: N/A: Calls a function that removes the habit from a DB
    """
    verified = False
    while not verified:
        remove_habit_name = input("Please input the name of the habit to be removed: ")
        print("You entered \"" + remove_habit_name + "\"")
        check = input("Is this correct? Y/N: ")
        if check.lower() == "y":
            break
    verified = False
    while not verified:
        remove_habit_period = input("Please input the periodicity of the habit to be removed: ")
        if remove_habit_period.lower() == "daily" or remove_habit_period.lower() == "weekly":
            break
        else:
            print("Not a valid period, please retry")

    removed_habit = Habits(remove_habit_name.lower(), remove_habit_period.lower())  # Habits class information is passed
    remove_habit(removed_habit)


@habitual.command()
def display_habit():
    """
    Displays the DB formatted information to the user
    :return: N/A. Calls a procedure that does the display.
    """
    click.clear()
    all_habits = display_db()


@habitual.command()
def tick_habit():
    """
    Allows for the completion of a habit
    Requires the user to input a habit name and period
    :return: N/A. Calls a function that completes the habit
    """

    verified = False
    while not verified:
        completed_habit_name = input("Please input the name of the habit you completed: ")
        print("You entered \"" + completed_habit_name + "\"")
        check = input("Is this correct? Y/N: ")
        if check.lower() == "y":
            break
    verified = False
    while not verified:
        completed_habit_period = input("Please input the periodicity of the habit you completed: ")
        if completed_habit_period.lower() == "daily" or completed_habit_period.lower() == "weekly":
            break
        else:
            print("Not a valid period, please retry")

    print("Habit successfully completed. Well done!")
    completed_habit = Habits(completed_habit_name.lower(), completed_habit_period.lower())  # Passes class instance
    complete_habit(completed_habit)


@habitual.command()
def display_period_habit():
    """
    Display all habits with a given period
    :return: N/A. CLI function that calls other subroutines
    """
    periodicity = input("Please input the periodicity of the habits you want to see: ")
    display_periodicity(periodicity.lower())


@habitual.command()
def display_high_streak():
    """
    Displays the highest streak
    :return: N/A. CLI function that calls other subroutines
    """
    display_highest_streak()


@habitual.command()
def display_high_streak_period():
    """
    Displays the highest streak for a given period.
    Requires the user to input a valid period.
    :return:  N/A. CLI function that calls other subroutines
    """
    periodicity = input("Please input the periodicity: ")
    display_highest_streak_periodicity(periodicity.lower())


# Calls the main function to begin the program. The CLI then takes over and allows the user access to all functionality
if __name__ == "__main__":
   # sys.argv[0] = "Click"  # Workaround for PyInstaller in order to generate a .exe with CLI exposed
    habitual()

