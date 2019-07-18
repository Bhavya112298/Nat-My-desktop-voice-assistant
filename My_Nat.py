import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


dict = {'bhawik':'bhawiktannacurious@gmail.com','bhavya':'ayvahb22@gmail.com','dad':'rmgowd@gmail.com'}
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')


engine.setProperty('voice',voices[1].id)






def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=3 and hour<5:
        speak("it is too early to wake up. please go to sleep")
    elif hour>=5 and hour<7:
        speak("each morning we are born again what we do today is what matters the most. good morning ")
    elif hour>=7 and hour<12:
        speak("good morning. i hope you had your breakfast")
    elif hour>=12 and hour<=14:
        speak("good afternoon. hope you had a good lunch")
    elif hour>14 and hour<16:
        speak("such a lazy afternoon. you can take a nap if you want")
        
    elif hour>=16 and hour<21:
        speak("Good evening. i am Natasha Romanoff how can i help you? ")
    elif hour >=21 and hour <24:
        speak("Early to bed and early to rise makes a man healhy wealthy and wise. please go to sleep stop using your phone")


    elif hour >= 0 and hour <3:
        speak("sleep is essential go to sleep")
        
        
        
def takecommand(): 
    #it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Iam listening.....")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said:{query}\n")
        
    except Exception as e:
        print("Say that again please...")
        return "None"
    return(query)
        
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('sender@gmail.com','senderpassword')
    server.sendmail('sender@gmail.com',to,content)
   

        

if __name__ == "__main__":
    wishme()
    while(True):
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace('wikipedia',"")
            results = wikipedia.summary(query,sentences = 2)
            speak('According to wikipedia')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open geeksforgeeks' in query:
            webbrowser.open("geeksforgeeks.com")
        elif 'facebook' in query:
            webbrowser.open("facebook.com")
        elif 'play music' in query:
            music_dir='C:\\Users\\canara\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Ma'am, the time is {strTime}")
        elif 'email to recievername' in query:
            try:
                speak("what should i say")
                content = takecommand()
                to = 'reciever@gmail.com'
                sendEmail(to,content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("sorry unable to send the email at the moment. please try again")
                 
            
        elif 'quit' in query:
              speak("good bye. see you soon!")
              quit()
           
       
            

            
     
   
 
