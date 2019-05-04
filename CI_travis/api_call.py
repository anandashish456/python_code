import requests

MENU_PROMPT = "Enter Name: "


def call_google():
    response = requests.get('https://www.google.com')
    return response


def get_input():
    value_from_user = input(MENU_PROMPT)
    return value_from_user
