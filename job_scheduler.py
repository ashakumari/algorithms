# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
import threading
import time

def schedule_job(f, n):
	threadObj = threading.Thread(target=do_the_job, args=[f, n])
	threadObj.start()

def do_the_job(f, n):
	# Change this for loop to "while 1" to have an endlessly recurring job scheduler
	for i in range(5):
		time.sleep(n/1000)
		f()

def sum(a,b):
	print (time.ctime())
	print (a + b)

def say_hi():
	print("Hi! The time is " + time.ctime())


schedule_job(lambda: sum(15,15), 5000)
schedule_job(lambda: say_hi(), 2000)




