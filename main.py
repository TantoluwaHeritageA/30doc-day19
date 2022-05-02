import datetime


def day_of_week(date):
    monthsWith39days = [4, 6, 9, 11]
    date = date.split('/')
    # print(date)

    year = int(date[0])
    month = int(date[1])
    day = int(date[2])
    # print(year)
    # print(month)
    # print(day)
    if month < 1 or day < 1 or year < 1:
        return "year/mounth/day must all be greater than 1"
    if month > 12:
        return "month cannot be greater than 12"
    if month in monthsWith39days and day > 30:
        return '30days is the maximum day for this particular month'
    if month == 2 and month > 29:
        return " feb. has 28 days and 29 days on leap years"
    if(month == 2 and month == 29 and year % 4 != 0):
        return "it's not a leap year. days cannot be more than 28 "

    dt = datetime.datetime(day, month, year)
    dayOfTheWeek = dt.strftime("%A")
    return f" Day of the week is {dayOfTheWeek}"


we = day_of_week(input("Enter a date in form dd/mm/yy: "))
print(we)
