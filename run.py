import holidays
from datetime import datetime

# List of countries
countries = [
    "Albania",
    "Algeria",
    "American Samoa",
    "Andorra",
    "Angola",
    "Argentina",
    "Armenia",
    "Aruba",
    "Australia",
    "Austria",
    "Azerbaijan",
    "Bahamas",
    "Bahrain",
    "Bangladesh",
    "Barbados",
    "Belarus",
    "Belgium",
    "Belize",
    "Bolivia",
    "Bosnia and Herzegovina",
    "Botswana",
    "Brazil",
    "Brunei",
    "Bulgaria",
    "Burkina Faso",
    "Burundi",
    "Cambodia",
    "Cameroon",
    "Canada",
    "Chad",
    "Chile",
    "China",
    "Colombia",
    "Costa Rica",
    "Croatia",
    "Cuba",
    "Curacao",
    "Cyprus",
    "Czechia",
    "Denmark",
    "Djibouti",
    "Dominican Republic",
    "Ecuador",
    "Egypt",
    "El Salvador",
    "Estonia",
    "Eswatini",
    "Ethiopia",
    "Finland",
    "France",
    "Gabon",
    "Georgia",
    "Germany",
    "Ghana",
    "Greece",
    "Guam",
    "Guatemala",
    "Honduras",
    "Hong Kong",
    "Hungary",
    "Iceland",
    "India",
    "Indonesia",
    "Iran",
    "Ireland",
    "Isle of Man",
    "Israel",
    "Italy",
    "Jamaica",
    "Japan",
    "Jersey",
    "Kazakhstan",
    "Kenya",
    "Kuwait",
    "Kyrgyzstan",
    "Laos",
    "Latvia",
    "Lesotho",
    "Liechtenstein",
    "Lithuania",
    "Luxembourg",
    "Madagascar",
    "Malawi",
    "Malaysia",
    "Maldives",
    "Malta",
    "Marshall Islands (the)",
    "Mexico",
    "Moldova",
    "Monaco",
    "Montenegro",
    "Morocco",
    "Mozambique",
    "Namibia",
    "Netherlands",
    "New Zealand",
    "Nicaragua",
    "Nigeria",
    "Northern Mariana Islands (the)",
    "North Macedonia",
    "Norway",
    "Pakistan",
    "Panama",
    "Papua New Guinea",
    "Paraguay",
    "Peru",
    "Philippines",
    "Poland",
    "Portugal",
    "Puerto Rico",
    "Romania",
    "Russia",
    "San Marino",
    "Saudi Arabia",
    "Serbia",
    "Seychelles",
    "Singapore",
    "Slovakia",
    "Slovenia",
    "South Africa",
    "South Korea",
    "Spain",
    "Sweden",
    "Switzerland",
    "Taiwan",
    "Tanzania",
    "Thailand",
    "Timor Leste",
    "Tonga",
    "Tunisia",
    "Turkey",
    "Ukraine",
    "United Arab Emirates",
    "United Kingdom",
    "United States Minor Outlying Islands",
    "United States of America (the)",
    "United States Virgin Islands (the)",
    "Uruguay",
    "Uzbekistan",
    "Vanuatu",
    "Vatican City",
    "Venezuela",
    "Vietnam",
    "Virgin Islands (U.S.)",
    "Zambia",
    "Zimbabwe",
]

# List of countries with holidays varying with the state
countries_state_holidays = [
    "Australia",
    "Austria",
    "Bolivia",
    "Bosnia and herzegovina",
    "Brazil",
    "Canada",
    "Chile",
    "El salvador",
    "France",
    "Germany",
    "India",
    "Italy",
    "Malaysia",
    "New zealand",
    "Nicaragua",
    "Portugal",
    "Spain",
    "Switzerland",
    "United kingdom",
    "United states of america",
]


def get_country():
    """
    Gets country from the user's input and checks for valid input.
    While loop keeps prompting for correct input until a valid
    country name from the list is given as an input.
    """
    while True:
        # Converts input to lowercase and deletes empty spaces
        user_input = input("Please enter a country: ").strip().lower()
        # Validation to check if input is a number instead of text
        if user_input.isdigit():
            print(
                "Invalid input. Please enter a valid country name (text, not a number)."
            )
        # Validation to prevent sumbission of empty input or white spaces
        elif not user_input:
            print("Input cannot be empty. Please enter a country.")
        # Converts country name from the list to lowercase
        elif user_input and user_input in [country.lower() for country in countries]:
            return (
                # Returns the country name with the first letter capitalized
                user_input.capitalize()
            )
        else:
            print("Invalid input. Please enter a valid country name in English.")


def choose_state(country):
    if country == "Australia":
        user_input_state = input(
            "Please enter one of the territorries: ACT, NSW, NT, QLD, SA, TAS, VIC, WA: "
        )
    elif country == "Austria":
        user_input_state = input(
            "Please enter one of the states:  B, K, N, O, S, St, T, V, W: "
        )
    elif country == "Bolivia":
        user_input_state = input(
            "Please enter one of the Departments: B, C, H, L, N, O, P, S, T: "
        )
    elif country == "Bosnia and herzegovina":
        user_input_state = input("Please enter one District: BIH, BRC, SRP: ")
    elif country == "Brazil":
        user_input_state = input(
            "Please enter a state (two letters abrbreviation, e.g. AC for Acre): "
        )
    elif country == "Canada":
        user_input_state = input(
            "Please enter a province  AB, BC, MB, NB, NL, NS, NT, NU, ON, PE, QC, SK, YT: "
        )


def main():
    selected_country = get_country()
    print("You selected:", selected_country)
    if selected_country in countries_state_holidays:
        choose_state(selected_country)


main()
