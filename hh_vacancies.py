from main_functions import predict_salary, draw_table, get_vacancies_statistic
import requests
import time
import argparse


def predict_rub_salary_hh(vacancy):
    salary = vacancy["salary"]
    if not salary:
        return None
    if salary["currency"] != "RUR":
        return None
    return predict_salary(salary["from"], salary["to"])


def collect_hh_vacancies(languages):
    vacancies = {}
    professional_role_id = 96
    city_id = 1
    days = 30
    for language in languages:
        vacancies[language] = []
        page_number = 1
        page = 0
        while page < page_number:
            params = {
                "professional_role": professional_role_id,
                "area": city_id,
                "period": days,
                "text": language,
                "search_field": "name",
                "page": page
            }
            try:
                page_response = requests.get(
                    "https://api.hh.ru/vacancies", params=params
                )
                page_response.raise_for_status()

                time.sleep(0.5)
            except requests.exceptions.HTTPError:
                time.sleep(1)

            page_payload = page_response.json()
            page_number = page_payload["pages"]
            page += 1

            page_vacancies = page_payload["items"]
            for vacancy in page_vacancies:
                vacancies[language].append(vacancy)
    return vacancies


def draw_hh_statistic(languages):
    hh_vacancies = collect_hh_vacancies(languages)
    hh_statistic = get_vacancies_statistic(hh_vacancies, predict_rub_salary_hh)
    return draw_table(hh_statistic, "HeadHunter Moscow")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""Скрипт высчитывает среднюю зарплату по вакансиям разработчиков 
        в г.Москва на сервисе HeadHunter в разрезе языков программирования."""
    )
    parser.add_argument(
        "-l",
        "--languages",
        nargs="+",
        help="список языков программирования",
    )
    args = parser.parse_args()

    print(draw_hh_statistic(args.languages))
