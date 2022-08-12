from time import sleep
from selenium.webdriver.common.alert import Alert

from common import setup_chrome_webdriver
from screenshot import get_full_screenshot_image


def get_geolocation(domain, ipv4, nowStr):

    driver = setup_chrome_webdriver()

    driver.get('https://www.geolocation.com/')

    sleep(1)

    Alert(driver).accept()

    ip_input = driver.find_element_by_xpath(
        '/html/body/div[2]/div/div[1]/div[3]/div/div/form/div/input')
    ip_input.clear()
    ip_input.send_keys(ipv4)

    sleep(1)

    driver.find_element_by_xpath(
        '/html/body/div[2]/div/div[1]/div[3]/div/div/form/div/div/button').click()

    sleep(5)

    data = {
        "screenshot_path": ""
    }

    try:
        # 検索処理が成功していることの確認
        driver.find_element_by_xpath(
            '//*[@id="ipresult"]/div[2]/div[1]/table/tbody/tr[2]/td[1]'
        )

        screenshot = get_full_screenshot_image(driver)
        screenshot_path = 'screenshot/' + domain + '_geolocation_' + nowStr + '.png'
        screenshot.save(screenshot_path)

        data['screenshot_path'] = screenshot_path

    except:
        print("error")

    driver.close()

    return data
