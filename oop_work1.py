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

    def average_grade(self):
        self.new_grades = {}
        for x in self.grades:
            self.new_grades[x] = self.grades[x][0]
        self.y_grades = []
        for one_grade in  self.new_grades.values():
            self.y_grades.append(int(one_grade))
            self.av_grade = sum(self.y_grades)/len(self.y_grades)
        # print(self.av_grade)

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Преподавателей и студентов нельзя сравнить'
        return self.av_grade < other.av_grade


    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress or course in self.finished_courses:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.av_grade}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        

   

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades  = {}

    def average_grade(self):
        self.new_grades = {}
        for x in self.grades:
            self.new_grades[x] = self.grades[x][0]
        self.y_grades = []
        for one_grade in  self.new_grades.values():
            self.y_grades.append(int(one_grade))
            self.av_grade = sum(self.y_grades)/len(self.y_grades)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.av_grade}'
        
class Reviewer(Mentor):
     def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and  course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        

     def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'



# def get_avg_lect_grade(lecturers, course):
#     sum_ = 0
#     for lecturer in lecturers:
#         sum_ += sum(lecturer.grades[course]) / len(lecturer.grades[course])

#     return sum_ / len(lecturers)


some_student_1 = Student('Bob', 'Johnson', 20)
some_student_2 = Student ('Emma', 'Brown', 19)

some_student_1.courses_in_progress += ['Python', 'Git']
some_student_2.courses_in_progress += ['Python', 'Full-stuc']

some_student_1.add_courses('Введение в программирование')
some_student_2.add_courses('Java')


some_reviewer_1 = Reviewer('Lily', 'Oldwin')
some_reviewer_2 = Reviewer('Barney', 'Stinckson')


some_reviewer_1.rate_hw(some_student_1, 'Python', 7)
some_reviewer_1.rate_hw(some_student_1, 'Git', 9)
some_reviewer_2.rate_hw(some_student_1, 'Python', 9)
some_reviewer_2.rate_hw(some_student_1, 'Git', 10)

some_reviewer_1.rate_hw(some_student_2, 'Python', 7)
some_reviewer_1.rate_hw(some_student_2, 'Full-stuck', 9)
some_reviewer_2.rate_hw(some_student_2, 'Python', 9)
some_reviewer_2.rate_hw(some_student_2, 'Full-stuck', 10)


some_lecturer_1 = Lecturer('ANDREY', 'KURPAT')
some_lecturer_2 = Lecturer('BOB', 'MARLY')

some_lecturer_1.courses_attached = ['Python', 'Git']
some_lecturer_2.courses_attached = ['Python', 'Full-stuck']


some_student_1.rate_lecturer(some_lecturer_1, 'Python', 9)
some_student_1.rate_lecturer(some_lecturer_1, 'Git', 5)
some_student_2.rate_lecturer(some_lecturer_1, 'Python', 8)
some_student_2.rate_lecturer(some_lecturer_1, 'Git', 9)

some_student_1.rate_lecturer(some_lecturer_2, 'Python', 6)
some_student_1.rate_lecturer(some_lecturer_2, 'Full-stuck', 7)
some_student_2.rate_lecturer(some_lecturer_2, 'Python', 4)
some_student_2.rate_lecturer(some_lecturer_2, 'Full-stuck', 8)

some_student_1.average_grade()
some_student_2.average_grade()

# print(some_student_1.new_grades)
# print(some_student_1.y_grades)
# some_student_1.__lt__(some_student_2)
# some_student_2.average_grade()

some_lecturer_1.average_grade()
some_lecturer_2.average_grade()

print(some_student_1)
print(some_student_2)
print('---------------------')


print(some_reviewer_1)
print(some_reviewer_2)
print('-----------------------')


print(some_lecturer_1)
print(some_lecturer_2)
print('---------------------')

# print(get_avg_lect_grade([some_lecturer_1], 'Python'))
