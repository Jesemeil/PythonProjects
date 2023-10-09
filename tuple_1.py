# t1 =(1, 3, 2)
# x = t1[0] + t1[2]
# print(x)

t1 = (1, 3, 2, [1, 2, 3], 3)
x = t1[0] + t1[2]
print(list(t1))


def test2(x):
    return x % 2 == 0


x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(filter(test2, x1)))


def test3(n):
    return n ** 2


print(list(map(test3, x1)))

y = [i for i in x1 if i ** 2]