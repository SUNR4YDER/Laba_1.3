import random
a = random.randint (0,10)
b = random.randint (0,10)
c = a + b
print(a ," + ", b, " = ")
ans = int(input())
if (ans == c):
    print("Правильно!")
else:
    print("Неправильно!")