import json
from webdriver import Browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def config_browser():
    with open('Resources/config.json') as f:
        data = json.load(f)
        f.close()
    if 'browser' not in data:
        raise Exception('The config file does not contain "browser"')
    elif data['browser'] not in ['chrome', 'firefox']:
        raise Exception(f'"{data["browser"]}" is not a supported browser')
    return data


def get_data():
    with open('Resources/data.json') as f:
        data = json.load(f)
        f.close()
    return data
