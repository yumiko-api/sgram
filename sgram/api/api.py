import requests


def chatbot(message):
    API = f"http://yumikoapi.herokuapp.com/chatbot?message={message}"
    req = requests.get(API).json()["url"]
    return(req)
