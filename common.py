from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def setup_chrome_webdriver():
    """
    chromeWebドライバーをダウンロードする
    """
    return webdriver.Chrome(ChromeDriverManager().install())


def disp_content(driver, disp_content_list, dispIndex, isAllHidden):
    for index, disp_content in enumerate(disp_content_list):
        try:
            if isAllHidden:
                driver.execute_script(
                    "arguments[0].setAttribute('style','display: none;')", driver.find_element_by_xpath(
                        disp_content
                    ))
            else:
                if index == dispIndex:
                    driver.execute_script(
                        "arguments[0].setAttribute('style','display: block;')", driver.find_element_by_xpath(
                            disp_content
                        ))
                else:
                    driver.execute_script(
                        "arguments[0].setAttribute('style','display: none;')", driver.find_element_by_xpath(
                            disp_content
                        ))
        except:
            print(disp_content + "のコンテンツがありません")
