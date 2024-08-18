import re

from src.utils import top_vacancies, filter_words, sorting_of_salary, work_with_user
from src.work_with_API import HeadHunter
from src.work_with_vacancies import Vacancies


def main():
    """ Основная функция для работы с пользователем """

    # Создаем класс для работы с API + приветствие
    platform = HeadHunter()
    print("Приветствую Вас, меня зовут Бот Хантер и я помогу найти Вам подходящую работу.\n")

    # Получение информации по API в зависимости от заданной вакансии или нет
    search_query = input("Пожалуйста, введите вакансия которая Вам интересна: ")
    result_search_query = platform.get_vacancies(search_query)
    # Преобразуем список словарей в класс Вакансий
    to_vacancies = Vacancies.cast_to_object_list(result_search_query)

    # Сортируем ТОП вакансий по зарплате
    top_n = int(input("Введите количество вакансий желающие видеть с наибольшей ЗП: "))
    result_top_n = top_vacancies(to_vacancies, top_n)

    # Фильтруем вакансии по заданному слову в описании
    filter_word = input("Введите слово интересующее Вас связанное с вакансией: ")
    result_filter_words = filter_words(result_top_n, filter_word)

    # Сортируем по заданному диапазону цен
    print("Введите диапазон ЗП: ")
    ans_salary_from = int(re.sub(r"[^\d]", "", input("От: ")))
    ans_salary_to = int(re.sub(r"[^\d]", "", input("До: ")))
    result_sort_salary = sorting_of_salary(result_filter_words, ans_salary_from, ans_salary_to)

    # Обрабатываем для удобного чтения пользователю
    to_user = work_with_user(result_sort_salary)

    return to_user


if __name__ == "__main__":
    main()
