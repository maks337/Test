def test_nod(a, b):
    while b > 0:
        node = a % b
        a = b
        b = node
    return a




def fact(num):
    n = 1
    for i in range(num + 1):
        if i != 0:
            n = n * i
    return n


def sort_list(li):
    n = 1
    while len(li) > n:
        for i in range(0, (len(li) - n)):
            if li[i] > li[i + 1]:
                li[i], li[i + 1] = li[i + 1], li[i]
        n += 1
    return li


def fibo(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibo(num - 1) + fibo(num - 2)


li = [5, 2, 7, 4, 0, 9, 8, 6]

print(sort_list(li))
print(fact(5))
print(test_nod(18, 27))
print(fibo(9))
