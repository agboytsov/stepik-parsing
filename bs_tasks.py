from bs4 import BeautifulSoup
import requests
import time

# with open('index/index.html', 'r', encoding='utf-8') as file:
#     soup2 = BeautifulSoup(file, 'lxml')
#     print(soup2)


# html_doc = """
# <!DOCTYPE html>
# <html lang="ru">
# <head>
#     <meta charset="UTF-8">
#     <title>Пример карточки товара</title>
# </head>
# <body>
#     <div class="card">
#         <img src="image.jpg" alt="Пример изображения товара">
#         <h2 class="card-title"> iPhone 15 </h2>
#         <p class="card-description">Аппаратной основой Apple iPhone 15 Pro Max стал 3-нанометровый чипсет A17 Pro с 6-ядерным GPU и поддержкой трассировки лучей.</p>
#         <p class="card-price">999 999 руб.</p>
#         <a href="https://example.com/product-link" class="card-link">Подробнее</a>
#     </div>
# </body>
# </html>
# """
#
# def main ():
#     soup = BeautifulSoup(html_doc,'html.parser')
#
#     p_description = soup.find(('p', {'class': 'card-description'})).text
#     print(p_description)
# main()


# html = """<p class="card-articul">Артикул: 104774</p>
# <p class="card-articul">Артикул: 105550</p>
# <p class="card-articul">Артикул: 106200</p>"""
# soup = BeautifulSoup(html,'lxml')
# all_p = soup.find_all('p', {'class': 'card-articul'})
# res = 0
# res = sum(int(p.text.split()[1]) for p in all_p)
# # for p in all_p:
# #     num = p.text.split()[1]
# #     res += int(num)
#
# print(res)

# responce = requests.get('https://parsinger.ru/4.3/3/index.html')
#
# soup = BeautifulSoup(responce.text, 'lxml')
#
# imgs = soup.find_all('img')
# sm = sum(int(i.attrs['alt']) for i in imgs)
# print(sm)
# for i in imgs:
#     print(int(i.attrs['alt']))



html ='''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Тестовая страница для веб-парсинга</title>
</head>
<body>
    <p id="435456" class="123984">Веб-парсинг – это мощный инструмент для анализа данных в интернете.</p>
    <p id="284359" class="493572">Python предоставляет отличные библиотеки для парсинга веб-страниц.</p>
    <p id="789234" class="293487">Для начинающих веб-парсеров важно изучить основы HTML и CSS.</p>
    <p id="239048" class="392874">Библиотека BeautifulSoup позволяет легко извлекать данные с веб-страниц.</p>
    <p id="923874" class="120948">Scrapy – другой популярный фреймворк для веб-парсинга на Python.</p>
    <p id="982374" class="302984">Веб-парсинг может помочь аналитикам и маркетологам собирать ценную информацию.</p>
    <p id="238940" class="238492">Соблюдение законов и правил при парсинге веб-сайтов – это ключевой момент.</p>
    <p id="923485" class="283947">Ограничения robots.txt могут влиять на возможность парсинга некоторых сайтов.</p>
    <p id="293847" class="394872">Динамические веб-сайты могут требовать использование Selenium для парсинга.</p>
    <p id="239487" class="238492">Регулярные выражения могут быть полезными при извлечении специфических данных.</p>
    <p id="203984" class="394872">При веб-парсинге важно учитывать нагрузку на целевой веб-сайт.</p>
    <p id="394872" class="203984">Кэширование данных может ускорить процесс парсинга и снизить нагрузку на сервер.</p>
    <p id="238492" class="394872">Прокси-сервера могут помочь обойти ограничения, связанные с IP-адресом.</p>
    <p id="239847" class="238947">Парсинг может быть автоматизирован с помощью планировщика задач.</p>
    <p id="394872" class="238492">Обработка ошибок – важный этап в разработке парсера.</p>
    <p id="238492" class="394872">Сохранение данных в базу данных позволяет легко анализировать и обрабатывать информацию.</p>
    <p id="293847" class="203984">Многопоточность может значительно ускорить процесс парсинга веб-сайтов.</p>
    <p id="394872" class="203984">Веб-парсинг – это не только технический процесс, но и аналитический навык.</p>
    <p id="293847" class="394872">Изучение веб-парсинга открывает новые возможности для исследования интернета.</p>
    <p id="238947" class="238492">Качественный парсер требует тщательной проработки и тестирования.</p>
    <p id="384756" class="293487">Парсинг веб-страниц – это процесс извлечения данных с онлайн-ресурсов.</p>
    <p id="238947" class="293487">Python стал популярным языком для веб-парсинга благодаря своей простоте и богатой экосистеме.</p>
    <p id="384756" class="238492">Знание структуры HTML и CSS сделает вас более эффективным веб-парсером.</p>
    <p id="238947" class="238492">BeautifulSoup предоставляет удобные методы для поиска и извлечения данных из HTML-документов.</p>
    <p id="384756" class="293487">Scrapy облегчает парсинг множества страниц и управление запросами.</p>
    <p id="238947" class="293487">Веб-парсинг помогает в анализе конкурентов и рынка для бизнеса.</p>
    <p id="384756" class="238492">Соблюдение этичных и юридических норм важно при веб-парсинге.</p>
    <p id="238947" class="238492">Файл robots.txt указывает правила доступа для веб-краулеров и парсеров.</p>
    <p id="384756" class="293487">Selenium полезен для парсинга динамических веб-сайтов с JavaScript.</p>
    <p id="238947" class="293487">Регулярные выражения могут быть мощным инструментом для извлечения данных из текста.</p>
    <p id="384756" class="238492">Оптимизация запросов и паузы важны для избежания блокировки при парсинге.</p>
    <p id="238947" class="238492">Кэширование данных улучшает производительность парсера и снижает нагрузку.</p>
    <p id="384756" class="293487">Использование прокси-серверов помогает в обходе ограничений по IP-адресу.</p>
    <p id="238947" class="293487">Автоматизация парсинга с помощью планировщика может сэкономить время.</p>
    <p id="384756" class="238492">Обработка и логирование ошибок важны для стабильной работы парсера.</p>
    <p id="238947" class="238492">Сохранение данных в базу данных обеспечивает их долгосрочное хранение и анализ.</p>
    <p id="384756" class="293487">Многопоточность увеличивает скорость парсинга и снижает время выполнения задач.</p>
    <p id="238947" class="293487">Веб-парсинг требует аналитического мышления и понимания данных.</p>
    <p id="384756" class="238492">Изучение веб-парсинга расширяет возможности для исследования интернета и данных.</p>
    <p id="238947" class="238492">Разработка качественного парсера – это процесс, требующий тщательной проработки и тестирования.</p>
    <p id="384756" class="293487">Извлечение данных из веб-страницы – ключевой этап в анализе интернет-контента.</p>
    <p id="238947" class="293487">Python предоставляет множество возможностей для работы с текстом и данными.</p>
    <p id="384756" class="238492">Оптимизация запросов и управление скоростью парсинга – залог успешного сбора данных.</p>
    <p id="238947" class="238492">Использование кэширования может значительно снизить нагрузку на серверы и ускорить работу парсера.</p>
    <p id="384756" class="293487">Прокси-сервера – надежный способ обойти ограничения по IP и повысить анонимность.</p>
    <p id="238947" class="293487">Автоматизация задач с помощью планировщика обеспечивает регулярное обновление данных.</p>
    <p id="384756" class="238492">Обработка ошибок и их логирование помогают выявить проблемы и улучшить стабильность парсера.</p>
    <p id="238947" class="238492">Сохранение данных в базе обеспечивает их сохранность и возможность дальнейшего анализа.</p>
    <p id="384756" class="293487">Использование многопоточности позволяет параллельно обрабатывать множество страниц.</p>
    <p id="238947" class="293487">Веб-парсинг – это искусство анализа и извлечения информации из виртуального мира.</p>
    <p id="384756" class="238492">Изучение веб-парсинга даёт возможность исследовать интернет в поисках ценных данных.</p>
    <p id="238947" class="238492">Разработка парсера – это непрерывный процесс улучшения и оптимизации.</p>
    <p id="384756" class="293487">API предоставляют более удобный способ доступа к данным, чем парсинг страниц.</p>
    <p id="238947" class="293487">XPath – мощный инструмент для навигации и извлечения данных из XML и HTML.</p>
    <p id="384756" class="238492">Парсинг данных из JSON позволяет эффективно работать с данными в этом формате.</p>
    <p id="238947" class="238492">Анализ времени выполнения запросов помогает оптимизировать парсинг и снизить нагрузку.</p>
    <p id="384756" class="293487">Эффективный веб-парсинг требует понимания принципов работы HTTP-протокола.</p>
    <p id="238947" class="293487">Системы управления версиями помогают отслеживать изменения в коде парсера.</p>
    <p id="384756" class="238492">Интеграция с облачными хранилищами данных облегчает анализ собранных данных.</p>
    <p id="238947" class="238492">Аналитика и визуализация данных помогают получить ценные инсайты из собранных информационных ресурсов.</p>
    <p id="384756" class="293487">Понимание DOM-структуры помогает эффективно навигировать по веб-страницам.</p>
    <p id="238947" class="293487">Python имеет богатую экосистему для анализа данных, что делает его отличным выбором для парсинга.</p>
    <p id="384756" class="238492">Контроль частоты запросов позволяет избегать блокировок со стороны серверов.</p>
    <p id="238947" class="238492">Использование регулярных выражений требует навыков и практики, но может быть мощным инструментом.</p>
    <p id="384756" class="293487">Прокси-сервера могут быть необходимы для работы с сайтами, блокирующими IP-адреса.</p>
    <p id="238947" class="293487">Планировщики задач помогают автоматизировать процесс парсинга по расписанию.</p>
    <p id="384756" class="238492">Обработка ошибок включает в себя исключения и стратегии восстановления парсера.</p>
    <p id="238947" class="238492">Сохранение данных в базе обеспечивает надежное хранение и возможность долгосрочного анализа.</p>
    <p id="384756" class="293487">Использование многопоточности может значительно ускорить процесс сбора данных.</p>
    <p id="238947" class="293487">Веб-парсинг помогает исследователям извлекать информацию из различных источников.</p>
    <p id="384756" class="238492">Разработка парсера требует тщательного планирования и тестирования функциональности.</p>
    <p id="238947" class="238492">Интеграция с RESTful API облегчает получение данных с веб-серверов.</p>
    <p id="384756" class="293487">XPath позволяет точно находить и извлекать элементы на веб-странице.</p>
    <p id="238947" class="293487">JSON является удобным форматом для передачи и хранения данных при парсинге.</p>
    <p id="384756" class="238492">Мониторинг и управление ресурсами помогают избежать перегрузки серверов.</p>
    <p id="238947" class="293487">Знание структуры URL важно для формирования правильных запросов.</p>
    <p id="384756" class="293487">Веб-парсинг может использоваться для сравнения цен на товары и услуги.</p>
    <p id="238947" class="238492">Эффективный парсер должен быть адаптирован к особенностям целевых веб-сайтов.</p>
    <p id="384756" class="293487">Интеграция с базами данных позволяет хранить и анализировать большие объемы данных.</p>
    <p id="238947" class="238492">Аналитика данных позволяет выявить тенденции и паттерны в собранных информационных ресурсах.</p>
</body>
</html>
'''
#
# def sum_even_length_ids(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     all_p = soup.find_all('p')
#     total_id_sum = 0
#     total_class_sum = 0
#     for p in all_p:
#         temp = p.text.replace(' ', '')
#         if len(temp) % 2 == 0:
#            total_id_sum += int(p.attrs['id'])
#            print(p.attrs)
#            total_class_sum = int(''.join(p.attrs['class']))
#
#
#
#     return print(f"Сумма ID и CLASS тегов <p> с чётной длиной текста без пробелов: {total_id_sum + total_class_sum}")
#
#
# sum_even_length_ids(html)



html ='''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Онлайн Магазин Книг</title>
</head>
<body>
    <div class="book-card">
        <img src="1.png" alt="Обложка книги 1" class="book-cover book-cover_hard">
        <h2 class="book pages">Название Книги 1</h2>
        <p class="book-author">Автор: Автор 1</p>
        <p class="book-isbn">ISBN: 978-1234567890</p>
        <p class="book-cover-type">Обложка: Твердая</p>
        <p class="count price">Цена: $20.00</p>
        <p class="book-format">Формат: Мягкая обложка</p>
        <p class="count pages">Количество страниц: 300</p>
        <p class="count stock">Количество на складе: 75</p>
        <p class="book-publisher">Издательство: Издательство 1</p>
        <p class="book-publication-date">Дата публикации: 01.01.2023</p>
        <p class="count rating">Рейтинг: 4.5</p>
        <p class="book-genre">Жанр: Роман</p>
        <p class="book-language">Язык: Английский</p>
        <p class="book-availability">Доступность: В наличии</p>
        <p class="book-description">Описание: Краткое описание книги 1.</p>
        <button class="book-purchase-btn">Добавить в корзину</button>
    </div>
    <div class="book-card">
        <img src="2.png" alt="Обложка книги 2" class="book-cover book-cover_hard">
        <h2 class="book pages">Название Книги 2</h2>
        <p class="book-author">Автор: Автор 2</p>
        <p class="book-isbn">ISBN: 978-9876543210</p>
        <p class="book-cover-type">Обложка: Мягкая</p>
        <p class="count price">Цена: $18.50</p>
        <p class="book-format">Формат: Электронная версия (e-book)</p>
        <p class="count pages">Количество страниц: 250</p>
        <p class="count stock">Количество на складе: 119</p>
        <p class="book-publisher">Издательство: Издательство 3</p>
        <p class="book-publication-date">Дата публикации: 20.03.2023</p>
        <p class="count rating">Рейтинг: 4.7</p>
        <p class="book-genre">Жанр: Детская литература</p>
        <p class="book-language">Язык: Французский</p>
        <p class="book-availability">Доступность: В наличии</p>
        <p class="book-description">Описание: Краткое описание книги 2.</p>
         <button class="book-purchase-btn">Добавить в корзину</button>
    </div>
    <div class="book-card">
        <img src="3.png" alt="Обложка книги 3" class="book-cover book-cover_hard">
        <h2 class="book pages">Название Книги 3</h2>
        <p class="book-author">Автор: Автор 3</p>
        <p class="book-isbn">ISBN: 978-0987654321</p>
        <p class="book-cover-type">Обложка: Твердая</p>
        <p class="count price">Цена: $25.00</p>
        <p class="book-format">Формат: Мягкая обложка</p>
        <p class="count pages">Количество страниц: 400</p>
        <p class="count stock">Количество на складе: 216</p>
        <p class="book-publisher">Издательство: Издательство 2</p>
        <p class="book-publication-date">Дата публикации: 15.02.2023</p>
        <p class="count rating">Рейтинг: 4.8</p>
        <p class="book-genre">Жанр: Фантастика</p>
        <p class="book-language">Язык: Русский</p>
        <p class="book-availability">Доступность: В наличии</p>
        <p class="book-description">Описание: Краткое описание книги 3.</p>
        <button class="book-purchase-btn">Добавить в корзину</button>
    </div>
    <div class="book-card">
        <img src="4.png" alt="Обложка книги 4" class="book-cover book-cover_hard">
        <h2 class="book pages">Название Книги 4</h2>
        <p class="book-author">Автор: Автор 4</p>
        <p class="book-isbn">ISBN: 978-5432109876</p>
        <p class="book-cover-type">Обложка: Твердая</p>
        <p class="count price">Цена: $22.00</p>
        <p class="book-format">Формат: Мягкая обложка</p>
        <p class="count pages">Количество страниц: 350</p>
        <p class="count stock">Количество на складе: 17</p>
        <p class="book-publisher">Издательство: Издательство 4</p>
        <p class="book-publication-date">Дата публикации: 10.04.2023</p>
        <p class="count rating">Рейтинг: 4.9</p>
        <p class="book-genre">Жанр: Детектив</p>
        <p class="book-language">Язык: Английский</p>
        <p class="book-availability">Доступность: В наличии</p>
        <p class="book-description">Описание: Краткое описание книги 4.</p>
        <button class="book-purchase-btn">Добавить в корзину</button>
    </div>
    <div class="book-card">
        <img src="5.png" alt="Обложка книги 5" class="book-cover book-cover_hard">
        <h2 class="book pages">Название Книги 5</h2>
        <p class="book-author">Автор: Автор 5</p>
        <p class="book-isbn">ISBN: 978-8765432109</p>
        <p class="book-cover-type">Обложка: Мягкая</p>
        <p class="count price">Цена: $19.50</p>
        <p class="book-format">Формат: Мягкая обложка</p>
        <p class="count pages">Количество страниц: 280</p>
        <p class="count stock">Количество на складе: 63</p>
        <p class="book-publisher">Издательство: Издательство 5</p>
        <p class="book-publication-date">Дата публикации: 05.05.2023</p>
        <p class="count rating">Рейтинг: 4.6</p>
        <p class="book-genre">Жанр: Фэнтези</p>
        <p class="book-language">Язык: Испанский</p>
        <p class="book-availability">Доступность: В наличии</p>
        <p class="book-description">Описание: Краткое описание книги 5.</p>
        <button class="book-purchase-btn">Добавить в корзину</button>
    </div>
</body>
</html>
'''

# def calculate_total_price(html: str) -> float:
#     # Инициализация BeautifulSoup.
#     soup = BeautifulSoup(html, 'html.parser')
#     total = 0
#     all_divs = soup.find_all('div', class_='book-card')
#     for div in all_divs:
#         price = float(div.find('p', class_='count price').text.replace(':','').split()[1][1:])
#         amount = int(div.find('p', class_='count stock').text.replace(':','').split()[-1])
#         total += price * amount
#     return total
#
#
# print(f"Общая стоимость в случае продажи всех товаров: ${calculate_total_price(html)}")

#
# responce = requests.get('https://parsinger.ru/html/index1_page_1.html')
# responce.encoding = 'UTF-8'
# soup = BeautifulSoup(responce.text, 'html.parser')
# total = 0
# div = soup.find_all('div', class_='item')
# for item in div:
#     total += int(item.find('p', class_='price').text.split()[0])
#
# print(total)

#
# responce = requests.get('https://parsinger.ru/html/hdd/4/4_1.html')
# responce.encoding = 'UTF-8'
# soup = BeautifulSoup(responce.text, 'html.parser')
# price = float(soup.find('span', id='price').text.split()[0])
# old_price = float(soup.find('span', id='old_price').text.split()[0])
# discount = (old_price - price) * 100 / old_price #(старая цена - новая цена) * 100 / старая цена)
# print(round(discount, 1))

# url = 'https://parsinger.ru/html/index3_page_'
# res = []
# for i in range(1,5):
#     responce = requests.get(f'{url}{str(i)}.html')
#     responce.encoding = 'UTF-8'
#     soup = BeautifulSoup(responce.text, 'lxml')
#     divs = soup.find_all('div', class_='item')
#     names = [item.find('a', class_='name_item').text for item in divs]
#     res.append(names)
# print(res)

# url = 'https://parsinger.ru/html/index3_page_'
# res = []
# total = 0
# for i in range(1,5):
#     response = requests.get(f'{url}{str(i)}.html')
#     response.encoding = 'UTF-8'
#     soup = BeautifulSoup(response.text, 'lxml')
#     divs = soup.find_all('div', class_='item')
#     names = [item.find('a', class_='name_item') for item in divs]
#
#     def get_mouse(link):
#         base_url = 'https://parsinger.ru/html/'
#         response = requests.get(base_url + link)
#         response.encoding = 'UTF-8'
#         soup = BeautifulSoup(response.text, 'lxml')
#         art = int(soup.find('p', class_='article').text.split()[1])
#         return art
#
#
#     for mouse in names:
#         total += get_mouse(mouse.attrs['href'])
#
# print(total)

# base_url = 'https://parsinger.ru/html/'
#
#
# first_link = 'https://parsinger.ru/html/index1_page_1.html'
# r = requests.get(first_link)
# r.encoding = 'UTF-8'
# soup = BeautifulSoup(r.text, 'lxml')
# menu = soup.find('div', class_='nav_menu')
# cats = menu.find_all('a')
# total = 0
# for cat in cats:
#     url = base_url + cat.attrs['href']
#     r = requests.get(url)
#     r.encoding = 'UTF-8'
#     soup = BeautifulSoup(r.text, 'lxml')
#     pages = soup.find('div', class_='pagen').find_all('a')
#     for link in pages:
#         page_url = base_url + link.attrs['href']
#         page_req = requests.get(page_url)
#         page_req.encoding = 'UTF-8'
#         page_soup = BeautifulSoup(page_req.text, 'lxml')
#         divs = page_soup.find_all('div', class_='item')
#         names = [item.find('a', class_='name_item').attrs['href'] for item in divs]
#         for name in names:
#             item_url = base_url + name
#             item_req = requests.get(item_url)
#             item_req.encoding = 'UTF-8'
#             item_soup = BeautifulSoup(item_req.text, 'lxml')
#             stock = item_soup.find('span', id='in_stock').text.split()[2]
#             price = item_soup.find('span', id='price').text.split()[0]
#             total += int(stock) * int(price)
#
# print(total)

#
# url = 'https://parsinger.ru/table/1/index.html'
# r = requests.get(url)
# soup = BeautifulSoup(r.text, 'lxml')
# table = soup.find('table')
#
# # Извлекаем все строки таблицы
# rows = table.find_all('tr')
# all_nums = []
# # Проходим по строкам таблицы, начиная со второй (индекс 1), так как первая строка - это заголовки
# for row in rows[1:]:
#     columns = row.find_all('td')
#     lst = [float(i.text) for i in columns if float(i.text) not in all_nums]
#     all_nums.extend(lst)
# print(sum(all_nums))

#
# url = 'https://parsinger.ru/table/2/index.html'
# r = requests.get(url)
# soup = BeautifulSoup(r.text, 'lxml')
# table = soup.find('table')
#
# # Извлекаем все строки таблицы
# rows = table.find_all('tr')
# all_nums = []
# # Проходим по строкам таблицы, начиная со второй (индекс 1), так как первая строка - это заголовки
# for row in rows[1:]:
#     columns = row.find_all('td')
#     all_nums.append(float(columns[0].text))
#
# print(sum(all_nums))


#
# url = 'https://parsinger.ru/table/4/index.html'
# r = requests.get(url)
# soup = BeautifulSoup(r.text, 'lxml')
# table = soup.find('table')
# res = []
# # Извлекаем все строки таблицы
# rows = table.find_all('tr')
# for row in rows[1:]:
#     b = row.find_all('td', 'green')  #1
#     b = row.select('.green')  #2
#     print(b)
#     for i in b:
#         print(i.text)
#     lst = [float(i.text) for i in b]
#     res.extend(lst)
#
# print(sum(res))


#
# url = 'https://parsinger.ru/table/5/index.html'
# r = requests.get(url)
# soup = BeautifulSoup(r.text, 'lxml')
# table = soup.find('table')
# res = []
# # Извлекаем все строки таблицы
# rows = table.find_all('tr')
# for row in rows[1:]:
#     orange = row.select('.orange')[0]  #2
#     blue = row.find_all('td')[-1]
#     res.append(float(orange.text) * int(blue.text))
#
#
# print(sum(res))


# url = 'https://parsinger.ru/table/5/index.html'
# r = requests.get(url)
# soup = BeautifulSoup(r.text, 'lxml')
# table = soup.find('table')
#
# # Извлекаем все строки таблицы
# rows = table.find_all('tr')
# names = table.find_all('th')
# res = {k.text:0 for k in names}
# for row in rows[1:]:
#     columns = row.find_all('td')
#     print(columns)
#     for i, k in enumerate(res):
#         res[k] += float(columns[i].text)
#
# for k, v in res.items():
#     res[k] = round(v, 3)
#
# print(res)


# url = 'https://parsinger.ru/4.8/7/index.html'
# r = requests.get(url)
# soup = BeautifulSoup(r.text, 'lxml')
# tables = soup.find_all('table')
# total = 0
# for table in tables:
#     tds = table.find_all('td')
#     sm = sum([int(i.text) for i in tds if int(i.text) % 3 == 0])
#     total += sm
#     print(total)

# start = time.time()
# url = 'https://parsinger.ru/4.8/8/index.html'
# r = requests.get(url)
# soup = BeautifulSoup(r.text, 'lxml')
# table = soup.find('table')
# res = []
# th = table.find_all()
# for t in th:
#     if t.has_attr('colspan') and len(t.find_all()) == 0:
#         res.append(int(t.text))
# print(sum(res))
# print(time.time() - start)
# start = time.time()
# r = requests.get('https://parsinger.ru/4.8/8/index.html')
# s = BeautifulSoup(r.text, 'html.parser')
#
# print(sum([int(i.text) for i in s.select('table td [colspan]')]))
# print(time.time() - start)

# import json
# import copy
#
# url = 'https://parsinger.ru/4.8/6/index.html'
# r = requests.get(url)
# r.encoding = 'UTF-8'
# soup = BeautifulSoup(r.text, 'lxml')
# table = soup.find('table')
# names = table.find_all('th')
# dct = {k.text:0 for k in names}
# res = []
#
# rows = table.find_all('tr')
# for row in rows[1:]:
#     temp_dct = {}
#     columns = row.find_all('td')
#     for i, k in enumerate(dct):
#         if columns[i].text.isdigit():
#             temp_dct[k] = int(columns[i].text)
#         else:
#             temp_dct[k] = columns[i].text
#
#     #print(temp_dct['Стоимость авто'] < 4_000_000, dct['Стоимость авто'], dct['Год выпуска'] > 2004, dct['Год выпуска'],dct['Тип двигателя'] == 'Бензиновый')
#     if temp_dct['Стоимость авто'] < 4_000_000 and temp_dct['Год выпуска'] > 2004 and temp_dct['Тип двигателя'] == 'Бензиновый':
#         res_dct = {
#             'Марка Авто': temp_dct['Марка Авто'],
#             'Год выпуска': temp_dct['Год выпуска'],
#             'Тип двигателя': temp_dct['Тип двигателя'],
#             'Стоимость авто': temp_dct['Стоимость авто']
#         }
#         res.append(res_dct)
#
# sorted_cars = res
# res = json.dumps(sorted(sorted_cars, key=lambda x: x["Стоимость авто"]), indent=4, ensure_ascii=False)
# print(res)


import csv
import requests
from bs4 import BeautifulSoup

# # 1 ------------------------------------------------------
# with open('hdd.csv', 'w', encoding='utf-8-sig', newline='') as file:
#     writer = csv.writer(file, delimiter=';')
#     writer.writerow([
#         'Наименование', 'Бренд', 'Форм-фактор', 'Ёмкость', 'Объем буферной памяти', 'Цена'])
# # 1 ------------------------------------------------------
#
# # 2 ------------------------------------------------------
# url = 'https://parsinger.ru/html/index4_page_'
#
# for i in range(1,5):
#     search = f'{url}{i}.html'
#     response = requests.get(url=search)
#     response.encoding = 'utf-8'
#     soup = BeautifulSoup(response.text, 'lxml')
#
# # 2 ------------------------------------------------------
#
# # 3 ------------------------------------------------------
# # Извлекаем имена товаров и убираем лишние пробелы
#     name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
#
#     # Извлекаем описание товаров и разбиваем на строки
#     description = [x.text.split('\n') for x in soup.find_all('div', class_='description')]
#
#     # Извлекаем цены товаров
#     price = [x.text for x in soup.find_all('p', class_='price')]
# # 3 ------------------------------------------------------
#
#
# # 4------------------------------------------------------
# # Открываем файл для дополнительной записи данных
#     with open('hdd.csv', 'a', encoding='utf-8-sig', newline='') as file:
#         writer = csv.writer(file, delimiter=';')
#         for item, price, descr in zip(name, price, description):
#
#             # Формируем строку для записи
#             flatten = item, *[x.split(':')[1].strip() for x in descr if x], price
#             print(flatten)
#             writer.writerow(flatten)
#
# print('Файл res.csv создан')


# articles = []
# root = 'https://parsinger.ru/html/'
#
#
# for i in range(1, 5):
#     url = f'http://parsinger.ru/html/index1_page_{i}.html'
#     r = requests.get(url)
#     r.encoding = 'UTF-8'
#     soup = BeautifulSoup(r.text, 'lxml')
#
#     for x in soup.find_all('div', 'sale_button'):
#         href = root + x.find('a')['href']
#         r = requests.get(href)
#         r.encoding = 'utf-8'
#         s = BeautifulSoup(r.text, 'lxml')
#         res = {
#             'Наименование': s.find('p', id='p_header').text,
#             'Артикул': int(s.find('p', class_='article').text.split()[-1]),
#             'Бренд':  s.find('li', id='brand').text.split(': ')[-1],
#             'Модель': s.find('li', id='model').text.split(': ')[-1],
#             'Тип': s.find('li', id='type').text.split(': ')[-1],
#             'Технология экрана': s.find('li', id='display').text.split(': ')[-1],
#             'Материал корпуса' : s.find('li', id='material_frame').text.split(': ')[-1],
#             'Материал браслета': s.find('li', id='material_bracer').text.split(': ')[-1],
#             'Размер': s.find('li', id='size').text.split(': ')[-1],
#             'Сайт производителя': s.find('li', id='site').text.split(': ')[-1],
#             'Наличие': int(s.find('span', id='in_stock').text.split(': ')[-1]),
#             'Цена': s.find('span', id='price').text.split(': ')[-1],
#             'Старая цена': s.find('span', id='old_price').text.split(': ')[-1],
#             'Ссылка на карточку с товаром': href
#         }
#         articles.append(res)
# fieldnames = [*articles[0].keys()]
# print(fieldnames)
# with open('all_stock.csv', 'w', encoding='UTF-8', newline='') as file:
#     writer = csv.DictWriter(file, delimiter=";", fieldnames=fieldnames)
#     writer.writeheader()
#     for row in articles:
#         writer.writerow(row)
#     print('ok!')


# import requests, csv
# from bs4 import BeautifulSoup
#
# all_items_list = []
# for category in range(1, 6):
#     for page in range(1, 5):
#         URL = f'https://parsinger.ru/html/index{category}_page_{page}.html'
#         response = requests.get(url=URL)
#         response.encoding = 'utf-8'
#         soup = BeautifulSoup(response.text, 'lxml')
#
#         name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
#         description = [x.text.split('\n') for x in soup.find_all('div', class_='description')]
#         price = [x.text for x in soup.find_all('p', class_='price')]
#
#         for item, price, descr in zip(name, price, description):
#             flatten = item, *[x.split(':')[1].strip() for x in descr if x], price
#             all_items_list.append(flatten)
#
# with open('all_items.csv', 'w', encoding='UTF-8', newline='') as file:
#     writer = csv.writer(file, delimiter=';')
#     writer.writerows(all_items_list)

