from time import sleep
import os

from common import setup_chrome_webdriver, disp_content, get_full_screenshot_image


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

        try:
            os.mkdir('screenshot/' + domain + "/ip")
        except:
            print("フォルダ作成エラー")

        screenshot_path = 'screenshot/' + domain + '/ip/'

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

        ssl_tls_content_list = [
            '//*[@id="ssl_table_section"]/div[2]/div[1]',
            '//*[@id="ssl_table_section"]/div[2]/div[2]',
            '//*[@id="ssl_table_section"]/div[2]/h4',
            '//*[@id="ssl_table_section"]/div[2]/table',
            '//*[@id="ssl_table_section"]/div[2]/h3[1]',
            '//*[@id="ssl_table_section"]/div[2]/div[3]',
            '//*[@id="ssl_table_section"]/div[2]/h3[2]',
            '//*[@id="ssl_table_section"]/div[2]/p[1]',
            '//*[@id="ssl_table_section"]/div[2]/p[2]'
        ]

        site_technology_content_list = [
            '//*[@id="technology_table_section"]/div[2]/ul/li[1]',
            '//*[@id="technology_table_section"]/div[2]/ul/li[2]',
            '//*[@id="technology_table_section"]/div[2]/ul/li[3]',
            '//*[@id="technology_table_section"]/div[2]/ul/li[4]',
            '//*[@id="technology_table_section"]/div[2]/ul/li[5]',
            '//*[@id="technology_table_section"]/div[2]/ul/li[6]',
            '//*[@id="technology_table_section"]/div[2]/ul/li[7]',
            '//*[@id="technology_table_section"]/div[2]/ul/li[8]',
            '//*[@id="technology_table_section"]/div[2]/ul/li[9]',
            '//*[@id="technology_table_section"]/div[2]/ul/li[10]',
            '//*[@id="technology_table_section"]/div[2]/ul/li[11]',
            '//*[@id="technology_table_section"]/div[2]/ul/li[12]',
            '//*[@id="technology_table_section"]/div[2]/ul/li[13]',
            '//*[@id="technology_table_section"]/div[2]/ul/li[14]',
            '//*[@id="technology_table_section"]/div[2]/ul/li[15]',
            '//*[@id="technology_table_section"]/div[2]/ul/li[16]',
            '//*[@id="technology_table_section"]/div[2]/ul/li[17]',
            '//*[@id="technology_table_section"]/div[2]/ul/li[18]',
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

        # 画面サイズ変更
        driver.set_window_size(1000, 400)

        # Background以外を非表示にする
        if disp_content(driver, disp_content_list, [0], False):
            sleep(1)

            file_path = screenshot_path + "background_" + nowStr + ".png"
            get_full_screenshot_image(driver, file_path)
            data['screenshot_path_list'].append(file_path)

        # Network以外非表示にする
        if disp_content(driver, disp_content_list, [1], False):
            sleep(1)

            file_path = screenshot_path + "network_" + nowStr + ".png"
            get_full_screenshot_image(driver, file_path)
            data['screenshot_path_list'].append(file_path)

        # SSL/TLS以外非表示にする
        if disp_content(driver, disp_content_list, [2], False):
            sleep(1)

            if disp_content(driver, ssl_tls_content_list, [0], False):
                file_path = screenshot_path + "ssltls1_" + nowStr + ".png"
                get_full_screenshot_image(driver, file_path)
                data['screenshot_path_list'].append(file_path)

            # セクションヘッダー削除
            driver.execute_script(
                "arguments[0].setAttribute('style','display: none;')", driver.find_element_by_xpath(
                    '//*[@id="ssl_table_section"]/div[1]'
                ))

            if disp_content(driver, ssl_tls_content_list, [1, 2, 3, 4, 5, 6, 7, 8], False):
                file_path = screenshot_path + "ssltls2_" + nowStr + ".png"
                get_full_screenshot_image(driver, file_path)
                data['screenshot_path_list'].append(file_path)

        # SSL Certificate Chain以外非表示にする
        if disp_content(driver, disp_content_list, [3], False):
            # 要素を表示する
            driver.find_element_by_xpath(
                '//*[@id="ssl_chain_table_section"]').click()

            sleep(1)

            file_path = screenshot_path + "sslcertificatechain_" + nowStr + ".png"
            get_full_screenshot_image(driver, file_path)
            data['screenshot_path_list'].append(file_path)

        # Hosting History以外非表示にする
        if disp_content(driver, disp_content_list, [4], False):
            sleep(1)

            file_path = screenshot_path + "hostinghistory_" + nowStr + ".png"
            get_full_screenshot_image(driver, file_path)
            data['screenshot_path_list'].append(file_path)

        # Sender Policy Framework以外非表示にする
        if disp_content(driver, disp_content_list, [5], False):
            sleep(1)

            file_path = screenshot_path + "senderpolicyframework_" + nowStr + ".png"
            get_full_screenshot_image(driver, file_path)
            data['screenshot_path_list'].append(file_path)

        # DMARC以外非表示にする
        if disp_content(driver, disp_content_list, [6], False):
            sleep(1)

            file_path = screenshot_path + "dmarc_" + nowStr + ".png"
            get_full_screenshot_image(driver, file_path)
            data['screenshot_path_list'].append(file_path)

        # Web Trackers以外非表示にする
        if disp_content(driver, disp_content_list, [7], False):
            sleep(1)

            file_path = screenshot_path + "webtracker_" + nowStr + ".png"
            get_full_screenshot_image(driver, file_path)
            data['screenshot_path_list'].append(file_path)

        # Site Technology以外非表示にする
        if disp_content(driver, disp_content_list, [8], False):
            sleep(1)

            if disp_content(driver, site_technology_content_list, [0, 1, 2], False):
                file_path = screenshot_path + "sitetechnology1_" + nowStr + ".png"
                get_full_screenshot_image(driver, file_path)
                data['screenshot_path_list'].append(file_path)

            # セクションヘッダー削除
            driver.execute_script(
                "arguments[0].setAttribute('style','display: none;')", driver.find_element_by_xpath(
                    '//*[@id="technology_table_section"]/div[1]'
                ))

            if disp_content(driver, site_technology_content_list, [3, 4, 5], False):
                file_path = screenshot_path + "sitetechnology2_" + nowStr + ".png"
                get_full_screenshot_image(driver, file_path)
                data['screenshot_path_list'].append(file_path)
            if disp_content(driver, site_technology_content_list, [6, 7, 8], False):
                file_path = screenshot_path + "sitetechnology3_" + nowStr + ".png"
                get_full_screenshot_image(driver, file_path)
                data['screenshot_path_list'].append(file_path)
            if disp_content(driver, site_technology_content_list, [9, 10, 11], False):
                file_path = screenshot_path + "sitetechnology4_" + nowStr + ".png"
                get_full_screenshot_image(driver, file_path)
                data['screenshot_path_list'].append(file_path)
            if disp_content(driver, site_technology_content_list, [12, 13, 14], False):
                file_path = screenshot_path + "sitetechnology5_" + nowStr + ".png"
                get_full_screenshot_image(driver, file_path)
                data['screenshot_path_list'].append(file_path)
            if disp_content(driver, site_technology_content_list, [15, 16, 17], False):
                file_path = screenshot_path + "sitetechnology6_" + nowStr + ".png"
                get_full_screenshot_image(driver, file_path)
                data['screenshot_path_list'].append(file_path)

    except Exception as e:
        print(e.message)

    driver.close()

    return data
