import speech_recognition as sr
import pyttsx3
from datetime import date, datetime
import time
import playsound
import os
from gtts import gTTS
import webbrowser
import wikipedia
robot_mouth = pyttsx3.init()
#set up voice
""" RATE"""
rate = robot_mouth.getProperty('rate')   # getting details of current speaking rate               
robot_mouth.setProperty('rate', 150)     # setting up new voice rate
"""VOLUME"""
volume = robot_mouth.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
robot_mouth.setProperty('volume',1)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = robot_mouth.getProperty('voices')       #getting details of current voice
robot_mouth.setProperty('voice', voices[1].id)  #changing index, changes voices. 1 for female
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
output = gTTS(robot_brain,lang="vi", slow=False)
output.save("output.mp3")
playsound.playsound('output.mp3')
os.remove('output.mp3')
#create searching informatioin function by wikipedia
#listen what you're saying
while True:
    r =sr.Recognizer()
    with sr.Microphone() as mic:
        r.adjust_for_ambient_noise(mic)# reduce noise
        audio = r.listen(mic, timeout=4, phrase_time_limit=4)
        try:
            you = r.recognize_google(audio, language="vi-VI").lower()
            print("Bạn: {}".format(you))
        except:
            robot_brain = "Mình chưa hiểu bạn nói gì"
            output = gTTS(robot_brain,lang="vi", slow=False)
            output.save("output.mp3")
            playsound.playsound('output.mp3')
            os.remove('output.mp3')
            continue
    #understanding
        if "cảm ơn" in you:
            robot_brain = "Mình có thể giúp gì cho bạn"
        elif "khỏe không" in you:
            robot_brain = "Mình khỏe, hihi, mình có thể làm việc liên tục luôn"
        elif "hôm nay" in you:
            today = date.today()
            robot_brain = today.strftime("Hôm nay là ngày %d tháng %m năm %Y")
        elif "mấy giờ" in you:
            now = datetime.now()
            robot_brain = now.strftime("Lúc này là: %H gi{y} %M phút").format(y='ờ')
        elif "mở youtube" in you:
            webbrowser.open('https://www.youtube.com/',new=1)
            robot_brain = "ok! youtube đang được mở"
            print(robot_brain)
            output = gTTS(robot_brain,lang="vi", slow=False)
            output.save("output.mp3")
            playsound.playsound('output.mp3')
            os.remove('output.mp3')
            break
        elif "nhạc edm" in you:
            webbrowser.open('https://www.youtube.com/watch?v=C3UJBMAy5xE',new=1)
            robot_brain = "ok!nhạc edm đang được mở"
            print(robot_brain)
            output = gTTS(robot_brain,lang="vi", slow=False)
            output.save("output.mp3")
            playsound.playsound('output.mp3')
            os.remove('output.mp3')
            break
        elif "facebook" in you:
            webbrowser.open('https://www.facebook.com/',new=1)
            robot_brain = "ok! facebook đang được mở"
            print(robot_brain)
            output = gTTS(robot_brain,lang="vi", slow=False)
            output.save("output.mp3")
            playsound.playsound('output.mp3')
            os.remove('output.mp3')
            break
        elif "gmail" in you:
            webbrowser.open('https://mail.google.com/mail/u/1/#inbox',new=1)
            robot_brain = "ok! gmail đang được mở"
            print(robot_brain)
            output = gTTS(robot_brain,lang="vi", slow=False)
            output.save("output.mp3")
            playsound.playsound('output.mp3')
            os.remove('output.mp3')
            break
        elif "wikipedia" in you:
            r =sr.Recognizer()
            with sr.Microphone() as mic:
                print("Wikipedia:...")
                audio = r.listen(mic, timeout=4, phrase_time_limit=4)
                try:
                    wiki = r.recognize_google(audio, language="vi-VI").lower()
                except:
                    wiki = "sorry, mình không tìm thấy thông tin "
                wikipedia.set_lang("vi")
                wiki = wikipedia.summary(wiki)
                print(wiki)
                robot_brain = wiki
                rate = robot_mouth.getProperty('rate')   # getting details of current speaking rate               
                robot_mouth.setProperty('rate', 350) 
                output = gTTS(robot_brain,lang="vi", slow=False)
                output.save("output.mp3")
                playsound.playsound('output.mp3')
                os.remove('output.mp3')
                robot_brain = "đó là những thông tin mình tìm được"
                continue

        elif "tạm biệt" in you:
            robot_brain = "Chào Đăng"
            print("Alice: ",robot_brain)
            output = gTTS(robot_brain,lang="vi", slow=False)
            output.save("output.mp3")
            playsound.playsound('output.mp3')
            os.remove('output.mp3')
            break
        else:
            robot_brain = "Mình chưa được học những thứ này"
    
    #respond
        output = gTTS(robot_brain,lang="vi", slow=False)
        output.save("output.mp3")
        playsound.playsound('output.mp3')
        os.remove('output.mp3')
