import speech_recognition as sr
import datetime, wikipedia, os, pyttsx3
import webbrowser as wb
import sys
from PyDictionary import PyDictionary as dic
import requests, json, re, random
import keyboard as ky
import math
import bot
from urllib.request import urlopen
import calendar
import chat_system 
import operator as op
import pyaudio
import time
import defined_functions as f
import data_values as data

#RUN THIS MAIN FILE ON PC START:
import getpass
USER_NAME = getpass.getuser()

def add_to_startup(file_path=""):
    if file_path == "":
        folder_path = os.path.dirname(os.path.realpath(__file__))
        file_path = f"{folder_path}\\{os.path.basename(__file__)}"
    bat_path = r'C:\\Users\\{}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'.format(USER_NAME)
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)
add_to_startup()
#Code Required Variables
temp = f.weather("temperature")
humidity = f.weather("humidity")
pressure = f.weather("pressure")
report = f.weather("report")
ip = f.get_location("ip")
org = f.get_location("org")
city = f.get_location("city")
country = f.get_location("country")
country = f.country_codes[country]
region = f.get_location("region")
#User Changable Variables
def user_choice_for_name(input):
  if data.choice_for_name == "1":
        user_name = data.call_as
        call_as = data.call_as
  elif data.choice_for_name == "2":
        user_name = data.user_name
        call_as = data.user_name
  else:
        user_name = data.user_name
        call_as = data.call_as
  if input == "user_name":
        return user_name
  elif input == "call_as":
        return call_as
  else:
        pass
bot_name = data.bot_name
user_name = user_choice_for_name("user_name")
call_as = user_choice_for_name("call_as")
music_dir = data.music_dir
bot_help_random = [f'How may I have your assistance, {call_as}!',f'How can I help  you, {call_as}!',f"I'm here to help you {call_as}!",f"Always ready to help you, {call_as}!"]
bot_doing_random=[f"I'm simply trying to help you {call_as}!",f"I've been up long helping you {call_as}!",f"Thought for a while, here to help you {call_as}!",f"In your service, {call_as}!"]
#The 10 customizable apps!
app1 = data.app1
app2 = data.app2
app3 = data.app3
app4 = data.app4
app5 = data.app5
app6 = data.app6
app7 = data.app7
app8 = data.app8
app9 = data.app9
app10 = data.app10
#The 10 directories for the customizable apps!
dir1 = data.dir1
dir2 = data.dir2
dir3 = data.dir3
dir4 = data.dir4
dir5 = data.dir5
dir6 = data.dir6
dir7 = data.dir7
dir8 = data.dir8
dir9 = data.dir9
dir10 = data.dir10

#Which type of voice you want for jarvis. (Default set in the code is DAVID)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#If your computer supports more voice types, just change the "voices[0]" in the next line to 1 or 2 or 3, depending on the type and number of
#voices installed in your device!
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMeonStart():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak(f"Good Morning {call_as}! It's {temp} degrees celcius outside. The weather outside has {report}!")
    elif hour>11 and hour< 17:
      speak(f"Good Afternoon {call_as}! It's {temp} degrees celcius outside. The weather outside has {report}!")
    elif hour>17 and hour< 21:
      speak(f"Good Evening {call_as}! It's {temp} degrees celcius outside. The weather outside has {report}!" )
    speak(f"I'm {bot_name}! How may I have your assistance {call_as}?")
def sleeping_time():
      time = datetime.datetime.now().strftime("%H:%M")
      hour = int(time.hour)
      if hour>(data.sleeping_hour-1):
        speak(f"I suggest you should go to sleep {call_as}! It's {time}")
      else:
        pass
def userCommand():
    #user Input is Taken from Microphone and will return output of string!
    r = sr.Recognizer()

    with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
    try:
            print("Recognizing...")
            query = r.recognize_google(audio)
            print(f"User input: {query}\n")
    except Exception as e:
            #print(e)
            return "None"
            
    return query
def get_operation(op):
    return {
        '+' : op.add,
        '-' : op.sub,
        'x' : op.mul,
        'divided' :op.__truediv__,
        'Mod' : op.mod,
        'mod' : op.mod,
        '^' : op.xor,
        }[op]     

if __name__ == '__main__':
    print(f"{bot_name} is successfully working!")
    speak(f"I'm now awake {call_as}!")
    wishMeonStart()
    #This LOGIC is for TASKS based on QUERY
    while True:
      query = userCommand().casefold()
      #Wikipedia Query
      if 'wikipedia' in query:
        speak("Searching Wikipedia...")
        query = query.lstrip("wikipedia")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia...")
        speak(results)
      #Open Specific Sites

      elif 'open youtube' in query or 'open yt' in query:
        wb.open("youtube.com")
        speak("Opening Youtube!")
      elif 'open google' in query:
        wb.open("google.com")
        speak("Opening Google!")
      elif 'open discord' in query:
        wb.open("discord.com/app")
        speak("Opening Discord!")
      elif 'open mail' in query:
        wb.open("mail.google.com")
        speak("Opening Mail!")
      elif 'open github' in query:
        wb.open("github.io")
        speak("Opening GitHub!")
      elif 'open my stuff' in query:
            wb.open('mail.google.com')
            wb.open('discord.com/app')
            wb.open('youtube.com')
            wb.open('classroom.google.com')
            speak('Opened your required websites!')
      elif 'open ' in query:
          if any(a in query for a in app1):
                try:
                  if dir1 == "":
                    speak(f"Sorry {call_as}, there is no directory for {app1[0]}! Try checking the directory in data_values.py")
                  else:
                    os.startfile(dir1)
                    speak(f'Opening {app1[0]}')
                except Exception as FileNotFoundError:
                  speak(f"Sorry {call_as}, the directory for {app1[0]} was not found! Try checking the directory in data_values.py")
                  print(f"No such directory for '{app1[0]}' was not found! Try changing the directory '{dir1}' from `dir1` in `data_values.py` and read the `info.txt` for info!")
          elif any(a in query for a in app2):
                try:
                  if dir2 == "":
                    speak(f"Sorry {call_as}, there is no directory for {app2[0]}! Try checking the directory in data_values.py")
                  else:
                    os.startfile(dir2)
                    speak(f'Opening {app2[0]}')
                except Exception as FileNotFoundError:
                  speak(f"Sorry {call_as}, the directory for {app2[0]} was not found! Try checking the directory in data_values.py")
                  print(f"No such directory for '{app2[0]}' was not found! Try changing the directory '{dir2}' from `dir2` in `data_values.py` and read the `info.txt` for info!")
          
          elif any(a in query for a in app3):
                try:
                  if dir3 == "":
                    speak(f"Sorry {call_as}, there is no directory for {app3[0]}! Try checking the directory in data_values.py")
                  else:
                    os.startfile(dir3)
                    speak(f'Opening {app3[0]}')
                except Exception as FileNotFoundError:
                  speak(f"Sorry {call_as}, the directory for {app3[0]} was not found! Try checking the directory in data_values.py")
                  print(f"No such directory for '{app3[0]}' was not found! Try changing the directory '{dir3}' from `dir3` in `data_values.py` and read the `info.txt` for info!")
          
          elif any(a in query for a in app4):
                try:
                  if dir4 == "":
                    speak(f"Sorry {call_as}, there is no directory for {app4[0]}! Try checking the directory in data_values.py")
                  else:
                    os.startfile(dir4)
                    speak(f'Opening {app4[0]}')
                except Exception as FileNotFoundError:
                  speak(f"Sorry {call_as}, the directory for {app4[0]} was not found! Try checking the directory in data_values.py")
                  print(f"No such directory for '{app4[0]}' was not found! Try changing the directory '{dir4}' from `dir4` in `data_values.py` and read the `info.txt` for info!")
          
          elif any(a in query for a in app5):
                try:
                  if dir5 == "":
                    speak(f"Sorry {call_as}, there is no directory for {app5[0]}! Try checking the directory in data_values.py")
                  else:
                    os.startfile(dir5)
                    speak(f'Opening {app5[0]}')
                except Exception as FileNotFoundError:
                  speak(f"Sorry {call_as}, the directory for {app5[0]} was not found! Try checking the directory in data_values.py")
                  print(f"No such directory for '{app5[0]}' was not found! Try changing the directory '{dir5}' from `dir5` in `data_values.py` and read the `info.txt` for info!")
          
          elif any(a in query for a in app6):
                try:
                  if dir6 == "":
                    speak(f"Sorry {call_as}, there is no directory for {app6[0]}! Try checking the directory in data_values.py")
                  else:
                    os.startfile(dir6)
                    speak(f'Opening {app6[0]}')
                except Exception as FileNotFoundError:
                  speak(f"Sorry {call_as}, the directory for {app6[0]} was not found! Try checking the directory in data_values.py")
                  print(f"No such directory for '{app6[0]}' was not found! Try changing the directory '{dir6}' from `dir6` in `data_values.py` and read the `info.txt` for info!")
          
          elif any(a in query for a in app7):
                try:
                  if dir7 == "":
                    speak(f"Sorry {call_as}, there is no directory for {app7[0]}! Try checking the directory in data_values.py")
                  else:
                    os.startfile(dir7)
                    speak(f'Opening {app7[0]}')
                except Exception as FileNotFoundError:
                  speak(f"Sorry {call_as}, the directory for {app7[0]} was not found! Try checking the directory in data_values.py")
                  print(f"No such directory for '{app7[0]}' was not found! Try changing the directory '{dir7}' from `dir7` in `data_values.py` and read the `info.txt` for info!")
          
          elif any(a in query for a in app8):
                try:
                  if dir8 == "":
                    speak(f"Sorry {call_as}, there is no directory for {app8[0]}! Try checking the directory in data_values.py")
                  else:
                    os.startfile(dir8)
                    speak(f'Opening {app8[0]}')
                except Exception as FileNotFoundError:
                  speak(f"Sorry {call_as}, the directory for {app8[0]} was not found! Try checking the directory in data_values.py")
                  print(f"No such directory for '{app8[0]}' was not found! Try changing the directory '{dir8}' from `dir8` in `data_values.py` and read the `info.txt` for info!")

          elif any(a in query for a in app9):
                try:
                  if dir9 == "":
                    speak(f"Sorry {call_as}, there is no directory for {app9[0]}! Try checking the directory in data_values.py")
                  else:
                    os.startfile(dir9)
                    speak(f'Opening {app9[0]}')
                except Exception as FileNotFoundError:
                  speak(f"Sorry {call_as}, the directory for {app9[0]} was not found! Try checking the directory in data_values.py")
                  print(f"No such directory for '{app9[0]}' was not found! Try changing the directory '{dir9}' from `dir9` in `data_values.py` and read the `info.txt` for info!")
          elif any(a in query for a in app10):
                try:
                  if dir10 == "":
                    speak(f"Sorry {call_as}, there is no directory for {app10[0]}! Try checking the directory in data_values.py")
                  else:
                    os.startfile(dir10)
                    speak(f'Opening {app10[0]}')
                except Exception as FileNotFoundError:
                  speak(f"Sorry {call_as}, the directory for {app10[0]} was not found! Try checking the directory in data_values.py")
                  print(f"No such directory for '{app10[0]}' was not found! Try changing the directory '{dir10}' from `dir10` in `data_values.py` and read the `info.txt` for info!")
        
      
      #GOOGLE RESULT
      elif 'google' in query:
        query = query.lstrip("jarvis")
        query = query.lstrip("google")
        speak(f"Surfing google and showing the results!")
        wb.open("https://google.com/search?q="+query)
        time.sleep(0.5)
        speak("Here are the results!")  
      #Play Music
      elif 'play music' in query:
        try:
          songs = os.listdir(music_dir)
          os.startfile(os.path.join(music_dir, songs[0])) 
          speak("Playing Music!")
        except Exception as FileNotFoundError:
            speak(f"Sorry {call_as}, the music directory was not found!") 
            print(f"No music directory with directory '{music_dir}' was found! To change the directory open the 'data_values.py' file and change the variable 'music_dir'!")
      #Get Current Time

      elif 'time' in query:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{call_as} the time is {current_time}")
      
      #get current day
      elif 'day' in query:
          current_date = datetime.date.today()
          calendar_day = calendar.day_name[current_date.weekday()] 
          month = f.get_month(current_date.month)
          day = f.get_day(current_date.day)
          speak(f"{call_as} today is {calendar_day}, {month} the {day}.")
      #get current day
      elif 'date' in query:
          current_date = datetime.date.today()
          calendar_day = calendar.day_name[current_date.weekday()] 
          month = f.get_month(current_date.month)
          day = f.get_day(current_date.day)
          speak(f"{call_as} today is {calendar_day}, {month} the {day}.")
      #Open specific files
      elif 'repeat' in query:
        speak(f"Repeating after you {call_as}!")
        f.repeat() 

      
      elif 'ip' in query:
        speak(f"{call_as}, your ip address is: {ip}!")
        print(f"Your ip address is: {ip}")
      elif 'where am i' in query:
        speak(f"Your current location is {city}, {region}, {country}!")
      #WEATHER
      elif "weather" in query:
        speak(f"""
        Here are the weather reports:-
        Temperature: {temp} degrees
        Humidity: {humidity}%
        Pressure: {pressure}atm
        Report: {report}
        """)     
 
      elif 'go to sleep' in query or 'shutdown' in query:
        speak(f'Going to sleep, {call_as}')
        print(f'Going to sleep, {call_as}!')
        break
      elif 'play' in query or 'youtube' in query:
            search = query.lstrip('play').lstrip('ok').lstrip('me').lstrip('hi').lstrip("jarvis")
            speak(f'Searching {search} and playing the first video!')
            search_code = search.replace("@","%40").replace("#","%20").replace("/","%2F").replace("+","%2B").replace("$","%24").replace("%","%25").replace(" ",'+')
            data = urlopen(f"https://youtube.com/results?search_query={search_code}")
            videos = re.findall(r"watch\?v=(\S{11})",data.read().decode())
            wb.open(f'https://youtube.com/watch?v={videos[0]}')
            speak(f'Video found, playing the video!')
            print(f'Video Link: https://youtube.com/watch?v={videos[0]}')
      
      elif 'close the tab' in query or 'close tab' in query:
        ky.press('ctrl + w')
        ky.release("ctrl + w")
        speak('Closed the tab!')
      elif 'open new tab' in query or 'open a new tab' in query:
        ky.press('ctrl + t')
        ky.release("ctrl + t")
        speak('Opened a new tab!')
      elif 'pause' in query:
        ky.press('k')
        ky.release("k")
        speak('Paused the video')
      elif 'resume' in query:
        ky.press('k')
        ky.release("k")
        speak('Resumed the video')
      elif 'mute site' in query or 'mute the site' in query:
        ky.press('ctrl + m')
        ky.release("ctrl + m")
        speak('Muted the site!')
      elif 'copy url' in query or 'copy the url' in query:
        ky.press('ctrl + l')
        ky.release("ctrl + l")
        ky.press('ctrl + c')
        ky.release("ctrl + c")
        speak('Copied the url to clipboard!')
      elif 'copy' in query:
          ky.press('ctrl + c')
          speak('Copied!')
      elif 'paste' in query:
        ky.press('ctrl + v')
        ky.release("ctrl + v")
        speak('Pasted!')
      elif 'switch window' in query:
        ky.press('alt+ tab')
        ky.release("alt + tab")
        speak('Switched!')
      elif 'meaning' in query:
        word= 'what does man mean'.lstrip('what does').lstrip('what do you mean by').lstrip('meaning').lstrip('mean').lstrip('jarvis').lstrip('meaning of').lstrip('what is the')
        meaning = dic().meaning(word)
        if meaning is None:
            speak(f'No such word, {word}')
        else:
            k = list(meaning.keys())[0]
            if [k.startswith(i) for i in ['a','e','i','o','u']] != []:
                speak(f'The word {word} means, {meaning[k][0]}. It is used as an {k}')
            else:
                print(f'The {word} means, {meaning[k][0]}. It is used as a {k}')
      elif 'what does' in query and 'mean' in query:
        word= query.lstrip('what does').lstrip('what do you mean by').lstrip('meaning').lstrip('mean').lstrip('jarvis').lstrip('meaning of').lstrip('what is the').lstrip('an').lstrip('a')
        meaning = dic().meaning(word)
        print(word)
        if meaning is None:
            speak(f'No such word, {word}')
        else:
            k = list(meaning.keys())[0]
            if [k.startswith(i) for i in ['a','e','i','o','u']] != []:
                speak(f'The word {word} means, {meaning[k][0]}. It is used as an {k}')
                print(f"The word {word} means, {meaning[k][0]}. It is used as an {k}")
            else:
                speak(f'The word {word} means, {meaning[k][0]}. It is used as a {k}')
                print(f"The word {word} means, {meaning[k][0]}. It is used as a {k}")
      elif 'start writing' in query:
            speak(f"Writing as you speak, {call_as}!")
            text = userCommand().casefold()
            text = f.str_to_text(text)
            print(text)              

      #CALLING JARVIS
      elif 'hypixel' in query or 'high pixel' in query:
            speak('Entering high pixel mode!')
            speak("Now you can simply say, Gamemode Player, for example bedwars MASTERMUDITH!")
            while True:
              cmd = userCommand().casefold()
              print(cmd)
              if cmd == 'exit' or cmd == 'exit hypixel mode':
                speak('Exiting hypixel mode!')
                break
              elif cmd.isspace():
                    pass
              elif cmd is None:
                    pass
              else:
                cmd = cmd.split(' ')
                for i in cmd:
                  if len(i) > 1 and 'me' not in i:
                      del cmd[cmd.index(i)]
                if cmd == []:
                  cmd = ['mastermudith']
                cmd = list(''.join(cmd))
                if 'sky' in cmd:
                  cmd.append('sky')
                else:
                  cmd.append('bed')
                print(f'Hi: {cmd}')
                stats = f.hypixel_mode(cmd)
              speak(stats)


      elif bot_name.lower() in query.casefold():
        speak(random.choice(bot_help_random))