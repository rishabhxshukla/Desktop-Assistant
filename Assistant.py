from tkinter import *
import speech_recognition as sr
import pyttsx3
import random
import datetime
import wikipedia
import webbrowser
import pyjokes
import subprocess
import os

# TKINTER
window = Tk()
window.title("Desktop Assistant")
window.geometry('540x640')
window.resizable(width=False, height=False)

# PYTTSX3
engine = pyttsx3.init()
engine.setProperty("rate", 130)

#-------------------------------------------------------------------------------------------------------#

# GREETING
A = ["Hi,nice to meet you","hello","Nice to meet you","hey,nice to meet you","good to meet you!"]
ch = random.choice(A)
engine.say(ch)
engine.runAndWait()


# MENU BAR
menu = Menu(window)
window.config(menu=menu)
filemenu = Menu(menu)

# View:
def fullscreen():
    window.resizable(width=True, height=True)
viewmenu = Menu(menu)
menu.add_cascade(label='View', menu=viewmenu)
viewmenu.add_command(label='Enable Fullscreen', command= fullscreen)

# Help:
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')
helpmenu.add_command(label='Check Version')

# Exit:
menu.add_cascade(label='Exit', command=window.quit)


# HEADING
heading = Label(text="Good evening! What can I do for you?", font=("Consolas", 18))
heading.pack(side="top")


# IMAGE
icon = PhotoImage(file = r"D:\PROGRAMMING\Python Programming\Python Project\icon.png", width=540, height=540)
l1 = Label(window, image = icon)
l1.pack()


# Function to make the assitant speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function which gets called repeatedly when the button is clicked
def onclick():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print()
            print("LISTENING...")
            voice = listener.listen(source)
            query = listener.recognize_google(voice)
            print("You said: " + query)
            query = query.lower()
            
            
            # PERSONAL QUESTIONS
            if "who are you" in query or "what can you do" in query:
                print('I am Desktop Assistant version 1.O.\n'
                      'I can tell you the current time. I can find articles for you from wikipedia.\n'
                      'I can open websites like YouTube, Gmail and Spotify. I can open different system applications on this computer and also explore the web for you.\n'
                      'I can get the top headlines from Times of India. I can tell you funny jokes and open few games for you. I can also turn-off your PC')
                speak('I am Desktop Assistant version 1 point O.'
                      'I can tell you the current time. I can find articles for you from wikipedia.'
                      'I can open websites like YouTube, Gmail and Spotify. I can open different system applications on this computer and also explore the web for you.'
                      'I can get the top headlines from Times of India. I can tell you funny jokes and open few games for you. I can also turn-off your PC')    
            elif "who made you" in query or "who created you" in query or "who developed you" in query:
                print("I was developed by Rishabh and Bhumika on 15th November, 2021")
                speak("I was developed by Rishabh and Bhoomika on 15th November, 2021")
            
            
            # TIME
            if "time" in query:
                time = datetime.datetime.now().strftime("%H:%M:%S")
                print(f"Sir, the time is {time} at the moment")
                speak(f"Sir, the time is {time} at the moment")       
                
            
            # WIKIPEDIA   
            if "wikipedia" in query:
                speak("Searching Wikipedia")
                query = query.replace("wikipedia","")
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak("According to Wikipedia " + result)
            
            
            # OPENING LINKS
            if "open youtube" in query:
                print("Opening YouTube..")
                speak("Opening YouTube")
                webbrowser.open('youtube.com')
            if "open google" in query:
                print("Opening Google..")
                speak("Opening Google")
                webbrowser.open('google.com')
            if "open gmail" in query:
                print("Opening GMail..")
                speak("Opening GMail")
                webbrowser.open('mail.google.com')
            if "open spotify" in query:
                print("Opening Spotify..")
                speak("Opening Spotify")
                webbrowser.open('open.spotify.com')
            if "open my class" in query:
                print("Opening My Class..")
                speak("Opening My Class")
                webbrowser.open('myclass.lpu.in')
            if "open u m s" in query:
                print("Opening UMS..")
                speak("Opening U M S")
                webbrowser.open('ums.lpu.in')
            
            
            # SYSTEM APPS
            if "play music" in query:
                print("Playing Music..")
                speak("Playing Music")
                os.system(r"D:\PROGRAMMING\Python Programming\Python Project\sampleaudio.mp3")
            if "open notepad" in query:
                print("Opening Notepad..")
                speak("Opening Notepad")
                os.system("Notepad")
            if "open browser" in query:
                print("Opening Browser..")
                speak("Opening Browser")
                os.startfile(r"C:\Program Files\Mozilla Firefox\firefox.exe")
            if "open epic games" in query:
                print("Opening Epic Games..")
                speak("Opening Epic Games")
                os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Epic Games Launcher.lnk")
            
            
            # JOKE
            if "joke" in query:
                joke = pyjokes.get_joke(language="en", category="neutral")
                print(joke)
                speak(joke)
                speak("How was it?")
            
            
            # NEWS
            if "news" in query:
                speak("Here are some headlines from the Times of India, Happy reading")
                news = webbrowser.open('https://timesofindia.indiatimes.com/home/headlines')
            
                    
            # SEARCH WEB
            if "search" in query:
                query = query.replace("search", "")
                speak("Searching" + query)
                webbrowser.open(query)
            
            
            # GAME
            if "play game" in query:
                print("Would you like to play Subway Surfers or Temple Run?")
                speak("Would you like to play Subway Surfers or Temple Run?")
                
                with sr.Microphone() as source:
                    print()
                    print("LISTENING...")
                    voice = listener.listen(source)
                    query = listener.recognize_google(voice)
                    print("You said: " + query)
                
                if "Subway Surfers" in query:
                    print("Opening Subway Surfers..")
                    speak("Opening Subway Surfers")
                    webbrowser.open('https://poki.com/en/g/subway-surfers')
                elif "Temple Run" in query:
                    print("Opening Temple Run..")
                    speak("Opening Temple Run")
                    webbrowser.open('https://poki.com/en/g/temple-run-2')
                else:
                    print("Sorry I could not recognize your input")
                    speak("Sorry I could not recognize your input")
            
            
            # EXIT PROGRAM
            if "exit program" in query:
                print("Exiting the program..")
                speak("Sorry to see you go. Closing the program.")
                os._exit(0)
                
            
            # LOG-OFF PC
            if "log off" in query or "shut down" in query:
                print("Ok, your pc will log off in 10 seconds make sure you exit from all applications")
                speak("Ok, your pc will log off in 10 seconds make sure you exit from all applications")
                subprocess.call(["shutdown", "/l"])       
    except:
        pass


# BUTTON
btn = Button(
    text = "Click to command", 
    font = ("Lucida Sans", 16), 
    width = 45,
    height = 2, 
    command = onclick,
    relief = "groove",
    fg = "Black",
    bg = "Cyan"
)
btn.pack(side="bottom")


# BUTTON COLOUR
def hover(e):
   btn.config(bg = "OrangeRed3", fg= "White")

def leave(e):
   btn.config(bg = "Cyan", fg= "Black")

#Binding the Enter and Leave Events to the Button:
btn.bind('<Enter>', hover)
btn.bind('<Leave>', leave)
window.mainloop()