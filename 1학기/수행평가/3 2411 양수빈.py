phone = {"박서연" : "010-6573-5011", "원채연" : "010-4069-8091", "강은서" : "010-4202-7249"}
name = input("이름을 입력해 주세요 : ")
print(name + " 님의 전화번호는 " + phone.get(name) + " 입니다.")

