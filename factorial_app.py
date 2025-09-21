# file: factorial_app.py
import argparse
import math
import sys

ERR_PREFIX = "[Ошибка]"

def parse_positive_int(raw: str) -> int:
    raw = raw.strip()
    if not raw.isdigit():
        raise ValueError("Ожидается положительное целое число.")
    n = int(raw)
    if n < 0:
        raise ValueError("Число не должно быть отрицательным.")
    return n

def ask_number_interactive() -> int:
    while True:
        try:
            value = input("Введите положительное целое число n: ")
            return parse_positive_int(value)
        except (EOFError, KeyboardInterrupt):
            print(f"\n{ERR_PREFIX} Ввод прерван.")
            sys.exit(1)
        except ValueError as e:
            print(f"{ERR_PREFIX} {e} Повторите ввод.")

def main():
    parser = argparse.ArgumentParser(description="Вычисление факториала положительного целого числа.")
    parser.add_argument("--n", type=str, help="Положительное целое число")
    args = parser.parse_args()

    if args.n is not None:
        try:
            n = parse_positive_int(args.n)
        except ValueError as e:
            print(f"{ERR_PREFIX} {e}")
            sys.exit(2)
    else:
        n = ask_number_interactive()

    try:
        result = math.factorial(n)
    except (OverflowError, MemoryError) as e:
        print(f"{ERR_PREFIX} Не удалось вычислить факториал: {e}")
        sys.exit(3)

    print(f"{n}! = {result}")

if __name__ == "__main__":
    main()
