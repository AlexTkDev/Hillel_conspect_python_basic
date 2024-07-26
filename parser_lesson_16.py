import csv
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Заголовок для отправки запросов к серверу
header = {
    'User-Agent':
         'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/117.0',
    'Accept':
            'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}

def get_data_by_selenium(url: str) -> str:
    """Функция для получения HTML-кода страницы по URL с использованием Selenium."""
    # Инициализация сервиса для драйвера Firefox
    service = Service(path="geckodriver")
    driver = webdriver.Firefox(service=service)
    driver.get(url)  # Переход по указанному URL
    time.sleep(3)  # Ожидание загрузки страницы
    data = driver.page_source  # Получение HTML-кода страницы
    driver.quit()  # Закрытие браузера
    return data

def parse_data(data: str) -> list:
    """Функция парсинга данных из HTML-документа."""
    rez = []
    if data:
        soup = BeautifulSoup(data, 'html.parser')
        li_list = soup.find_all('li', attrs={'class': 'catalog-grid__cell'})
        for li in li_list:
            # Поиск тега <a> с классом 'goods-tile__heading'
            a = li.find('a', attrs={'class': 'goods-tile__heading'})
            # Извлечение ссылки из атрибута href
            href = a['href']
            # Извлечение текста, содержащего название товара
            title = a.text
            # Поиск блока со старой ценой
            old = li.find('div', attrs={'class': 'goods-tile__price--old'})
            # Поиск блока с текущей ценой
            price = li.find('div', attrs={'class': 'goods-tile__price'})
            # Обработка старой цены (если она есть)
            old_price = ''
            if old:
                old = old.text
                if old:
                    # Извлечение только цифр из текста старой цены
                    old_price = int(''.join(c for c in old if c.isdigit()))
            # Извлечение только цифр из текста текущей цены
            price = int(''.join(c for c in price.text if c.isdigit()))
            # Запись результатов по каждому товару в виде словаря
            rez.append({
                'title': title, 'href': href, 'price': price,
                'old_price': old_price
            })
    return rez

def save_to_csv(rows) -> None:
    """Функция сохранения данных в CSV-файл."""
    csv_title = ['title', 'href', 'price', 'old_price']
    with open('videocards.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=csv_title, delimiter=';')
        writer.writeheader()  # Запись заголовка
        writer.writerows(rows)  # Запись строк данных

def main() -> None:
    """Главная функция."""
    url = 'https://hard.rozetka.com.ua/videocards/c80087/page={}/'
    rows = []
    for i in range(1, 3):
        data = get_data_by_selenium(url.format(i))  # Получение данных для каждой страницы
        rows += parse_data(data)  # Парсинг данных и добавление их в общий список
        time.sleep(3)  # Ожидание перед переходом на следующую страницу

    save_to_csv(rows)  # Сохранение данных в CSV-файл

if __name__ == '__main__':
    main()
