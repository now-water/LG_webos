from azure.cognitiveservices.speech import AudioDataStream, SpeechConfig, SpeechSynthesizer, SpeechSynthesisOutputFormat
from azure.cognitiveservices.speech.audio import AudioOutputConfig

import requests
import pyglet
import time
import pygame

def tts(item, res):
    speech_config = SpeechConfig(subscription="bc0912f626b44d5a8bb00e4497644fa4", region="westus")
    audio_config = AudioOutputConfig(filename="./result.wav")

    synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    appendString = ""
    if res == "OK":
        appendString = "is in direction you're looking"
    else:
        appendString = "is not in direction you're looking"
    result = synthesizer.speak_text_async(item + appendString).get()
    stream = AudioDataStream(result)
    stream.save_to_wav_file("./result.mp3")

    from threading import Timer
    player = sound.play()
    t = Timer(player.source.duration, player.next_source)
    t.start()

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("result.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)       
