'''
Рассмотрим два HTML-документа A и B.

Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри A есть тег <a href="B">, возможно с дополнительными параметрами внутри тега. Из A можно перейти в B за два перехода если существует такой документ C, что из A в C можно перейти за один переход и из C в B можно перейти за один переход.

Вашей программе на вход подаются две строки, содержащие url двух документов A и B. Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.

Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML документы.

Sample Input 1:

https://stepic.org/media/attachments/lesson/24472/sample0.html

https://stepic.org/media/attachments/lesson/24472/sample2.html

Sample Output 1:

Yes

Sample Input 2:

https://stepic.org/media/attachments/lesson/24472/sample0.html

https://stepic.org/media/attachments/lesson/24472/sample1.html

Sample Output 2:

No

Sample Input 3:

https://stepic.org/media/attachments/lesson/24472/sample1.html

https://stepic.org/media/attachments/lesson/24472/sample2.html

Sample Output 3:

Yes
'''
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
