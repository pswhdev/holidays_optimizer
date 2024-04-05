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

### Development

I began by developing functions to collect user input for the country and state (if available).

Since I intended to utilize the holidays library to retrieve holidays based on the country input, ensuring accurate results required obtaining the country abbreviation in accordance with the ISO 3166-1 alpha-2 code, as outlined in the [library's documentation](https://pypi.org/project/holidays/).

To enhance user-friendliness and enable input of country names, I created a separate file containing a dictionary. This dictionary mapped country names to their respective abbreviations. Additionally, within the same file, I established a second dictionary called 'database,' which listed countries with available lists of states within the library to be used by the functions on the program.

To prevent mistypes and improve the user experience, I integrated the autocomplete feature from the [prompt_toolkit](https://python-prompt-toolkit.readthedocs.io/en/master/) library when prompting for the country's name.

I relied on the flowchart as my guide throughout the development process, ensuring that each function worked properly and that validations were effectively implemented at every step.

After implementing the functions to obtain the country, state, and dates from the user, I decided to incorporate an additional confirmation step after each input. This way, users wouldn't need to restart the program in case of accidental input errors.

After some consideration, I also decided not to include the previously planned prompts for the number of days and the option for month or period. These data wouldn't contribute significantly to achieving the desired result.

With these changes during the process the resulting flowchart was slightly changed.

![Holiday Optimizer final FlowChart](documentation/flowchart-final.png) 