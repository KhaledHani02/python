import speech_recognition as sr
import  PySimpleGUI as sg

recognizer_instance = sr.Recognizer()

layout = [[sg.Text('Converter', font='Helvetica 15')],
          [sg.ReadButton('Speak'), sg.ReadButton('Stop')],
          [sg.Output(size=(80, 10))],
          [sg.Exit()]]

window = sg.Window('Speech Recognition').Layout(layout)

while True:
    event,values = window.Read()
    if event is None or event == 'Exit':
        break
    elif event == 'Speak':
        with sr.Microphone() as source:
            recognizer_instance.adjust_for_ambient_noise(source)
            audio = recognizer_instance.listen(source)
            value = recognizer_instance.recognize_google(audio, language="ar-AR")
            with open("file.txt", "a", encoding="utf-8") as file:
                file.write(value+"\n") 
                file.close()
            print(value)

window.Close()