import sys
import requests

def stt:
    client_id = "jklurq0vrx"
    client_secret = "d7Yl0vV5ipjjsl7IPhkRTQX8TmW7dhPFNUJFcPGe"
    lang = "Eng" # 언어 코드 ( Kor, Jpn, Eng, Chn )
    url = "https://naveropenapi.apigw.ntruss.com/recog/v1/stt?lang=" + lang
    data = open('음성 파일 경로', 'rb')
    headers = {
        "X-NCP-APIGW-API-KEY-ID": client_id,
        "X-NCP-APIGW-API-KEY": client_secret,
        "Content-Type": "application/octet-stream"
    }
    response = requests.post(url,  data=data, headers=headers)
    rescode = response.status_code
    if(rescode == 200):
        print (response.text)
    else:
        print("Error : " + response.text)

