# Logika Boolean
# NOT, AND, OR, XOR

# NOT (membalik nilai boolean)
print("========== NOT ==========")
x = False
z = not x
print("nilai z = ", z)

x = True
z = not x
print("nilai z = ", z)

# AND (jika ada salah, maka hasilnya salah)
print("========== AND ==========")
x = False
y = False
nilai = x and y
print(x, "and", y, "=", nilai)

x = False
y = True
nilai = x and y
print(x, "and", y, "=", nilai)

x = True
y = False
nilai = x and y
print(x, "and", y, "=", nilai)

x = True
y = True
nilai = x and y
print(x, "and", y, "=", nilai)

# OR (jika ada benar, maka hasilnya benar)
print("========== OR ==========")
x = False
y = False
nilai = x or y
print(x, "or", y, "=", nilai)

x = False
y = True
nilai = x or y
print(x,"or",y,"=",nilai)

# XOR (akan true jika salah satu true, tapi tidak keduanya)
print("========== XOR ==========")
x = False
y = False
nilai = x ^ y
print(x, "xor", y, "=", nilai)

x = False
y = True
nilai = x ^ y
print(x, "xor", y, "=", nilai)

x = True
y = False
nilai = x ^ y
print(x, "xor", y, "=", nilai)

x = True
y = True
nilai = x ^ y
print(x, "xor", y, "=", nilai)
