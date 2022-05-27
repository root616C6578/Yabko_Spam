# -*- coding: utf-8 -*-
import os

from send_requests import send_requests
from tools.check_input import CheckInput
from tools.colors import BOLD, FG, RESET_ALL
from tools.text import banner, cursor, replace


def clear_screen():
    return (
        os.system("cls") if os.sys.platform == "win32" else os.system("clear")
    )


def main():
    clear_screen()
    print(banner, replace + "Wpisz numer telefonu:" + RESET_ALL, sep="\n")
    phone = input(cursor)
    phone = CheckInput().verification_phone(phone)

    print(replace + "Wprowadź liczbę cykli:" + RESET_ALL)
    count = input(cursor)
    count = CheckInput().verification_cycles(count)
    clear_screen()
    print(banner)
    if count >= 10:
        print(
            f"{FG.green}*Wprowadziłeś więcej niż 10 cykli, "
            f"po 5. wskaźnik spamu zmniejszy się{RESET_ALL}"
        )
    send_requests(phone, count)
    clear_screen()
    print(
        BOLD + f"{FG.green}Gotowe!",
        f"Telefon: {FG.purple}{phone}",
        f"{FG.green}Liczba cykli: {FG.purple}{count}",
        sep="\n",
    )


if __name__ == "__main__":
    main()
