import os
import json
import requests
from pprint import pprint
from dotenv import load_dotenv

from models.job_search import JobSearchAPI

load_dotenv()

superjob_api_key = os.environ.get("SUPERJOB_API_KEY")


class SuperJobAPI(JobSearchAPI):
    def __init__(self, filter_words) -> None:
        self._api_key: str = superjob_api_key
        self.filter_words = filter_words
        self.headers: dict = {
            "Host": "api.superjob.ru",
            "X-Api-App-Id": self._api_key,
            "Authorisation": f"Bearer {self._api_key[3:]}",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        self.params: dict = {
            "keywords": self.filter_words
        }
        self.response: str = self.authenticate()

    def authenticate(self) -> str:
        return requests.get("https://api.superjob.ru/2.0/vacancies/", headers=self.headers, params=self.params).text

    def get_vacancies(self) -> list:
        data = json.loads(self.response)
        vacancies = []

        for vacancy in data["objects"]:
            address = vacancy.get("address")
            city = "Not defined"
            if address is not None:
                city_parts = address.split(",")
                if len(city_parts) > 0:
                    city = city_parts[0].strip()

            currency = vacancy.get("currency", "Not defined")
            payment_from = vacancy.get("payment_from", "Not defined")
            payment_to = vacancy.get("payment_to", "Not defined")

            formatted_salary = {
                "currency": currency,
                "from": payment_from,
                "to": payment_to
            }

            formatted_vacancy = {
                "id": vacancy.get("id", "Not defined"),
                "name": vacancy.get("profession", "Not defined"),
                "salary": formatted_salary,
                "description": vacancy.get("candidat", "Not defined"),
                "city": city,
                "alternate_url": vacancy.get("link", "Not defined"),
                "platform": "SuperJob"
            }

            vacancies.append(formatted_vacancy)

        return vacancies


if __name__ == "__main__":
    pprint(SuperJobAPI("программист").get_vacancies())
