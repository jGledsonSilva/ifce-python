fibonacci = [[0], [1]]
a = 0
b = 0
c = 1
for i in range(21):
    a = b
    b = c
    c = a+b
    fibonacci.append([c])
print(fibonacci)
