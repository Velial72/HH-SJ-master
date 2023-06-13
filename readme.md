# Проект сбора статистики по вакансиям программистов на сайтах HeadHunter и SuperJob.

Программа призвана автоматизировать сбор информации о вакансиях программистов в г. Москва с сайтов HeadHunter и SuperJob.

Основной скрипт выводит информацию в табличной форме о средней зарплате и количестве просмотренных вакансий в разрезе самых популярных языков программирования.

## Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
Для корректной работы понадобится в корневом каталоге проекта в файле `.env` прописать свой токен (`SUPERJOB_API_KEY`) для сайта superjob.ru. По ссылке можно получить токен:[инструкции](https://api.superjob.ru/) 
```
SUPERJOB_API_KEY=<SUPERJOB_API_KEY>
```

## Использование скриптов

Проект включает в себя несколько скриптов, имеющих следующий функционал.

### Основной исполняемый скрипт `main.py`
Выводит информацию в табличной форме о средней зарплате и количестве просмотренных вакансий в разрезе самых популярных языков программирования, сразу для двух площадок HeadHunter и SuperJob.

Пример запуска:
```bash
python main.py
```

### Вспомогательный скрипт `hh_vacancies.py`
Выводит информацию в табличной форме о средней зарплате и количестве просмотренных вакансий в разрезе указанных языков программирования на HeadHunter (г.Москва).

Принимает обязательный аргумент: 
* "-l", "--languages", - список языков программирования для поиска вакансий.


Пример запуска:
```bash
python hh_vacancies.py -l 'Python', 'C++', 'Java'
```

### Вспомогательный скрипт `sj_vacancies.py`
Выводит информацию в табличной форме о средней зарплате и количестве просмотренных вакансий в разрезе указанных языков программирования на SuperJob (г.Москва).
Требует получения SUPERJOB_API_KEY, который должен быть указан в переменной .env

Принимает обязательный аргумент: 
* "-l", "--languages", - список языков программирования для поиска вакансий.


Пример запуска:
```bash
python sj_vacancies.py -l 'Python', 'C++', 'Java'
```
