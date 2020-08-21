import requests

url = "https://kakaoi-newtone-openapi.kakao.com/v1/synthesize"
header = {
    "Content-Type" : "application/xml",
    "Authorization" : "KakaoAK a1e32e1055d027ca475ecce06329971a"
}
data = "<speak> 지옥에서 다시 돌아온 우분투 </speak>"

response = requests.post(url, headers=header, data=data.encode('utf-8'))
rescode = response.status_code
print("Server response code : " + str(rescode))
if rescode == 200:
    with open("./result.mp3", 'wb') as f:
        f.write(response.content)
        print("Saved audio file!")
else:
    print("Not valid request!")