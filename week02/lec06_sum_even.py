import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()
ROOT.withdraw()

def simple_gui_input(text="값을 입력하세요."):
    return int(simpledialog.askstring(title="GUI 창",
                                prompt=text))

def is_even(a):
    return a % 2 == 0

def main():

    number = simple_gui_input("짝수의 합을 알고 싶나?")
    # a = int(input("숫자를 입력하세요."))
    evens = [x for x in range(1, 101) if is_even(x)]
    sum_even = sum(evens)

    print(f"1부터 {number}까지의 짝수의 합은{sum_even}입니다.")

if __name__ == "__main__":
    main()