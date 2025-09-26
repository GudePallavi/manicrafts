n=int(input("Enter a number:"))
length=len(str(n))
sum=0
temp=n
while(n>0):
	rem=n%10
	sum+=rem**length
	n=n//10
if(temp==sum):
	print(f"{temp} is a Armstrong")
else:
	print(f"{temp} is not a Armstrong")
	

	