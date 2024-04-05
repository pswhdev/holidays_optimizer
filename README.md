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
To help with planning my project, I used [Lucidchart](https://www.lucidchart.com/pages/) to produce a flowchart.

Initially I had planned

![Holiday Optimizer initial FlowChart](documentation/initial-flowchart.png)  




