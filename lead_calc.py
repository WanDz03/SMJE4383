#1. Take the number of points one team is ahead
points_str = input("Enter the lead in points: ")
points_remain_int = int(points_str)

#2. Subtract 3
lead_calc_float = float(points_remain_int - 3)
has_ball_str = (input('Does the lead team have a ball? (Yes/No): '))

#3. Add a half point if the team that is ahead has the ball
# Subtract a half point if the team that is ahead does not have the ball
if has_ball_str == 'Yes':
	lead_calc_float = lead_calc_float + 0.5
else:
	lead_calc_float = lead_calc_float - 0.5

# Numbers less than 0 becomes 0	
if lead_calc_float < 0:
	lead_calc_float = 0

#4. Square the floating number	
lead_calc_float = lead_calc_float** 2

#5. If the result is greater than the seconds remaining,
# The lead is safe
seconds_remain_int = int(input('Enter the remaining seconds: '))

if lead_calc_float > seconds_remain_int:
	print("Lead is safe")
else:
	print("Lead is not safe")
