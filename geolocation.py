from time import sleep
from selenium.webdriver.common.alert import Alert
import os

from common import setup_chrome_webdriver, disp_content, get_full_screenshot_image


def get_geolocation(domain, ipv4, nowStr):

    driver = setup_chrome_webdriver()

    driver.get('https://www.geolocation.com/')

    sleep(1)

    try:
        Alert(driver).accept()
    except:
        print("アラート無し")

    ip_input = driver.find_element_by_xpath(
        '/html/body/div[2]/div/div[1]/div[3]/div/div/form/div/input')
    ip_input.clear()
    ip_input.send_keys(ipv4)

    sleep(1)

    driver.find_element_by_xpath(
        '/html/body/div[2]/div/div[1]/div[3]/div/div/form/div/div/button').click()

    sleep(10)

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

        try:
            os.makedirs('screenshot/' + domain + "/geolocation", exist_ok=True)
        except:
            print("フォルダ作成エラー")

        screenshot_path = 'screenshot/' + domain + '/geolocation/'

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
            '//*[@id="ipresult"]/div[2]/div[2]',
        ]

        disp_content_list = [
            '//*[@id="ipresult"]',
            '/html/body/div[3]/div/div[1]/div[5]/div/div/div[1]',
            '/html/body/div[3]/div/div[1]/div[5]/div/div/div[2]'
        ]

        notDispResult = False
        processCount = 0
        while notDispResult == False:
            # 取得要素以外を非表示にする
            notDispResult = disp_content(
                driver, not_disp_content_list, "", True)
            processCount += 1

            if processCount > 3:
                return False

        # padding削除
        driver.execute_script(
            "arguments[0].setAttribute('style','padding-top: 0px;')", driver.find_element_by_xpath(
                '/html/body/div[3]'
            ))

        # 地図テーブル以外非表示
        if disp_content(driver, disp_content_list, [0], False):
            # 画面サイズ変更
            driver.set_window_size(800, 750)
            # 上部までスクロール
            driver.execute_script("window.scrollBy(0, -1000);")

            file_path = screenshot_path + "map_" + nowStr + ".png"
            driver.save_screenshot(file_path)
            data['screenshot_path_list'].append(file_path)

            # 地図の非表示
            driver.execute_script(
                "arguments[0].setAttribute('style','display: none;')", driver.find_element_by_xpath(
                    '//*[@id="ipresult"]/div[2]/div[1]/table/tbody/tr[1]/td/div'
                ))

            # 画面サイズ変更
            driver.set_window_size(800, 850)

            file_path = screenshot_path + "mapdata_" + nowStr + ".png"
            get_full_screenshot_image(driver, file_path)
            data['screenshot_path_list'].append(file_path)

        # Try Our IP2Location Geolocation API以外非表示
        if disp_content(driver, disp_content_list, [1], False):
            # 画面サイズ変更
            driver.set_window_size(800, 1000)

            sleep(1)

            file_path = screenshot_path + "ip2location_" + nowStr + ".png"
            get_full_screenshot_image(driver, file_path)
            data['screenshot_path_list'].append(file_path)

        # Try Our IP2Proxy Geolocation API以外非表示
        if disp_content(driver, disp_content_list, [2], False):
            # 画面サイズ変更
            driver.set_window_size(800, 900)

            sleep(1)

            file_path = screenshot_path + "ip2proxy_" + nowStr + ".png"
            get_full_screenshot_image(driver, file_path)
            data['screenshot_path_list'].append(file_path)

    except Exception as e:
        print(e)

    driver.close()

    return data
