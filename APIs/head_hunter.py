import requests
from pprint import pprint

from models.job_search import JobSearchAPI


class HeadHunterAPI(JobSearchAPI):
    def __init__(self, filter_words) -> None:
        self._url = "https://api.hh.ru"
        self.filter_words = filter_words

    def get_vacancies(self) -> list:
        params = {
            "text": self.filter_words
        }
        data = requests.get("https://api.hh.ru/vacancies", params=params).json()
        vacancies = []

        for vacancy in data["items"]:
            address = vacancy.get("address")
            city = "Not defined"
            if address is not None:
                city = address.get("city")

            description = vacancy.get("snippet", {})
            requirements = description.get("requirement", "Not defined")
            responsibilities = description.get("responsibility", "Not defined")

            formatted_description = "Not defined"
            if requirements != "Not defined" or responsibilities != "Not defined":
                formatted_description = f"Requirements: {requirements}\nResponsibilities: {responsibilities}"

            formatted_vacancy = {
                "id": vacancy.get("id", "Not defined"),
                "name": vacancy.get("name", "Not defined"),
                "salary": vacancy.get("salary", "Not defined"),
                "description": formatted_description,
                "url": vacancy.get("alternate_url", "Not defined"),
                "city": city,
                "platform": "hh.ru"
            }
            vacancies.append(formatted_vacancy)

        return vacancies


if __name__ == "__main__":
    pprint(HeadHunterAPI("CEO").get_vacancies())
