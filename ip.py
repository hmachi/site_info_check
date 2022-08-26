from time import sleep
from common import setup_chrome_webdriver, disp_content


def get_ip(url, domain, nowStr):

    driver = setup_chrome_webdriver()

    driver.get('https://sitereport.netcraft.com/')

    sleep(1)

    url_input = driver.find_element_by_xpath(
        '//*[@id="site_report_query"]/div/input')
    url_input.send_keys(url)

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

        screenshot_path = 'screenshot/' + domain + '_ip_' + nowStr

        # 取得要素以外
        not_disp_content_list = [
            '/html/body/div[1]/header',
            '/html/body/div[1]/main/header',
            '/html/body/div[1]/main/div[1]/div/div',
            '/html/body/div[1]/main/section',
            '//*[@id="ip_geolocation_section"]',  # TODO 必要かどうか
            '/html/body/footer',
            '/html/body/footer/div',
            '/html/body/footer/a',
            '/html/body/div[1]/main/div[2]'
        ]

        # 取得要素セクション
        disp_content_list = [
            '//*[@id="background_table_section"]',
            '//*[@id="network_table_section"]',
            '//*[@id="ssl_table_section"]',
            '//*[@id="ssl_chain_table_section"]',
            '//*[@id="history_table_section"]',
            '//*[@id="spf_table_section"]',
            '//*[@id="dmarc_table_section"]',
            '//*[@id="webbugs_section"]',
            '//*[@id="technology_table_section"]',
        ]

        # 取得要素以外を非表示にする
        disp_content(driver, not_disp_content_list, "", True)

        # Background以外を非表示にする
        disp_content(driver, disp_content_list, 0, False)

        driver.set_window_size(1000, 450)
        sleep(0.5)
        driver.save_screenshot(screenshot_path + "_background.png")
        data['screenshot_path_list'].append(
            screenshot_path + "_background.png")

        # Network以外非表示にする
        disp_content(driver, disp_content_list, 1, False)

        driver.set_window_size(1000, 1000)
        sleep(0.5)
        driver.save_screenshot(screenshot_path + "_network.png")
        data['screenshot_path_list'].append(
            screenshot_path + "_Network.png")

        # SSL/TLS以外非表示にする
        disp_content(driver, disp_content_list, 2, False)

        driver.set_window_size(1000, 1500)
        sleep(0.5)
        driver.save_screenshot(screenshot_path + "_ssltls1.png")
        data['screenshot_path_list'].append(
            screenshot_path + "_ssltls1.png")
        driver.execute_script("window.scrollBy(0, 2000);")
        sleep(0.5)
        driver.save_screenshot(screenshot_path + "_ssltls2.png")
        data['screenshot_path_list'].append(
            screenshot_path + "_ssltls2.png")

        # SSL Certificate Chain以外非表示にする
        disp_content(driver, disp_content_list, 3, False)
        # 要素を表示する
        driver.find_element_by_xpath(
            '//*[@id="ssl_chain_table_section"]').click()

        driver.set_window_size(1000, 600)
        sleep(0.5)
        driver.save_screenshot(screenshot_path + "_sslcertificatechain.png")
        data['screenshot_path_list'].append(
            screenshot_path + "_sslcertificatechain.png")

        # Hosting History以外非表示にする
        disp_content(driver, disp_content_list, 4, False)

        driver.set_window_size(1000, 500)
        sleep(0.5)
        driver.save_screenshot(screenshot_path + "_hostinghistory.png")
        data['screenshot_path_list'].append(
            screenshot_path + "_hostinghistory.png")

        # Sender Policy Framework以外非表示にする
        disp_content(driver, disp_content_list, 5, False)

        driver.set_window_size(1000, 600)
        sleep(0.5)
        driver.save_screenshot(screenshot_path + "_senderpolicyframework.png")
        data['screenshot_path_list'].append(
            screenshot_path + "_senderpolicyframework.png")

        # DMARC以外非表示にする
        disp_content(driver, disp_content_list, 6, False)

        driver.set_window_size(1000, 700)
        sleep(0.5)
        driver.save_screenshot(screenshot_path + "_dmarc.png")
        data['screenshot_path_list'].append(
            screenshot_path + "_dmarc.png")

        # Web Trackers以外非表示にする
        disp_content(driver, disp_content_list, 7, False)

        driver.set_window_size(1000, 800)
        sleep(0.5)
        driver.save_screenshot(screenshot_path + "_webtracker.png")
        data['screenshot_path_list'].append(
            screenshot_path + "_webtracker.png")

        # Site Technology以外非表示にする
        disp_content(driver, disp_content_list, 8, False)

        driver.set_window_size(1000, 900)
        sleep(0.5)
        driver.save_screenshot(screenshot_path + "_sitetechnology1.png")
        data['screenshot_path_list'].append(
            screenshot_path + "_sitetechnology1.png")
        driver.execute_script("window.scrollBy(0, 1000);")
        sleep(0.5)
        driver.save_screenshot(screenshot_path + "_sitetechnology2.png")
        data['screenshot_path_list'].append(
            screenshot_path + "_sitetechnology2.png")

    except Exception as e:
        print(e.message)

    driver.close()

    return data
