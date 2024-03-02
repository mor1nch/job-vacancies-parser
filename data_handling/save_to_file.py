import json
from pprint import pprint

from APIs.head_hunter import HeadHunterAPI
from APIs.super_job import SuperJobAPI


def save_vacancies_to_file(data, path: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def load_vacancies_from_file(path: str) -> list:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


if __name__ == "__main__":
    headhunter = HeadHunterAPI("программист")
    superjob = SuperJobAPI("программист")
    path_to_file = "../data/vacancies.json"

    vacancies = headhunter.get_vacancies() + superjob.get_vacancies()
    save_vacancies_to_file(vacancies, "../data/vacancies.json")
    print("Data updated")

    pprint(load_vacancies_from_file(path_to_file))
