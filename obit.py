#############################################################################
#
# obit.py                                 
#
# Description:
#  
# This program scrapes the SaltWire web site (Cape Breton Post) for obituaries
# listed there, and writes it out into HTML
#
# History:
#
#       2022.03.30	Initial implementation. (BLM)
#
# Examples:
#
#       To call the program, enter: python obit.py <yyyy month_full dd>
#       If you pass no parameters, it will go with todays date. 
#       If you pass parameters, you need to pass three:
#           e.g. 2022 december 25
#
#############################################################################

import requests						# Needed to get the web page
from bs4 import BeautifulSoup		# Needed to parse the web page
import datetime						# Needed to get current date, time
import sys							# needed to process input parameters

# Process the input parameters. Determine the year, month and date of the obt
# that you want

if len(sys.argv) == 4:
	theyear = sys.argv[1]
	themonth = sys.argv[2]
	theday = sys.argv[3]

elif len(sys.argv) == 1:
    x = datetime.datetime.now()
    theyear = x.strftime("%Y")
    themonth = x.strftime("%B")
    theday = x.strftime("%d")

else:
	print "to call this program, enter: python obit.py <yyyy month_full dd>"
	sys.exit()
	
html = 1

# Create the URI to get the obit for the date in question.

URIdate = theyear + "/" + themonth + "/" + theday + "/" 
URI = "https://www.saltwire.com/cape-breton/obituaries/" + URIdate

# Get the web page and run it through Beautiful Soup

page = requests.get(URI)
soup = BeautifulSoup(page.content, "html.parser")

# All the data for this web page are stored in DIV with class covid-data-block

results = soup.find_all('div', class_="sw-obit-list__item")

# Go through the results. Strip out the extra blanks and blank lines.
# 1st and 7th string contain the information you want. Most of what is in the list 
# in the final_details is blank

print "<h2>" + "Obituaries for "  + themonth + " "  + theday + ", " + theyear + "</h2>"
for result in results:
    # name = result.find("h3").text.strip()
    details = result.find("div").text.strip()
    details  = details.encode('ascii', 'ignore')
    details = details.replace("\n", "")
    final_details = (details.split("     "))
    
    print "<p>", "<strong>", final_details[0], "</strong>", final_details[6], "..."


    



