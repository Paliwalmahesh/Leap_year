
def Leap_year1(year):
    if (year<0) :
        str="Year cannot be negative"
        return str
    if (year % 4 ==0):
        return True
    else:
        return False

