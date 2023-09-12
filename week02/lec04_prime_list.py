import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()
ROOT.withdraw()

def simple_gui_input(text="값을 입력하세요."):
    return int(simpledialog.askstring(title="GUI 창",
                                prompt=text))

def is_prime(num):
    if num <= 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def main():

    number = simple_gui_input("숫자를 알고 싶나?")

    list_prime = [x for x in range(1, number+1) if is_prime(x)]

    print(f"1~{number}까지 소수의 개수는 {list_prime}입니다.")
    print(f"1-{number}까지 중 소수의 갯수는 {len(list_prime)}입니다.")


if __name__ == "__main__":
    main()