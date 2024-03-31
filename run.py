# next steps:
# generate a holidays calendar using the information got from the user
# Find out the day of the week the holidays are at
# Develop a logic to check what days could be taken off as bridge days based on the day of the week the holiday landed on
# Return the list of bridge days avaiable on the requested period
# If there is time: find a way to display the information in a pleasant and direct way to the user
# include some colors and a nice title to the program on the terminal
# write docstrings for all functions
# try to use classes and inheritance

import database

import holidays
from datetime import datetime, timedelta

# For the ASCII art of the logo (https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/)
import pyfiglet

# To colour the text
# from: https://stackoverflow.com/questions/67474578/making-coloured-ascii-text-with-python)
from rich import print

# To use autocomplete on inputs (https://stackoverflow.com/questions/63843224/python-prompt-toolkit-how-to-always-open-show-autocompleter)
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter


def prints_logo():
    """
    Prints the logo to the terminal
    """
    banner_part1 = pyfiglet.figlet_format("     Holidays", font="doom")
    banner_part2 = pyfiglet.figlet_format(
        "                      Optimizer", font="doom"
    )

    print(f"[bright_cyan]{banner_part1}[/bright_cyan]")
    print(f"[bright_cyan]{banner_part2}[/bright_cyan]")
    print(
        "[magenta]                                               By Patricia Halley[/magenta]"
    )
    print("\n" * 3)


# WordCompleter object with the keys on the dictrionary of countries set to ignore case to make the autocomplete regardless of typing with lower or uppercase
country_completer = WordCompleter(database.countries.keys(), ignore_case=True)


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

            # To find the country's abbreviation given the country name
            for country, abbreviation in database.countries.items():
                if user_input == country.lower():
                    while True:
                        confirmation = (
                            input(
                                f"The selected country was {country}. Is this the desired country? (y/n): "
                            )
                            .strip()
                            .lower()
                        )
                        if confirmation == "y":
                            # To return the country's abbreviation used on the holidays library
                            return abbreviation
                        elif confirmation == "n":
                            # Prompt for another country
                            break
                        else:
                            print("Invalid input. Please enter 'y' or 'n'.")
                    # Prompt for another country
                    break
            else:
                raise ValueError(
                    "Invalid input. Please enter a valid country name in English."
                )
        except ValueError as e:
            print(e)


def specify_state(country):
    """
    Ask the user to input a state for the given country and confirm.
    """
    while True:
        if country in database.states_by_country:
            # Display available states for the given country
            print(
                f"States or territories in {country}: {', '.join(database.states_by_country[country])}"
            )
            state_input = input("Please enter a state: ").strip().upper()
            if state_input in database.states_by_country[country]:
                while True:
                    confirmation = (
                        input(
                            f"The selected state/territory/province was {state_input}. Is this the desired one? (y/n): "
                        )
                        .strip()
                        .lower()
                    )
                    if confirmation == "y":
                        return state_input
                    elif confirmation == "n":
                        break
                    else:
                        print("Invalid input. Please enter 'y' for yes or 'n' for no.")
            else:
                print("Invalid state. Please enter a state from the provided list.")
        else:
            return None


def get_date(message):
    """
    Prompt the user to enter start date and confirm their selection.
    """
    while True:
        try:
            selected_date_str = input(f"{message} (DD-MM-YYYY): ").strip()
            # Conversion of the given dates into date objects to be used by the datetime library (https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)
            selected_date = datetime.strptime(selected_date_str, "%d-%m-%Y")
            # Checks if the user's input is anything other than the requested date format and promts for the correct format

            # if no problem is found with the date format entry it returns the value to main() and stops the loop
            return selected_date
        except ValueError as e:
            if "time data" in str(e):
                print(
                    "Invalid date format. Please enter the date in DD-MM-YYYY format."
                )


def verify_dates(start_date, end_date):
    """
    Prompt the user to enter start and end dates and confirm their selection.
    """
    while True:
        try:
            # Check if end date is a date in the future of the start_date
            if end_date < start_date:
                raise ValueError("End date cannot be before the start date.")
            if end_date == start_date:
                raise ValueError("End date cannot be the same as the start date.")
            # Check if dates are maximum one year apart (https://docs.python.org/3/library/datetime.html#timedelta-objects)
            if (end_date - start_date).days > 366:
                raise ValueError("Please enter dates that are maximum one year apart.")
            # To break the loop in case there is no problem with the chosen dates validation
            return
        except ValueError as e:
            print(e)
            new_start_date = get_date("Please select a new start date ")
            new_end_date = get_date("Please select a new end date ")
            start_date = new_start_date
            end_date = new_end_date
            return start_date, end_date


def confirm_dates(start_date, end_date):
    while True:
        confirmation = (
            input(
                f"The selected period was {start_date.strftime('%d-%m-%Y')} and {end_date.strftime('%d-%m-%Y')}. Are you happy with these dates? (yes/no): "
            )
            .strip()
            .lower()
        )

        if confirmation == "n":
            # Asks for new start and end dates
            new_start_date = get_date("Please select a new start date ")
            new_end_date = get_date("Please select a new end date ")
            start_date = new_start_date
            end_date = new_end_date
            return start_date, end_date
        elif confirmation == "y":
            # To stop the loop and return the dates
            return start_date, end_date
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")


# https://pypi.org/project/holidays/
def check_holidays(start_date, end_date, country, state=None):
    # Holidays for the specified country and state
    holiday_calendar = holidays.CountryHoliday(country, state)

    # Initialize a dictionary to store holidays
    holiday_dict = {}

    # Iterate through each day between start_date and end_date
    check_date = start_date
    while check_date <= end_date:
        # Check if the current date is a holiday and if it is add the holiday to the dictionary
        if check_date in holiday_calendar:
            holiday_name = holiday_calendar[check_date]
            holiday_dict[check_date] = holiday_name

        # Move to the next day. If use only += 1 it gives an error: unsupported operand type(s) for +=: 'datetime.datetime' and 'int'
        check_date += timedelta(days=1)
    if not holiday_dict:
        print("There are no holidays during the selected period in your area")
    else:
        # Print the dictionary to the user
        if holiday_dict:
            print("The public holidays in your region during the selected period are:")
            for date, holiday in sorted(holiday_dict.items()):
                print(f"{date.strftime('%d-%m-%Y')}: {holiday}")

    return holiday_dict


# def get_bridge_days(start_date, end_date):
#     #elaborate this function


def main():
    prints_logo()
    print("Welcome to the Holiday Optimizer!")

    selected_country_abb = get_country()

    selected_state = specify_state(selected_country_abb)

    print("Please enter the start and end dates to check for holidays.")

    start_date = get_date("Please enter the start date ")

    end_date = get_date("Please enter the end date ")

    verify_dates(start_date, end_date)

    confirm_dates(start_date, end_date)

    check_holidays(start_date, end_date, selected_country_abb, selected_state)

    # get_bridge_days(start_date, end_date)


main()
