# SpeechToGPT
This repository contains a Python-based speech recognition assistant that transcribes spoken input, processes it using the GPT-4o model. It is a little project I initially created in 2022, but updated recently.

# Features
- Speech-to-Text: Converts spoken language into text using Google Speech Recognition.
- GPT-4o Integration: Sends transcribed text to the GPT-4o model for intelligent responses.
- Text-to-Speech: Converts the GPT-4o's response back into spoken audio.
- Graphical User Interface (GUI): Simple Tkinter-based interface for interaction.
- Ambient Noise Adjustment: Automatically adjusts for varying levels of background noise.

# Requirements
Before running the application, ensure you have the following installed:
- Python 3.x
- openai library
- SpeechRecognition library
- pyttsx3 library
- tkinter (usually included with Python)
- An OpenAI API key.

# Setup
- Clone the repository
- Create a config.py file in the same directory as gpt.py and add your OpenAI API key.

Python
```python
# config.py
gpt_api_key = "YOUR_OPENAI_API_KEY"
```

# How to Run
Execute the speech_to_text.py script:

```Bash
python speech_to_text.py
```
