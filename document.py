import docx
import shutil
import datetime
from docx import Document
from pptx.util import Inches


def create_document(whois, ip, geolocation, url, domain, nowStr):

    new_doc_name = domain + "_" + nowStr + ".docx"
    new_doc_path = "document/" + new_doc_name

    shutil.copyfile("document/document.docx", new_doc_path)

    doc = docx.Document(new_doc_path)

    now = datetime.datetime.now(datetime.timezone(
        datetime.timedelta(hours=9)))

    # 行単位の置換
    for paragraph in doc.paragraphs:
        replace_text(paragraph, whois, ip, geolocation, now, url, domain)

    paragraphs = (paragraph
                  for table in doc.tables
                  for row in table.rows
                  for cell in row.cells
                  for paragraph in cell.paragraphs)

    # テーブルのセル単位の置換
    for paragraph in paragraphs:
        replace_text(paragraph, whois, ip, geolocation, now, url, domain)

    # 画像の貼り付け
    doc.add_picture(ip['screenshot_path'], width=Inches(6.2))
    doc.add_picture(geolocation['screenshot_path'], width=Inches(6.2))

    doc.save(new_doc_path)

    return {
        "name": new_doc_name,
        "path": new_doc_path
    }


def replace_text(paragraph, whois, ip, geolocation, now, url, domain):
    """
    word文書の文字の置換
    ※行単位・セル単位で文字の置換をする必要がある
    """
    if paragraph.text == "${doc_creation_date}":
        paragraph.text = "令和" + \
            str(int(str(now.strftime('%Y'))[1:]) - 18) + "年" + \
            now.strftime('%m') + "月" + now.strftime('%d') + "日"

    if paragraph.text == "${name}":
        paragraph.text = ip["company"]
    if paragraph.text == "${url}":
        paragraph.text = url
    if paragraph.text == "${url_brackets}":
        paragraph.text = "【" + url + "】"
    if paragraph.text == "${address}":
        paragraph.text = geolocation["country"]
    if paragraph.text == "${domain}":
        paragraph.text = domain
    if paragraph.text == "${host}":
        paragraph.text = "ホスト名：" + ip["host"]
    if paragraph.text == "${area}":
        paragraph.text = "エリア：" + geolocation["country"]
    if paragraph.text == "${ipv4}":
        paragraph.text = ip["ipv4"]

    if paragraph.text == "${domain_name}":
        paragraph.text = whois["domain_name"] if whois["domain_name"] != "" else (
            ip["domain_name"] if ip["domain_name"] != "" else "不明")
    if paragraph.text == "${expiration_date}":
        paragraph.text = whois["expiration_date"] if whois["expiration_date"] != "" else (
            ip["expiration_date"] if ip["expiration_date"] != "" else "不明")
    if paragraph.text == "${domain_status}":
        paragraph.text = whois["domain_status"] if whois["domain_status"] != "" else (
            ip["domain_status"] if ip["domain_status"] != "" else "不明")
    if paragraph.text == "${name_server}":
        paragraph.text = whois["name_server"] if whois["name_server"] != "" else (
            ip["name_server"] if ip["name_server"] != "" else "不明")
    if paragraph.text == "${registrant_email}":
        paragraph.text = whois["registrant_email"] if whois["registrant_email"] != "" else (
            ip["registrant_email"] if ip["registrant_email"] != "" else "不明")
    if paragraph.text == "${admin_email}":
        paragraph.text = whois["admin_email"] if whois["admin_email"] != "" else (
            ip["admin_email"] if ip["admin_email"] != "" else "不明")
    if paragraph.text == "${creation_date}":
        paragraph.text = whois["creation_date"] if whois["creation_date"] != "" else (
            ip["creation_date"] if ip["creation_date"] != "" else "不明")
    if paragraph.text == "${registrar}":
        paragraph.text = whois["registrar"] if whois["registrar"] != "" else (
            ip["registrar"] if ip["registrar"] != "" else "不明")
