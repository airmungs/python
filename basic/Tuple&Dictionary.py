#Tuple
point=(3,5)
x,y=point
print(x,y)


#Dictionary
user = {"name":"홍길동","age":"40","address":"서울시"}
print(user["name"])
print(user["age"])
print(user["address"])

user["Job"]="개발자"
print(user)

for key,value in user.items():
    print(key,value)