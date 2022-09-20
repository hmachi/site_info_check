from time import sleep
from common import setup_chrome_webdriver
import os


def get_site_info(url, domain, nowStr):

    driver = setup_chrome_webdriver()

    driver.get(url)

    sleep(1)

    try:
        os.makedirs('screenshot/' + domain + "/site", exist_ok=True)
    except:
        print("フォルダ作成エラー")

    screenshot_path = 'screenshot/' + domain + '/site/'

    driver.set_window_size(1000, 800)
    sleep(1)
    driver.save_screenshot(screenshot_path + "top_" + nowStr + ".png")

    driver.close()

    return {
        'screenshot_path': screenshot_path + "top_" + nowStr + ".png"
    }
