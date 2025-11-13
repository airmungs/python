'''
class Animal {
    void sound() {
        System.out.println("동물 소리");
    }
}

class Dog extends Animal {
    void sound() {
        System.out.println("멍멍");
    }
}
'''
#inheritance
class Animal:
    def sound(self):
        print("동물소리")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("월월")
dog = Dog()
dog.sound()

class Cat(Animal):
    def sound(self):
        super().sound()
        print("먕")


# class var / instance var
class Counter:
    count=0

    def __init__(self):
        Counter.count+=1
        self.id=Counter.count #인스턴스 변수

a = Counter()
b = Counter()
print(a.id,b.id)
print(Counter.count)

#Encapsulation
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.__secret="***"
p=Person("Java", 20)
print(p.name,p.age)
print(p._Person__secret)

#Magic Method
# __init__ 생성자 -> obj-> Class()
# __str__ print(obj) -> return 문자열
# __len__ len(obj) -> return length
# __add__ '+'
# __eq__ '=='

#연산자 오버로딩
class Point:
    def __init__(self,x,y):
        self.x,self.y=x,y
    def __add__(self,other):
        return Point(self.x + other.x, self.y + other.y)
    def __str__(self):
        return f"({self.x},{self.y})"
p1 = Point(3,5)
p2 = Point(3,6)
print(p1+p2)

#클래스 메서드 / 정적 메서드
class MathUtil:
    @staticmethod
    def add(a,b):
        return a+b

    @classmethod
    def info(cls):
        return f"이 클래스 이름은{cls.__name__}이다"

print(MathUtil.add(3,5))
print(MathUtil.info())