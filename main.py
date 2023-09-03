# Import necessary libraries
import time

from psutil import sensors_battery
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import requests, json
import random
import pyautogui
import psutil
import os
import pyjokes

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
PAVoices = engine.getProperty('voices')
engine.setProperty('voice', PAVoices[0].id)


# Function to make the assistant speak
def speakPA(audio):
    engine.say(audio)
    engine.runAndWait()


# Greet the user based on the time of the day
def wishTheMaster():
    hour = int(datetime.datetime.now().hour)
    if (hour >= 5 and hour < 12):
        print("PA - Good morning master, i hope you slept good.")
        speakPA("Good morning master, i hope you slept good.")
    elif (hour == 12):
        print("PA - Good noon master, hope you're having a good day.")
        speakPA("Good noon master, hope you're having a good day.")
    elif (hour > 12 and hour < 17):
        print("PA - Good Afternoon Master")
        speakPA("Good Afternoon Master")
    elif( hour >= 1 and hour < 5):
        print("PA - You should take sleep at this time, whatever how can i help you???")
        speakPA("You should take sleep at this time, whatever how can i help you???")
    else:
        print("PA - Good evening master, which voice do you want me to operate in ?")
        speakPA("Good evening master, which voice do you want me to operate in ?")



# Function to change the assistant's voice
def changeVoice(voice):
    if ("male" in voice):
        engine.setProperty('voice', PAVoices[0].id)
        print("PA - Hi i am PA, How can i help you ? ")
        speakPA("Hi i am PA, How can i help you ? ")
    elif ("female" in voice):
        engine.setProperty('voice', PAVoices[1].id)
        print("PA - Hi i am Female PA, How can i help you ? ")
        speakPA("Hi i am Female PA, How can i help you ? ")
    return True



# Function to get user's voice command
def tcommandfromMaster():
    recGogNizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nPA - Listening....")
        speakPA("listening")
        recGogNizer.pause_threshold = 1
        recGogNizer.energy_threshold = 1000
        audio = recGogNizer.listen(source)
    try:
        print("PA - Recognizing...")
        speakPA("Recognizing")
        myQuery = recGogNizer.recognize_google(audio, language='en-in')
        print(f"USER - {myQuery}\n")
    except Exception as e:

        print("PA - Please say that again")
        speakPA("Please say that again")

        return "None"

    return myQuery


if __name__ == "__main__":
    wishTheMaster()
    myQuery = tcommandfromMaster().lower()
    while True:
        # Implement various commands and actions based on the user's query
        if "female" in myQuery:
            # Handle voice change to female
            engine.setProperty('voice', PAVoices[1].id)
            print("PA - I am PA,  Tell me how can i help you .")
            speakPA("I am PA,  Tell me how can i help you .")
            myQuery = tcommandfromMaster().lower()

        if "male" in myQuery:
            # Handle voice change to male
            engine.setProperty('voice', PAVoices[0].id)
            print("PA - I am PA,  Tell me how can i help you .")
            speakPA("I am PA,  Tell me how can i help you .")
            myQuery = tcommandfromMaster().lower()

        if "change voice" in myQuery:
            # Handle voice change request
            print("PA - In which voice do you want me to operate in ?")
            speakPA("In which voice do you want me to operate in ?")
            x = tcommandfromMaster().lower()
            ret = changeVoice(x)
            myQuery = tcommandfromMaster().lower()

        if "hello" in myQuery:
            # Respond to a greeting
            print("PA - Hi There")
            speakPA("Hi There")
            myQuery = tcommandfromMaster().lower()
            
        if "calculate" in myQuery:
            # Perform calculations
            print("PA - Enter first number")
            speakPA("Enter first number")
            a = int(input("Enter here : "))
            print("PA - Enter second number")
            speakPA("Enter Second number")
            b = int(input("Enter here : "))
            print("PA - Tell me the operation")
            speakPA("Tell me the operation")
            myQuery = tcommandfromMaster().lower()
            if "add" in myQuery:
                print(f"PA - Answer is : {a+b}")
                speakPA(f"Answer is : {a+b}")
            if "subtract" in myQuery:
                print(f"PA - Answer is : {a-b}")
                speakPA(f"Answer is : {a-b}")
            if "multiply" in myQuery:
                print(f"PA - Answer is : {a*b}")
                speakPA(f"Answer is : {a*b}")
            if "divide" in myQuery:
                print(f"PA - Answer is : {a/b}")
                speakPA(f"Answer is : {a/b}")
            myQuery = tcommandfromMaster().lower()
            
        elif "joke" in myQuery:
            # Tell a joke
            joke = pyjokes.get_joke(language='en', category='neutral')
            print(f"PA - {joke}")
            speakPA(joke)
            myQuery = tcommandfromMaster().lower()

        elif "battery" in myQuery:
            # Check battery status
            cpu = str(sensors_battery().percent)
            print(f"PA - You have  {cpu} %  battery")
            speakPA(f"You have  {cpu} %  battery")
            if (sensors_battery().percent < 50):
                if (sensors_battery().power_plugged == False):
                    print("PA - You should plugin your charger master")
                    speakPA("You should plugin your charger master")
            else:
                print("PA - You can continue your work without plugging in")
                speakPA("You can continue your work without plugging in")

            myQuery = tcommandfromMaster().lower()


        elif "how are you" in myQuery:
            # Respond with different answers about well-being
            lst2 = ["I am good", "Fine, what about you?", "Great, as always", "amazing, have nothing to be sad about"]
            rndd = random.randint(0, 3)
            print(f"PA - {lst2[rndd]}")
            speakPA(lst2[rndd])
            myQuery = tcommandfromMaster().lower()
            lst3 = ["Life is too short to be sad", "That's good to hear", "That's wonderful"]
            rnddd = random.randint(0, 2)
            print(f"PA - {lst3[rnddd]}")
            speakPA(lst3[rnddd])
            myQuery = tcommandfromMaster().lower()
            
        elif "what are you doing" in myQuery:
            # Share different activities the assistant is doing
            lst4 = ["Just hanging out with siri", "Serving you",
                    "Thinking ways to satisfy parent's expectations hahaha", "Thinking about better ways to serve you",
                    "Learning new tasks", "Pushing my limits", "Chilling with a wine"]
            rndddd = random.randint(0, 6)
            print(f"PA - {lst4[rndddd]}")
            speakPA(lst4[rndddd])
            print("PA - What about you")
            speakPA("What about you")
            myQuery = tcommandfromMaster().lower()
            print(f"USER - {myQuery}")
            print("PA -Good, tell me what you have for me in the plate")
            speakPA("Good, tell me what you have for me in the plate")
            myQuery = tcommandfromMaster().lower()
            
        elif "screenshot" in myQuery:
            # Take a screenshot and provide information about it
            img = pyautogui.screenshot()
            img.save("C:\\Users\\HP\\Pictures\\Screenshots\\PA.png")
            print("PA - Screenshot done, You can view it in C:\\Users\\HP\\Pictures\\Screenshots\\PA.png")
            speakPA("Screenshot done, You can view it in C:\\Users\\HP\\Pictures\\Screenshots\\PA.png")
            myQuery = tcommandfromMaster().lower()
            
        elif "time" in myQuery:
            # Provide the current time
            print(f"PA - {datetime.datetime.now().time()}")
            speakPA(datetime.datetime.now().time())
            myQuery = tcommandfromMaster().lower()
            
        elif "write down" in myQuery:
            # Take a note and save it to a file
            print("PA - What should i write down sir")
            speakPA("What should i write down sir")
            notes = tcommandfromMaster()
            file1 = open('data.txt', 'w')
            file1.write(notes)
            file1.close()
            print("PA - I have noted that sir , do you want me to repeat?")
            speakPA("I have noted that sir , do you want me to repeat?")
            myQuery = tcommandfromMaster().lower()
            if "yes" in myQuery:
                print(f"PA - I have noted: {notes}")
                speakPA(f"I have noted: {notes}")
            else:
                print("PA - okay")
                speakPA("okay")
            myQuery = tcommandfromMaster().lower()
            
        elif "remember" in myQuery:
            # Retrieve and speak remembered content
            file1 = open("data.txt", 'r')

            print(f"PA - You told me to remember that {file1.read()}")
            speakPA(f"You told me to remember that {file1.read()}")
            myQuery = tcommandfromMaster().lower()

        elif "wikipedia" in myQuery:
            # Search Wikipedia and provide a summary
            print("PA - Searching wikipedia...")
            speakPA("Searching wikipedia")
            myQuery = myQuery.replace("wikipedia", "")
            results = wikipedia.summary(myQuery, sentences=2)
            print("PA - According to wikipedia...")
            speakPA("According to wikipedia")
            print(f"PA - {results}")
            speakPA(results)
            myQuery = tcommandfromMaster().lower()


        elif "open youtube" in myQuery:
            # Open YouTube website
            print("PA - opening youtube...")
            speakPA("opening youtube")
            webbrowser.open_new_tab("youtube.com")
            myQuery = tcommandfromMaster().lower()

        elif "open google" in myQuery:
            # Open Google website
            print("PA - opening google...")
            speakPA("opening google")
            webbrowser.open_new_tab("google.com")
            myQuery = tcommandfromMaster().lower()


        elif "outside" in myQuery:
            # Fetch weather information for a specified city when asked to "outside"
            print("PA - Which city's weather would you like to know?")
            speakPA("Which city's weather would you like to know?")
            city = tcommandfromMaster().lower()

            # API request for weather information
            api_key = "8bdc1d60e7103c410fbe5ca70951a6f5"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            complete_url = base_url + "appid=" + api_key + "&q=" + city
            response = requests.get(complete_url)
            rj = response.json()

            # Process weather data and provide information
            if rj["cod"] != "404":
                w = rj["main"]
                current_temperature = int(w["temp"] - 273.15)
                current_pressure = w["pressure"]
                current_humidity = w["humidity"]
                z = rj["weather"]
                weather_desc = z[0]["description"]
                print("PA - Temperature (in celcius unit) = " +
                      str(current_temperature) + " Celcius" +
                      "\n atmospheric pressure (in hPa unit) = " +
                      str(current_pressure) +
                      "\n humidity (in percentage) = " +
                      str(current_humidity) +
                      "\n description = " +
                      str(weather_desc))
                speakPA(current_temperature)
                speakPA(weather_desc + "  in  " + city)
            else:
                print("PA - City not found")
                speakPA("City not found")
            myQuery = tcommandfromMaster().lower()
            
        elif "coin" in myQuery:
            # Flip a coin and announce the result when asked to "coin"
            lst1 = ["Heads", "Tails"]
            result = random.randint(0, 1)
            print("PA - It's a " + lst1[result])
            speakPA("It's a " + lst1[result])
            myQuery = tcommandfromMaster().lower()
            
        elif "left" in myQuery:
            # Move cursor to left
            print("PA - moving cursor to left")
            speakPA("moving cursor to left")
            pyautogui.moveTo(500, 300, 2)
            print("PA - cursor is moved to left")
            speakPA("cursor is moved to left")
            myQuery = tcommandfromMaster().lower()
            
        elif "open amazon" in myQuery:
            # Open Amazon website
            webbrowser.open("amazon.com")
            print("PA - opening amazon...")
            speakPA("opening amazon")
            myQuery = tcommandfromMaster().lower()

        elif "open flipkart" in myQuery:
            webbrowser.open("flipkart.com")
            print("PA - opening flipkart...")
            speakPA("opening flipkart")
            myQuery = tcommandfromMaster().lower()

        elif "open facebook" in myQuery:
            webbrowser.open("facebook.com")
            print("PA - opening facebook...")
            speakPA("opening facebook")
            myQuery = tcommandfromMaster().lower()

        elif "open instagram" in myQuery:
            webbrowser.open("instagram.com")
            print("PA - opening instagram...")
            speakPA("opening instagram")
            myQuery = tcommandfromMaster().lower()

        elif "open yahoo" in myQuery:
            webbrowser.open("yahoo.com")
            print("PA - opening yahoo...")
            speakPA("opening yahoo")
            myQuery = tcommandfromMaster().lower()

        elif "open gmail" in myQuery:
            webbrowser.open("gmail.com")
            print("PA - opening gmail...")
            speakPA("opening gmail")
            myQuery = tcommandfromMaster().lower()

        elif "open stack overflow" in myQuery:
            webbrowser.open("stackoverflow.com")
            print("PA - opening stackoverflow...")
            speakPA("opening stackoverflow")
            myQuery = tcommandfromMaster().lower()

        elif "open gfg" in myQuery:
            webbrowser.open("geeksforgeeks.org")
            print("PA - opening geeksforgeeks...")
            speakPA("opening geeksforgeeks")
            myQuery = tcommandfromMaster().lower()

        elif "open college website" in myQuery:
            webbrowser.open("jmit.ac.in")
            print("PA - opening jmit...")
            speakPA("opening jmit")
            myQuery = tcommandfromMaster().lower()

        elif "open spotify" in myQuery:
            webbrowser.open("spotify.com")
            print("PA - opening spotify")
            speakPA("opening spotify")
            myQuery = tcommandfromMaster().lower()

        elif "open gaana" in myQuery:
            webbrowser.open("gaana.com")
            print("PA - opening gaana")
            speakPA("opening gaana")
            myQuery = tcommandfromMaster().lower()

        elif "open hungama" in myQuery:
            webbrowser.open("hungama.com")
            print("PA - opening hungama")
            speakPA("opening hungama")
            myQuery = tcommandfromMaster().lower()

        elif "open twitter" in myQuery:
            webbrowser.open("twitter.com")
            print("PA - opening twitter")
            speakPA("opening twitter")
            myQuery = tcommandfromMaster().lower()

        elif "open udemy" in myQuery:
            webbrowser.open("udemy.com")
            print("PA - opening udemy")
            speakPA("opening udemy")
            myQuery = tcommandfromMaster().lower()

        elif "open leet code" in myQuery:
            webbrowser.open("leetcode.com")
            print("PA - opening leetcode")
            speakPA("opening leetcode")
            myQuery = tcommandfromMaster().lower()

        elif "open hacker Earth" in myQuery:
            webbrowser.open("hackerearth.com")
            print("PA - opening hackerearth")
            speakPA("opening hackerearth")
            myQuery = tcommandfromMaster().lower()

        elif "open maps" in myQuery:
            webbrowser.open("maps.google.com")
            print("PA - opening maps")
            speakPA("opening maps")
            myQuery = tcommandfromMaster().lower()

        elif "open netflix" in myQuery:
            webbrowser.open("netflix.com")
            print("PA - opening netflix")
            speakPA("opening netflix")
            myQuery = tcommandfromMaster().lower()

        elif "open Prime video" in myQuery:
            webbrowser.open("primevideo.com")
            print("PA - opening prime video")
            speakPA("opening prime video")
            myQuery = tcommandfromMaster().lower()

        elif "open hotstar" in myQuery:
            webbrowser.open("hotstar.com")
            print("PA - opening hotstar")
            speakPA("opening hotstar")
            myQuery = tcommandfromMaster().lower()

        elif "open my protein" in myQuery:
            webbrowser.open("myprotein.com")
            print("PA - opening myprotein")
            speakPA("opening myprotein")
            myQuery = tcommandfromMaster().lower()

        elif "open sony" in myQuery:
            webbrowser.open("sonyliv.com")
            print("PA - opening sonyliv")
            speakPA("opening sonyliv")
            myQuery = tcommandfromMaster().lower()

        elif "open airtel" in myQuery:
            webbrowser.open("airtel.in")
            print("PA - opening airtel")
            speakPA("opening airtel")
            myQuery = tcommandfromMaster().lower()

        elif "open v i" in myQuery:
            webbrowser.open("myvi.in")
            print("PA - opening vodafone idea")
            speakPA("opening vodafone idea")
            myQuery = tcommandfromMaster().lower()

        elif "open HDFC" in myQuery:
            webbrowser.open("hdfcbank.com")
            print("PA - opening hdfc")
            speakPA("opening hdfc")
            myQuery = tcommandfromMaster().lower()

        elif "open sbi" in myQuery:
            webbrowser.open("onlinesbi.com")
            print("PA - opening sbi")
            speakPA("opening sbi")
            myQuery = tcommandfromMaster().lower()

        elif "open linkedin" in myQuery:
            webbrowser.open("linkedin.com")
            print("PA - opening linkedin")
            speakPA("opening linkedin")
            myQuery = tcommandfromMaster().lower()

        elif "open microsoft" in myQuery:
            webbrowser.open("microsoft.com")
            print("PA - opening microsoft")
            speakPA("opening microsoft")
            myQuery = tcommandfromMaster().lower()
            
        elif 'play music' in myQuery:
            # Play music from a specified directory
            # music_dir = 'D:\\song'
            music_dir = 'C:\\Users\\HP\\PycharmProjects\\Virtual Personal Assistant\\Song'
            song = os.listdir(music_dir)
            print(f"PA - {song}")
            song_num = random.randint(0,4)
            os.startfile(os.path.join(music_dir, song[song_num]))
            time.sleep(60)
            myQuery = tcommandfromMaster().lower()

            
        elif 'code' in myQuery:
            # Open code editor
            cpathh = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(cpathh)
            myQuery = tcommandfromMaster().lower()

        elif 'pycharm' in myQuery:
            # Open PyCharm IDE
            pypath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2023.1\\bin\\pycharm64.exe"
            os.startfile(pypath)
            myQuery = tcommandfromMaster().lower()

        elif "right" in myQuery:
            # Move cursor to the right
            print("PA - moving cursor to right")
            speakPA("moving cursor to right")
            pyautogui.moveRel(1100, 0, 2)
            print("PA - cursor moved to right")
            speakPA("cursor moved to right")
            myQuery = tcommandfromMaster().lower()
            
        elif "left" in myQuery:
            # Move cursor to the left
            print("PA - moving cursor to left")
            speakPA("moving cursor to left")
            pyautogui.moveRel(-400, 0, 2)
            print("PA - cursor moved to left")
            speakPA("cursor moved to left")
            myQuery = tcommandfromMaster().lower()
            
        elif "down" in myQuery:
            # Move cursor downwards
            print("PA - moving cursor to down")
            speakPA("moving cursor to down")
            pyautogui.moveRel(600, 700, 2)
            print("PA - cursor moved to downwards")
            speakPA("cursor moved to downwards")
            myQuery = tcommandfromMaster().lower()

        elif "up" in myQuery:
            # Move cursor upwards
            print("PA - moving cursor to up")
            speakPA("moving cursor to up")
            pyautogui.moveTo(1266, 15, 2)
            print("PA - cursor moved to upwards")
            speakPA("cursor moved to upwards")
            myQuery = tcommandfromMaster().lower()

        elif "right click" in myQuery:
            # Perform right-click action
            pyautogui.click(x=1000, y=500, clicks=1, button='right')
            myQuery = tcommandfromMaster().lower()

        elif "bluetooth" in myQuery:
            # Toggle Bluetooth
            print("PA - Toggling Bluetooth")
            speakPA("Toggling Bluetooth")
            # pyautogui.moveTo(1266, 15, 2)
            # pyautogui.moveTo(1777, 21, 2)
            # pyautogui.click()
            pyautogui.moveTo(1550,1078, 2)
            pyautogui.click()
            pyautogui.moveTo(1567,924, 1)
            pyautogui.click()
            pyautogui.moveTo(1643,730, 1)
            pyautogui.click()
            myQuery = tcommandfromMaster().lower()

        elif "windows" in myQuery:
            # Press Windows keypython in one video
            pyautogui.press('win')
            myQuery = tcommandfromMaster().lower()
            
        elif "video" in myQuery:
            # Play a YouTube video when asked to "video"
            # pyautogui.moveTo(1239, 1047, 2)
            # pyautogui.click()
            # pyautogui.moveTo(345, 98, 2)
            # pyautogui.click()
            pyautogui.moveTo(707, 119, 2)
            pyautogui.click()
            keys = [['p', 'y', 't', 'h', 'o', 'n', 'space', 'i', 'n', 'space', 'o', 'n', 'e', 'space', 'v', 'i', 'd',
                     'e', 'o'], ['s', 'i', 'd', 'h', 'u', 'space', 'm', 'o', 'o', 's', 'e', 'w', 'a', 'l', 'a']]
            typingkey = random.choice(keys)
            pyautogui.press(typingkey)
            pyautogui.press('enter')
            myQuery = tcommandfromMaster().lower()


        elif ("quit" or "bye") in myQuery:
            # Say goodbye and exit when asked to "quit" or "bye"
            lst = ["Until next time", "Nice serving you", "byee", "Have a good day"]
            rnd = random.randint(0, 3)
            print(f"PA - {lst[rnd]}")
            speakPA(lst[rnd])
            exit()

        elif("ok"or"thanks") in myQuery:
            lst = ["No Problem","no probem"]
            rnd = random.randint(0, 1)
            print(f"PA - {lst[rnd]}")
            speakPA(lst[rnd])
            exit()
            
        elif "game" in myQuery:
            # Play interactive games when asked to "game"
            print("PA - Which game would you like to play. I have these")
            print(
                "PA - 1.Guess a number \n 2.Guess the animal \n 3. Flip a coin and get a chance to command me more if you win ")
            speakPA("Which game would you like to play. I have these")

            x = int(input("Enter here: "))
            if (x == 1):
                rnd = random.randint(0, 100)
                print("PA - Guess the number")
                speakPA("Guess the number")
                count = 0
                flag = True
                while (flag):
                    inp = int(input("Guess the number: "))

                    if (inp > rnd):
                        print("PA - Your number is larger")
                        speakPA("Your number is larger")
                        count += 1
                    if (inp < rnd):
                        print("PA - Your number is smaller")
                        speakPA("Your number is smaller")
                        count += 1
                    else:
                        print("PA - Yayy! You guessed it in " + str(count) + " times")
                        speakPA("Yayy! You guessed it in " + str(count) + " times")
                        flag = False
            if (x == 2):
                print("PA - Guess the animal")
                speakPA("Guess the animal")
                lst = ["lion", "giraffe", "goat", "dog", "penguin", "cat", "monkey", "tiger", "cheetah", "cow"]
                rndd = random.randint(0, 9)
                anm = lst[rndd]
                print("PA - 3... 2... 1......")
                print("PA - Guess it now...")
                inp = tcommandfromMaster().lower()
                if (inp == anm):
                    print("PA - Congratulations you guessed right")
                else:
                    print("PA - Beep Beep wrong")
            myQuery = tcommandfromMaster().lower()


        else:
            # If no recognized command, inform the user
            print("PA - Sorry,That maybe beyond my abilities at the moment. Try Something different")
            speakPA("Sorry,That maybe beyond my abilities at the moment. Try Something different")
            myQuery = tcommandfromMaster().lower()