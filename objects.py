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
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def student_avg_hwgrade(self):
        if not self.grades:
            return 0
        all_grades = []
        for grade in self.grades.values():
            all_grades.extend(grade)
        return round(sum(all_grades)/len(all_grades), 2)

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка за домашние задания: {self.student_avg_hwgrade()}\n" \
               f"Курсы в процессе изучения: {self.courses_in_progress}\n" \
               f"Завершенные курсы: {self.finished_courses}\n" \
 
    def __it__(self, other):
        if not isinstance(other, Student):
            raise Exception ('Ошибка')
        return self.student_avg_hwgrade() < other.student_avg_hwgrade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            raise Exception ('Ошибка')
        return self.student_avg_hwgrade() == other.student_avg_hwgrade()

    def __le__(self, other):
        if not isinstance(other, Student):
            raise Exception ('Ошибка')
        return self.student_avg_hwgrade() > other.student_avg_hwgrade()

                
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades= {}

    def lecturer_avg_grade(self):
        if not self.grades:
            return 0
        all_grades_lect = []
        for grade in self.grades.values():
            all_grades_lect.extend(grade)
        return round(sum(all_grades_lect)/len(all_grades_lect), 2)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.lecturer_avg_grade()}"

    def __it__(self, other):
        if not isinstance(other, Lecturer):
            raise Exception ('Ошибка')
        return self.lecturer_avg_grade() < other.lecturer_avg_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            raise Exception ('Ошибка')
        return self.student_avg_hwgrade() == other.student_avg_hwgrade()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            raise Exception ('Ошибка')
        return self.lecturer_avg_grade() > other.lecturer_avg_grade()

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

def total_avg(persons, list):
    if not isinstance(persons, list):
        return 'нет списка'
    all_grades = []
    for person in persons:
        all_grades.extend(person.grades.get(course,[]))
    if not all_grades:
        return 'нет оценок по курсу'
    return round(sum(all_grades)/len(all_grades),2)

std1 = Student('X','Jay','man')
std1.courses_in_progress += ['Graphs']
std1.courses_in_progress += ['Logic']


std2 = Student('Y','Mcjay','man')
std2.courses_in_progress += ['ICT']
std2.courses_in_progress += ['Logic']

lct1 = Lecturer('A','Bcd')
lct1.courses_attached += ['Logic']
std1.rate_lecturer(lct1,'Logic',5)
std2.rate_lecturer(lct1,'Logic',7)

lct2 = Lecturer('K','Lmn')
lct2.courses_attached += ['ICT']
std2.rate_lecturer(lct1,'Logic',5)

rvw1 = Reviewer('Y','Zxw')
rvw1.rate_hw(std1,'Logic',3)
rvw1.rate_hw(std1,'Logic',10)

print(std1,std2)
print(lct1,lct2)
    
