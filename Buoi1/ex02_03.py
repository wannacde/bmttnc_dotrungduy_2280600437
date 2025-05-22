def dao_nguoc(lst):
    return lst[::-1]

input_list=input("nhap danh sach")
numbers=list(map(int, input_list.split(',')))
list_dao_nguoc=dao_nguoc(numbers)
print("danh sach sau dao nguoc", list_dao_nguoc)
