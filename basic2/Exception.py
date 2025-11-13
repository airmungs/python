try:
    x=int(input("x:"))
    y=10/x
except ValueError:
    print("정수만 입력해라")
except ZeroDivisionError:
    print("0으로 니가 나눠봐")
else:
    print("값",y)
finally:
    print("굳굳")


def parse_age(s: str)->int:
    try:
        age = int(s)
        if age<0:
            raise ValueError("음수나이불가")
        return age
    except ValueError as e:
        # 원인 보존하며 의미있는 예외로 감싸기
        raise ValueError(f"나이 파싱 실패:{s!r}") from e

print(parse_age("-10"))