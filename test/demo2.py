import os
import time
import speech_recognition as sr
from gtts import gTTS
import transformers

class ChatBot:
    def __init__(self, name):
        self.name = name
        self.nlp = transformers.pipeline(
            "text-generation", model="microsoft/DialoGPT-medium")
        self.questions = [
            "What is your FirstName?",
            "What is your LastName?",
            "What is your email?",
            "What is your mobile number?",
            "What is your Age?",
            "What is your Sex?",
            "What is your Appointment date and time?"
        ]
        self.current_question_index = 0
        self.responses = []
        self.unanswered_questions = 0
        self.max_unanswered = 2

    def speech_to_text(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
            print("Listening...", end='\r')
            audio = recognizer.listen(mic)
            self.text = "ERROR"
        try:
            self.text = recognizer.recognize_google(audio)
            print("Patient Say: ", self.text)
            self.responses.append(self.text)
            self.unanswered_questions = 0
        except sr.UnknownValueError:
            print("Patient Say: ")
            self.unanswered_questions += 1

    def text_to_speech(self, text):
        print(f"Bot Say: {text}")
        speaker = gTTS(text=text, lang="en", slow=False)
        speaker.save("res.mp3")
        os.system('start res.mp3')
        time.sleep(2)
        os.remove("res.mp3")

    def handle_questions(self):
        if self.current_question_index < len(self.questions):
            return self.questions[self.current_question_index]
        else:
            return None

    def handle_conversation(self):
        welcome_message = f"Thank you for calling Vancouver dental clinic. My name is {
            self.name}, how may I assist you?"
        self.text_to_speech(welcome_message)

        while True:
            question = self.handle_questions()
            if question:
                self.text_to_speech(question)
                self.speech_to_text()
                self.current_question_index += 1
                if self.unanswered_questions >= self.max_unanswered:
                    self.text_to_speech(
                        "I'm sorry, but I didn't receive a response. Ending the conversation.")
                    break
            else:
                self.text_to_speech("Your appointment is Successfully booked")
                break

        self.text_to_speech("Bye")

if __name__ == "__main__":
    ai = ChatBot(name="AI Bot")
    ai.handle_conversation()
