import datetime
from urllib.parse import urlparse
from tkinter import messagebox
import tkinter as tk

from whois import get_whois
from ip import get_ip
from geolocation import get_geolocation
from document import create_document
from upload import upload_document

print("urlを入力")
print("例）https://example.com")

url = input()

parsed_url = urlparse(url)

domain = parsed_url.netloc

now = datetime.datetime.now(datetime.timezone(
    datetime.timedelta(hours=9)))
nowStr = now.strftime('%Y%m%d%H%M%S')

whois = get_whois(domain)
ip = get_ip(domain, nowStr)
geolocation = get_geolocation(domain, ip['ipv4'], nowStr)

# 報告書wordファイルの作成
document = create_document(whois, ip, geolocation, url, domain, nowStr)

# googleドキュメントへのアップロード
# upload_document(document)

root = tk.Tk()
root.attributes('-topmost', True)
root.withdraw()
root.lift()
root.focus_force()
messagebox.showinfo("報告書自動作成処理", "完了!!")
