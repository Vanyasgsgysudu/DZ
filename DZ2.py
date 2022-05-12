import random
from time import sleep

class cat:
    def __init__(self, n):
        self.name = Murzik
        self.gladness = 0
        self.progress = 0
        self.hungry = 1
        self.greeting()
    def greeting(self):
        print(f"I am {self.name}")
    def rest(self):
        #gladnes растет, progress уменьшается (1-3)
        self.gladness += random.randint(1, 3)
        self.progress -= random.randint(1, 3)
        self.hungry -= random.randint(1, 10)
        print(f"{self.name} | Rest | Gladness: {self.gladness} | Progress: {self.progress}")
    def hungry (self):
        self.gladness -= random.randint(1, 3)
        self.progress += random.randint(1, 3)
        print(f"{self.name} | hungry | Gladness: {self.gladness} | Progress: {self.progress}")
    def eat(self):
        self.hungry += 2


cat = []
cat.append(Student("Maxim"))
cat.append(Student("Vasya"))
cat.append(Student("Masha"))

gwinner = None
pwinner = None
day = 1
while True:
    print("Day: ", day)
    for student in students:
        actions = [cat.rest, cat.study, student.eat]
        action = random.choice(actions)
        action()
        if cat.gladness >= 100 and not gwinner:
            gwinner = cat
        if cat.progress >= 100 and not pwinner:
            pwinner = cat
        if student.eat <= -5:
            cats.remove(cat)
    day += 1
    if gwinner and pwinner:
        break

print(gwinner.name + " первый достиг максимальный уровень счастья")
print(pwinner.name + " первый достиг максимальный уровень прогресс")
print(gwinner.name + " первый достиг максимальный уровень сытости")
