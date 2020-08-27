import threading
import ttsMp3
import sys

time_end=0

def exit_timer():
    global time_end
    time_end += 1
    timer = threading.Timer(1, exit_timer)
    timer.start()
    
    if time_end==120:
        timer.cancel()
        ttsMp3.pysound("./infoSound/exitapp.wav")