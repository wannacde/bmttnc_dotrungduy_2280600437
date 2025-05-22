def kiem_tra(n):
    if n<=1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i ==0:
            return False
    return True
number=int(input("nhap so can kiem tra: "))
if kiem_tra(number):
    print(number, " la so nguyen to ")
else:
    print(number, " khong phai la so nguyen to")
    