#grading program:
# Score	Grade
# 90~100	A
# 70~89	B
# 60~69	C
# 0~59	D
# others	Invalid score


score = int(raw_input("Enter the score:"))
if 90 <= score < 100:
	print 'A'
elif 70 <= score <= 89:
	print 'B'
elif 60 <= score <= 69:
	print 'C'
elif 0 <= score <= 59:
	print 'D'
else:
	print 'Invalid score.'