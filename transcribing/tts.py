import requests
import pyglet
import time
import pygame

url = "https://kakaoi-newtone-openapi.kakao.com/v1/synthesize"
header = {
    "Content-Type" : "application/xml",
    "Authorization" : "KakaoAK a1e32e1055d027ca475ecce06329971a"
}
data = "<speak> 지옥에서 다시 돌아온 우분투 </speak>"



def play_and_stop(sound):
    from threading import Timer
    player = sound.play()
    t = Timer(player.source.duration, player.next_source)
    t.start()


response = requests.post(url, headers=header, data=data.encode('utf-8'))
rescode = response.status_code
print("Server response code : " + str(rescode))
if rescode == 200:
    with open("./result.wav", 'wb') as f:
        f.write(response.content)
        print("Saved audio file!")
       # sound = pyglet.media.load("./result.mp3",streaming=False)
       # play_and_stop(sound)
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("result.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
         time.sleep(0.1)       
else:
    print("Not valid request!")

