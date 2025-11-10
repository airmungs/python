print("Test")
test="테스트중"
print(test,"입니다")
testList=["개발서버","운영서버","스테이징서버"]
print(testList[0])
print(testList[1])
print(testList[2])
print(testList[0],test,"입니다")

testList.append({123,"에러수정중"})
print (testList)

for i in range(10):
    print(i)


count = 0
while count < 10:
    print("반복중",count)
    count+=1