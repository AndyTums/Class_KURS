from src.work_with_API import HeadHunter
from src.work_with_vacancies import Vacancies
import re


def top_vacancies(vacancies: list, value: int) -> list:
    """ Функция принимает в себя список класса Вакансий и кол-во вывода вакансий с самой высокой ЗП """

    sort_list = sorted(vacancies, key=lambda x: x.salary_from, reverse=True)  # Сортируем по ТОП ЗП
    return sort_list[0:value]  # Возвращаем необходимое кол-во вакансий


def filter_words(vacancies: list, words: str) -> list:
    """ Функция принимает список класса вакансий и фильтрует по заданному слову в описании """

    # filters = [sort for sort in vacancies if sort.description is not None and words in sort.description]
    filters = [sort for sort in vacancies if
               sort.description is not None and re.findall(words, sort.description, flags=re.IGNORECASE)]

    return filters


if __name__ == "__main__":
    head = HeadHunter()
    head_1 = head.get_vacancies()
    vac = Vacancies.cast_to_object_list(head_1)
    print(filter_words(vac, "товар")[0].description)
