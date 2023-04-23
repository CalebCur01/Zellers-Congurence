import math
import dateValidation as dv
    
def main():
    days = ["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]

    while True:
        date = input("Enter a date (DD/MM/YYYY):\n")
        if dv.valid_date(date):
            day,month,year = dv.getValues(date)
            break
    dayOfWeek = findDay(int(day),int(month),int(year))
    print("The day of the week for {} is {}".format(date,days[dayOfWeek]))
    



def findDay(day, month, year):
    if month == 1:
        year = year-1
        month = 13
    if month == 2:
        year = year-1
        month = 12

    cent_year = year%100
    zero_year = math.floor(year/100)
    
    dayOfWeek = (day+math.floor((13*(month+1))/5) + cent_year + math.floor(cent_year/4) + math.floor(zero_year/4)- 2*zero_year)%7

    return dayOfWeek

if __name__ == "__main__":
    main()


