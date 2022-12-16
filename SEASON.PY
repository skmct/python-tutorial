# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

month=input("enter the month:")
day=int(input("enter the day:"))
if month in('september','october', 'november'):
    print("autum")
elif month in('decmber','january', 'february'):
    print("winter")   
elif month in('march','april', 'may'):
    print("spring")
elif    month in('june','july', 'august'):
    print("summer")
else:
    print("default")        