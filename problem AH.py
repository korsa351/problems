from bs4 import BeautifulSoup
import requests


url1 = input()
url2 = input()
first_red = BeautifulSoup(requests.get(url1).content, "html.parser").find_all("a")
sec_red = []
if not first_red:
    print("No")
    exit()
for url in first_red:
    url = BeautifulSoup(str(url), "html.parser").a.attrs["href"]
    sec_red.extend(BeautifulSoup(requests.get(url).content, "html.parser").find_all("a"))
if not sec_red:
    print("No")
    exit()
for url in sec_red:
    url = BeautifulSoup(str(url), "html.parser").a.attrs["href"]
    if url == url2:
        print("Yes")
        exit()
print("No")
exit()