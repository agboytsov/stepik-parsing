import requests

import os

def get_file_size(file_name, absolute=None) -> int:
    if not absolute:
        direct = os.path.dirname(os.path.abspath(__file__))
        file_name = os.path.join(direct, file_name)
    return os.path.getsize(file_name)  # - размер файла в байтах.


# url = 'https://parsinger.ru/video_downloads/videoplayback.mp4'
# # Выполняем GET-запрос к указанному URL с параметром stream=True.
# # Параметр stream=True гарантирует, что соединение будет удерживаться, пока не будут получены все данные.
# response = requests.get(url=url, stream=True)
#
# # Открываем (или создаем) файл 'file.mp4' в режиме 'wb' (write binary),
# # чтобы сохранить в него бинарные данные.
# with open('file.mp4', 'wb') as file:
#
#     # Записываем содержимое ответа (response.content) в файл.
#     # Этот метод подходит для относительно небольших файлов,
#     # так как все содержимое файла сначала загружается в оперативную память.
#     file.write(response.content)
# file_name = 'file.mp4'
# print(round(get_file_size(file_name) / 1024 / 1024), 1)

# # От
# https://parsinger.ru/3.3/2/1.html
#
# # До
# https://parsinger.ru/3.3/2/200.html
# url ='https://parsinger.ru/3.3/1/'
# total = 0
# for i in range(1,201):
#     new_url = url + f'{str(i)}'+'.html'
#     code = requests.get(new_url, timeout=1)
#     if code.ok:
#         print(new_url)



# name_img= ['1663231240183817644.jpg',
#  '1663231245165469794.jpg',
#  '1663231252148267596.jpg',
#  '16632460271311817.jpg',
#  '1663260860165832550.jpg',
#  '1663260862112644405.jpg',
#  '1663260864114071369.jpg',
#  '1663260869127473152.jpg',
#  '1663260874115452216.jpg',
#  '1663260877136512181.jpg',
#  '1663260878140464277.jpg',
#  '1663267600193799276.jpg',
#  '1663267613117130673.jpg',
#  '1663267619197170483.jpg',
#  '1663267626154597739.jpg',
#  '1663267648135114690.jpg',
#  '166326765416196421.jpg',
#  '1663267662118079649.jpg',
#  '1663267668165066872.jpg',
#  '1663267878176341940.jpg',
#  '166326990115068678.jpg',
#  '1663269922185881885.jpg',
#  '1663269927127433209.jpg',
#  '1663269942143420441.jpg',
#  '1663269946174943071.jpg',
#  '1663269964195277579.jpg',
#  '1663269970148058649.jpg',
#  '1663269974197750992.jpg',
#  '166326997917397750.jpg',
#  '1663270039138442380.jpg',
#  '1663388012194470737.jpg',
#  '166342371029995280.jpg',
#  '1663423712288242036.jpg',
#  '1663423715255612089.jpg',
#  '1663423720221155166.jpg',
#  '1663423722211139858.jpg',
#  '1663423724211218483.jpg',
#  '1663423728215479371.jpg',
#  '1663423729298828299.jpg',
#  '1663423732225964403.jpg',
#  '1663424198111663025.jpg',
#  '1663424199157537861.jpg',
#  '1663424200184778832.jpg',
#  '166342420214123494.jpg',
#  '166342420317539591.jpg',
#  '1663424204161674559.jpg',
#  '1663424206188873432.jpg',
#  '166342420813193185.jpg',
#  '1663424209187179962.jpg',
#  '1663424212162573102.jpg']
# url = 'https://parsinger.ru/3.3/3/img/'
# res = (0,'0')
# for img in name_img:
#     new_url = url + img
#     r = requests.get(new_url, timeout=1)
#     size = int(r.headers.get('Content-Length'))
#     if size > res[0]:
#         res = (size, img[:-4])
#
#
# print(res)

# url = 'https://parsinger.ru/3.3/4/'
# first = 0
# last = 0
# for i in range(1,101):
#     new_url = url + f'{str(i)}' + '.html'
#     it = requests.get(new_url, timeout=1)
#     print(it.status_code, it.url)
#     if it.status_code == 200:
#         if not first:
#             first = i
#         last = i
# print(f"Первая доступная страница: {first}.html")
# print(f"Последняя доступная страница: {last}.html")

#
# r = requests.get('https://parsinger.ru/3.4/2/index.html')
# r.encoding = 'utf-8'
# print(r.text)

#
# url = 'https://parsinger.ru/img_download/img/ready/'
# where = '/img_ready/'
# for i in range(1,161):
#     file = str(i) + '.png'
#     file_name = where+file
#     print(file_name)
#     r = requests.get(url+file)
#     with open(file, 'wb') as f:
#         f.write(r.content)


# url ='https://parsinger.ru/3.4/1/json_weather.json'
#
# r = requests.get(url).json()
# new_dict = []
# for i in r:
#     temp = i['Температура воздуха'][:-2]
#     i['Температура воздуха'] = int(temp)
#     print(int(temp))
#
# minimum = min(r, key=lambda x: x['Температура воздуха'])
# print(minimum)


r = requests.get('https://parsinger.ru/3.4/3/dialog.json').json()

message_counts = {}

# Функция для рекурсивного обхода древовидной структуры переписки
def count_messages(participants):
    for participant in participants:
        username = participant["username"]

        if username in message_counts:
            message_counts[username] += 1
        else:
            message_counts[username] = 1

        if participant['comments'] != []:
            count_messages(participant["comments"])

# Вызов функции для подсчета сообщений
count_messages(r['comments'])
message_counts[r['username']] += 1 #добавляем первого участника

# Сортировка словаря по убыванию количества сообщений и лексикографическому порядку имен
sorted_message_counts = dict(sorted(message_counts.items(), key=lambda x: (-x[1], x[0])))

answer = sorted_message_counts

print(sorted_message_counts)







