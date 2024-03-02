from abc import abstractmethod, ABC


class JobSearchAPI(ABC):
    @abstractmethod
    def get_vacancies(self):
        pass
