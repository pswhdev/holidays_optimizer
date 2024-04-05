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
    Prints the logo to the terminal and waits for the user to press any key.
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

    # Wait for the user to press any key (https://pieriantraining.com/how-to-wait-for-a-keypress-in-python/)
    input("Press enter to continue...")


# WordCompleter object with the keys on the dictrionary of countries set to ignore case to make the autocomplete regardless of typing with lower or uppercase
country_completer = WordCompleter(database.countries.keys(), ignore_case=True)


def get_country():
    """
    Prompts user for a country name and returns its abbreviation after validation.
    Ensures the input is a non-numeric, valid country name.
    Confirms the choice with the user before proceeding.
    """
    while True:
        try:
            # Autocomplete to improve UX and avoid misspells
            user_input = prompt(
                "Please enter a country, or select from the list using arrow/tab keys: ",
                completer=country_completer,
            )
            # Converts input to lowercase and deletes empty spaces
            user_input = user_input.strip().lower()

            # Validation block to check if input is not empty, space or digit instead of text.
            if user_input.isdigit():
                raise ValueError(
                    "Please enter a valid country name (text, not a number)."
                )
            elif not user_input:
                raise ValueError("Input cannot be empty. Please enter a country.")
            # If the input is valid:
            # To find the country's abbreviation given the country name to work with the holidays library
            for country, abbreviation in database.countries.items():
                if user_input == country.lower():
                    # Confirmation block with the user about county's choice, it keeps on asking for a valid answer ('y' or 'n')
                    while True:
                        print(
                            f"[bright_green]The selected country was {country}. [/bright_green]"
                        )
                        confirmation = (
                            input("Is this the desired country? (y/n): ")
                            .strip()
                            .lower()
                        )
                        if confirmation == "y":
                            # If the user confirms, it returns the country's abbreviation (used on the holidays library)
                            return abbreviation
                        elif confirmation == "n":
                            # If the user decides to choose another country it has to get out of this inner loop
                            break
                        else:
                            print("Please enter 'y' or 'n'.")
                    # Since the first input (country's name) was a valid one, if the user's input was 'n' inside the confirmation block, the inner loop is stopped and the outer loop also needs to be stopped so the block restarts and prompts for choice of country again.
                    break
            else:
                raise ValueError("Please enter a valid country name in English.")
        except ValueError as e:
            print("[bright_red]Invalid input.[/bright_red]", e)


def specify_state(country):
    """
    Ask the user to input a state for the given country.
    Confirms the choice with the user before proceeding.

    """
    while True:
        if country in database.states_by_country:
            # Display available states for the given country
            print(
                f"[bright_yellow]States or territories in {country}:[/bright_yellow] {', '.join(database.states_by_country[country])}"
            )
            state_input = input("Please enter a state: ").strip().upper()
            if state_input in database.states_by_country[country]:
                while True:
                    print(
                        f"[bright_green]The selected state/territory/province was {state_input}. [/bright_green]"
                    )
                    confirmation = (
                        input("Is this the desired one? (y/n): ").strip().lower()
                    )
                    if confirmation == "y":
                        return state_input
                    elif confirmation == "n":
                        break
                    else:
                        print(
                            "[bright_red]Invalid input.[/bright_red] Please enter 'y' for yes or 'n' for no."
                        )
            else:
                print(
                    "[bright_red]Invalid state[/bright_red]. Please enter a state from the provided list."
                )
        else:
            return None


def get_date(message):
    """
    Prompts the user to enter a date and validates it.
    The date must be in the future and within 10 years from today.
    """
    while True:
        try:
            selected_date_str = input(f"{message} (DD-MM-YYYY): ").strip()

            # Check if the input matches the expected format
            if (
                len(selected_date_str) != 10
                or selected_date_str[2] != "-"
                or selected_date_str[5] != "-"
            ):
                print("[bright_red]Invalid date format. [/bright_red]")
                raise ValueError("Please enter the date in DD-MM-YYYY format.")

            # Conversion of the given dates into date objects to be used by the datetime library (https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)
            selected_date = datetime.strptime(selected_date_str, "%d-%m-%Y")

            if selected_date < datetime.now():
                print("[bright_red]You cannot choose a date in the past. [/bright_red]")
                raise ValueError(
                    f"Today is {datetime.now().strftime('%d-%m-%Y')}. Please choose a date in the future."
                )
            # Check if the selected date is within 10 years from today
            max_date = datetime.now() + timedelta(days=365 * 10)
            if selected_date > max_date:
                print(
                    "[bright_red]The selected date is too far in the future. [/bright_red]"
                )
                raise ValueError(
                    f"Today is {datetime.now().strftime('%d-%m-%Y')}. Please choose a date within the next 10 years."
                )

            # if no problem is found with the date format entry it returns the value to main() and stops the loop
            return selected_date
        except ValueError as e:
            # Checks if the user's input is anything other than the requested date format and promts for the correct format
            if "time data" in str(e):
                print(
                    "[bright_red]Invalid date format.[/bright_red] Please enter the date in DD-MM-YYYY format."
                )
            else:
                print(e)


def verify_dates(start_date, end_date):
    """
    Validates the user's date choices, ensuring the end date
    is after the start date and within one year.
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
            return start_date, end_date
        except ValueError as e:
            print("[bright_red]Invalid choice. [/bright_red]", e)
            start_date = get_date("Please select a new start date ")
            end_date = get_date("Please select a new end date ")


def confirm_dates(start_date, end_date):
    """
    Confirms the selected date range with the user and
    allows for reselection if not satisfied.
    """
    while True:
        print(
            f"[bright_green]The selected period was [/bright_green]{start_date.strftime('%d-%m-%Y')}[bright_green] and [/bright_green]{end_date.strftime('%d-%m-%Y')}[bright_green].[/bright_green]"
        )
        confirmation = input("Are you happy with these dates? (y/n): ").strip().lower()

        if confirmation == "n":
            # Asks for new start and end dates
            start_date, end_date = handle_new_dates()
            return start_date, end_date
        elif confirmation == "y":
            # To stop the loop and return the dates
            return start_date, end_date
        else:
            print(
                "[bright_red]Invalid input.[/bright_red] Please enter 'y' for yes or 'n' for no."
            )


def handle_new_dates():
    """
    Handles the process of obtaining and confirming new
    start and end dates from the user.
    """
    start_date = get_date("Please select a new start date ")
    end_date = get_date("Please select a new end date ")
    start_date, end_date = verify_dates(start_date, end_date)
    start_date, end_date = confirm_dates(start_date, end_date)
    return start_date, end_date


# https://pypi.org/project/holidays/
def check_holidays(start_date, end_date, country, state=None):
    """
    Identifies public holidays in a specified country (and state when that is the case)
    between given start and end dates. Returns a dictionary of public holidays.
    """

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
            #For the countries that have Sunday on the holidays library saved as holidays (e.g. Sweeden)
            if holiday_name != "Sunday" and holiday_name != "Söndag":
                holiday_dict[check_date] = holiday_name

        # Move to the next day. If use only += 1 it gives an error: unsupported operand type(s) for +=: 'datetime.datetime' and 'int'
        check_date += timedelta(days=1)
    if not holiday_dict:
        print(
            "[bright_yellow]There are no holidays during the selected period in your area[/bright_yellow]"
        )
    else:
        # Print the dictionary to the user
        if holiday_dict:
            print(
                "[bright_green]The public holidays in your region during the selected period are:[/bright_green]"
            )
            for date, holiday in sorted(holiday_dict.items()):
                print(f"{date.strftime('%d-%m-%Y')}: {holiday}")
                
    return holiday_dict


def is_weekend(date):
    """
    Checks if a certain date is a weekday(Mo-Fr)
    """
    # Uses the method .weekday() from the Python's module daytime to find the day of the week. It returns an integer where Monday is 0 and Sunday is 6
    return date.weekday() >= 5


def find_blocks(start_date, end_date, holidays):
    """
    Finds blocks of workdays between free days that could be suggested as vacation days.
    It iterates over the days within the given range and whenever a weekend or a holiday
    is found, it creates a block of dates that are saved independently within the workday_blocks
    and continues the iteration.
    """
    workday_blocks = []
    current_workday_block = []

    current_date = start_date
    while current_date <= end_date:
        if not is_weekend(current_date) and current_date not in holidays:
            current_workday_block.append(current_date)
        else:
            if current_workday_block:  # Append non-empty blocks
                workday_blocks.append(current_workday_block)
            current_workday_block = []
        # Increments current_date by one day
        current_date += timedelta(days=1)
    # To append the last block if it contains working days after the loop is finished
    if current_workday_block:
        workday_blocks.append(current_workday_block)

    return workday_blocks


def vacation_suggestions(workday_blocks, holidays):
    """
    Gathers, sorts, and prints vacation suggestions based on blocks containing 1 and 2 days and
    in special cases for 3-day period where the remaing two week days are holydays and 4-day periods
    where either a Friday and the immediately following Monday are both holidays, or a Monday and
    the immediately preceding Friday are both holidays.
    """
    suggestions_dict = {}

    for block in workday_blocks:
        if len(block) == 4:
            first_date = block[0]
            last_date = block[-1]
            # Check if the last date is a Thursday (meaning there is a holiday on Friday) and the next Monday is a holiday
            if last_date.weekday() == 3 and (last_date + timedelta(days=4) in holidays):
                # Adds the block of dates with the first_date of the block as key to the suggestions dictionary
                suggestions_dict[block[0]] = block
            # Check if the end date is a Tuesday (meaning Monday is a holiday) and the previous Friday is a holiday
            elif first_date.weekday() == 1 and (
                first_date + timedelta(days=-4) in holidays
            ):
                suggestions_dict[block[0]] = block
        elif len(block) == 3:
            first_date = block[0]
            last_date = block[-1]
            # Check if the last date is a Wednesday (meaning there is a holiday on Thursday) and if Friday is also a holiday
            if last_date.weekday() == 2 and (last_date + timedelta(days=2) in holidays):
                suggestions_dict[block[0]] = block
            # Check if the last date is a Wednesday (meaning there is a holiday on Tuesday) and if Monday is also a holiday
            elif first_date.weekday() == 2 and (
                first_date + timedelta(days=-2) in holidays
            ):
                suggestions_dict[block[0]] = block
        # Collects suggestions for 1-2 day blocks
        elif 1 <= len(block) <= 2:
            suggestions_dict[block[0]] = block

    # To sort suggestions by the first date in each block
    sorted_by_date = sorted(suggestions_dict.keys())

    if sorted_by_date:
        print(
            "\n[bright_green]Suggested vacation days for time off optimization: [/bright_green]"
        )
        # Iterates over the sorted list of dates and gets the block of dates on that corresponding key from the dicrionary
        for date in sorted_by_date:
            block = suggestions_dict[date]
            # Iterates over the dates within the block and formats it to DD-MM-YYYY
            formatted_dates = [d.strftime("%d-%m-%Y") for d in block]
            print(f"{', '.join(formatted_dates)}")
    else:
        print(
            "\n[bright_green]No optimal vacation suggestions found in the given date range.[/bright_green]]"
        )


def what_next():
    """
    Allows for the user to either restart the program or finish it.
    """
    print()
    while True:
        what_next = input(
            "If you wish to make a new inquiry, press 'r', to finish the program, press 'f': "
        )
        if what_next == "r":
            main()
        elif what_next == "f":
            print(
                "\n[bright_green]Thank you for using Holidays Optimizer! Enjoy your time off :-)[/bright_green]"
            )
            # Stops the loop
            break
        else:
            print("[bright_red]Invalid entry. [/bright_red]")


def main():
    """
    Controls the order of execution of the functions guiding the user through the process of selecting a country,
    specifying dates, and checking for public holidays. It then suggests optimal days for taking time off to maximize
    holiday periods.
    """
    prints_logo()
    print("\nWelcome to the Holiday Optimizer!")
    print(
        "\nThis interactive tool helps you maximize your holiday time off."
        "Simply select your country and desired dates, and the Holidays Optimizer"
        " will identify public holidays in your region. It then suggests the best"
        " days to take off work, turning regular holidays into extended breaks. "
        "With easy-to-follow prompts and a user-friendly interface, planning your "
        "time off of work has never been easier!\n"
    )
    selected_country_abb = get_country()
    selected_state = specify_state(selected_country_abb)
    print("Please enter the start and end dates to check for holidays.")
    start_date = get_date("Please enter the start date ")
    end_date = get_date("Please enter the end date ")
    # Important to reassign the start and end date in case they had been reentered as part of the validation and confirmation steps
    start_date, end_date = verify_dates(start_date, end_date)
    start_date, end_date = confirm_dates(start_date, end_date)
    holidays = check_holidays(
        start_date, end_date, selected_country_abb, selected_state
    )
    # get_bridge_days(holidays)
    workday_blocks = find_blocks(start_date, end_date, holidays)
    vacation_suggestions(workday_blocks, holidays)
    what_next()


main()
