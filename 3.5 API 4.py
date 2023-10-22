'''
В этой задаче вам необходимо воспользоваться API сайта artsy.net

API проекта Artsy предоставляет информацию о некоторых деятелях искусства, их работах, выставках.

В рамках данной задачи вам понадобятся сведения о деятелях искусства (назовем их, условно, художники).

Вам даны идентификаторы художников в базе Artsy. Для каждого идентификатора получите информацию о имени художника и годе рождения. Выведите имена художников в порядке неубывания года рождения. В случае если у художников одинаковый год рождения, выведите их имена в лексикографическом порядке.

Работа с API Artsy

Полностью открытое и свободное API предоставляют совсем немногие проекты. В большинстве случаев, для получения доступа к API необходимо зарегистрироваться в проекте, создать свое приложение, и получить уникальный ключ (или токен), и в дальнейшем все запросы к API осуществляются при помощи этого ключа.

Чтобы начать работу с API проекта Artsy, вам необходимо пройти на стартовую страницу документации к API https://developers.artsy.net/start и выполнить необходимые шаги, а именно зарегистрироваться, создать приложение, и получить пару идентификаторов Client Id и Client Secret. Не публикуйте эти идентификаторы.

После этого необходимо получить токен доступа к API. На стартовой странице документации есть примеры того, как можно выполнить запрос и как выглядит ответ сервера. Мы приведем пример запроса на Python.

import requests
import json

client_id = '...'
client_secret = '...'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]
Теперь все готово для получения информации о художниках. На стартовой странице документации есть пример того, как осуществляется запрос и как выглядит ответ сервера. Пример запроса на Python.

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}

# инициируем запрос с заголовком
r = requests.get("https://api.artsy.net/api/artists/4d8b92b34eb68a1b2c0003f4", headers=headers)

# разбираем ответ сервера
j = json.loads(r.text)
Примечание: ﻿В качестве имени художника используется параметр sortable_name в кодировке UTF-8.

Пример входных данных: 4d8b92b34eb68a1b2c0003f4 537def3c139b21353f0006a6 4e2ed576477cc70001006f99

Пример выходных данных: Abbott Mary Warhol Andy Abbas Hamra
'''

import requests
import json

client_id = '799b62ae0720f0d75570'
client_secret = 'e35c977afaca7cfc765e75c5ea16e40c'

r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

j = json.loads(r.text)
artist = {}
token = j["token"]
headers = {"X-Xapp-Token" : token}
with open('dataset_24476_4.txt', 'r', encoding='utf-8') as f:
    data = f.read()
    lines = data.strip().split('\n')
for line in lines:
    r = requests.get(f"https://api.artsy.net/api/artists/{line}", headers=headers)
    j = json.loads(r.text)
    artist[j['sortable_name']] = int(j['birthday'])
sorted_artist = sorted(artist.items(), key=lambda x: (x[1], x[0]))
for artist in sorted_artist:
    print(artist[0])
print('\n')
