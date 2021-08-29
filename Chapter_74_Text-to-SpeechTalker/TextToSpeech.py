import pyttsx3

print('Text to Speech Talker')
print("""Text-to-speech using the pyttsx3 module, which in turn uses
the NSSpeechSynthesizer (on macOS), SAPI5 (on Windows), or eSpeak (on Linux) speech engines.
""")

engine = pyttsx3.init()
while True:
    print('Enter the text to speak, or QUIT to quit.')
    userText = input('> ').upper()

    if userText == 'QUIT':
        print('Thanks for playing!')
        break

    engine.say(userText)
    engine.runAndWait()
