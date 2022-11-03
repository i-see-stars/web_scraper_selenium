# Web Scraper

Web Scraper, реализованный с помощью библиотеки `Selenium`.

### Требования

- Python 3.10 (протестировано для Python 3.10.6)
- Google Chrome версия 107
- ChromeDriver 107.0.5304.62 (есть в репозитории)

### Установка и запуск

- Клонируем репозиторий `git clone https://github.com/i-see-stars/web_scraper_selenium.git`
- Переходим в склонированный репозиторий `cd web_scraper_selenium`
- `python3 -m venv .venv`
- `source .venv/bin/activate`
- `python -m pip install -r requirements.txt`
- `python scrape.py`

### Примечания

Не самая быстрая реализация. Хотел сымитировать поведение браузера 
в случае \"бесконечного скроллинга\". 
Делалось на скорую руку, это лишь черновая версия. 
Конечно, у меня есть много идей по улучшению скрапера.

### TODO:

- Написать функцию для обработки подкатегорий (`Laptops`, `Tablets`, `Touch`)
- Реализовать следующее
    - реализовать переход на [домашнюю страницу](https://webscraper.io/test-sites/e-commerce/scroll)
    - подождать прогрузки
    - перейти в категорию (`Computers`, `Phones`)
    - подождать прогрузки
    - перейти в подкатегории (`Laptops`, `Tablets`, `Touch`)
- Почистить `requirements.txt` от лишних пакетов