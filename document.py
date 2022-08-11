import docx
import shutil


def create_document(whois, ip, geolocation, domain, nowStr):

    new_doc_path = "document/" + domain + "_" + nowStr + ".docx"

    shutil.copyfile("document/document.docx", new_doc_path)

    target_doc = docx.Document(new_doc_path)

    # TODO 取得確認
    print(whois["domain_name"])
    print(whois["expiration_date"])
    print(whois["domain_status"])
    print(whois["name_server"])
    print(whois["registrant_email"])
    print(whois["admin_email"])
    print(whois["creation_date"])
    print(whois["registrar"])
    print(whois["admin_contact"])
    print(whois["technical_contact"])
    print(whois["public_contact_email"])

    # TODO 取得確認
    print(ip['ipv4'])
    print(ip['screenshot_name'])

    # TODO 取得確認
    print(geolocation['screenshot_name'])

# TODO word文章に必要事項を書き込む
