import pyttsx3                                     # pip install pyttsx3
import datetime
import speech_recognition as sr                    # pip install SpeechRecognition
# import pyaudio                                   # pip install pipwin and then pipwin install pyaudio
import wikipedia                                   # pip install wikipedia
import webbrowser
import os
import sys
import smtplib
from email.message import EmailMessage
import pywhatkit                                   # pip install pywhatkit
import MyAlarm                                     # user-defined
import pyjokes                                     # pip install pyjokes
from speedtest import Speedtest                    # pip install speedtest-cli
from pywikihow import search_wikihow               # pip install pywikihow
import pyautogui                                   # pip install pyAutoGUI
import poetpy                                      # pip install poetpy
import random
from forex_python.converter import CurrencyRates   # pip install forex-python
import requests                                    # pip install requests
import bs4                                         # pip install beautifulsoup4
import time
import wolframalpha                                # pip install wolframalpha
from quote import quote                            # pip install quote
import winshell as winshell                        # pip install winshell
from geopy.geocoders import Nominatim              # pip install geopy  and pip install geocoder
from geopy import distance

engine = pyttsx3.init()


def fun_talk(audio):
    engine.say(audio)
    engine.runAndWait()


def wish_user():
   
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        fun_talk("Good Morning !")

    elif hour >= 12 and hour < 18:
        fun_talk("Good Afternoon !")

    else:
        fun_talk("Good Evening !")

    fun_talk("I am P.A. (Python Assistant). Tell me how may I help you.")


def get_command():
    

    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        rec.pause_threshold = 1

        audio = rec.listen(source)

        try:
            print("Recognizing...")
            query = rec.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            # print(e)
            print("Say that again please...")
            return "None"
        return query


if _name_ == '_main_':
    
    wish_user()

    while True:
        
        query = get_command().lower()

        if 'wikipedia' in query:
            fun_talk('Searching Wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            fun_talk("According to Wikipedia")
            print(results)
            fun_talk(results)

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("www.google.com")

        elif 'open cu login' in query:
            webbrowser.open("uims.cuchd.in/uims/")

        elif 'open blackboard' in query:
            webbrowser.open("cuchd.blackboard.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            fun_talk(f"The time is {strTime}")

        elif 'the date' in query:
            strDate = datetime.datetime.today().strftime('%Y-%m-%d')
            print(strDate)
            fun_talk(f"The date is {strDate}")

        elif 'open visual studio code' in query:
            os.startfile("C:\\Users\\91954\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\"
                         "Programs\\Visual Studio Code\\Visual Studio Code")

        elif 'open eclipse' in query:
            os.startfile("C:\\Users\\91954\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\"
                         "Programs\\Eclipse\\Eclipse IDE for Java Developers - 2020-06")

        elif 'open notepad' in query:
            os.startfile("C:\\Users\\91954\\AppData\\Roaming\\Microsoft\\Windows\\"
                         "Start Menu\\Programs\\Accessories\\Notepad")

        elif 'open pycharm' in query:
            os.startfile("C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1.1\\bin\\pycharm64.exe")

        elif 'open code blocks' in query:
            os.startfile("C:\\Users\\91954\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\"
                         "Programs\\CodeBlocks\\CodeBlocks")

        elif 'open mozilla firefox' in query:
            os.startfile("C:\\Program Files\\Mozilla Firefox\\firefox.exe")

        elif 'open chrome' in query:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        elif 'open whatsapp' in query:
            os.startfile("C:\\Users\\91954\\AppData\\Local\\WhatsApp\\WhatsApp.exe")

        elif 'open vlc' in query:
            os.startfile("C:\\Program Files\\VideoLAN\\VLC\\vlc.exe")

        elif 'who are you' in query:
            fun_talk("I am P.A. (Python Assistant), developed by Rishabh Ranjan, Himanshi, "
                     "Rachit Dwivedi and Umesh Singh as a project in their college.")

        elif 'what you want to do' in query:
            fun_talk("I want to help people to do certain tasks on their single voice commands.")

        elif 'alexa' in query:
            fun_talk("I don't know Alexa, but I've heard of Alexa. If you have Alexa, "
                     "I may have just triggered Alexa. If so, sorry Alexa.")

        elif 'google assistant' in query:
            fun_talk("He was my classmate, too intelligent guy. We both are best friends.")

        elif 'siri' in query:
            fun_talk("Siri, She's a competing virtual assistant on   a competitor's phone. "
                     "Not that I'm competitive or anything.")

        elif 'cortana' in query:
            fun_talk("I thought you'd never ask. So I've never thought about it.")

        elif 'python assistant' in query:
            fun_talk("Are you joking. You're coming in loud and clear.")

        elif 'what language you use' in query:
            fun_talk("I am written in Python and I generally speak english.")

        elif 'send email' in query:

            def send_mail(receiver, subject, message):

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login('your_email@something.com', 'your_password')

                email = EmailMessage()
                email['From'] = 'your_email@something.com'
                email['To'] = receiver
                email['Subject'] = subject
                email.set_content(message)
                server.send_message(email)


            email_list = {
                'Umesh': 'ums945891@gmail.com',
                'Rishabh': 'rishabhran123@gmail.com',
                'name': 'something@something.com',
                'assitant': 'something@something.com'
            }


            def get_mail_info():
                fun_talk('To whom you want to send email')
                name = get_command()
                receiver = email_list[name]
                print(receiver)
                fun_talk('What is the subject of your email?')
                subject = get_command()
                fun_talk('Tell me the text in your email')
                message = get_command()

                send_mail(receiver, subject, message)

                fun_talk('Hey lazy person. Your email is sent Successfully.')

                fun_talk('Do you want to send more email?')
                send_more = get_command()
                if 'yes' in send_more:
                    get_mail_info()


            get_mail_info()

        elif 'play' in query:
            cmd_info = query.replace('play', '')
            fun_talk(f'Playing {cmd_info} ')
            print(cmd_info)
            pywhatkit.playonyt(cmd_info)

        elif 'search' in query:
            query = query.replace('search', '')
            pywhatkit.search(query)

        elif 'set alarm' in query:
            fun_talk("Tell me the time to set an Alarm. For example, set an alarm for 11:21 AM")
            a_info = get_command()
            a_info = a_info.replace('set an alarm for', '')
            a_info = a_info.replace('.', '')
            a_info = a_info.upper()
            MyAlarm.alarm(a_info)

        elif 'exit p a' in query:
            fun_talk("Exiting Sir...")
            sys.exit()

        elif 'close command prompt' in query:
            os.system("TASKKILL /F /IM cmd.exe")

        elif 'close firefox' in query:
            os.system("TASKKILL /F /IM firefox.exe")
            # subprocess.call(["taskkill", "/F", "/IM", "firefox.exe"])

        elif 'close visual studio code' in query:
            os.system("TASKKILL /F /IM Code.exe")

        elif 'close eclipse' in query:
            os.system("TASKKILL /F /IM eclipse.exe")

        elif 'close notepad' in query:
            os.system("TASKKILL /F /IM notepad.exe")

        elif 'close pycharm' in query:
            os.system("TASKKILL /F /IM pycharm64.exe")

        elif 'close code blocks' in query:
            os.system("TASKKILL /F /IM codeblocks.exe")

        elif 'close chrome' in query:
            os.system("TASKKILL /F /IM chrome.exe")

        elif 'close whatsapp' in query:
            os.system("TASKKILL /F /IM WhatsApp.exe")

        elif 'close vlc' in query:
            os.system("TASKKILL /F /IM vlc.exe")

        elif 'close spotify' in query:
            os.system("TASKKILL /F /IM Spotify.exe")

        elif 'poem' in query:
            fun_talk('Poem of which author you want to listen?')
            auth = get_command()
            poem = poetpy.get_poetry('author', auth, 'title,linecount') 
            poems = poetpy.get_poetry('author', auth, 'lines')  

            poem_len = len(poem)
            # print(poem_len)
            poem_no = random.randint(1, poem_len)
            print("Title- ", poem[poem_no]['title'])
            fun_talk(f"Title- {poem[poem_no]['title']}")
            print("No. of lines-", poem[poem_no]['linecount'])
            fun_talk(f"No. of lines- {poem[poem_no]['linecount']}")
            poem_str = '\n'
            print("Poem-\n", poem_str.join(poems[poem_no]['lines']))
            fun_talk(f"Poem-\n {poem_str.join(poems[poem_no]['lines'])}")

        elif 'resume' in query or 'pause' in query:
            pyautogui.press("playpause")

        elif 'previous' in query:
            pyautogui.press("prevtrack")

        elif 'next' in query:
            pyautogui.press("nexttrack")

        elif 'convert currency' in query:
            try:
                curr_list = {
                    'dollar': 'USD', 'taka': 'BDT', 'dinar': 'BHD',
                    'rupee': 'INR', 'afghani': 'AFN', 'real': 'BRL',
                    'yen': 'JPY', 'peso': 'ARS', 'pound': 'EGP', 'rial': 'OMR',
                    'lek': 'ALL', 'kwanza': 'AOA', 'manat': 'AZN', 'franc': 'CHF'
                }

                cur = CurrencyRates()
                # print(cur.get_rate('USD', 'INR'))
                fun_talk('From which currency u want to convert?')
                from_cur = get_command()
                src_cur = curr_list[from_cur.lower()]
                fun_talk('To which currency u want to convert?')
                to_cur = get_command()
                dest_cur = curr_list[to_cur.lower()]
                fun_talk('Tell me the value of currency u want to convert.')
                val_cur = float(get_command())
                # print(val_cur)
                print(cur.convert(src_cur, dest_cur, val_cur))
                     
            except Exception as e:
                print("Couldn't get what you have said, Can you say it again??")

        elif 'covid-19' in query or 'corona' in query:
            fun_talk('For which region u want to see the Covid-19 cases. '
                     'Overall cases in the world or any specific country?')
            c_query = get_command()
            if 'overall' in c_query or 'over all' in c_query or 'world' in c_query or 'total' in c_query or 'worldwide' in c_query:
                def world_cases():
                    try:
                        url = 'https://www.worldometers.info/coronavirus/'
                        info_html = requests.get(url)
                        info = bs4.BeautifulSoup(info_html.text, 'lxml')
                        info2 = info.find('div', class_='content-inner')
                        new_info = info2.findAll('div', id='maincounter-wrap')
                        # print(new_info)
                        print('Worldwide Covid-19 information--')
                        fun_talk('Worldwide Covid-19 information--')

                        for i in new_info:
                            head = i.find('h1', class_=None).get_text()
                            counting = i.find('span', class_=None).get_text()
                            print(head, "", counting)
                            fun_talk(f'{head}: {counting}')

                    except Exception as e:
                        pass


                world_cases()

            elif 'country' in c_query or 'specific country' in c_query:
                def country_cases():
                    try:
                        fun_talk('Tell me the country name.')
                        c_name = get_command()
                        c_url = f'https://www.worldometers.info/coronavirus/country/{c_name}/'
                        data_html = requests.get(c_url)
                        c_data = bs4.BeautifulSoup(data_html.text, 'lxml')
                        new_data = c_data.find('div', class_='content-inner').findAll('div', id='maincounter-wrap')
                        # print(new_data)
                        print(f'Covid-19 information for {c_name}--')
                        fun_talk(f'Covid-19 information for {c_name}')

                        for j in new_data:
                            c_head = j.find('h1', class_=None).get_text()
                            c_counting = j.find('span', class_=None).get_text()
                            print(c_head, "", c_counting)
                            fun_talk(f'{c_head}: {c_counting}')

                    except Exception as e:
                        pass


                country_cases()

        elif 'weather' in query or 'temperature' in query:
            try:
                fun_talk("Tell me the city name.")
                city = get_command()
                api = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=eea37893e6d01d234eca31616e48c631"
                w_data = requests.get(api).json()
                weather = w_data['weather'][0]['main']
                temp = int(w_data['main']['temp'] - 273.15)
                temp_min = int(w_data['main']['temp_min'] - 273.15)
                temp_max = int(w_data['main']['temp_max'] - 273.15)
                pressure = w_data['main']['pressure']
                humidity = w_data['main']['humidity']
                visibility = w_data['visibility']
                wind = w_data['wind']['speed']
                sunrise = time.strftime("%H:%M:%S", time.gmtime(w_data['sys']['sunrise'] + 19800))
                sunset = time.strftime("%H:%M:%S", time.gmtime(w_data['sys']['sunset'] + 19800))

                all_data1 = f"Condition: {weather} \nTemperature: {str(temp)}°C\n"
                all_data2 = f"Minimum Temperature: {str(temp_min)}°C \nMaximum Temperature: {str(temp_max)}°C \n" \
                            f"Pressure: {str(pressure)} millibar \nHumidity: {str(humidity)}% \n\n" \
                            f"Visibility: {str(visibility)} metres \nWind: {str(wind)} km/hr \nSunrise: {sunrise}  " \
                            f"\nSunset: {sunset}"
                fun_talk(f"Gathering the weather information of {city}...")
                print(f"Gathering the weather information of {city}...")
                print(all_data1)
                fun_talk(all_data1)
                print(all_data2)
                fun_talk(all_data2)

            except Exception as e:
                pass

        elif 'month' in query or 'month is going' in query:
            def tell_month():
                localtime = time.asctime(time.localtime(time.time()))
                m_onth = localtime[4:7]
                if m_onth == "Jan":
                    fun_talk("it's january")
                if m_onth == "Feb":
                    fun_talk("it's february")
                if m_onth == "Mar":
                    fun_talk("it's march")
                if m_onth == "Apr":
                    fun_talk("it's april")
                if m_onth == "May":
                    fun_talk("it's may")
                if m_onth == "Jun":
                    fun_talk("it's june")
                if m_onth == "Jul":
                    fun_talk("it's july")
                if m_onth == "Aug":
                    fun_talk("it's august")
                if m_onth == "Sep":
                    fun_talk("it's september")
                if m_onth == "Oct":
                    fun_talk("it's october")
                if m_onth == "Nov":
                    fun_talk("it's november")
                if m_onth == "Dec":
                    fun_talk("it's december")


            tell_month()

        elif 'day' in query or 'day today' in query:
            def tell_day():
                localtime = time.asctime(time.localtime(time.time()))
                day = localtime[0:3]
                if day == "Sun":
                    fun_talk("it's sunday")
                if day == "Mon":
                    fun_talk("it's monday")
                if day == "Tue":
                    fun_talk("it's tuesday")
                if day == "Wed":
                    fun_talk("it's wednesday")
                if day == "Thu":
                    fun_talk("it's thursday")
                if day == "Fri":
                    fun_talk("it's friday")
                if day == "Sat":
                    fun_talk("it's saturday")


            tell_day()

        elif "calculate" in query:
            try:
                app_id = "JUGV8R-RXJ4RP7HAG"
                client = wolframalpha.Client(app_id)
                indx = query.lower().split().index('calculate')
                query = query.split()[indx + 1:]
                res = client.query(' '.join(query))
                answer = next(res.results).text
                print("The answer is " + answer)
                fun_talk("The answer is " + answer)

            except Exception as e:
                print("Couldn't get what you have said, Can you say it again??")

        elif 'quote' in query or 'quotes' in query:
            fun_talk("Tell me the author or person name.")
            q_author = get_command()
            quotes = quote(q_author)
            quote_no = random.randint(1, len(quotes))
            # print(len(quotes))
            # print(quotes)
            print("Author: ", quotes[quote_no]['author'])
            print("-->", quotes[quote_no]['quote'])
            fun_talk(f"Author: {quotes[quote_no]['author']}")
            fun_talk(f"He said {quotes[quote_no]['quote']}")

        elif 'what' in query or 'who' in query:  # or 'where' in query:  
            
            client = wolframalpha.Client("JUGV8R-RXJ4RP7HAG")
            res = client.query(query)
            try:
                print(next(res.results).text)
                fun_talk(next(res.results).text)

            except StopIteration:
                print("No results found!!")

        elif 'empty recycle bin' in query or 'clear recycle bin' in query:
            try:
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                print("Recycle Bin is cleaned successfully.")
                fun_talk("Recycle Bin is cleaned successfully.")

            except Exception as e:
                print("Recycle bin is already Empty.")
                fun_talk("Recycle bin is already Empty.")

        elif 'write a note' in query or 'make a note' in query:
            fun_talk("What should I write, sir??")
            note = get_command()
            file = open('Notes.txt', 'a')
            fun_talk("Should I include the date and time??")
            n_conf = get_command()
            if 'yes' in n_conf:
                str_time = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(str_time)
                file.write(" --> ")
                file.write(note)
                fun_talk("Point noted successfully.")
            else:
                file.write("\n")
                file.write(note)
                fun_talk("Point noted successfully.")

        elif 'show me the notes' in query or 'read notes' in query:
            fun_talk("Reading Notes")
            file = open("Notes.txt", "r")
            data_note = file.readlines()
            # for points in data_note:
            print(data_note)
            fun_talk(data_note)

        elif 'distance' in query:
            geocoder = Nominatim(user_agent="Singh")
            fun_talk("Tell me the first city name??")
            location1 = get_command()
            fun_talk("Tell me the second city name??")
            location2 = get_command()

            coordinates1 = geocoder.geocode(location1)
            coordinates2 = geocoder.geocode(location2)

            lat1, long1 = coordinates1.latitude, coordinates1.longitude
            lat2, long2 = coordinates2.latitude, coordinates2.longitude

            place1 = (lat1, long1)
            place2 = (lat2, long2)

            distance_places = distance.distance(place1, place2)

            print(f"The distance between {location1} and {location2} is {distance_places}.")
            fun_talk(f"The distance between {location1} and {location2} is {distance_places}")

        elif 'screenshot' in query:
            sc = pyautogui.screenshot()
            sc.save('pa_ss.png')
            print("Screenshot taken successfully.")
            fun_talk("Screenshot taken successfully.")

        elif 'volume up' in query:
            pyautogui.press("volumeup")

        elif 'volume down' in query:
            pyautogui.press("volumedown")

        elif 'mute volume' in query:
            pyautogui.press("volumemute")

        elif 'shut down' in query:
            print("Do you want to shutdown you system?")
            fun_talk("Do you want to shutdown you system?")
            cmd = get_command()
            if 'no' in cmd:
                continue
            else:
                
                os.system("shutdown /s /t 1")

        elif 'restart' in query:
            print("Do you want to restart your system?")
            fun_talk("Do you want to restart your system?")
            cmd = get_command()
            if 'no' in cmd:
                continue
            else:
                
                os.system("shutdown /r /t 1")

        elif 'log out' in query:
            print("Do you want to logout from your system?")
            fun_talk("Do you want to logout from your system?")
            cmd = get_command()
            if 'no' in cmd:
                continue
            else:
                os.system("shutdown -l")

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            print(joke)
            fun_talk(joke)

        elif 'internet speed' in query:
            st = Speedtest()
            print("Wait!! I am checking your Internet Speed...")
            fun_talk("Wait!! I am checking your Internet Speed...")
            dw_speed = st.download()
            up_speed = st.upload()
            dw_speed = dw_speed / 1000000
            up_speed = up_speed / 1000000
            print('Your download speed is', round(dw_speed, 3), 'Mbps')
            print('Your upload speed is', round(up_speed, 3), 'Mbps')
            fun_talk(f'Your download speed is {round(dw_speed, 3)} Mbps')
            fun_talk(f'Your upload speed is {round(up_speed, 3)} Mbps')

        elif 'send message on whatsapp' in query:
            phno_list = {
                'Umesh': '+911234567890',
                'Rishabh': '+919876543210',
                'assitant': '+910000000000'
            }


            def send_whtmsg():
                fun_talk('To whom you want to send message on WhatsApp')
                recepient = get_command()
                check_recep = phno_list[recepient]
                print(check_recep)
                fun_talk('Tell me the text in your message')
                msg = get_command()
                fun_talk('Do you want to send it immediately?')
                act_msg = get_command()
                if 'yes' in act_msg:
                    hr = datetime.datetime.now().time().hour
                    min = datetime.datetime.now().time().minute
                    pywhatkit.sendwhatmsg(check_recep, msg, hr, min + 2)
                    print('Hey lazy person. Your message is sent successfully.')
                else:
                    fun_talk('At what time you want to send this message. For example, 11:21 PM')
                    msg_time = get_command()

                    hr = 12
                    min = 52
                    pywhatkit.sendwhatmsg(check_recep, msg, hr, min)
                    print('Hey lazy person. Your message is sent successfully.')
                fun_talk('Do you want to send more WhatsApp messages?')
                more_msg = get_command()
                if 'yes' in more_msg:
                    send_whtmsg()


            send_whtmsg()

        elif 'how to' in query:
            try:
                # query = query.replace('how to', '')
                max_results = 1
                data = search_wikihow(query, max_results)
                # assert len(data) == 1
                data[0].print()
                fun_talk(data[0].summary)
            except Exception as e:
                fun_talk('Sorry, I am unable to find the answer for your query.')
