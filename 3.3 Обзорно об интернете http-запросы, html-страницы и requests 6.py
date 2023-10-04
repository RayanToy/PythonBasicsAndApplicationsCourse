import requests
from bs4 import BeautifulSoup

url = input()
check_link = input()
url = url.replace('stepic.org', 'stepik.org')
check_link = check_link.replace('stepic.org', 'stepik.org')
check = []
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
links = soup.find_all('a', href=True)
for link in links:
    href = link.get('href')
    response = requests.get(href)
    soup = BeautifulSoup(response.text, 'html.parser')
    lnks = soup.find_all('a', href=True)
    for lnk in lnks:
        lnk = lnk.get('href').replace('stepic.org', 'stepik.org')
        check.append(lnk)
print("Yes" if check_link in check else "No")  