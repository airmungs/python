f = open("test.txt","w", encoding="utf-8") # w: 쓰기모드
f.write("파일 입출력\n")
f.write("파이썬 학습")
f.close()

f = open("test.txt","r",encoding="utf-8")
data = f.read()
print(data)
f.close()

with open("test.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())

lists=['java','python','js']

with open("lists.txt", "w", encoding="utf-8") as f:
    for list in lists:
        f.write(list+"\n")
        f.flush()
        f.close()

