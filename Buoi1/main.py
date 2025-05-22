from QuanLySinhVien import StudentManager

def menu():
    manager = StudentManager()
    while True:
        print("\n1. Thêm sinh viên\n2. Cập nhật sinh viên\n3. Xóa sinh viên\n4. Tìm kiếm sinh viên"
              "\n5. Sắp xếp theo điểm trung bình\n6. Sắp xếp theo chuyên ngành\n7. Hiển thị danh sách\n8. Thoát")
        choice = input("Chọn chức năng: ")
        if choice == "1":
            name = input("Nhập tên: ")
            gender = input("Nhập giới tính: ")
            major = input("Nhập chuyên ngành: ")
            gpa = float(input("Nhập điểm trung bình: "))
            manager.add_student(name, gender, major, gpa)
            print("Thêm sinh viên thành công.")
        elif choice == "2":
            student_id = int(input("Nhập ID sinh viên cần cập nhật: "))
            name = input("Nhập tên mới (nhấn Enter để bỏ qua): ")
            gender = input("Nhập giới tính mới (nhấn Enter để bỏ qua): ")
            major = input("Nhập chuyên ngành mới (nhấn Enter để bỏ qua): ")
            gpa = input("Nhập điểm trung bình mới (nhấn Enter để bỏ qua): ")
            gpa = float(gpa) if gpa else None
            print(manager.update_student(student_id, name, gender, major, gpa))
        elif choice == "3":
            student_id = int(input("Nhập ID sinh viên cần xóa: "))
            print(manager.delete_student(student_id))
        elif choice == "4":
            name = input("Nhập tên sinh viên cần tìm: ")
            result = manager.search_by_name(name)
            for student in result:
                print(f"ID: {student.id}, Tên: {student.name}, Chuyên ngành: {student.major}, GPA: {student.gpa}")
        elif choice == "5":
            students = manager.sort_by_gpa()
            for student in students:
                print(f"ID: {student.id}, Tên: {student.name}, GPA: {student.gpa}")
        elif choice == "6":
            students = manager.sort_by_major()
            for student in students:
                print(f"ID: {student.id}, Tên: {student.name}, Chuyên ngành: {student.major}")
        elif choice == "7":
            manager.display_students()
        elif choice == "8":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ.")

menu()
