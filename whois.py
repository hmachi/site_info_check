from time import sleep

from common import setup_chrome_webdriver


def get_whois(domain):

    driver = setup_chrome_webdriver()

    driver.get('https://www.whois.com/whois')

    sleep(1)

    domain_input = driver.find_element_by_xpath(
        '//*[@id="query"]')
    domain_input.send_keys(domain)

    sleep(1)

    driver.find_element_by_xpath(
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

        result = driver.find_element_by_xpath(
            '//*[@id="registryData"]').text

        rowList = result.split("\n")

        for row in rowList:
            if 'Domain Name:' in row:
                isAdd = False
                for column in row.split():
                    if isAdd:
                        if column:
                            data["domain_name"] += column + " "
                    if column == 'Name:':
                        isAdd = True
            if 'Expiration Date:' in row:
                isAdd = False
                for column in row.split():
                    if isAdd:
                        if column:
                            data["expiration_date"] += column[0:10] + " "
                    if column == 'Date:':
                        isAdd = True
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
            if 'Registrant Email:' in row:
                isAdd = False
                for column in row.split():
                    if isAdd:
                        if column:
                            data["registrant_email"] += column + " "
                    if column == 'Email:':
                        isAdd = True
            if 'Admin Email:' in row:
                isAdd = False
                for column in row.split():
                    if isAdd:
                        if column:
                            data["admin_email"] += column + " "
                    if column == 'Email:':
                        isAdd = True
            if 'Creation Date:' in row:
                isAdd = False
                for column in row.split():
                    if isAdd:
                        if column:
                            data["creation_date"] += column[0:10] + " "
                    if column == 'Date:':
                        isAdd = True
            if 'Registrar:' in row:
                isAdd = False
                for column in row.split():
                    if isAdd:
                        if column:
                            data["registrar"] += column + " "
                    if column == 'Registrar:':
                        isAdd = True

        if data["domain_name"] == "":
            for row in rowList:
                if '[Domain Name]' in row:
                    isAdd = False
                    for column in row.split():
                        if isAdd:
                            if column:
                                data["domain_name"] += column + " "
                        if column == 'Name]':
                            isAdd = True
                if '[State]' in row:
                    isAdd = False
                    for column in row.split():
                        if isAdd:
                            if column:
                                data["expiration_date"] += column.replace(
                                    ")", "").replace("(", "") + " "
                        if column == 'Connected':
                            isAdd = True
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
                if '[Registered Date]' in row:
                    isAdd = False
                    for column in row.split():
                        if isAdd:
                            if column:
                                data["creation_date"] += column + " "
                        if column == 'Date]':
                            isAdd = True

    except Exception as e:
        print(e)

    driver.close()

    return data
