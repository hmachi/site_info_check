from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def setup_chrome_webdriver():
    return webdriver.Chrome(ChromeDriverManager().install())
