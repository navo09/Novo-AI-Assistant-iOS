import speech_recognition as sr
import webbrowser
import requests
from gtts import gTTS
import pygame
import os
import pyttsx3
from deep_translator import GoogleTranslator
from google import genai
import musicLibrary
from groq import Groq




import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# তোর গিটহাব টোকেন এখানে দিবি (No Expiration টোকেনটা)
GITHUB_TOKEN = "your git-token"
endpoint = "https://models.inference.ai.azure.com"

# গিটহাব ক্লায়েন্ট তৈরি
client_gh = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(GITHUB_TOKEN)
)

# এপিআই কি

NEWS_API_KEY = "your news api"




recognizer = sr.Recognizer()

def speak(text):
    print(f"ATX Speaking: {text}")
    engine = pyttsx3.init()
    engine.setProperty('rate', 175) 
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def speak_bangla(text):
    try:
        tts = gTTS(text=text, lang='bn')
        tts.save("news.mp3")
        pygame.mixer.init()
        pygame.mixer.music.load("news.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
        pygame.mixer.quit()
        if os.path.exists("news.mp3"):
            os.remove("news.mp3")
    except Exception as e:
        print(f"Bangla Speak Error: {e}")

def aiProcess(command):
    try:
        response = client_gh.complete(
            messages=[
                SystemMessage(content="You are a helpful assistant named Novo."),
                UserMessage(content=command),
            ],
            model="gpt-4o-mini", # একদম ফ্রি এবং ফাস্ট মডেল
        )
        # এআই এর উত্তর রিটার্ন করা
        return response.choices[0].message.content
    except Exception as e:
        return f"AI Error: {e}"

def processCommand(c):
    c_lower = c.lower().strip()
    
    if "open google" in c_lower:
        webbrowser.open("https://google.com")
    elif "open facebook" in c_lower:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c_lower:
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    
    elif c_lower.startswith("play"):
        song = c_lower.split(" ")[1]
        if song in musicLibrary.music:
            webbrowser.open(musicLibrary.music[song])
        else:
            speak("Song not found.")

    elif "news in bangla" in c_lower:
        r = requests.get(f"https://newsapi.org/v2/everything?q=bangladesh&sortBy=publishedAt&apiKey={NEWS_API_KEY}")
        if r.status_code == 200:
            articles = r.json().get('articles', [])
            speak("Reading news in Bengali.")
            for article in articles[:3]:
                title = article['title']
                translated = GoogleTranslator(source='auto', target='bn').translate(title)
                print(f"Bengali News: {translated}")
                speak_bangla(translated)

    elif "news in english" in c_lower:
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}")
        if r.status_code == 200:
            articles = r.json().get('articles', [])
            speak("Here are the top headlines.")
            for article in articles[:5]:
                title = article.get("title")
                if title:
                    speak(title)
        else:
            speak("Failed to fetch news.")

    else:
        # এখানে 'command' এর বদলে 'c' ফিক্স করা হয়েছে
        output = aiProcess(c)
        print(f"\nAI Response: {output}")

        is_bangla = any('\u0980' <= char <= '\u09FF' for char in output)
        if is_bangla:
            speak_bangla(output)
        else:
            speak(output)

if __name__ == "__main__":
    speak("ATX is online.")
    
    while True:
        try:
            print("\n1. Say 'ATX' | 2. Type Command")
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=2)
                word = recognizer.recognize_google(audio)

            if word.lower() == "ATX":
                speak("Yes Boss?")
                with sr.Microphone() as source:
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    processCommand(command)

        except Exception:
            user_input = input("Type command: ")
            if user_input.strip():
                processCommand(user_input)