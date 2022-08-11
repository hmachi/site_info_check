import datetime

from whois import get_whois
from ip import get_ip
from geolocation import get_geolocation
from document import create_document

print("domain情報を入力")
print("例）example.com")

# TODO
# domain = input()
domain = "yahoo.co.jp"

now = datetime.datetime.now(datetime.timezone(
    datetime.timedelta(hours=9)))
nowStr = now.strftime('%Y%m%d%H%M%S')

whois = get_whois(domain)
ip = get_ip(domain, nowStr)
geolocation = get_geolocation(domain, ip['ipv4'], nowStr)

create_document(whois, ip, geolocation, domain, nowStr)
