
def Leap_year1(year):
    if (year<0) :
        str="Year cannot be negative"
        return str
    if (year % 400 == 0) and (year % 100 == 0):
        return True
    elif (year % 4 ==0) and (year % 100 != 0):
        return True
    else:
        return False

