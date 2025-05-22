from SinhVien import Student

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, name, gender, major, gpa):
        student = Student(name, gender, major, gpa)
        self.students.append(student)

    def update_student(self, student_id, name=None, gender=None, major=None, gpa=None):
        for student in self.students:
            if student.id == student_id:
                if name: student.name = name
                if gender: student.gender = gender
                if major: student.major = major
                if gpa is not None: student.gpa = gpa
                return f"Cập nhật sinh viên ID {student_id} thành công."
        return "Sinh viên không tồn tại."

    def delete_student(self, student_id):
        self.students = [student for student in self.students if student.id != student_id]
        return f"Đã xóa sinh viên ID {student_id}."

    def search_by_name(self, name):
        return [student for student in self.students if name.lower() in student.name.lower()]

    def sort_by_gpa(self):
        return sorted(self.students, key=lambda student: student.gpa, reverse=True)

    def sort_by_major(self):
        return sorted(self.students, key=lambda student: student.major)

    def display_students(self):
        for student in self.students:
            print(f"ID: {student.id}, Tên: {student.name}, Giới tính: {student.gender}, "
                  f"Chuyên ngành: {student.major}, GPA: {student.gpa}, "
                  f"Học lực: {student.get_academic_performance()}")
