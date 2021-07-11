import requests
import json
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.Spvoice")
    speak.Speak(str)

if __name__ == '__main__':
    # speak("news for today")
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=d7ca1f181e9847988d7e487d2fd88688"
    news = requests.get(url).text
    news_l = json.loads(news)
    art = news_l["articles"]
    for articles in art:
        speak(articles["title"])
        speak("Next news is ")
    speak("thanks for listening")