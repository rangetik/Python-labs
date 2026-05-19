# Лабораторна 9

# Тема: Використання регулярних виразів для пошуку та заміни в рядках

# Загальне завдання: Написати програму, яка вводить початкові дані, формує результат
# з використанням регулярних виразів та виводить його на екран або зберігає у файл.

# Варіант 8: Реалізувати програму для заміни всіх дат у форматі dd-mm-yyyy на yyyy-mm-dd.

import re
import os

# Функція для відображення вмісту файлу в консолі
def print_file_content(filename, description):
    print(f"\nВміст файлу: {description} ({filename})")
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            print(f.read())
    else:
        print("Файл не знайдено.")
    print("-" * 50)

# Функція для виконання загального завдання
# (Пошук усіх цифр/чисел у тексті)
def process_general_task(input_text, output_file):
    print("\nПошук чисел у тексті")

    # findall – повертає список усіх збігів за шаблоном
    # \d+ – означає одну або більше цифр
    numbers = re.findall(r'\d+', input_text)

    result_str = f"Оригінальний текст: {input_text}\nЗнайдені числа: {', '.join(numbers)}"
    print(result_str)

    # Зберігаємо результат у файл
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(result_str)
    print(f"Результат загального завдання збережено у '{output_file}'")


# Функція для виконання індивідуального завдання
# Заміна формату дати за допомогою re.sub()
def process_individual_task(input_text, output_file):
    print("\nФорматування дат")

    # Шаблон для dd-mm-yyyy: дві цифри, дефіс, дві цифри, дефіс, чотири цифри
    # Використовуємо групування (), щоб потім змінити їх місцями
    date_pattern = r'(\d{2})-(\d{2})-(\d{4})'

    # re.sub(pattern, repl, string) замінює всі входження за шаблоном
    # \3-\2-\1 – це посилання на групи (рік-місяць-день)
    processed_text = re.sub(date_pattern, r'\3-\2-\1', input_text)

    print(f"Текст до обробки: {input_text}")
    print(f"Текст після заміни дат: {processed_text}")

    # Записуємо оброблений текст у файл
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(processed_text)
    print(f"Результат індивідуального завдання збережено у '{output_file}'")


def main():
    # Початкові дані
    raw_text = "Сьогодні 25-10-2023, а наступна зустріч відбудеться 05-11-2023."

    # Виконання загального завдання (пошук чисел)
    process_general_task(raw_text, 'general_results.txt')

    # Виконання заміни формату дат
    process_individual_task(raw_text, 'formatted_dates.txt')

    # Перевірка вмісту створених файлів
    print_file_content('general_results.txt', "Результати пошуку чисел")
    print_file_content('formatted_dates.txt', "Текст із виправленими датами")

if __name__ == "__main__":
    main()
