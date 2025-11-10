def add(a,b):
    return a+b

print (add(123589,12893))

def greet(name="누구신지 모르겠지만"):  # 함수 안에 들어간 변수 정의 값은 default 인듯 하다
    print(f"{name} 안녕하세요")

greet()
greet("(누구지..)")