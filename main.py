from pprint import pprint

from APIs.head_hunter import HeadHunterAPI
from APIs.super_job import SuperJobAPI
from data_handling.json_saver import JSONSaver
from data_handling.vacancy import Vacancy
from models.vacancies import Vacancies

new_vacancy = Vacancies("Программист С++", "<https://hh.ru/vacancy/92547066>", "150 000-230 000 руб.",
                        "Требуемый опыт работы: 3–6 лет")

json_saver = JSONSaver()
json_saver.get_vacancies_by_salary("150 000-230 000 руб.")


def main():
    city = ""

    platform = input("Choose your platform\nHeadHunter - 1\nSuperJob - 2\nWrite 1 or 2: ")

    filter_words = input("Enter keywords to filter vacancies: ").split()

    amount = input("Enter the number of vacancies to display in top: ")
    if amount is None or amount == "":
        amount = 10
    else:
        amount = int(amount)

    sort_key = input("Enter sorting key (salary, city): ")
    if sort_key.lower() == "city":
        city = input("Enter title of city: ")

    reverse_sort = input("Sort in reverse order (yes or no): ").lower() == "yes"
    print()

    if "1" in platform.lower():
        hh_api = HeadHunterAPI(filter_words)
        filtered_vacancies = hh_api.get_vacancies()
    else:
        superjob_api = SuperJobAPI(filter_words)
        filtered_vacancies = superjob_api.get_vacancies()

    vacancy = Vacancy(filtered_vacancies, amount, filter_words)

    if sort_key:
        if sort_key == "city":
            filtered_vacancies = vacancy.sort_vacancies_by_city(filtered_vacancies, city)
        elif sort_key == "salary":
            filtered_vacancies = vacancy.sort_vacancies_by_salary(filtered_vacancies, reverse_sort)
    sorted_vacancies = vacancy.get_top_vacancies(filtered_vacancies)

    return pprint(sorted_vacancies)


if __name__ == "__main__":
    print(main())
