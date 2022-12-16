from time import sleep

from common import setup_chrome_webdriver
from selenium.webdriver.common.by import By


def get_whois(domain):

    driver = setup_chrome_webdriver()

    driver.get('https://www.whois.com/whois')

    sleep(1)

    domain_input = driver.find_element(
        By.XPATH,
        '//*[@id="query"]')
    domain_input.send_keys(domain)

    sleep(1)

    driver.find_element(
        By.XPATH,
        '//*[@id="page-wrapper"]/div[1]/form/button').click()

    sleep(5)

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

        result = ""

        try:
            result = driver.find_element(
                By.XPATH,
                '//*[@id="registrarData"]').text
        except:
            result = driver.find_element(
                By.XPATH,
                '//*[@id="registryData"]').text

        rowList = result.split("\n")

        for row in rowList:
            # ドメイン名
            if 'Domain Name:' in row:
                isAdd = False
                for column in row.split():
                    if isAdd:
                        if column:
                            data["domain_name"] += column + " "
                    if column == 'Name:':
                        isAdd = True
            # 有効期限1
            if 'Expiration Date:' in row:
                isAdd = False
                for column in row.split():
                    if isAdd:
                        if column:
                            data["expiration_date"] += column[0:10] + " "
                    if column == 'Date:':
                        isAdd = True
            # 有効期限2
            if 'Expiry Date:' in row:
                isAdd = False
                for column in row.split():
                    if isAdd:
                        if column:
                            data["expiration_date"] += column[0:10] + " "
                    if column == 'Date:':
                        isAdd = True

            # ドメインステータス
            if 'Domain Status:' in row:
                if data["domain_status"] != "":
                    data["domain_status"] += "\n"
                isAdd = False
                for column in row.split():
                    if isAdd:
                        if column:
                            data["domain_status"] += column + " "
                            isAdd = False
                    if column == 'Status:':
                        isAdd = True
            # ネームサーバー
            if 'Name Server:' in row:
                if data["name_server"] != "":
                    data["name_server"] += "\n"
                isAdd = False
                for column in row.split():
                    if isAdd:
                        if column:
                            data["name_server"] += column + " "
                    if column == 'Server:':
                        isAdd = True
            # 登録者メールアドレス
            if 'Registrant Email:' in row:
                isAdd = False
                for column in row.split():
                    if isAdd:
                        if column:
                            data["registrant_email"] += column + " "
                    if column == 'Email:':
                        isAdd = True
            # 管理者メールアドレス
            if 'Admin Email:' in row:
                isAdd = False
                for column in row.split():
                    if isAdd:
                        if column:
                            data["admin_email"] += column + " "
                    if column == 'Email:':
                        isAdd = True
            # 作成日
            if 'Creation Date:' in row:
                isAdd = False
                for column in row.split():
                    if isAdd:
                        if column:
                            data["creation_date"] += column[0:10] + " "
                    if column == 'Date:':
                        isAdd = True
            # レジストラ
            if 'Registrar:' in row:
                isAdd = False
                for column in row.split():
                    if isAdd:
                        if column:
                            data["registrar"] += column + " "
                    if column == 'Registrar:':
                        isAdd = True

        # パターン2の画面
        if data["domain_name"] == "":

            for row in rowList:
                # ドメイン名
                if '[Domain Name]' in row:
                    isAdd = False
                    for column in row.split():
                        if isAdd:
                            if column:
                                data["domain_name"] += column + " "
                        if column == 'Name]':
                            isAdd = True
                # 有効期限
                if '[State]' in row:
                    isAdd = False
                    for column in row.split():
                        if isAdd:
                            if column:
                                data["expiration_date"] += column.replace(
                                    ")", "").replace("(", "") + " "
                        if column == 'Connected':
                            isAdd = True
                # ドメインステータス
                if '[State]' in row:
                    if data["domain_status"] != "":
                        data["domain_status"] += "\n"
                    isAdd = False
                    for column in row.split():
                        if isAdd:
                            if column:
                                data["domain_status"] += column + " "
                        if column == '[State]':
                            isAdd = True
                # ネームサーバー
                if '[Name Server]' in row:
                    if data["name_server"] != "":
                        data["name_server"] += "\n"
                    isAdd = False
                    for column in row.split():
                        if isAdd:
                            if column:
                                data["name_server"] += column + " "
                        if column == 'Server]':
                            isAdd = True
                # 登録日
                if '[Registered Date]' in row:
                    isAdd = False
                    for column in row.split():
                        if isAdd:
                            if column:
                                data["creation_date"] += column + " "
                        if column == 'Date]':
                            isAdd = True

                data["registrant_email"] = "不明"
                data["admin_email"] = "不明"
                data["registrar"] = "不明"

        if "Please query" in data["registrant_email"]:
            data["registrant_email"] = "不明"
        if "Please query" in data["admin_email"]:
            data["admin_email"] = "不明"

    except Exception as e:
        print(e)

    driver.close()

    return data
