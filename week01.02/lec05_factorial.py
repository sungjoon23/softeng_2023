def fact(num):
    pass

def main():
    n = int(input("숫자를 입력하세요."))
    f = 1
    for i in range(1, n+1):
        f = f * i

    print(f"n!은 {f}이다.")

if __name__ == "__main__":
    main()