n = int(input("Дольки: "))
m = int(input("Дольки: "))
k = int(input("Дольки: "))
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print("YES")
else:
    print("NO")