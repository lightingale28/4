"""A year is a leap year if it is divisible by 4, except that years divisible by 100 are not leap years unless they are also divisible by 400.
Write a program that asks the user for a year and prints out whether it is a leap year or not."""
x=int(input("please enter your year "))
if x%400==0:
    print("leap year")
elif x%100==0:
    print("not a leap year")
elif x%4==0:
    print("leap year")
else:
    print("not a leap year")