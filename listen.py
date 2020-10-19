import speech_recognition as sr

r=sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Listening...")
    audio=r.listen(source,timeout=3,phrase_time_limit=5)
    print(audio)
    try:  
        statement=r.recognize_google(audio,language='en-in')
        print(f"user said:{statement}\n")

    except Exception as e:
        print("Pardon me, please say that again")
        print('None')
    print(statement)