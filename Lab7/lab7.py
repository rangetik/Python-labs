# Лабораторна 7

# Тема: Основи обробки винятків у мові програмування Python

# Загальне завдання: Передбачити можливість виникнення та реалізувати коректну обробку винятків.
# Інформацію про виникнення винятків необхідно виводити на екран та зберігати у логфайл.

# Варіант 8: Написати програму для обробки арифметичних помилок із записом інформації про виняток у файл.

import os
import datetime


# Функція для відображення вмісту файлу  в консолі (для перевірки)
def print_file_content(filename, description):
    print(f"\nВміст файлу: {description} ({filename})")
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            print(f.read())
    else:
        print("Файл не знайдено.")
    print("-" * 50)


# Функція для запису помилок у лог-файл
def log_error_to_file(filename, error_type, message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(f"[{timestamp}] ТИП: {error_type} | ПОВІДОМЛЕННЯ: {message}\n")


# Функція для виконання завдання з обробки помилок введення (ValueError)
def process_input_task(log_file):
    print("\nПеревірка введення даних")
    try:
        # Спроба зчитати та перетворити введені дані у число
        user_input = input("Введіть ціле число: ")
        number = int(user_input)
    except ValueError as e:
        # Обробка помилки некоректного типу даних
        error_msg = f"Неможливо перетворити '{user_input}' у ціле число."
        print(f"Перехоплено виняток: {error_msg}")
        log_error_to_file(log_file, "ValueError", error_msg)
    else:
        # Виконується, якщо помилок не було
        print(f"Успішно. Ви ввели число: {number}")
    finally:
        # Виконується завжди
        print("Блок перевірки введення завершив роботу.")


# Функція для виконання завдання з обробки помилок роботи з файлами (FileNotFoundError)
def process_file_task(filename, log_file):
    print("\nЧитання неіснуючого файлу")
    try:
        # Спроба відкрити файл, якого немає
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError as e:
        # Обробка помилки відсутності файлу
        error_msg = f"Файл '{filename}' не знайдено в системі."
        print(f"Перехоплено виняток: {error_msg}")
        log_error_to_file(log_file, "FileNotFoundError", error_msg)
    else:
        print("Файл успішно прочитано.")
    finally:
        print("Блок роботи з файлом завершив роботу.")


# Функція для виконання індивідуального завдання
# Обробка арифметичних помилок (ZeroDivisionError та OverflowError)
def process_individual_task(log_file):
    print("\nнАрифметичні помилки")

    # Ділення на нуль
    try:
        print("Спроба виконати ділення на нуль (10 / 0)")
        result = 10 / 0
    except ZeroDivisionError as e:
        error_msg = "Спроба ділення на нуль."
        print(f"Помилка: {error_msg}")
        log_error_to_file(log_file, "ZeroDivisionError", error_msg)

    # Переповнення при обчисленні великих чисел
    try:
        print("Спроба обчислити занадто велике число (експонента)")
        # Швидке зведення у величезний ступінь викликає помилку переповнення float
        result = 2.0 ** 1000000
    except OverflowError as e:
        error_msg = "Результат арифметичної операції занадто великий (переповнення)."
        print(f"Помилка: {error_msg}")
        log_error_to_file(log_file, "OverflowError", error_msg)
    else:
        print(f"Результат обчислення: {result}")
    finally:
        print("Обробка арифметичних помилок завершена.")


def main():
    log_file = 'errors_log.txt'

    # Очищаємо або створюємо новий лог-файл на початку роботи програми
    with open(log_file, 'w', encoding='utf-8') as f:
        f.write("ЛОГ ЗАПУСКУ ПРОГРАМИ\n")

    # Обробка помилок введення
    process_input_task(log_file)

    # Обробка помилок роботи з файлами
    process_file_task('non_existent_file.txt', log_file)

    # Обробка арифметичних помилок
    process_individual_task(log_file)

    # Виведення фінального лог-файлу для перевірки результатів
    print_file_content(log_file, "Журнал винятків (Лог-файл)")


if __name__ == "__main__":
    main()
