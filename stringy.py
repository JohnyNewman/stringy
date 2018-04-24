def stringy(size):
	size = int(size)
	if size == 0:
		return ""
	elif size == 1:
		return "1"
	else:
		string= "10"
		if size%2 == 0:
			iter= int(size/2)
			for i in range(1, iter):
				string = string + "10"
			return string
		else:
			iter= int((size-1)/2)
			for i in range(1, iter):
				string = string + "10"
			return string + "1"
print(stringy(1))
