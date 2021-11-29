from bs4 import BeautifulSoup
import requests
import re

html = BeautifulSoup(requests.get("https://pastebin.com/raw/hfMThaGb").content, "html.parser").find_all("a")
urls = [BeautifulSoup(str(i), "html.parser").a.attrs["href"] for i in html]
pattern = r"(([\w\-]+\.)+)\w{2,3}\W"
good_urls = []
for url in urls:
    try:
        url = re.search(pattern, url, re.MULTILINE)
        if url[0][:-1] not in good_urls:
            good_urls.append(url[0][:-1])
    except TypeError:
        pass
good_urls.sort()
print(*good_urls, sep="\n")
