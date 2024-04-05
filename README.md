# Holidays Optimizer
![Holiday Optimizer logo](documentation/logo-screen.png)

The "Holidays Optimizer" is a user-friendly program designed to help the user make the most out of their vacation days. It cleverly identifies public holidays within a given time frame and suggests the best days to take off from work. This way, regular holidays can be extended into longer breaks. The program is especially useful to maximize time off without using up too many leave days. By aligning vacation with existing public holidays, and considering weekends, it helps to achieve longer periods of leisure.

Visit the deployed program: [Holidays Optimizer](https://holidays-optimizer-02bf64773985.herokuapp.com/) - ***Use Ctrl (Cmd) and click to open in a new window.*** 

## Contents

<!-- Instert table of contents here -->


## Introduction

This program assists users in planning their vacation time by identifying public holidays within a specified period and suggesting optimal days for taking time off. Its goal is to maximize extended breaks around these holidays.

# User Experience 
  
## User Goals
- As a user, I want an attractive and engaging application.
- As a user, I want clear instructions provided throughout the application.
- As a user, I want feedback confirming my choices of country, state, and selected period.
- As a user, I want to be able to re-enter data entered by mistake during the process without having to restart the program.
- As a user, I want a clear and sorted output of the suggested vacation dates.

# Creation Process   

## Project planning

My idea for this project was to develop a program that, when provided with user-specified dates, automatically pinpoints public holidays and recommends bridge days, which are strategically chosen to effectively prolong holiday breaks, to be taken as vacations optimizing the break periods by using less vacation.

Reseraching online I found that in order to offer the product to a wider range of users, I have decided to use a [holidays library](https://pypi.org/project/holidays/) available for Python, which includes holidays from many different countries.

 My main goals for the application were to:

- Obtain location input from the user, including country and state/province or territory (depending on the availability of those in the holidays library).
- Gather start and end dates from the user to generate a list of holidays within the specified period.
- Implement input validation to ensure that no empty spaces or inappropriate date formats or date ranges are accepted.
- Produce clear output with a sorted list of dates, serving as suggestions for vacation dates.

## Flowchart   
To help with planning my project, I used [Lucidchart](https://www.lucidchart.com/pages/) to produce a flowchart and organize the flow of the program.

![Holiday Optimizer initial FlowChart](documentation/initial-flowchart.png)  

## Development

I began by developing functions to collect user input for the country and state (if available).

Since I intended to utilize the holidays library to retrieve holidays based on the country input, ensuring accurate results required obtaining the country abbreviation in accordance with the ISO 3166-1 alpha-2 code, as outlined in the [library's documentation](https://pypi.org/project/holidays/).

To enhance user-friendliness and enable input of country names, I created a separate file containing a dictionary. This dictionary mapped country names to their respective abbreviations. Additionally, within the same file, I established a second dictionary called 'database,' which listed countries with available lists of states within the library to be used by the functions on the program.

To prevent mistypes and improve the user experience, I integrated the autocomplete feature from the [prompt_toolkit](https://python-prompt-toolkit.readthedocs.io/en/master/) library when prompting for the country's name.

I relied on the flowchart as my guide throughout the development process, ensuring that each function worked properly and that validations were effectively implemented at every step.

After implementing the functions to obtain the country, state, and dates from the user, I decided to incorporate an additional confirmation step after each input. This way, users wouldn't need to restart the program in case of accidental input errors.

After some consideration, I also decided not to include the previously planned prompts for the number of days and the option for month or period. These data wouldn't contribute significantly to achieving the desired result.

With these changes during the process the resulting flowchart was slightly changed.

![Holiday Optimizer final FlowChart](documentation/flowchart-final.png)


## Design Choices      

As this project focused on back-end programming, I, a student of the [Code Institute](https://codeinstitute.net/ie/), did not undertake front-end production myself. The command-line interface (CLI) code was provided through the use of CI's [Python Essentials template](https://github.com/Code-Institute-Org/python-essentials-template), and I chose not to modify the HTML or JavaScript code, maintaining the original interface design. The CLI application displayed within an 80-character window with a vertical scrollbar.

ASCII art was used using the [pyfiglet module](https://pypi.org/project/pyfiglet/) for the program's logo at the start of the program as described [here](https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/) using the font "doom".

![Holiday Optimizer logo](documentation/logo-screen.png)

## Colors scheme

The [Rich python library](https://rich.readthedocs.io/en/stable/introduction.html) was utilized to craft a vibrant and engaging user interface. Colors were incorporated to aid in localization during program execution on the CLI, as well as to provide visual feedback.

By establishing a consistent color scheme throughout the application, users can predict what to expect. This predictability enhances usability and overall user experience.

### Green

All feedback of choices and results are printed in green. The color green is commonly linked with positivity, success, and affirmation. By employing green for feedback messages, the application provides a clear and unmistakable signal of valid choices made by the user. This assists users in distinguishing between successful interactions and potential errors or warnings with ease.
![Green feedback](documentation/green-feedback.png)

### Yellow

Yellow was used when listing the states of a country because it is a color that stands out among several white lines in the CLI.
![Yellow listing states](documentation/yellow-states.png)

Yellow was also utilized for feedback indicating that no holidays were present during the selected period, distinguishing it from the green feedback message used when listing the holidays and vacation day suggestions.
![Yellow feedback](documentation/yellow-feedback.png)

### Red

Any input provided by the user that fails validation will result in an 'Error' message printed in red. This provides the user with feedback to pay close attention to their input, as invalid data will prevent them from proceeding with the operations.
![Red warning](documentation/red-feedback.png)

### Cyan

The dates are displayed in cyan, standing out from the rest of the content.
![Cyan dates](documentation/cyan-dates.png)


# Features

## Wait for a keypress

Because of the limitation of the size of the CLI application, I used an input function that waits for the user to press "Enter" before the screen scrolls down and the first prompt comes up.

![Press enter feature](documentation/press-enter.png)

## Autocomplete

## Confirmation after each input

## Clear display of results

## Thank you message