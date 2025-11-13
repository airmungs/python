#public class Person {
#    String name;
#    int age;

#    Person(String name, int age) {
#        this.name = name;
#        this.age = age;
#    }

#    void greet() {
#        System.out.println("안녕하세요, " + name + "입니다.");
#    }
#}

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"두 값의 합은 {self.x+self.y} 입니다."

p = Point(10,20)
print(p)

'''
이름을 입력하세요: 희문
나이를 입력하세요: 28
안녕하세요, 28살 희문님!

짝수만 출력
x = [1, 2, 3, 4, 5, 6, 7, 8]
'''

class introduce:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return(f"안녕하세요 {self.name}님, {self.age} 살 맞으면 말 놓을게요")

name = input("이름을 입력하세요:")
age = input("나이를 입력하세요:")

greet = introduce(name,age)
print(greet)


class Numbering:
    def __init__(self, x):
        self.x = x

    def get_even_numbers(self):
        even_numbers = []
        for n in self.x:
            if n % 2 == 0:
                even_numbers.append(n)
        return even_numbers

x = [1, 2, 3, 4, 5, 6, 7, 8]
numbering = Numbering(x)

print(numbering.get_even_numbers())
print(Numbering.get_even_numbers(x))


class NumberingMethod:
    @classmethod
    def get_even_numbers(cls, numbers):
        return [n for n in numbers if n % 2 == 0]

x = [1, 2, 3, 4, 5, 6, 7, 8]
print(NumberingMethod.get_even_numbers(x))