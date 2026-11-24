#Step-1 : pip install pyttsx3 (converts text into voice)

import pyttsx3

#datetime gives current date and time 
from datetime import datetime

#Define a function to speak text
def speak(text):
    print("🤖 AI Bot: ",text)

    #Initialize the text-to-speech engine.
    # Creates a speech engine to use methods like say(), runAndWait() and setProperty().
    engine = pyttsx3.init('sapi5')
    engine.say(text)
    engine.runAndWait()
    engine.stop()

#greet
print("NOVA : Hello! I am NOVA-your python ai assistant. Type 'exit' to end\n ")

#Start chatting loop
while True:
    user=input("👤 You: ").lower()

    if "hello" in user or "hi" in user:
        speak("Hello! I am NOVA , How may I assist you today?")

    elif "how are you" in user:
        speak("I am just code but I feel awesome helping you.")

    elif "name" in user:
        speak("My name is NOVA- your python AI assistant.")

    elif "time" in user:
        current_time=datetime.now().strftime("%H : %M : %S")
        speak(current_time)

    elif "date" in user:
        speak(str(datetime.now().date()))

    elif "calculate" in user:
        try:
            result=eval(user.replace("calculate",""))
            speak(f"Result is: {result}")
        except:
            speak("I could not understand the calculation.")
    elif "exit" in user:
        speak("Goodbye! Have a nice day.")
        break

    else:
        speak("Sorry!I could not understand the command.")