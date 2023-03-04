import requests


def chatbot(text):
    API = f"http://yumikoapi.herokuapp.com/chatbot?text={text}"
    req = requests.get(API).json()["url"]
    return(req)
