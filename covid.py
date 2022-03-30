#############################################################################
#
# covid.py                                 
#
# Description:
#  
#	This program scrapes the Ontario COVID web site and extracts out key 
#   information.
#
# History:
#
#       2022.03.25	Initial implementation. (BLM)
#
# Examples:
#
#       To call the program, enter: python covid19.py
#
#############################################################################

import requests						# Needed to get the web page
from bs4 import BeautifulSoup		# Needed to parse the web page
import datetime						# Needed to get current date, time

# Strings needed for the final output string

output = "Ontario COVID data:"
currentTime = datetime.datetime.now()

# Get the web page and run it through Beautiful Soup

URL = "https://covid-19.ontario.ca/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

# If you need to test the code, use this statement instead
# soup = BeautifulSoup(open("covid-19.ontario.ca.html"), "html.parser")


# All the data for this web page are stored in DIV with class covid-data-block

results = soup.find_all('div', class_="covid-data-block")

# Go through the results, find data on ICU, cases, and hospitalization, and store in 
# in title and data. Then append that to the variable output
for result in results:
    title = result.find("p", class_="covid-data-block__title").text.strip()
    data = result.find("p", class_="covid-data-block__number").text.strip()
    if (title.find("Hospitalized") > -1): output = output + " " + title + " " + data + ","
    if (title.find("ICU") > -1): output = output + " " + title + " " + data + ","
    if (title.find("cases") > -1): output = output + " " + title + " " + data + " "
    
# Add the data and time to output and then write it out.
    
output = output + "for " + currentTime.strftime("%c")
print output


