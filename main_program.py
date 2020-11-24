import speech_recognition as sr
import pyttsx3
from datetime import date, datetime
import time
import playsound
import os
from gtts import gTTS
import webbrowser
import wikipedia
import requests, json
import googletrans
from googletrans import Translator
#initial to let robot can hear and speak
robot_mouth = pyttsx3.init()
robot_ear = sr.Recognizer()
r =sr.Recognizer()
#create function for robot can speak
def speakVi(robot_brain):
    output = gTTS(robot_brain,lang="vi", slow=False)
    output.save("output.mp3")
    playsound.playsound('output.mp3')
    os.remove('output.mp3')
#create function for robot can listen
def listen():
    with sr.Microphone() as mic:
        r.adjust_for_ambient_noise(mic)# reduce noise
        audio = r.listen(mic, timeout=4, phrase_time_limit=4)
        try:
            you = r.recognize_google(audio, language="vi-VI").lower()
            print("Bạn: {}".format(you))
        except:
            robot_brain = "Mình chưa hiểu bạn nói gì"
            speakVi(robot_brain)
    return you
#create function to translate English into Vietnamese
def translateEtoV(key):
    translator = Translator()
    trans = (translator.translate(key, src='en',dest='vi')).text
    return trans
# getting the weater information each city 
def weather(city_name):
    api_key = "f720ec4ecd191873afc1b7fe3f407ec4"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url+ "appid="+ api_key+ "&q="+ city_name 
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = int(y["temp"] - 273.15) #k = C+273.15
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        weather_description = translateEtoV(weather_description)
        meomeo_brain = "Thời tiết thành phố "+city_name + " Hiện đang có " + str(weather_description) + " nhiệt độ là " + str(current_temperature)+ " độ C " + "độ ẩm là "+ str(current_humidity) +" %"
    else:
        meomeo_brain = "Không tìm thấy tên thành phố"
    return meomeo_brain
#initial robot's saying sentence hello
h = datetime.now()
time = int(h.strftime("%H"))
if (1<=time<=10):
    robot_brain = "Chào Đăng, chúc bạn buổi sáng tốt lành"
elif (10<time<=17):
    robot_brain = "Chào Đăng, chúc bạn buổi trưa vui vẻ"
elif (17<time<=22):
    robot_brain = "Chào Đăng, chúc buổi tối tràn đầy năng lượng"
else:
    robot_brain = "Chào Đăng, sắp đến giờ ngủ rồi, bạn có cần gì không"
speakVi(robot_brain)
#Initial things which robot is able to do
while True:
    r =sr.Recognizer()
    you = listen()
    #understanding
    if "cảm ơn" in you:
        robot_brain = "Mình có thể giúp gì cho bạn"
    elif "khỏe không" in you:
        robot_brain = "Mình khỏe, hihi, mình có thể làm việc liên tục luôn"
    elif "ngày mấy" in you:
        today = date.today()
        robot_brain = today.strftime("Hôm nay là ngày %d tháng %m năm %Y")
    elif "sinh nhật" in you:
        robot_brain ="Sinh nhật của bạn là ngày 9 tháng 1"
    elif "mấy giờ" in you:
        now = datetime.now()
        robot_brain = now.strftime("Lúc này là: %H gi{y} %M phút").format(y='ờ')
    elif "thời tiết hôm nay" in you:
        robot_brain = "Bạn muốn xem thời tiết ở thành phố nào"
        r =sr.Recognizer()
        you = listen()
        print("Alice : Thời tiết ở thành phố "+ you)
        robot_brain = weather(you)
        print("Alice: ",robot_brain)
        speakVi(robot_brain)
        continue
    elif "mở youtube" in you:
        webbrowser.open('https://www.youtube.com/',new=1)
        robot_brain = "ok! youtube đang được mở"
        print("Alice: ",robot_brain)
        speakVi(robot_brain)
        break
    elif "nhạc edm" in you:
        webbrowser.open('https://www.youtube.com/watch?v=C3UJBMAy5xE',new=1)
        robot_brain = "ok!nhạc edm đang được mở"
        print("Alice: ",robot_brain)
        speakVi(robot_brain)
        break
    elif "facebook" in you:
        webbrowser.open('https://www.facebook.com/',new=1)
        robot_brain = "ok! facebook đang được mở"
        print("Alice: ",robot_brain)
        speakVi(robot_brain)
        break
    elif "gmail" in you:
        webbrowser.open('https://mail.google.com/mail/u/1/#inbox',new=1)
        robot_brain = "ok! gmail đang được mở"
        print(robot_brain)
        speakVi(robot_brain)
        break
    elif "wikipedia" in you:
        you = listen()
        wikipedia.set_lang("vi")
        robot_brain = wikipedia.summary(you)
        speakVi(robot_brain)
        robot_brain = "đó là những thứ mình tìm được"
        speakVi(robot_brain)
        continue
    elif "tạm biệt" in you:
        robot_brain = "Chào Đăng"
        print("Alice: ",robot_brain)
        speakVi(robot_brain)
        break
    else:
        robot_brain = "Mình chưa được học những thứ này"    
    
    #respond
    print("Alice: ",robot_brain)
    speakVi(robot_brain)
