import requests
from main_functions import predict_salary, draw_table, get_vacancies_statistic
import time
from dotenv import load_dotenv
import os
import argparse


def predict_rub_salary_for_superJob(vacancy):
    if vacancy["currency"] != "rub":
        return None
    return predict_salary(vacancy["payment_from"], vacancy["payment_to"])


def collect_superjob_vacancies(languages, superjob_key):
    headers = {"X-Api-App-Id": superjob_key}
    vacancies = {}
    city_id = 4
    profession_id = 48
    number_vacancies_on_page = 20
    vacancies_number_limit = 1000
    for language in languages:
        vacancies[language] = []
        page_number = 1
        page = 0
        while page < page_number:
            params = {
                "town": city_id,
                "catalogues": profession_id,
                "keyword": language,
                "page": page,
                "count": number_vacancies_on_page
            }
            try:
                page_response = requests.get(
                    "https://api.superjob.ru/2.0/vacancies/",
                    headers=headers,
                    params=params,
                )
                page_response.raise_for_status()

                time.sleep(0.5)
            except requests.exceptions.HTTPError:
                time.sleep(1)

            page_payload = page_response.json()
            if page_payload["total"] > vacancies_number_limit:
                page_number = vacancies_number_limit // number_vacancies_on_page
            elif page_payload["total"] < number_vacancies_on_page:
                page_number = 1
            else:
                page_number = page_payload["total"] // number_vacancies_on_page
            page += 1

            page_vacancies = page_payload["objects"]
            vacancies[language].extend(page_vacancies)
    return vacancies


if __name__ == "__main__":
    load_dotenv()
    superjob_api_key = os.environ["SUPERJOB_API_KEY"]

    parser = argparse.ArgumentParser(
        description="""Скрипт для подсчета средней зарплаты по вакансиям программистов 
        в г.Москва на сервисе SuperJob в разрезе языков программирования. """
    )
    parser.add_argument(
        "-l",
        "--languages",
        nargs="+",
        help="список языков программирования",
    )
    args = parser.parse_args()

    sj_vacancies = collect_superjob_vacancies(languages, superjob_key)
    sj_statistic = get_vacancies_statistic(sj_vacancies, predict_rub_salary_for_superJob)

    print(draw_table(sj_statistic, "SuperJob Moscow"))
