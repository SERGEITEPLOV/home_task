class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if  isinstance(lecturer, Lecturer) and (course in self.courses_in_progress) and (course in lecturer.courses_attached):
            lecturer.lecturer_grades[course] = [grade]

    def student_avg_hwgrade(self):
        sum_grades = 0
        for subject, grade in self.grades.items():
            sum_grades += grade
        return round(sum_grades/len(self.grades), 2)

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка за домашние задания: {self.student_avg_hwgrade}\n" \
               f"Курсы в процессе изучения: {self.courses_in_progress}\n" \
               f"Завершенные курсы: {self.finished_courses}\n" \
 
    def __compare__(self,other):
        if isinstance(other, Student):
            if self.student_avg_hwgrade() > other.student_avg_hwgrade():
                return self.student_avg_hwgrade() > other.student_avg_hwgrade()
            elif self.student_avg_hwgrade() == other.student_avg_hwgrade():
                return self.student_avg_hwgrade() == other.student_avg_hwgrade()
            elif self.student_avg_hwgrade() < other.student_avg_hwgrade():
                return self.student_avg_hwgrade() < other.student_avg_hwgrade()
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    
class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.lecturer_grades= {}

    def lecturer_avg_grade(self):
        sum_grades = 0
        for subject, grade in self.lecturer_grades.items():
            sum_grades += grade
        return round(sum_grades/len(self.lecturer_grades),2)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.lecturer_avg_grade}"

    def __compare__(self,other):
        if isinstance(other, Lecturer):
            if self.lecturer_avg_grade() > other.lecturer_avg_grade():
                return self.lecturer_avg_grade() > other.lecturer_avg_grade()
            elif self.lecturer_avg_grade() == other.lecturer_avg_grade():
                return self.student_avg_hwgrade() == other.student_avg_hwgrade()
            elif self.lecturer_avg_grade() < other.lecturer_avg_grade():
                return self.lecturer_avg_grade() < other.lecturer_avg_grade()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"
        

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка' 



