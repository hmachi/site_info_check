from time import sleep
from common import setup_chrome_webdriver


def get_site_info(url, domain, nowStr):

    driver = setup_chrome_webdriver()

    driver.get(url)

    sleep(1)

    screenshot_path = 'screenshot/' + domain + '_site_' + nowStr + ".png"

    driver.set_window_size(1000, 800)
    sleep(0.5)
    driver.save_screenshot(screenshot_path)

    driver.close()

    return {
        'screenshot_path': screenshot_path
    }
