import pytest
import klausur as klausur
import re

def test_aufgabe_01(capsys):
    klausur.aufgabe_01()
    actual_output = capsys.readouterr().out
    error_msg = (
        "\033[1;31m"  # fett und rot
        "FEHLER:\n"
        'Es wird folgender Text erwartet:\n'
        '    "Hello World!"\n'
        f"Aber ausgegeben wurde:\n    \"{actual_output.strip()}\"\033[0m"
    )
    assert re.match(r"h[e3]l{1,3}o[\s\-_]*w[o0]r[l1]d[\s\-_]*!", actual_output, re.IGNORECASE), error_msg

@pytest.mark.parametrize("value1, value2, expected", [
    (10, 3, 1), # 10 modulo 3 is 1
    (20, 4, 0), # 20 modulo 4 is 0
    (15, 6, 3), # 15 modulo 6 is 3
    (7, 5, 2),  # 7 modulo 5 is 2
    (9, 2, 1)   # 9 modulo 2 is 1
])
def test_aufgabe_02(value1, value2, expected):
    error_msg = (
        "\033[1;31m"  # fett und rot
        f"FEHLER:\n"
        f'Es wird erwartet, dass bei Übergabe der Werte {value1} und {value2} folgendes herauskommt: {expected}.\n'
        f"Aber es wurde {klausur.aufgabe_02(value1, value2)} zurückgegeben.\033[0m"
    )
    assert klausur.aufgabe_02(value1, value2) == expected, error_msg

@pytest.mark.parametrize("value1, value2, expected", [
    (5, 10, 45),  # Sum from 6 to 10 is 40
    (1, 1, 1),    # No numbers between 1 and 1
    (10, 5, 45),  # Sum from 6 to 10 is 45
    (0, 0, 0),    # No numbers between 0 and 0
    (3, 7, 25),   # Sum from 4 to 7 is 25
    (-3, 3, 0),  # Sum from -3 to 3 is 0
    (10, -3, 49),  # Sum from -3 to 10 is 49
    (-3, -5, -12),  # Sum from -5 to -3 is -12
])
def test_aufgabe_03(value1, value2, expected):
    error_msg = (
        "\033[1;31m"  # fett und rot
        f"FEHLER:\n"
        f'Es wird erwartet, dass bei Übergabe der Werte {value1} und {value2} folgendes herauskommt: {expected}.\n'
        f"Aber es wurde {klausur.aufgabe_03(value1, value2)} zurückgegeben.\033[0m"
    )
    assert klausur.aufgabe_03(value1, value2) == expected, error_msg

@pytest.mark.parametrize("year, expected", [
    (2020, True),  # Leap year
    (2000, True),  # Leap year (divisible by 400)
    (2100, False), # Not a leap year (divisible by 100 but not 400)
    (2021, False), # Not a leap year
    (1900, False), # Not a leap year (divisible by 100 but not 400)
    (1600, True),  # Leap year (divisible by 400)
])
def test_aufgabe_04(year, expected):
    error_msg = (
        "\033[1;31m"  # fett und rot
        f"FEHLER:\n"
        f'Es wird erwartet, dass bei Übergabe der Jahreszahl {year} folgendes herauskommt: {expected}.\n'
        f"Aber es wurde {klausur.aufgabe_04(year)} zurückgegeben.\033[0m"
    )
    assert klausur.aufgabe_04(year) == expected, error_msg