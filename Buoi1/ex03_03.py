def tao_tuple(lst):
    return tuple(lst)
input_list=input("nhap danh sach")
numbers=list(map(int, input_list.split(',')))
my_tuple=tao_tuple(numbers)
print("list:", numbers)
print("tuple:", my_tuple)
