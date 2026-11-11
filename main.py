from pathlib import Path
from files_lab import read_matrix, selected_sum
from table import column_sums, row_sums


def read_positive_integer(prompt):
    while True:
        raw_val = input(prompt).strip()
        try:
            val = int(raw_val)
        except ValueError:
            print("Ошибка: введено не целое число")
            continue

        if val <= 0:
            print("Ошибка: число должно быть больше нуля")
            continue

        return val


def main():
    folder = Path(__file__).resolve().parent
    matrix_path = folder / "matrix.txt"
    report_path = folder / "report.txt"

    try:
        matrix = read_matrix(matrix_path)
    except FileNotFoundError as e:
        print(f"Ошибка файлового доступа: {e}")
        return
    except UnicodeError:
        print("Ошибка: неверная кодировка файла. Ожидается UTF-8")
        return
    except ValueError as e:
        print(f"Ошибка формата данных: {e}")
        return
    except OSError as e:
        print(f"Ошибка доступа к файлу: {e}")
        return

    r_sums = row_sums(matrix)
    c_sums = column_sums(matrix)
    val_sum = selected_sum(matrix)

    r_sums_str = " ".join(str(x) for x in r_sums)
    c_sums_str = " ".join(str(x) for x in c_sums)

    try:
        with open(report_path, "w", encoding="utf-8") as file:
            file.write(f"Суммы строк: {r_sums_str}\n")
            file.write(f"Суммы столбцов: {c_sums_str}\n")
            file.write(f"Результат варианта: {val_sum}\n")
        print("Отчёт успешно записан в report.txt")
    except OSError as e:
        print(f"Ошибка при записи отчёта: {e}")


if __name__ == "__main__":
    main()
