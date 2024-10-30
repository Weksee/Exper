file = open("24.txt").readline()
maxi = 0
for i in range (len(file)-1):
    D = 0
    count = 0
    for j in range(i, len(f)):
        count += 1
        if f[j] == 'D':
            D += 1
        if D > 7:
            maxi = max(maxi, count - 1)
            break
print(maxi)
