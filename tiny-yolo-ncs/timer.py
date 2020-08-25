import threading
import ttsMp3
import sys

end=False

def timer(second=5):
    global end
    
    if end:
        ttsMp3.tts("./infoSound/exitapp.wav")
        sys.exit(0)
        
    threading.Timer(second,timer,[second]).start()
    
    
timer(10)