def is_prime(num):
    pass

def main():
    b = 0
    for i in range(1, 101):
        if num % i == 0:
            b = 1
    if b == 0:
        return True

    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

    for num in range(1, 101):
        print("1~100까지 소수의 개수는 {num}입니다.")


if __name__ == "__main__":
    main()