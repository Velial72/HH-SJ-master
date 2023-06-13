from dotenv import load_dotenv
import os
from main_functions import draw_table, get_vacancies_statistic
from hh_vacancies import collect_hh_vacancies, predict_rub_salary_hh
from sj_vacancies import collect_superjob_vacancies, predict_rub_salary_for_superJob


if __name__ == "__main__":
    load_dotenv()
    languages = [
        "JavaScript",
        "Java",
        "Python",
        "Ruby",
        "PHP",
        "C++",
        "C#",
        "C",
        "Go",
        "Shell",
        "Objective-C",
        "Scala",
        "Swift"
    ]
    superjob_key = os.environ["SUPERJOB_API_KEY"]

    hh_vacancies = collect_hh_vacancies(languages)
    hh_statistic = get_vacancies_statistic(hh_vacancies, predict_rub_salary_hh)
    sj_vacancies = collect_superjob_vacancies(languages, superjob_key)
    sj_statistic = get_vacancies_statistic(sj_vacancies, predict_rub_salary_for_superJob)
    print()
    print(draw_table(hh_statistic, "HeadHunter Moscow"))
    print(draw_table(sj_statistic, "SuperJob Moscow"))
