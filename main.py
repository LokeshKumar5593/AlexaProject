import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
from datetime import datetime
import pyjokes

def talk(answer):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(answer)
    engine.runAndWait()

def processQuestion(question):
    if 'what are you doing' in question:
        print("I am waiting for your question ")
        talk("I am waiting for your question")
        return True

    elif 'how are you' in question:
        print("I am good, thank you. How can I help you?")
        talk("I am good, thank you. How can I help you?")
        return True

    elif 'play' in question:
        talk("Now, I am Playing song for You Enjoy")
        pywhatkit.playonyt(question)
        return True

    elif 'who is' in question:
        question = question.replace("Who is", '')
        print(wikipedia.summary(question, 1))
        talk(wikipedia.summary(question, 1))
        return True

    elif 'time' in question:
        time = datetime.today().time().strftime("%I:%M %p")
        print(time)
        talk(time)
        return True

    elif 'joke' in question:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())
        return True

    elif "Tata" in question:
        talk("Bye Bye , Please take Care. Will meet you again later")
        return False

    else:
        print("I didn't get you, Can you say that once again?")
        talk("I didn't get you, Can you say that once again?")
        return True

def getQuestion():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something")
        audio = r.listen(source)
    try:
        print(r.recognize_google(audio))
        question = r.recognize_google(audio)
        if 'Lokesh' in question:
            question = question.replace('Lokesh','')
            print(question)
            return question
        else:
            # print("You are not talking with me carry on.")
            # talk("You are not talking with me carry on.")
            return "notwithme"

    except sr.UnknownValueError:
        print("Sorry, I can't get your question")
        talk("Sorry, I can't get your question")


canAskQuestion = True
while canAskQuestion:
    question=getQuestion()

    if(question=="notwithme"):
        print("You are not talk with me.Carry-on with your friends, bye bye!")
        talk("You are not talk with me.Carry-on with your friends, bye bye!")
        canAskQuestion=False
    else:
        canAskQuestion=processQuestion(question)