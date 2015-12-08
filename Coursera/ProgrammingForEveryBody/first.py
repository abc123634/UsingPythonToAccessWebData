largest = None
smallest = None
while True:
	num = raw_input("Enter a number: ")
	if num == "done": 
		print "Maximum is", largest
		print "Minimum is", smallest
		break
	else:
		try:
			num = int(num)

			if largest is None and smallest is None:
				largest = num
				smallest = num

			if num > largest:
				largest = num
			if num < smallest:
				smallest = num
		except:
			print "Invalid input"