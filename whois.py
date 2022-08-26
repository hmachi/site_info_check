from time import sleep

from common import setup_chrome_webdriver


def get_whois(domain):

    driver = setup_chrome_webdriver()

    driver.get('https://domain.sakura.ad.jp/whois/')

    sleep(1)

    domain_input = driver.find_element_by_xpath(
        '//*[@id="whois"]/main/div[3]/section[1]/div/div/div/input')
    domain_input.send_keys(domain)

    sleep(1)

    driver.find_element_by_xpath(
        '//*[@id="whois"]/main/div[3]/section[1]/div/div/div/div/button').click()

    sleep(3)

    data = {
        "domain_name": "",
        "expiration_date": "",
        "domain_status": "",
        "name_server": "",
        "registrant_email": "",
        "admin_email": "",
        "creation_date": "",
        "registrar": "",
    }

    try:
        # 検索処理が成功していることの確認
        driver.find_element_by_xpath(
            '//*[@id="whois"]/main/div[3]/section[2]/div/h2'
        )

        data["domain_name"] = driver.find_element_by_xpath(
            '//*[@id="wls0"]/td').text
        data["expiration_date"] = driver.find_element_by_xpath(
            '//*[@id="wls1"]/td').text
        data["domain_status"] = driver.find_element_by_xpath(
            '//*[@id="wls2"]/td').text
        data["name_server"] = driver.find_element_by_xpath(
            '//*[@id="wls3"]/td').text
        data["registrant_email"] = driver.find_element_by_xpath(
            '//*[@id="wls4"]/td').text
        data["admin_email"] = driver.find_element_by_xpath(
            '//*[@id="wls5"]/td').text
        data["creation_date"] = driver.find_element_by_xpath(
            '//*[@id="wls6"]/td').text
        data["registrar"] = driver.find_element_by_xpath(
            '//*[@id="wls7"]/td').text

    except Exception as e:
        print(e.message)

    driver.close()

    return data
