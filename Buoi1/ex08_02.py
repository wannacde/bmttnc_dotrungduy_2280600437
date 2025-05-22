def chia(so_nhi_phan):
    so_thap_phan=int(so_nhi_phan,2)
    if so_thap_phan % 5==0:
        return True
    else:
        return False
chuoi_so=input("nhap chuoi so: ")
so_list=chuoi_so.split(',')
so_chia_het_cho_5=[so for so in so_list if chia(so)]
if len(so_chia_het_cho_5) > 0:
    ket_qua=','.join(so_chia_het_cho_5)
    print("cac so nhi phan chia het cho 5: ", ket_qua)
else:
    print("khong co so nhi phan chia het cho 5 trong chuoi")
