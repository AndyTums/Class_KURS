from src.utils import top_vacancies
from src.work_with_API import HeadHunter
from src.work_with_vacancies import Vacancies


def main():
    platform = HeadHunter()
    print("Приветствую Вас, меня зовут Бот Хантер и я помогу найти Вам подходящую работу.\n")

    search_query = input("Пожалуйста, введите вакансия которая Вам интересна: ")
    result_search_query = platform.get_vacancies(search_query)
    to_vacancies = Vacancies.cast_to_object_list(result_search_query)
    print(to_vacancies)

    top_n = int(input("Введите количество вакансий желающие видеть с наибольшей ЗП: "))
    # result_top_n = top_vacancies(to_vacancies, top_n)
    # print(result_top_n)
    # filter_word = input("Введите слово интересующее Вас связанное с вакансией: ")
    # salary_range = input("Введите диапазон ЗП: ")


if __name__ == "__main__":
    main()