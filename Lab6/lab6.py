# Лабораторна 6

# Тема: Робота з JSON, CSV та Excel файлами у Python

# Загальне завдання: Навчитися працювати з різними форматами файлів (JSON, CSV, Excel),
# здійснювати читання, запис та маніпуляцію даними.

# Варіант 8: Написати програму для створення JSON-файлу з інформацією про курси,
# які викладаються на факультеті.

import json
import csv
import pandas as pd
import os

# Функція для відображення вмісту файлу в консолі (для перевірки)
def print_file_content(filename, description):
    print(f"\nВміст файлу: {description} ({filename})")
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            print(f.read())
    else:
        print("Файл не знайдено.")
    print("-" * 50)

# Функція для виконання завдання з JSON (читання, зміна, запис)
def process_json_task(input_file, output_file):
    # Створюємо початковий список словників та записуємо у файл
    initial_data = [
        {"id": 1, "name": "Іван", "age": 20, "faculty": "ФІОТ"},
        {"id": 2, "name": "Марія", "age": 19, "faculty": "ФПМ"}
    ]
    with open(input_file, 'w', encoding='utf-8') as f:
        json.dump(initial_data, f, ensure_ascii=False, indent=4)

    # Зчитуємо дані з JSON-файлу
    with open(input_file, 'r', encoding='utf-8') as f:
        students = json.load(f)

    # Додаємо новий запис та змінюємо існуючий
    students.append({"id": 3, "name": "Олег", "age": 21, "faculty": "ІПСА"})
    students[0]["age"] = 21

    # Записуємо змінені дані у новий JSON-файл
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(students, f, ensure_ascii=False, indent=4)
    print(f"Завдання JSON: Результат збережено у '{output_file}'")

# Функція для виконання завдання з CSV (DictReader та DictWriter)
def process_csv_task(input_file, output_file):
    # Створюємо початковий CSV-файл
    fieldnames = ["id", "name", "age", "faculty"]
    rows = [
        {"id": "1", "name": "Іван", "age": "20", "faculty": "ФІОТ"},
        {"id": "2", "name": "Марія", "age": "19", "faculty": "ФПМ"}
    ]
    with open(input_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    # Зчитуємо дані з CSV-файлу у список
    updated_rows = []
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            updated_rows.append(row)

    # Додаємо новий рядок
    updated_rows.append({"id": "3", "name": "Олег", "age": "21", "faculty": "ІПСА"})

    # Зберігаємо результат у новий CSV-файл
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(updated_rows)
    print(f"Завдання CSV: Результат збережено у '{output_file}'")

# Функція для виконання завдання з Excel (використання pandas)
def process_excel_task(input_file, output_file):
    # Створюємо DataFrame та записуємо в Excel
    data = {
        "name": ["Іван", "Марія", "Олег", "Анна"],
        "age": [20, 19, 22, 18],
        "faculty": ["ФІОТ", "ФПМ", "ФІОТ", "ТЕФ"]
    }
    df = pd.DataFrame(data)
    df.to_excel(input_file, index=False)

    # Зчитуємо дані з Excel-файлу у DataFrame
    df_read = pd.read_excel(input_file)

    # Виконуємо фільтрацію та сортування
    df_filtered = df_read[df_read['age'] > 18]
    df_sorted = df_filtered.sort_values(by='age')

    # Записуємо оброблені дані у новий Excel-файл
    df_sorted.to_excel(output_file, index=False)
    print(f"Завдання Excel: Результат збережено у '{output_file}'")

# Функція для виконання індивідуального завдання (Варіант 8)
def process_individual_task(output_file):
    # Створюємо структуру даних з інформацією про курси
    courses = [
        {"title": "Основи Python", "teacher": "Барбарук В.М.", "hours": 120},
        {"title": "Системне програмування", "teacher": "Павлов В.В..", "hours": 90},
        {"title": "Архітектура ПЗ", "teacher": "Грибенко Є.М.", "hours": 105}
    ]

    # Записуємо дані у JSON-файл
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(courses, f, ensure_ascii=False, indent=4)
    print(f"Індивідуальне завдання: Файл '{output_file}' створено")

def main():
    # Робота з JSON (Загальне завдання)
    process_json_task('students.json', 'students_updated.json')
    print_file_content('students_updated.json', "Оновлені дані студентів (JSON)")

    # Робота з CSV (Загальне завдання)
    process_csv_task('students.csv', 'students_updated.csv')
    print_file_content('students_updated.csv', "Оновлені дані студентів (CSV)")

    # Робота з Excel (Загальне завдання)
    process_excel_task('students.xlsx', 'students_processed.xlsx')
    # Для Excel виводимо повідомлення, оскільки read() не відобразить таблицю коректно
    print("\nФайл Excel 'students_processed.xlsx' успішно створено та оброблено.")
    print("-" * 50)

    # Індивідуальне завдання (Варіант 8)
    process_individual_task('faculty_courses.json')
    print_file_content('faculty_courses.json', "Курси факультету (Індивідуальне завдання)")

# Перевірка прямого запуску файлу
if __name__ == "__main__":
    main()
