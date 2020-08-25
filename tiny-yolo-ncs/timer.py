import threading
import ttsMp3
import sys

time_end=0

def exit_timer(state):
    global time_end
    time_end += 1
    timer = threading.Timer(1, exit_timer)
    timer.start()
    
    if(state=="close"):
        timer.cancel()
        ttsMp3.pysound("./infoSound/closetheapp.wav")
    
    else:
        if time_end==60:
            timer.cancel()
            ttsMp3.pysound("./infoSound/exitapp.wav")