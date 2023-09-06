def is_even(a):
    return a % 2 == 0

def main():
    a = int(input("숫자를 입력하세요."))
    evens = [x for x in range(1, 101) if is_even(x)]
    sum_even = sum(evens)

    print(f"1-100까지 숫자 중 짝수의 합은 {sum_even}입니다.")

if __name__ == "__main__":
    main()