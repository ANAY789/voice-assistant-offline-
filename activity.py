import speech_recognition as sr
import pyttsx3
from googletrans import Translator
def speak(text,language="en"):
    engine = pyttsx3.init()
    engine.setProperty('rate',150)
    voices = engine.getProperty('voices')
    if language == "en":
        engine.setProperty('voices',voices[0].id)
    else:
        engine.setProperty('voices',voices[1].id)
    engine.say(text)
    engine.runAndWait()
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("please speak now in english")
        audio = recognizer.listen(source)
    try:
        print("recognizing speech .. ")
        text = recognizer.recognize_google(audio,language="en-us")
        print(f"you said {text}")
        return text
    except sr.UnknownValueError:
        print("could not understand the audio")
    except sr.RequestError as e:
        print(f"api error:{e}")
    return ""
def translate_text(text,target_language="es"):
    translator = Translator()
    translation = translator.translate(text,dest=target_language)
    print(f"translated text:{translation.text}")
    return translation.text
def display_language_options():
    print("available translation languages:")
    print("1.hindi (hi)")
    print("2.tamil (ta)")
    print("3.telegu (te)")
    print("4.bengali(bn)")
    print("5.Marathi (mr)")
    print("6.gujarati (gu)")
    print("7.malayalam (ml)")
    print("8. punjabi (pa)")

    choice = input("please select the target language number (1-8):")
    language_dict = {"1":"hi",
                     "2":"ta",
                     "3":"te",
                     "4":"bn",
                     "5":"mr",
                     "6":"gu",
                     "7":"ml",
                     "8":"pa"}
    return language_dict.get(choice,"es")
def main():
    target_language=display_language_options()
    original_text = speech_to_text()
    if original_text:
        translated_text = translate_text(original_text,target_language=target_language)
        speak(translated_text,language="en")
        print("translated spoken out")
if __name__ == "__main__":
    main()