import pyperclip
x = 100
li = []


def prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


while x > 1:
    if prime(x):
        li.append(str(x))
    x -= 1

li.sort()

print(len(li))
output = ", ".join(li)
pyperclip.copy(f'[{output}]')
