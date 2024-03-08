import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine=pyttsx3.init()


def capture_voice_input():
    with sr.Microphone() as source:
        engine=pyttsx3.init()
        engine.say("Listening")
        engine.runAndWait()
        audio = recognizer.listen(source)
    return audio 
def convert_voice_to_text(audio):
    try:
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        text = ""
        engine.say("Sorry, I didn't understand that.")
        engine.runAndWait()
    except sr.RequestError as e:
        text = ""
        print("Error; {0}".format(e))
    return text
def process_voice_command(text):
    if "hello" in text.lower():
        engine.say("Hello! How can I help you?")
        engine.runAndWait()
    elif "goodbye" in text.lower():
        engine.say("Goodbye! Have a great day!")
        engine.runAndWait()
        return True
    else:
        engine.say("I didn't understand that command. Please try again.")
        engine.runAndWait()
    return False
def main():
    end_program = False
    while not end_program:
        audio = capture_voice_input()
        text = convert_voice_to_text(audio)
        end_program = process_voice_command(text)

if __name__ == "__main__":
    main()



# def SpeakText(command):
#     engine=pyttsx3.init()
#     engine.say(command)
#     engine.runAndWait()
#     with sr.Microphone() as source:
#         r.adjust_for_ambient_noise(source, duration=0.2)
#         audio=r.listen(source)
#         Mytext=r.recoognise_google(audio)
#         Mytext=Mytext.lower()
#         print("Did You Sayyy.. "+Mytext)
#         SpeakText(Mytext)

# SpeakText("Hello")