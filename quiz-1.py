# author CJP 10/19/2021

year = int(input("Enter the year of the date: "))
month = int(input("Enter the month of the date (January and February are counted as months 13 and 14 of the previous year): "))
day_of_month = int(input("Enter the day of the date: "))

j = year // 100
k = year % 100


day = ((day_of_month + ((26 * (month + 1)) // 10) + k + (k // 4) + (j // 4) + (5 * j)) % 7)

if day < 1:
    print("It is Saturday")
elif day < 2:
    print("It is Sunday")
elif day < 3:
    print("It is Monday")
elif day < 4:
    print("It is Tuesday")
elif day < 5:
    print("It is Wednesday")
elif day < 6:
    print("It is Thursday")
else:
    print("It is Friday")
