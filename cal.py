def cal():
	a = int(input("""

		Pick from the following and enter a valied methodical operator:
							 
		>> """))

	if a == str(a):
		print("this is a string:")
	elif a == int(a):
		print("this is a int")
	else:
		print(" program will close in 5 seconds ")
		close()

cal()
