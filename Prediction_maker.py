#importing pyttsx3 pythons speech api
import pyttsx3

# commands to set properties for speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
newVoiceRate = 140
engine.setProperty('rate', newVoiceRate)
engine.setProperty('volume', 1)


# this function gives the audio output
def speak(audio):
    print(audio)
    engine.say(audio)
    engine
    engine.runAndWait()


speak("Write your name and I will predict your future! ")
# empty string to store the value
output = ""
# keeps the count of inputs
count = 0
# command to stop the program
end = "quit"
while True:
    # variable to store the name
    name = input("Write here: ").lower()
    # already defined dictionaries
    prediction = {
        "<write the name>": '''<here write want you want to predict about the name> 
    '''

    }
    ### to check weather the input is present in the dictionary if present then speak the result
    if "hrithik" in name:
        if count == 0:
            output = prediction.get("hrithik")
            count += 1
        elif count > 0:
            output = "I already predicted your future!"
        speak(output)
    elif name == end:
        break
    else:
        output = prediction.get(name, "sorry i don't have enough data to predict your future!")
        speak(output)
###
