# -*- coding: utf-8 -*-
import re
from .colors import RESET_ALL, BOLD, FG


class CheckInput:
    def verification_phone(self, phone: str) -> str:
        self.phone = phone
        try:
            phone = re.sub("[^0-9]", "", phone)  
            if phone.startswith("0"):
                phone = "38" + phone
                return phone
            elif phone == "" or phone == " ":
                print(f"{BOLD + FG.red}Numer został wprowadzony błędnie!{RESET_ALL}")
                exit()
            elif phone.startswith("+"):
                return phone[1:]
            else:
                return phone
        except Exception:
            print(f"{BOLD + FG.red}Numer został wprowadzony błędnie!{RESET_ALL}")
            exit()

    def verification_cycles(self, cycles: str) -> int:
        try:
            self.cycles = cycles
            cycles = re.sub("[^0-9]", "", cycles)
            return int(cycles)
        except ValueError:
            print("\033[1;31m" + "Niewłaściwa liczba cykli!")
            exit()


if __name__ == "__main__":
    phone = input("Wpisz numer telefonu: ")
    cycles = input("Wprowadź liczbę cykli: ")
    print(CheckInput().verification_phone(phone))
    print(CheckInput().verification_cycles(cycles))
