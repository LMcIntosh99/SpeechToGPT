import speech_recognition as sr
import pyttsx3
import tkinter as tk
from threading import Thread
from gpt import ask_chatgpt


class SpeechRecognitionGUI:
    def __init__(self, master):
        """
        Initializes the GUI for the speech recognition application.

        Args:
            master (tk.Tk): The root Tkinter window.
        """
        self.master = master
        self.master.title("Speech Recognition")  # Set the window title

        # Label to display the current status of the application
        self.status_label = tk.Label(master, text="Waiting for prompt...")
        self.status_label.pack()

        # Initialize the speech recognizer and text-to-speech engine
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()

        # Button to start the listening process
        self.listen_button = tk.Button(master, text="Start Listening", command=self.start_listening)
        self.listen_button.pack()

    def start_listening(self):
        """
        Disables the listen button and starts the listening process in a new thread.
        This prevents the GUI from freezing during audio processing.
        """
        self.listen_button.config(state="disabled")  # Disable button to prevent multiple clicks
        self.status_label.config(text="Adjusting for ambient noise...")

        # Create and start new thread for listening
        self.listen_thread = Thread(target=self.listen)
        self.listen_thread.start()

    def listen(self):
        """
        Handles the core speech recognition, GPT-4o interaction, and text-to-speech.
        This method runs in a separate thread.
        """
        with sr.Microphone() as source:  # Use the default microphone as the audio source
            # Adjusts the recognizer for ambient noise levels for better accuracy
            self.recognizer.adjust_for_ambient_noise(source, duration=1)

            self.status_label.config(text="Listening...")  # Update status
            # Listen for audio input with a 10-second phrase time limit
            audio = self.recognizer.listen(source, phrase_time_limit=10)

            self.status_label.config(text="Processing...")  # Update status
            try:
                # Use Google Speech Recognition to convert audio to text and display it
                text = self.recognizer.recognize_google(audio)
                self.status_label.config(text="Heard: " + text)

                # Send the transcribed text to ChatGPT and get a response
                response = ask_chatgpt(text)
                self.status_label.config(text="Response: " + response)  # Display ChatGPT's response

                # Speak the response aloud
                self.engine.say(response)
                self.engine.runAndWait()
            except sr.UnknownValueError:
                # Handle cases where speech is unintelligible
                self.status_label.config(text="Unable to recognize speech")
            except sr.RequestError:
                # Handle errors related to the speech recognition service (e.g., no internet connection)
                self.status_label.config(text="Error requesting results")
            finally:
                # Re-enable the listen button after processing is complete or an error occurs
                self.listen_button.config(state="normal")


root = tk.Tk()
my_gui = SpeechRecognitionGUI(root)
root.mainloop()
