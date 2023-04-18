import datetime
import time

while(True):
	print(f'Started executing at: {datetime.datetime.now()}')
	with open("expo_parser.py") as f:
	    exec(f.read())
	print(f'Finished executing at: {datetime.datetime.now()}\nStarting sleep.\n')
	# Sleep 5 min
	# time.sleep(300)

	# Sleep 30 min
	time.sleep(1800)
