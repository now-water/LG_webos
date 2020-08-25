import os
import sys
import urllib.request
import pygame
import time


def tts(item):
    client_id = "srg3lxmwur"
    client_secret = "RiAtThkg0HjNOFT1a5DEUPbSkyycNTICeZuYHnLh"

    encText = urllib.parse.quote("We found the item! The" + item + "is right on your direction.")#tts item
    data = "speaker=clara&speed=0&text=" + encText

    url = "https://naveropenapi.apigw.ntruss.com/voice/v1/tts"
    request = urllib.request.Request(url)
    request.add_header("X-NCP-APIGW-API-KEY-ID",client_id)
    request.add_header("X-NCP-APIGW-API-KEY",client_secret)
    response = urllib.request.urlopen(request, data=data.encode('utf-8'))
    rescode = response.getcode()

    if(rescode==200):
        print("[INFO] : naver TTS")
        response_body = response.read()
        with open('result.mp3', 'wb') as f:
            f.write(response_body)
    else:
        print("Error Code:" + rescode)
    
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("result.mp3")
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)  


    time.sleep(0.5)