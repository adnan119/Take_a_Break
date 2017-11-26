import webbrowser
import time


total_breaks=3
break_count=0
time_to_wait=10

print("this program started on " + time.ctime())
while break_count < total_breaks:
    time.sleep(time_to_wait)
    webbrowser.open("https://docs.python.org/2/library/webbrowser.html")
    break_count = break_count+1
