from pathlib import Path


def read_matrix(path):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Файл не найден: {path}")

    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    if not lines:
        raise ValueError("Файл пуст")

    first_line = lines[0].strip()
    header_parts = first_line.split()
    if len(header_parts) != 2:
        raise ValueError("Заголовок должен содержать ровно 2 числа: количество строк и столбцов")

    try:
        rows = int(header_parts[0])
        cols = int(header_parts[1])
    except ValueError:
        raise ValueError("Размеры матрицы в заголовке должны быть целыми числами")

    if rows <= 0 or cols <= 0:
        raise ValueError("Размеры матрицы должны быть больше нуля")

    content_lines = lines[1:]

    if len(content_lines) > 0 and content_lines[-1].strip() == "":
        content_lines.pop()

    if len(content_lines) != rows:
        raise ValueError(f"Ожидалось {rows} строк данных, получено {len(content_lines)}")

    matrix = []
    for line_index, raw_line in enumerate(content_lines, start=2):
        line = raw_line.strip()
        parts = line.split()
        if len(parts) != cols:
            raise ValueError(f"Строка {line_index}: ожидалось {cols} чисел, получено {len(parts)}")
        
        row = []
        for part in parts:
            try:
                row.append(int(part))
            except ValueError:
                raise ValueError(f"Строка {line_index}: элемент '{part}' не является целым числом")
        matrix.append(row)

    return matrix


def selected_sum(matrix):
    total = 0
    for row in matrix:
        for val in row:
            if val > 0:
                total += val
    return total
