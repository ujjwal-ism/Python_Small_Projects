import time
import webbrowser

count = 0

print ("This progam started on  " + time.ctime())
while count < 3 :
	time.sleep(10)
	webbrowser.open("https://www.youtube.com/watch?v=RnBT9uUYb1w")
	count = count + 1