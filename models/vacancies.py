class Vacancies:
    def __init__(self, name: str, url: str, salary: str, description: str) -> None:
        self.name = name
        self.url = url
        self.salary = salary
        self.description = description

    def __str__(self):
        return f"{self.name}, salary: {self.salary}"
