from enum import Enum

r00 = 1.64490
r05 = 1.64560
r10 = 1.64790
r15 = 1.65180
r20 = 1.65780
r25 = 1.66460
r30 = 1.67380
r35 = 1.68520
r40 = 1.69920
r45 = 1.71630
r50 = 1.73710
r55 = 1.76210
r60 = 1.79150
r65 = 1.82510
r70 = 1.86250
r75 = 1.90340
r80 = 1.94720
r85 = 1.99360
r90 = 2.04240
r95 = 2.09320
r100 = 2.1460

def getCoefficient(r):
	if (r == 0.00):
		return r00
	elif (r == 0.05):
		return r05
	elif (r == 0.10):
		return r10
	elif (r == 0.15):
		return r15
	elif (r == 0.20):
		return r20
	elif (r == 0.25):
		return r25
	elif (r == 0.30):
		return r30
	elif (r == 0.35):
		return r35
	elif (r == 0.40):
		return r40
	elif (r == 0.45):
		return r45
	elif (r == 0.50):
		return r50
	elif (r == 0.55):
		return r55
	elif (r == 0.60):
		return r60
	elif (r == 0.65):
		return r65
	elif (r == 0.70):
		return r70
	elif (r == 0.75):
		return r75
	elif (r == 0.80):
		return r80
	elif (r == 0.85):
		return r85
	elif (r == 0.90):
		return r90
	elif (r == 0.95):
		return r95
	elif (r == 1.00):
		return r100
	else:
		return 0

def linearInterpolation(r):
	if (getCoefficient(r) == 0):
		first = 0
		second = 0
		temp = 0

		x1 = 0
		x2 = 0

		if (r > 0 and r < 0.05):
			first = r00
			second = r05
			temp = 0
		elif (r > 0.05 and r < 0.10):
			first = r05
			second = r10
			temp = 0.05
		elif (r > 0.10 and r < 0.15):
			first = r10
			second = r15
			temp = 0.10
		elif (r > 0.15 and r < 0.20):
			first = r15
			second = r20
			temp = 0.15
		elif (r > 0.20 and r < 0.25):
			first = r20
			second = r25
			temp = 0.20
		elif (r > 0.25 and r < 0.30):
			first = r25
			second = r30
			temp = 0.25
		elif (r > 0.30 and r < 0.35):
			first = r30
			second = r35
			temp = 0.30
		elif (r > 0.35 and r < 0.40):
			first = r35
			second = r40
			temp = 0.35
		elif (r > 0.40 and r < 0.45):
			first = r40
			second = r45
			temp = 0.40
		elif (r > 0.45 and r < 0.50):
			first = r45
			second = r50
			temp = 0.45
		elif (r > 0.50 and r < 0.55):
			first = r50
			second = r55
			temp = 0.50
		elif (r > 0.55 and r < 0.60):
			first = r55
			second = r60
			temp = 0.55
		elif (r > 0.60 and r < 0.65):
			first = r60
			second = r65
			temp = 0.60
		elif (r > 0.65 and r < 0.70):
			first = r65
			second = r70
			temp = 0.65
		elif (r > 0.70 and r < 0.75):
			first = r70
			second = r75
			temp = 0.70
		elif (r > 0.75 and r < 0.80):
			first = r75
			second = r80
			temp = 0.75
		elif (r > 0.80 and r < 0.85):
			first = r80
			second = r85
			temp = 0.80
		elif (r > 0.85 and r < 0.90):
			first = r85
			second = r90
			temp = 0.85
		elif (r > 0.90 and r < 0.95):
			first = r90
			second = r95
			temp = 0.90
		elif (r > 0.95 and r < 1.00):
			first = r95
			second = r100
			temp = 0.95

		x1 = r - temp
		x2 = 0.05 - x1

		return (x2 / 0.05) * first + (x1 / 0.05) * second
	else:
		return getCoefficient(r)
