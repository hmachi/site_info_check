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
        replace_text(paragraph, whois, ip, now, url, domain)

    paragraphs = (paragraph
                  for table in doc.tables
                  for row in table.rows
                  for cell in row.cells
                  for paragraph in cell.paragraphs)

    # テーブルのセル単位の置換
    for paragraph in paragraphs:
        replace_text(paragraph, whois, ip, now, url, domain)

    # 画像の貼り付け
    doc.add_picture(ip['screenshot_path'], width=Inches(6.2))
    doc.add_picture(geolocation['screenshot_path'], width=Inches(6.2))

    doc.save(new_doc_path)


def replace_text(paragraph, whois, ip, now, url, domain):
    """
    word文書の文字の置換
    ※行単位・セル単位で文字の置換をする必要がある
    """
    if paragraph.text == "${doc_creation_date}":
        paragraph.text = "令和" + \
            str(int(str(now.strftime('%Y'))[1:]) - 18) + "年" + \
            now.strftime('%m') + "月" + now.strftime('%d') + "日"

    if paragraph.text == "${investigation_date}":
        # 令和${before_year}年${before_month}月${before_day}日～令和${after_year}年${after_month}月${after_day}日
        paragraph.text = ""  # TODO
    if paragraph.text == "${name}":
        paragraph.text = ""  # TODO
    if paragraph.text == "${url}":
        paragraph.text = url
    if paragraph.text == "${url_brackets}":
        paragraph.text = "【" + url + "】"
    if paragraph.text == "${address}":
        paragraph.text = ""  # TODO
    if paragraph.text == "${domain}":
        paragraph.text = domain
    if paragraph.text == "${host}":
        paragraph.text = "ホスト名："  # TODO
    if paragraph.text == "${area}":
        paragraph.text = "エリア："  # TODO
    if paragraph.text == "${ipv4}":
        paragraph.text = ip["ipv4"]

    if paragraph.text == "${domain_name}":
        paragraph.text = whois["domain_name"]
    if paragraph.text == "${expiration_date}":
        paragraph.text = whois["expiration_date"]
    if paragraph.text == "${domain_status}":
        paragraph.text = whois["domain_status"]
    if paragraph.text == "${name_server}":
        paragraph.text = whois["name_server"]
    if paragraph.text == "${registrant_email}":
        paragraph.text = whois["registrant_email"]
    if paragraph.text == "${admin_email}":
        paragraph.text = whois["admin_email"]
    if paragraph.text == "${creation_date}":
        paragraph.text = whois["creation_date"]
    if paragraph.text == "${registrar}":
        paragraph.text = whois["registrar"]
