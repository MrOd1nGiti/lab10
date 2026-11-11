from pathlib import Path
from tempfile import TemporaryDirectory
from files_lab import read_matrix, selected_sum


def test_valid_reading():
    with TemporaryDirectory() as temp_dir:
        path = Path(temp_dir) / "matrix.txt"
        path.write_text("1 2\n7 -1\n", encoding="utf-8")
        assert read_matrix(path) == [[7, -1]]

        path_1x1 = Path(temp_dir) / "matrix_1x1.txt"
        path_1x1.write_text("1 1\n0\n", encoding="utf-8")
        assert read_matrix(path_1x1) == [[0]]


def test_invalid_reading():
    with TemporaryDirectory() as temp_dir:
        empty_path = Path(temp_dir) / "empty.txt"
        empty_path.write_text("", encoding="utf-8")
        try:
            read_matrix(empty_path)
            assert False, "Ошибка не обнаружена (пустой файл)"
        except ValueError:
            pass

        bad_header_path = Path(temp_dir) / "bad_header.txt"
        bad_header_path.write_text("0 3\n1 2 3\n", encoding="utf-8")
        try:
            read_matrix(bad_header_path)
            assert False, "Ошибка не обнаружена (неверный заголовок)"
        except ValueError:
            pass

        short_row_path = Path(temp_dir) / "short_row.txt"
        short_row_path.write_text("1 2\n1\n", encoding="utf-8")
        try:
            read_matrix(short_row_path)
            assert False, "Ошибка не обнаружена (короткая строка)"
        except ValueError as e:
            assert "Строка 2" in str(e)

        non_number_path = Path(temp_dir) / "non_number.txt"
        non_number_path.write_text("1 2\n1 x\n", encoding="utf-8")
        try:
            read_matrix(non_number_path)
            assert False, "Ошибка не обнаружена (нечисловой элемент)"
        except ValueError as e:
            assert "Строка 2" in str(e)

        extra_rows_path = Path(temp_dir) / "extra_rows.txt"
        extra_rows_path.write_text("1 1\n1\n2\n", encoding="utf-8")
        try:
            read_matrix(extra_rows_path)
            assert False, "Ошибка не обнаружена (лишние строки)"
        except ValueError:
            pass

        missing_path = Path(temp_dir) / "non_existent.txt"
        try:
            read_matrix(missing_path)
            assert False, "Ошибка не обнаружена (файл отсутствует)"
        except FileNotFoundError:
            pass


def test_variant():
    matrix = [[1, -2, 3], [4, 0, -6]]
    assert selected_sum(matrix) == 8
    assert selected_sum([[-1, -2], [-3, 0]]) == 0


if __name__ == "__main__":
    test_valid_reading()
    test_invalid_reading()
    test_variant()
    print("Все тесты для работы 10 успешно пройдены")
