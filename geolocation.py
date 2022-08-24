from time import sleep
from selenium.webdriver.common.alert import Alert

from common import setup_chrome_webdriver


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
        "country": "",
        "screenshot_path_list": []
    }

    try:
        # 検索処理が成功していることの確認
        driver.find_element_by_xpath(
            '//*[@id="ipresult"]/div[2]/div[1]/table/tbody/tr[2]/td[1]'
        )

        data["country"] = driver.find_element_by_xpath(
            '//*[@id="ipresult"]/div[2]/div[1]/table/tbody/tr[2]/td[1]').text

        index = 1
        screenshot_path = 'screenshot/' + domain + '_geolocation_' + nowStr + '_'

        driver.set_window_size(1000, 850)

        # ヘッダー要素を非表示にする
        driver.execute_script(
            "arguments[0].setAttribute('style','display: none;')", driver.find_element_by_xpath(
                '/html/body/div[2]/div/div'
            ))

        driver.save_screenshot(screenshot_path + str(index) + ".png")
        data['screenshot_path_list'].append(
            screenshot_path + str(index) + ".png")
        index += 1

        driver.execute_script("window.scrollBy(0, 450);")
        driver.save_screenshot(screenshot_path + str(index) + ".png")
        data['screenshot_path_list'].append(
            screenshot_path + str(index) + ".png")
        index += 1

        driver.execute_script("window.scrollBy(0, 600);")
        driver.save_screenshot(screenshot_path + str(index) + ".png")
        data['screenshot_path_list'].append(
            screenshot_path + str(index) + ".png")
        index += 1

        driver.execute_script("window.scrollBy(0, 400);")
        driver.save_screenshot(screenshot_path + str(index) + ".png")
        data['screenshot_path_list'].append(
            screenshot_path + str(index) + ".png")
        index += 1

        driver.execute_script("window.scrollBy(0, 600);")
        driver.save_screenshot(screenshot_path + str(index) + ".png")
        data['screenshot_path_list'].append(
            screenshot_path + str(index) + ".png")
        index += 1

    except:
        print("error")

    driver.close()

    return data
