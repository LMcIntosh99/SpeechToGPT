import speech_recognition as sr
import pyttsx3
import tkinter as tk
from threading import Thread
from gpt import ask_chatgpt


class SpeechRecognitionGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Speech Recognition")

        self.status_label = tk.Label(master, text="Waiting for prompt...")
        self.status_label.pack()

        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()

        self.listen_button = tk.Button(master, text="Start Listening", command=self.start_listening)
        self.listen_button.pack()

    def start_listening(self):
        self.listen_button.config(state="disabled")
        self.status_label.config(text="Adjusting for ambient noise...")
        self.listen_thread = Thread(target=self.listen)
        self.listen_thread.start()

    def listen(self):
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)

            self.status_label.config(text="Listening...")
            audio = self.recognizer.listen(source, phrase_time_limit=10)

            self.status_label.config(text="Processing...")
            try:
                text = self.recognizer.recognize_google(audio)
                self.status_label.config(text="Heard: " + text)
                response = ask_chatgpt(text)
                self.status_label.config(text="Response: " + response)
                self.engine.say(response)
                self.engine.runAndWait()
            except sr.UnknownValueError:
                self.status_label.config(text="Unable to recognize speech")
            except sr.RequestError:
                self.status_label.config(text="Error requesting results")
            finally:
                self.listen_button.config(state="normal")


root = tk.Tk()
my_gui = SpeechRecognitionGUI(root)
root.mainloop()
