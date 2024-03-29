class DeletableClass:
    def __del__(self):
        print("delete")

d = DeletableClass()
del d

class Person:
    def __init__(self, name, age, height):
        self.name = name;
        self.age = age;
        self.height = height
    
    def __str__(self):
        return "Person 설명, 이름은 " + self.name + " 키는 " + str(self.height)

    def __len__(self):
        return self.height
    
    def __getitem__(self, key):
        if key == "name":
            return self.name
        if key == "age":
            return self.age
        return None
    
p = Person("양수빈", 18, 158)
print(p)
printf("Person 설명, 이름은 " + p.name + " 키는 " + str(p.height))
print(len(p))
print(len(Person("지코", 29, 182)))