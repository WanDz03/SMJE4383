percent_float = float(input("What is your percentage: "))

if 90 <= percent_float <= 100:
	print("You received an A+")
elif 80 <= percent_float < 90:
	print("You received an A")
elif 75 <= percent_float < 80:
	print("You received an A-")
elif 70 <= percent_float < 75:
	print("You received a B+")
elif 65 <= percent_float < 70:
	print("You received a B")
elif 60 <= percent_float < 65:
	print("You received a B-")
elif 55 <= percent_float < 60:
	print("You received a C+")
elif 50 <= percent_float < 55:
	print("You received a C")
elif 45 <= percent_float < 50:
	print("You received a C-")
elif 40 <= percent_float < 45:
	print("You received a D+")
else: 
	print("You failed.. Too bad")
		
