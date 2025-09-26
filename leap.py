y=int(input("Enter a year:"))
if((y%4==0 and y%100!=0) or y%400==0):
	print(f"given {y} is a leap year")
else:
	print(f"given {y} is not a leap year")