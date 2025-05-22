class Student:
    _id_counter = 1

    def __init__(self, name, gender, major, gpa):
        self.id = Student._id_counter
        Student._id_counter += 1
        self.name = name
        self.gender = gender
        self.major = major
        self.gpa = gpa

    def get_academic_performance(self):
        if self.gpa >= 8:
            return "Giỏi"
        elif self.gpa >= 6.5:
            return "Khá"
        elif self.gpa >= 5:
            return "Trung bình"
        else:
            return "Yếu"
