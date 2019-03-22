from gtts import gTTS
import speech_recognition as sr 
import os
import webbrowser
import smtplib

def talktome(audio):
    print(audio)
    tts = gTTS(text=audio, lang='en')
    tts.save('audio.mp3')
    os.system('mpg123 audio.mp3')

# Listen for commands
def mycommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('I am ready for your next command')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration =1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said: " + command + "/n")
    # loop back to continue to listen for commands

    except sr.UnknownValueError:
        assistant(mycommand())

    return command

# if statement for executing commands
def assistant(command):
    if 'open Reddit Python' in command:
        chrome_path = "/usr/bin/google-chrome"
        url = 'https://www.reddit.com/r/python'
        webbrowser.get(chrome_path).open(url)

    if "What's up" in command:
        talktome("Waiting instructions")

    if 'email' in command:
        talktome('Who is the recipient')
        recipient = mycommand()

        if 'Rachid' in recipient:
            talktome('What shoul I send')
            content = mycommand()

            # init gmail smtp
            mail = smtplib.SMTP('smtp.gmail.com', 587)

            # Identify to server
            mail.ehlo()

            # encrypt session
            mail.starttls()

            # Login
            mail.login('username', 'password')

            # send message
            mail.sendmail('PERSON NAME', 'email address@wwww.com', content)

            # close mail connection
            mail.close()

            talktome("email sent")

talktome("I am ready for your commands")

while True:
    assistant(mycommand())
