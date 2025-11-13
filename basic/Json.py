import json

user={"name":"죠죠","age":18,"job":"Stand User"}

#JSON으로 저장
with open("user.json","w",encoding="utf-8") as f:
    json.dump(user,f,ensure_ascii=False,indent=4)

with open("user.json","r",encoding="utf-8") as f:
    data=json.load(f)

print(json.dumps(data,ensure_ascii=False,indent=4))