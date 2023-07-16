from os import system
system("color f0")
rabbits = []
add = []

class RabbitPair: #토끼 한쌍
    def __init__(self, age=0):
        self.age = age
        self.child = []

    def breed(self):
        if self.age == 0:
            self.age += 1
            return
        _child = RabbitPair()
        self.child.append(_child)
        add.append(_child)

rabbits.append(RabbitPair()) #a_1 = 1
print(f"1번째\t토끼 : {len(rabbits)}쌍")
for n in range(0, 9):
    add = []
    before = len(rabbits)
    for i in rabbits:
        i.breed()
    for i in add:
        rabbits.append(i)
    print(f"{n+2}번째\t토끼 : {len(rabbits)}쌍")
    before = len(rabbits)
