for line in open('dining.csv'):
	split = line.split(',')

	if len(split[1]) == 7:
		time = "0" + split[1]
	else:
		time = split[1]

	print split[0] + "," + time + "," + split[2]

for line in open('firestone.csv'):
	split = line.split(',')

	date = int((split[0])[3:5])
	
	if (date > 8 and date < 16):

		if (date == 9):
			day = "Sunday"
		if (date == 10):
			day = "Monday"
		if (date == 11):
			day = "Tuesday"
		if (date == 12):
			day = "Wednesday"
		if (date == 13):
			day = "Thursday"
		if (date == 14):
			day = "Friday"
		if (date == 15):
			day = "Saturday"

		hour = int(split[1][0:2])
		if (hour < 12):
			if (hour == 0):
				time = "12" + split[1][2:8] + " AM"
			else:
				time = split[1] + " AM"
		else:
			if (hour == 12):
				time = split[1] + " PM"
			else:
				time = str(int(split[1][0:2]) - 12) + split[1][2:8] + " PM"
		
		print "Firestone Library," + time + "," + day