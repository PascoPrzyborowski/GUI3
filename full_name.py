import sys
import getopt


def full_name():
	first_name = None
	last_name = None
	help_s = None
	argv = sys.argv[1:]

	try:
		opts, args = getopt.getopt(argv, "f:l:h:")
	
	except:
		print("Error")

	for opt, arg in opts:
		if opt in ['-f']:
			first_name = arg
		elif opt in ['-l']:
			last_name = arg
		elif opt in ['-h']:
			help_s = arg
	
	

	print( first_name +" " + last_name)

full_name()	
