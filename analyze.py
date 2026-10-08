"""
Кейс-стаді — аналіз CSV-файлу

Ваше завдання — пройти весь шлях від порожньої папки до проєкту на GitHub:

1. Створити папку з проєктом
2. Завантажити туди дані
3. Зробити аналіз
4. Зберегти результат у .txt файл
5. Запушити все на GitHub
"""


# ============================================================
# Крок 1. Створіть папку з проєктом
# ============================================================
# У терміналі:
#
#   mkdir students_analysis
#   cd students_analysis
#
# Усі наступні файли мають лежати всередині цієї папки.


# ============================================================
# Крок 2. Завантажте туди дані
# ============================================================
# Скопіюйте файл students.csv у папку students_analysis.
# Формат файлу: name,math,python,english
# (перший рядок — заголовок, далі по одному студенту в рядку)
#
# Також збережіть цей скрипт у ту саму папку як analyze.py.


# ============================================================
# Крок 3. Зробіть аналіз
# ============================================================
# Потрібно порахувати:
#   - середній бал по класу з кожного предмета (math, python, english);
#   - ім'я студента з найвищим середнім балом (по трьох предметах).

INPUT_FILE = "students.csv"
OUTPUT_FILE = "result.txt"

# TODO 1: відкрийте INPUT_FILE через with open(...) as f:
#   і пропустіть рядок заголовка (next(f))
with open(INPUT_FILE, encoding="utf-8") as f:
    next(f)
# TODO 2: пройдіться по рядках файлу (for line in f:), для кожного рядка:
#   - приберіть символ переносу рядка (line.strip())
#   - розбийте рядок по комі (line.split(","))
#   - перетворіть оцінки на числа (int або float)
    grade1 = 0
    grade2 = 0
    grade3 = 0
    grade1_sum = 0
    grade2_sum = 0
    grade3_sum = 0
    students = []
    student_avg = {}
    for line in f:
        stripped = line.strip()
        name, *grades = stripped.split(",")

# TODO 3: по ходу циклу накопичуйте:
#   - суми оцінок з кожного предмета та кількість студентів
#   - найкращого студента (ім'я та його середній бал) — порівнюйте
#     середній бал поточного студента з найкращим на цей момент
        students.append(name)
        grade1 = int(grades[0])
        grade2 = int(grades[1])
        grade3 = int(grades[2])
        medium = (grade1 + grade2 + grade3) / 3
        student_avg[name] = medium
        grade1_sum += grade1
        grade2_sum += grade2
        grade3_sum += grade3
        max_score = max(float(score) for score in student_avg.values())
        top_student = [top for top, score in student_avg.items() if float(score) == max_score]
# TODO 4: після циклу порахуйте середній бал по класу з кожного предмета
#   (сума / кількість студентів)
    print("Середній бал по класу: ")
    math_avg = round(grade1_sum / len(students), 1)
    python_avg = round(grade2_sum / len(students), 1)
    english_avg = round(grade3_sum / len(students), 1)
    top_student_str = "".join(top_student)
    print(f"math: {math_avg}")
    print(f"python: {python_avg}")
    print(f"english: {english_avg}")
    print(f"Найкращий студент: {top_student_str} ({max_score})")
# ============================================================
# Крок 4. Збережіть результат у .txt файл
# ============================================================
# TODO 5: відкрийте OUTPUT_FILE в режимі 'w' і запишіть туди результат
#   у такому вигляді (числа округліть до одного знака після коми):
#
#   Середній бал по класу:
#   math: 67.8
#   python: 67.9
#   english: 67.9
#
#   Найкращий студент: Ім'я Прізвище (97.0)
#
# Також виведіть цей самий текст на екран через print().
#
# Запустіть скрипт (python analyze.py) і перевірте, що в папці
# з'явився файл result.txt.
with open(OUTPUT_FILE, "w", encoding="utf-8") as output:
    output.write("Середній бал по класу: \n"
                 f"math: {math_avg}\n"
                 f"python: {python_avg}\n"
                 f"english: {english_avg}\n"
                 "\n"
                 f"Найкращий студент: {top_student_str} ({max_score})")


# ============================================================
# Крок 5. Запушіть усе на GitHub
# ============================================================
# 1) Створіть новий ПОРОЖНІЙ репозиторій на github.com
#    (без README і .gitignore).
#
# 2) У терміналі, всередині папки students_analysis:
#
#   git init
#   git add .
#   git commit -m "Students analysis"
#   git branch -M main
#   git remote add origin <посилання_на_ваш_репозиторій>
#   git push -u origin main
#
# 3) Оновіть сторінку репозиторію на GitHub і переконайтеся, що там
#    є students.csv, analyze.py та result.txt.
