#############################################################################
#
# icu.py                                 
#
# Description:
#  
# To use this program, enter: icu.sh.
# icu.sh will create the file icu.data using a curl command to get a dataset from
# data.ontario.ca and then it will call this program

#
# History:
#
#       2022.03.30	Initial implementation. (BLM)
#
# Examples:
#
#  See icu.sh
#
#############################################################################

# Using readlines() to load icu.data into Lines
file1 = open('icu.data', 'r')
Lines = file1.readlines()

# Go through all the data in Lines. Strip off the blanks, then parse the line
# using .split. From there, determine the stats concerning adult and ICU beds

for line in Lines:
    trimmed_line = line.strip()
    temp = trimmed_line.split(",")
    theDate = temp[0]
    adultICUbedsInUse = temp[4]
    adultICUbedsTotal = temp[5]
    childICUbedsInUse = temp[9]
    childICUbedsTotal = temp[10]
    adultICUbedpercent =   round(float(temp[4]) / float(temp[5]) * 100, 1)
    childICUbedpercent =   round(float(temp[9]) / float(temp[10]) * 100, 1)
    
    # Output the results
    output =  "Ontario ICU Data: Adult ICU beds in use " + adultICUbedsInUse + " (" + str(adultICUbedpercent) + "%), "
    output =  output + "child ICU beds in use " + childICUbedsInUse + " (" + str(childICUbedpercent) + "%)"
    output =  output + " for " + theDate.strip(' " " ')
    
    print output
 

