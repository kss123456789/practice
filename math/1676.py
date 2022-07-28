n = int(input())

factorial = 1
count = 0

for _ in range(n):
    factorial = factorial * n
    n -= 1

factorial = str(factorial)

for i in range(1,len(factorial)+1):
    n_factorial = factorial[-i]
    if n_factorial == '0':
        count += 1
    else:
        break

print(count)