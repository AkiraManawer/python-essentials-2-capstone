class Student:
    school_name = "Melsoft Academy"
    total_students = 0

    def __init__(self, name, student_id, score):
        self.name = name
        self.student_id = student_id
        self.score = score
        Student.total_students += 1

    def get_grade(self):
        if self.score >= 80:
            return "Distinction"
        elif self.score >= 50:
            return "Pass"
        else:
            return "F"

    def has_passed(self):
        return self.score >= 50

    def __str__(self):
        return f"Student Name: {self.name}, ID: {self.student_id}, Score: {self.score}, Grade: {self.get_grade()}"


class HonoursStudent(Student):
    def __init__(self, name, student_id, score, research_topic):
        super().__init__(name, student_id, score)
        self.research_topic = research_topic

    def get_grade(self):
        if self.score >= 75:
            return "Distinction (Honours)"
        else:
            return super().get_grade()
