from time import sleep

from common import setup_chrome_webdriver


def get_ip(domain, nowStr):

    driver = setup_chrome_webdriver()

    driver.get('https://sitereport.netcraft.com/')

    sleep(1)

    domain_input = driver.find_element_by_xpath(
        '//*[@id="site_report_query"]/div/input')
    domain_input.send_keys(domain)

    sleep(1)

    driver.find_element_by_xpath(
        '//*[@id="site_report_query"]/input').click()

    sleep(15)

    driver.find_element_by_xpath(
        '//*[@id="consent-form"]/div/button[2]').click()

    data = {
        "domain_name": "",
        "expiration_date": "",
        "domain_status": "",
        "name_server": "",
        "registrant_email": "",
        "admin_email": "",
        "creation_date": "",
        "registrar": "",
        "ipv4": "",
        "company": "",
        "host": "",
        "screenshot_path_list": []
    }

    try:
        # 検索処理が成功していることの確認
        driver.find_element_by_xpath(
            '/html/body/div[1]/main/header/div/div/h1'
        )

        data["domain_name"] = driver.find_element_by_xpath(
            '//*[@id="network_table_section"]/div[2]/div[1]/table[2]/tbody/tr[1]/td/a').text
        data["expiration_date"] = ""  # driver.find_element_by_xpath('').text
        data["domain_status"] = ""  # driver.find_element_by_xpath('').text
        data["name_server"] = ""  # driver.find_element_by_xpath('').text
        data["registrant_email"] = ""  # driver.find_element_by_xpath('').text
        data["admin_email"] = ""  # driver.find_element_by_xpath('').text
        data["creation_date"] = ""  # driver.find_element_by_xpath('').text
        data["registrar"] = ""  # driver.find_element_by_xpath('').text

        data["ipv4"] = driver.find_element_by_xpath(
            '//*[@id="ip_address"]').text
        data["company"] = driver.find_element_by_xpath(
            '//*[@id="background_table_section"]/div[2]/div/table[1]/tbody/tr[1]/td').text
        data["host"] = driver.find_element_by_xpath(
            '//*[@id="network_table_section"]/div[2]/div[1]/table[1]/tbody/tr[3]/td').text

        index = 1
        screenshot_path = 'screenshot/' + domain + '_ip_' + nowStr + '_'

        driver.set_window_size(1000, 870)

        # ヘッダー要素を非表示にする
        driver.execute_script(
            "arguments[0].setAttribute('style','display: none;')", driver.find_element_by_xpath(
                '/html/body/div[1]/header'
            ))

        driver.save_screenshot(screenshot_path + str(index) + ".png")
        data['screenshot_path_list'].append(
            screenshot_path + str(index) + ".png")
        index += 1

        driver.execute_script("window.scrollBy(0, 430);")
        driver.save_screenshot(screenshot_path + str(index) + ".png")
        data['screenshot_path_list'].append(
            screenshot_path + str(index) + ".png")
        index += 1

        driver.execute_script("window.scrollBy(0, 620);")
        driver.save_screenshot(screenshot_path + str(index) + ".png")
        data['screenshot_path_list'].append(
            screenshot_path + str(index) + ".png")
        index += 1

        driver.execute_script("window.scrollBy(0, 400);")
        driver.save_screenshot(screenshot_path + str(index) + ".png")
        data['screenshot_path_list'].append(
            screenshot_path + str(index) + ".png")
        index += 1

        driver.execute_script("window.scrollBy(0, 400);")
        driver.save_screenshot(screenshot_path + str(index) + ".png")
        data['screenshot_path_list'].append(
            screenshot_path + str(index) + ".png")
        index += 1

        driver.execute_script("window.scrollBy(0, 500);")
        driver.save_screenshot(screenshot_path + str(index) + ".png")
        data['screenshot_path_list'].append(
            screenshot_path + str(index) + ".png")
        index += 1

        driver.execute_script("window.scrollBy(0, 500);")
        driver.save_screenshot(screenshot_path + str(index) + ".png")
        data['screenshot_path_list'].append(
            screenshot_path + str(index) + ".png")

    except:
        print("error")

    driver.close()

    return data
