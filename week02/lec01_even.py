import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()
ROOT.withdraw()

def simple_gui_input(text="값을 입력하세요."):
    return int(simpledialog.askstring(title="GUI 창",
                                prompt=text))

def main():
    # number = int(input("숫자를 입력하세요."))
    number = simple_gui_input()

    if number % 2 ==0:
        if number % 10 == 2 or number % 10 == 4 or number % 10 == 5: # 는
            print(f"{number}는 홀수입니다.")
        else:  # 은
            print(f"{number}은 짝수입니다.")
    else:
        if number % 10 in [2, 4, 5, 9]:
            print(f"{number}은 짝수입니다.")
        else:
            print(f"{number}는 홀수입니다.")

if __name__ == "__main__":
    main()