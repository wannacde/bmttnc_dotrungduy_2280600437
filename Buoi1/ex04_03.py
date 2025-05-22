def truy_cap(tuple_data):
    first=tuple_data[0]
    last=tuple_data[-1]
    return first, last

input_tuple=input("nhap tuple")
first, last = truy_cap(input_tuple)
print("phan tu dau:", first)
print("phan tu cuoi:", last)
