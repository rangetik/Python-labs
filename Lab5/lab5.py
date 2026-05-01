# Лабораторна 5
# Тема: Робота з текстовими файлами: читання та запис
# Загальне завдання: Написати програму, яка зчитує дані з текстового файлу та записує їх у новий файл,
# виконуючи певні перетворення (наприклад, переведення всіх літер у нижній регістр).
# Варіант 8: Записати список чисел у файл та відсортувати їх.

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

# Функція для виконання загального завдання (зчитування та зміна регістру).
def process_general_task(input_file, output_file):
    if not os.path.exists(input_file):
        print(f"Помилка: Файл '{input_file}' не знайдено.")
        return

    # Зчитуємо рядки з файлу
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    # Переводимо всі літери у нижній регістр
    processed_lines = [line.lower() for line in lines]

    # Записуємо результат у новий файл
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.writelines(processed_lines)

    print(f"Загальне завдання: Результат збережено у '{output_file}'")

# Функція для виконання індивідуального завдання (сортування чисел).
def process_individual_task(input_file, output_file):
    # Створюємо список чисел та записуємо його у файл за умовою завдання
    raw_numbers = [45, 12, 89, 3, 22, 78, 1, 99, 34]
    with open(input_file, 'w', encoding='utf-8') as f:
        f.write(' '.join(map(str, raw_numbers)))

    if not os.path.exists(input_file):
        print(f"Помилка: Файл '{input_file}' не знайдено.")
        return

    # Зчитуємо дані з файлу
    with open(input_file, 'r', encoding='utf-8') as infile:
        data = infile.read()
        # Розбиваємо рядок на окремі елементи та перетворюємо їх у числа
        numbers_list = [int(x) for x in data.split()]

    # Сортуємо список чисел
    numbers_list.sort()

    # Записуємо відсортовані числа у новий файл
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(' '.join(map(str, numbers_list)))

    print(f"Індивідуальне завдання: Числа відсортовано та збережено у '{output_file}'")

def main():
    # Підготовка даних для загального завдання
    input_gen = 'input_gen.txt'
    output_gen = 'output_gen.txt'

    with open(input_gen, 'w', encoding='utf-8') as f:
        f.write("ПЕРШИЙ Рядок ДЛЯ Тестування.\n")
        f.write("ДРУГИЙ рядок З ВЕЛИКИМИ і малими ЛІТЕРАМИ.\n")

    # Виклик функції загального завдання
    process_general_task(input_gen, output_gen)

    # Виклик функції індивідуального завдання
    input_ind = 'numbers_input.txt'
    output_ind = 'numbers_output.txt'
    process_individual_task(input_ind, output_ind)

    # Виведення результатів на екран для перевірки та звіту
    print_file_content(output_gen, "Загальне завдання (Нижній регістр)")
    print_file_content(output_ind, "Індивідуальне завдання (Відсортовані числа)")

# Перевірка прямого запуску файлу
if __name__ == "__main__":
    main()
