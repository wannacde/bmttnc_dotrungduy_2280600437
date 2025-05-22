def dem(lst):
    count={}
    for item in lst:
        if item in count:
            count[item]+=1
        else:
            count[item]=1
    return count
input_string= input("nhap danh sach")
word_list=input_string.split()
xuat_hien=dem(word_list)
print("so lan xuat hien cua cac phan tu", xuat_hien)
