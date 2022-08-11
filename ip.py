from time import sleep

from common import setup_chrome_webdriver
from screenshot import get_full_screenshot_image


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

    sleep(10)

    data = {
        """
        "domain_name": "",
        "expiration_date": "",
        "domain_status": "",
        "name_server": "",
        "registrant_email": "",
        "admin_email": "",
        "creation_date": "",
        "registrar": "",
        "admin_contact": "",
        "technical_contact": "",
        "public_contact_email": "",
        """
        "ipv4": "",
        "screenshot_name": ""
    }

    try:
        # 検索処理が成功していることの確認
        driver.find_element_by_xpath(
            '/html/body/div[1]/main/header/div/div/h1'
        )

        screenshot = get_full_screenshot_image(driver)
        screenshot_name = domain + '_ip_' + nowStr + '.png'
        screenshot.save(screenshot_name)

        # TODO
        # whoisの検索でデータが取得できなかった場合、このサイトの情報を使用する
        """
        data["domain_name"] = driver.find_element_by_xpath('').text
        data["expiration_date"] = driver.find_element_by_xpath('').text
        data["domain_status"] = driver.find_element_by_xpath('').text
        data["name_server"] = driver.find_element_by_xpath('').text
        data["registrant_email"] = driver.find_element_by_xpath('').text
        data["admin_email"] = driver.find_element_by_xpath('').text
        data["creation_date"] = driver.find_element_by_xpath('').text
        data["registrar"] = driver.find_element_by_xpath('').text
        data["admin_contact"] = driver.find_element_by_xpath('').text
        data["technical_contact"] = driver.find_element_by_xpath('').text
        data["public_contact_email"] = driver.find_element_by_xpath('').text
        """
        data["ipv4"] = driver.find_element_by_xpath(
            '//*[@id="ip_address"]').text
        data['screenshot_name'] = screenshot_name
    except:
        print("error")

    driver.close()

    return data
