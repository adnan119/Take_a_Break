import webbrowser
import time


total_breaks=3
break_count=0

while break_count < total_breaks:

    time_to_wait=10
    time.sleep(time_to_wait)
    webbrowser.open("https://docs.python.org/2/library/webbrowser.html")
    break_count = break_count+1
