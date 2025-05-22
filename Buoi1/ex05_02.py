gio=float(input("nhap so gio lam"))
luong=float(input("nhap muc luong theo gio"))
gio_tieu_chuan=44
gio_vuot_chuan=max(0,gio-gio_tieu_chuan)
luong_rieu=gio_tieu_chuan*luong+gio_vuot_chuan*luong*1.5
print(f"so tien thuc nhan : {luong_rieu}")