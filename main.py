import datetime
from urllib.parse import urlparse
from tkinter import messagebox
import tkinter as tk
import os

from site_info import get_site_info
from whois import get_whois
from ip import get_ip
from geolocation import get_geolocation
from document import create_document
from upload import upload_document


def process(url):
    parsed_url = urlparse(url)

    domain = parsed_url.netloc

    now = datetime.datetime.now(datetime.timezone(
        datetime.timedelta(hours=9)))
    nowStr = now.strftime('%Y%m%d%H%M%S')

    try:
        os.mkdir('screenshot/' + domain)
    except:
        print("フォルダ作成エラー")

    root = tk.Tk()
    root.attributes('-topmost', True)
    root.withdraw()
    root.lift()
    root.focus_force()

    site_info = get_site_info(url, domain, nowStr)

    whois = get_whois(domain)
    ip = get_ip(url, domain, nowStr)

    if ip == False:
        messagebox.showinfo("報告書自動作成処理", "画像取得処理失敗")
    else:
        geolocation = get_geolocation(domain, ip['ipv4'], nowStr)

        if geolocation == False:
            messagebox.showinfo("報告書自動作成処理", "画像取得処理失敗")
        else:
            # 報告書wordファイルの作成
            document = create_document(
                site_info, whois, ip, geolocation, url, domain, nowStr)

            # googleドキュメントへのアップロード
            # upload_document(document)

            messagebox.showinfo("報告書自動作成処理", "完了!!")


def main():

    print("")
    print("urlを入力")
    print("例）https://example.com")
    print("終了する場合、Nを入力してEnter")

    url = ""

    while url == "":
        url = input()

        if url == "N":
            return

        if url:
            process(url)

            print("")
            print("追加でURLを入力する場合、Yを入力してEnter")
            print("Y以外を入力してEnterで処理終了")

            return input()
        else:
            print("")
            print("urlを入力")
            print("例）https://example.com")
            print("終了する場合、Nを入力してEnter")


process_flg = "Y"
while process_flg == "Y":
    process_flg = main()
