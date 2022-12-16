from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from PIL import Image
import io
from selenium.webdriver.common.by import By


def setup_chrome_webdriver():
    """
    chromeWebドライバーをダウンロードする
    """
    return webdriver.Chrome(ChromeDriverManager().install())


def disp_content(driver, disp_content_list, dispIndexList=[], isAllHidden=True):

    false_list = []

    for index, disp_content in enumerate(disp_content_list):
        try:
            if isAllHidden:
                driver.execute_script(
                    "arguments[0].setAttribute('style','display: none;')", driver.find_element(By.XPATH,
                                                                                               disp_content
                                                                                               ))
            else:
                if index in dispIndexList:
                    driver.execute_script(
                        "arguments[0].setAttribute('style','display: block;')", driver.find_element(By.XPATH,
                                                                                                    disp_content
                                                                                                    ))
                else:
                    driver.execute_script(
                        "arguments[0].setAttribute('style','display: none;')", driver.find_element(By.XPATH,
                                                                                                   disp_content
                                                                                                   ))
        except:
            if isAllHidden:
                print(disp_content + "のコンテンツがありません")
            else:
                if index in dispIndexList:
                    print(disp_content + "のコンテンツがありません")
                    false_list.append(False)

    if len(false_list) == 0:
        return True
    else:
        if len(false_list) == len(dispIndexList):
            return False
        else:
            return True


def get_full_screenshot_image(driver, file_path, reverse=False, driverss_contains_scrollbar=None):
    if driverss_contains_scrollbar is None:
        driverss_contains_scrollbar = isinstance(
            driver, webdriver.Chrome)
    # Scroll to the bottom of the page once
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(0.5)
    scroll_height, document_client_width, document_client_height, inner_width, inner_height = driver.execute_script(
        "return [document.body.scrollHeight, document.documentElement.clientWidth, document.documentElement.clientHeight, window.innerWidth, window.innerHeight]")
    streams_to_be_closed = []
    images = []
    try:
        # open
        for y_coord in range(0, scroll_height, document_client_height):
            driver.execute_script("window.scrollTo(0, arguments[0]);", y_coord)
            stream = io.BytesIO(driver.get_screenshot_as_png())
            streams_to_be_closed.append(stream)
            img = Image.open(stream)
            # Image, y_coord
            images.append((img, min(y_coord, scroll_height - inner_height)))
        # load
        scale = float(
            img.size[0]) / (inner_width if driverss_contains_scrollbar else document_client_width)
        img_dst = Image.new(mode='RGBA', size=(
            int(document_client_width * scale), int(scroll_height * scale)))
        for img, y_coord in (reversed(images) if reverse else images):
            img_dst.paste(img, (0, int(y_coord * scale)))

        img_dst.save(file_path)
    finally:
        # close
        for stream in streams_to_be_closed:
            stream.close()
        for img, y_coord in images:
            img.close()
