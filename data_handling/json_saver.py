import json


class JSONSaver:
    def __init__(self):
        self.path = "../data/vacancies.json"
        self.vacancies = []
        self.load_from_json()
        self.current_id = 1

    def __str__(self):
        return f"JSONSaver for {self.path}"

    def add_vacancy(self, vacancy) -> None:
        self.vacancies.append(vars(vacancy))
        self.save_to_json()

    def read_vacancy(self, vacancy_id):
        for vacancy in self.vacancies:
            if vacancy.get("id") == vacancy_id:
                return vacancy

        return None

    def update_vacancy(self, vacancy_id, name=None, url=None, salary=None, description=None):
        vacancy = self.read_vacancy(vacancy_id)
        if vacancy:
            if salary:
                salary = self.parse_salary(salary)
            if name:
                vacancy["name"] = name
            if url:
                vacancy["url"] = url
            if salary:
                vacancy["salary"] = salary
            if description:
                vacancy["description"] = description

            self.save_to_json()
            return vacancy

        return None

    def delete_vacancy(self, vacancy) -> None:
        self.vacancies.remove(vars(vacancy))
        self.save_to_json()

    def get_vacancies_by_salary(self, salary_range) -> list:
        filtered_vacancies = [v for v in self.vacancies if v["salary"] == salary_range]
        return filtered_vacancies

    def parse_salary(self, salary_str: str) -> dict | None:
        parts = salary_str.split(" - ")
        if len(parts) == 2:
            currency = "rub"
            from_salary = int(parts[0].replace(" ", ""))
            to_salary = int(parts[1].replace(" ", ""))
            return {"currency": currency, "from": from_salary, "to": to_salary}

        return None

    def save_to_json(self) -> None:
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(self.vacancies, file)

    def load_from_json(self) -> None:
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                self.vacancies = json.load(file)
        except FileNotFoundError:
            self.vacancies = []
