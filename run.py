# next steps:
# generate a holidays calendar using the information got from the user
# Find out the day of the week the holidays are at
# Develop a logic to check what days could be taken off as bridge days based on the day of the week the holiday landed on
# Return the list of bridge days avaiable on the requested period
# If there is time: find a way to display the information in a pleasant and direct way to the user
# include some colors and a nice title to the program on the terminal
import database

import holidays
from datetime import datetime

# For the ASCII art of the logo (https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/)
import pyfiglet

# To colour the text
# from: https://stackoverflow.com/questions/67474578/making-coloured-ascii-text-with-python)
from rich import print

# To use autocomplete on inputs (https://stackoverflow.com/questions/63843224/python-prompt-toolkit-how-to-always-open-show-autocompleter)
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter


# To print logo on the terminal
def prints_logo():
    banner_part1 = pyfiglet.figlet_format("     Holidays", font="doom")
    banner_part2 = pyfiglet.figlet_format(
        "                      Optimizer", font="doom"
    )

    print(f"[bright_cyan]{banner_part1}[/bright_cyan]")
    print(f"[bright_cyan]{banner_part2}[/bright_cyan]")
    print(
        "[magenta]                                               By Patricia Halley[/magenta]"
    )
    print("\n", "\n", "\n")


# WordCompleter object with the list of countries set to ignore case to make the autocomplete regardless of typing with lower or uppercase
country_completer = WordCompleter(database.countries, ignore_case=True)

def get_country():
    """
    Gets country from the user's input and checks for valid input.
    While loop keeps prompting for correct input until a valid
    country name from the list is given as an input.
    """
    while True:
        try:
            # Autocomplete to improve UX and avoid misspells
            user_input = prompt(
                "Please enter a country: ",
                completer=country_completer,
            )
            # Converts input to lowercase and deletes empty spaces
            user_input = user_input.strip().lower()

            # Validation to check if input is a number instead of text
            if user_input.isdigit():
                raise ValueError(
                    "Invalid input. Please enter a valid country "
                    "name (text, not a number)."
                )

            # Validation to prevent submission of empty input or white spaces
            elif not user_input:
                raise ValueError("Input cannot be empty. Please enter a country.")

            # To return the coutry name with proper casing if coutry
            # is found on country list
            for country in database.countries:
                if user_input == country.lower():
                    # To keep original case of the matched country name
                    return country

            else:
                raise ValueError(
                    "Invalid input. Please enter a valid country name in English."
                )
        except ValueError as e:
            print(e)


def specify_state(country):
    """Ask the user to input a state for the given country."""
    while True:
        if country in database.states_by_country:
            # Display available states for the given country
            print(
                f"States or territories in {country}: {', '.join(database.states_by_country[country])}"
            )
            state_input = input("Please enter a state: ").strip().upper()
            if state_input in database.states_by_country[country]:
                return state_input
            else:
                print("Invalid state. Please enter a state" "from the provided list.")


def get_date(message):
    while True:
        try:
            date = input(message + " (DD-MM-YYYY): ")
            # Conversion of the given date into a date to be used by the datetime library (https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)
            date_obj = datetime.strptime(date, "%d-%m-%Y")
            return date_obj
        except ValueError:
            print("Invalid date format. Please enter the date in DD-MM-YYYY format.")


def check_holidays(start_date, end_date):
    while True:
        try:
            # Check if end date is a date in the future of the start_date
            if end_date <= start_date:
                raise ValueError("End date cannot be before the start date.")

            # Check if dates are maximum one year apart (https://docs.python.org/3/library/datetime.html#timedelta-objects)
            if (end_date - start_date).days > 365:
                raise ValueError("Please enter dates that are maximum one year apart.")

            print(
                #strftime method is formatting the datetime object (yyyy-mm-dd 00:00:00) back into string on the desired dd-mm-yyyy format
                f"Checking for public holidays between {start_date.strftime('%d-%m-%Y')} and {end_date.strftime('%d-%m-%Y')}"
            )
            #To stop the loop
            return
        
        except ValueError as e:
            # Print error message
            print(e)
            # Prompt for new start and end dates
            start_date = get_date("Enter the start date")
            end_date = get_date("Enter the end date")



# def get_bridge_days(start_date, end_date):
#     #elaborate this function


def main():
    prints_logo()
    print("Welcome to the Holiday Optimizer!")

    selected_country = get_country()
    print("You selected:", selected_country)
    if selected_country in database.states_by_country:
        specify_state(selected_country)

    print("Please enter the start and end dates to check for holidays.")

    start_date = get_date("Enter the start date")
    end_date = get_date("Enter the end date")

    check_holidays(start_date, end_date)

    # get_bridge_days(start_date, end_date)


main()
