def tinh_tong(lst):
    tong=0
    for num in lst:
        if num % 2 == 0:
            tong += num
    return tong
input_list=input("nhap danh sach")
numbers=list(map(int, input_list.split(',')))
tong_chan=tinh_tong(numbers)
print("tong cac so trong danh sach ", tong_chan)