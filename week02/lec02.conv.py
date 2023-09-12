import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()
ROOT.withdraw()

def simple_gui_input(text="값을 입력하세요."):
    return int(simpledialog.askstring(title="GUI 창",
                                prompt=text))

def c2f(temp_c):
    temp_f = temp_c * 9/5 + 32
    return temp_f

def main():

    temp_c = int(simple_gui_input("섭씨 온도를 입력해주세요."))

    print(f"섭씨 {temp_c}도는 화씨로 {temp_c * 9/5 + 32}℃ 입니다")

if __name__=="__main__":
    main()

