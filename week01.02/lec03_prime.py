def is_prime(num):
    pass

def main():
    num = int(input("숫자를 입력하세요."))
    b=0
    for i in range(2,num):
        if num % i == 0:
            b=1
    if b==0:
        print("이 숫자는 소수입니다.")
    else:
        print("이 숫자는 소수가 아닙니다.")

if __name__ == "__main__":
    main()
