year=input("enter the year\n")
if(isinstance(year,int)):
if(year%4==0):
if((year%100!=0)or(year%400==0)):
print(year,"is a leap year")
else:
print(year,"is not a leap year")
else:
print(year,"is not a leap year")
else:
print("invalid input")
