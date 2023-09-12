import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()
ROOT.withdraw()

def simple_gui_input(text="값을 입력하세요."):
    return int(simpledialog.askstring(title="GUI 창",
                                prompt=text))
def fact(num):
    if num == 1:
        return 1
    # result = 1
    # for i in range(1, num+1)
    #   result = result * i
    #    return result
    return num * fact(num-1)


def main():

    number = simple_gui_input("팩토리얼을 구하고 싶나?")

    print(f"{number}!은 {fact(number)}입니다.")

if __name__ == "__main__":
    main()