# next steps:
# If there is time: find a way to display the information in a pleasant and direct way to the user
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
    input("Press any key to continue...")


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
                "Please enter a country: ",
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
                raise ValueError(
                    "Input cannot be empty. Please enter a country."
                )
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
                    # Since the first input (country's name) was a valid one,
                    # if the user's input was 'n' inside the confirmation block,
                    # the inner loop is stopped and the outer loop also needs to be stopped
                    # so the block restarts and prompts for choice of country again.
                    break
            else:
                raise ValueError(
                    "Please enter a valid country name in English."
                )
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
                        input(f"Is this the desired one? (y/n): ")
                        .strip()
                        .lower()
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
                print(
                    "[bright_red]You cannot choose a date in the past. [/bright_red]"
                )
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
                raise ValueError(
                    "End date cannot be the same as the start date."
                )
            # Check if dates are maximum one year apart (https://docs.python.org/3/library/datetime.html#timedelta-objects)
            if (end_date - start_date).days > 366:
                raise ValueError(
                    "Please enter dates that are maximum one year apart."
                )
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
        confirmation = (
            input("Are you happy with these dates? (y/n): ").strip().lower()
        )

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


def filter_weekday_holidays(holiday_dict):
    """
    Filters out weekend holidays from a dictionary of holidays,
    returning only those that fall on weekdays.
    """
    weekday_holidays = []
    for date, holiday in sorted(holiday_dict.items()):
        # Using datetime to find day of the week (https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes)
        weekday = date.strftime("%A")
        # Filter out weekends (Saturday and Sunday)
        if weekday not in ["Saturday", "Sunday"]:
            weekday_holidays.append(
                {"name": holiday, "date": date, "weekday": weekday}
            )
    return weekday_holidays


def get_bridge_days(holidays):
    """
    Identifies potential bridge days around public holidays to optimize vacation days.
    Analyzes weekdays holidays to suggest days off for extended breaks. Considers taking 1, 2 and
    4 days vacation in special cases like consecutive Friday and Monday holidays for longer breaks.
    """
    four_days_1 = {}
    four_days_2 = {}
    one_day = {}
    two_days_1 = {}
    two_days_2 = {}

    # Filters what holidays are on weekdays
    suitable_holidays = filter_weekday_holidays(holidays)

    # Checks if the following monday of a Friday holiday is also a holiday (like for easter in Europe for instance)
    # In this case, taking the remaining days of one of the two weeks (using 4 vacation days), the person has 10 days free
    for holiday in suitable_holidays:
        if holiday["weekday"] == "Friday":
            following_monday = holiday["date"] + timedelta(days=3)
            following_monday_holiday = None
            # Iterate through the holidays to find if the following Monday is also a holiday
            for h in suitable_holidays:
                if h["date"] == following_monday:
                    following_monday_holiday = h
                    break

            if following_monday_holiday:
                four_days_1[holiday["name"]] = [
                    (holiday["date"] + timedelta(days=-4)),
                    (holiday["date"] + timedelta(days=-3)),
                    (holiday["date"] + timedelta(days=-2)),
                    (holiday["date"] + timedelta(days=-1)),
                ]
                four_days_2[following_monday_holiday["name"]] = [
                    (holiday["date"] + timedelta(days=4)),
                    (holiday["date"] + timedelta(days=5)),
                    (holiday["date"] + timedelta(days=6)),
                    (holiday["date"] + timedelta(days=7)),
                ]
            # Logic for one and two days
            elif not following_monday_holiday:
                one_day[holiday["name"]] = [
                    (holiday["date"] + timedelta(days=-1)),
                    (holiday["date"] + timedelta(days=3)),
                ]
                two_days_1[holiday["name"]] = [
                    (holiday["date"] + timedelta(days=-2)),
                    (holiday["date"] + timedelta(days=-1)),
                ]
                two_days_2[holiday["name"]] = [
                    (holiday["date"] + timedelta(days=3)),
                    (holiday["date"] + timedelta(days=4)),
                ]
        elif holiday["weekday"] == "Monday":
            one_day[holiday["name"]] = [
                (holiday["date"] + timedelta(days=-3)),
                (holiday["date"] + timedelta(days=1)),
            ]
            two_days_1[holiday["name"]] = [
                (holiday["date"] + timedelta(days=-3)),
                (holiday["date"] + timedelta(days=1)),
            ]
            two_days_2[holiday["name"]] = [
                (holiday["date"] + timedelta(days=1)),
                (holiday["date"] + timedelta(days=2)),
            ]
        elif holiday["weekday"] == "Tuesday":
            one_day[holiday["name"]] = [(holiday["date"] + timedelta(days=-1))]
            two_days_1[holiday["name"]] = [
                (holiday["date"] + timedelta(days=-1)),
                (holiday["date"] + timedelta(days=1)),
            ]
        elif holiday["weekday"] == "Wednesday":
            two_days_1[holiday["name"]] = [
                (holiday["date"] + timedelta(days=-2)),
                (holiday["date"] + timedelta(days=-1)),
            ]
            two_days_2[holiday["name"]] = [
                (holiday["date"] + timedelta(days=1)),
                (holiday["date"] + timedelta(days=2)),
            ]
        elif holiday["weekday"] == "Thursday":
            one_day[holiday["name"]] = [(holiday["date"] + timedelta(days=1))]
            two_days_1[holiday["name"]] = [
                (holiday["date"] + timedelta(days=-1)),
                (holiday["date"] + timedelta(days=1)),
            ]

    # Print statements:
    if four_days_1:
        print(
            "\n[bright_green]Using[/bright_green] 4 [bright_green]vacation days in the suggested weeks gives you a[/bright_green] 10[bright_green]-day break.[/bright_green]"
        )
        print("Option 1:")
        for holiday_name, dates in four_days_1.items():
            print(
                f"{holiday_name}: {', '.join([date.strftime('%d-%m-%Y') for date in dates])}"
            )
        print("\nOption 2:")
        for holiday_name, dates in four_days_2.items():
            print(
                f"{holiday_name}: {', '.join([date.strftime('%d-%m-%Y') for date in dates])}"
            )
    if one_day:
        print(
            "\n[bright_green]By taking[/bright_green] 1 [bright_green]vacation day on the suggested date(s), you will have a long weekend of at least[/bright_green] 4 [bright_green]days.[/bright_green]"
        )
        for holiday_name, dates in one_day.items():
            dates_str = " or ".join(
                [date.strftime("%d-%m-%Y") for date in dates]
            )
            print(f"{holiday_name}: Take {dates_str}")

    if two_days_1:
        print(
            "\n[bright_green]By taking [/bright_green]2 [bright_green]vacation days on the suggested dates, you will have an extended break of at least[/bright_green] 5 [bright_green]days.[/bright_green]"
        )
        for holiday_name, dates in two_days_1.items():
            dates_str = " and ".join(
                [date.strftime("%d-%m-%Y") for date in dates]
            )
            print(f"{holiday_name}: Take {dates_str}")

    if two_days_2:
        print(
            "\n[bright_green]Alternatively, consider taking these [/bright_green]2 [bright_green]vacation days for an equally extended break of at least[/bright_green] 5 [bright_green]days.[/bright_green]"
        )
        for holiday_name, dates in two_days_2.items():
            dates_str = " and ".join(
                [date.strftime("%d-%m-%Y") for date in dates]
            )
            print(f"{holiday_name}: Take {dates_str}")

    return four_days_1, four_days_2, one_day, two_days_1, two_days_2


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
    get_bridge_days(holidays)
    what_next()


main()
