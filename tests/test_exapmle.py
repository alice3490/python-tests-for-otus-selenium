from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def test_one():
    options = Options()
    options.binary_location = "C:/Users/agostkina/web_drivers/yandexdriver.exe"
    service = Service(executable_path="C:/Users/agostkina/web_drivers/yandexdriver.exe")
    browser = webdriver.Chrome(service=service, options=options)
    browser.get("https://google.com")
    assert browser.title == "Google"