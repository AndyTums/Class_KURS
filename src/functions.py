import re


def top_vacancies(vacancies: list, value: int) -> list:
    """ Функция принимает в себя список класса Вакансий и кол-во вывода вакансий с самой высокой ЗП """

    sort_list = sorted(vacancies, key=lambda x: x.salary_from, reverse=True)  # Сортируем по ТОП ЗП
    return sort_list[0:value]  # Возвращаем необходимое кол-во вакансий


def filter_words(vacancies: list, words: str) -> list:
    """ Функция принимает список класса вакансий и фильтрует по заданному слову в описании """

    filters = [sort for sort in vacancies if
               sort.description is not None and re.findall(words, sort.description.replace(" ", "").lower(),
                                                           flags=re.IGNORECASE)]

    return filters


def sorting_of_salary(list_vacancies: list, salary_from: int, salary_to: int) -> list:
    """ Принимает список класса вакансий и два аргумента ЗП от и до, отдает отсортированный список """

    list_salary = []
    for vacancy in list_vacancies:
        if salary_from <= vacancy.salary_from and salary_to >= vacancy.salary_to:
            list_salary.append(vacancy)
        else:
            del vacancy

    return list_salary


def work_with_user(list_vacancies: list):
    """ Принимает список вакансий и выводит для работы с пользователем """

    for vac in list_vacancies:
        if vac.salary_from >= vac.salary_to:
            first = (f"Название вакансии: {vac.name}\nОписание: {vac.description}\nСсылка на вакансию: {vac.url}\n"
                     f"Зарплата: {vac.salary_from}\n")
            print(first)
        else:
            second = (
                f"Название вакансии: {vac.name}\nОписание: {vac.description}\nСсылка на вакансию: {vac.url}\n"
                f"Зарплата: {vac.salary_from} - {vac.salary_to}\n")
            print(second)
