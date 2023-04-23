# this program is meant to use regex to detect dates format DD/MM/YYYY
import re


  

dateRegex = re.compile(r'''
(0[0-9]|[1-2][0-9]|3[0-1])\/ #day
(0[1-9]|1[0-2])\/			   #month
([1-2][0-9]{3})			   #year
''',re.VERBOSE)

def valid_date(date):
        matches = dateRegex.findall(date)

        if matches == []:
                return False
        for groups in matches:
                return validDate(groups[0],groups[1],groups[2])

def getValues(date):
        matches = dateRegex.findall(date)
        for groups in matches:
                return groups[0],groups[1],groups[2]
     

def isLeapYear(year):
	intYear = int(year)
	divByFour = intYear%4==0
	divByHundred = intYear%100==0
	divByFourHundred = intYear%400==0
	if (divByHundred) and not (divByFourHundred):
		return False
	return divByFour
def validDate(day,month,year):
	intDay = int(day)
	intMonth = int(month)
	intYear = int(year)
	if((intMonth == 4) or (intMonth == 6) or (intMonth == 9) or (intMonth == 11)):
		if intDay > 30:
			return False
	if (intMonth == 2):
		if isLeapYear(year):
			if intDay > 29:
				return False
		else:
			if intDay > 28:
				return False
	return True
