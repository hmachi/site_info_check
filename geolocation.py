from time import sleep
from selenium.webdriver.common.alert import Alert

from common import setup_chrome_webdriver, disp_content


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

        screenshot_path = 'screenshot/' + domain + '_geolocation_' + nowStr + '_'

        not_disp_content_list = [
            '/html/body/div[1]',
            '/html/body/div[2]',
            '/html/body/div[3]/div/div[1]/div[1]',
            '/html/body/div[3]/div/div[1]/div[2]',
            '/html/body/div[3]/div/div[1]/div[3]',
            '/html/body/div[3]/div/div[1]/div[5]/div/h2',
            '/html/body/div[3]/div/div[1]/div[5]/div/p',
            '/html/body/div[3]/div/div[1]/div[6]',
            '/html/body/div[3]/div/div[1]/div[7]',
            '/html/body/div[3]/div/div[2]',
            '/html/body/div[4]',
        ]

        disp_content_list = [
            '//*[@id="ipresult"]',
            '/html/body/div[3]/div/div[1]/div[5]/div/div/div[1]',
            '/html/body/div[3]/div/div[1]/div[5]/div/div/div[2]'
        ]

        # 取得要素以外を非表示にする
        disp_content(driver, not_disp_content_list, "", True)

        # padding削除
        driver.execute_script(
            "arguments[0].setAttribute('style','padding-top: 0px;')", driver.find_element_by_xpath(
                '/html/body/div[3]'
            ))

        # 地図以外非表示
        disp_content(driver, disp_content_list, 0, False)

        driver.set_window_size(1000, 800)
        driver.execute_script("window.scrollBy(0, -1000);")
        sleep(0.5)
        driver.save_screenshot(screenshot_path + "_map1.png")
        data['screenshot_path_list'].append(
            screenshot_path + "_map1.png")
        driver.set_window_size(1000, 1000)
        driver.execute_script("window.scrollBy(0, 1000);")
        sleep(0.5)
        driver.save_screenshot(screenshot_path + "_map2.png")
        data['screenshot_path_list'].append(
            screenshot_path + "_map2.png")

        # Try Our IP2Location Geolocation API以外非表示
        disp_content(driver, disp_content_list, 1, False)

        driver.set_window_size(1000, 1000)
        sleep(0.5)
        driver.save_screenshot(screenshot_path + "_ip2location.png")
        data['screenshot_path_list'].append(
            screenshot_path + "_ip2location.png")

        # Try Our IP2Proxy Geolocation API以外非表示
        disp_content(driver, disp_content_list, 2, False)

        driver.set_window_size(1000, 800)
        sleep(0.5)
        driver.save_screenshot(screenshot_path + "_ip2proxy.png")
        data['screenshot_path_list'].append(
            screenshot_path + "_ip2proxy.png")

    except Exception as e:
        print(e.message)

    # driver.close()

    return data
