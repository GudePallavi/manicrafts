s=input("Enter a word:")
if s==s[::-1]:
	print(f"given {s} is palindrome")
else:
	print(f"given {s} is not a palindrome")