import simpleaudio as sa
import time

def pysound(item):
    wave_obj = sa.WaveObject.from_wave_file(item)
    play_obj = wave_obj.play()
    play_obj.wait_done()
    
    time.sleep(0.8)
