from abc import ABC, abstractmethod


class VacancyManager(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies_by_salary(self, salary_range):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass
