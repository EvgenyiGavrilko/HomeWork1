class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade = []

    def get_average_grade(self):
        list = []
        for course, grade in self.grades.items():
            list += grade
        self.average_grade = sum(list) / len(list)

    def lecturer_lavel(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.lavel:
                lecturer.lavel[course] += [grade]
            else:
                lecturer.lavel[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Студент:\nИмя: {self.name}\nФамилия: {self.surname}\n" \
               f"Средняя оценка за домашние задания: {self.average_grade}\n" \
               f"Курсы в процессе изучения: {self.courses_in_progress}\n" \
               f"Завершенные курсы: {self.finished_courses}"

    def __eq__(self, other):
        if self.average_grade == other.average_grade:
            return 'Средняя оценка выбранных СТУДЕНТОВ одинаковая'
        else:
            return 'Средняя оценка выбранных СТУДЕНТОВ разная'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.average_grade = []

class Lecturer(Mentor):
    lavel = {}

    def get_average_grade(self):
        for course, grade in self.lavel.items():
            average_grade = sum(grade) / len(grade)
            self.average_grade += [average_grade]

    def __str__(self):
        return f"Лектор:\nИмя: {self.name}\nФамилия: {self.surname}\n" \
               f"Средняя оценка за лекции: {self.average_grade}"

    def __eq__(self, other):
        if self.average_grade == other.average_grade:
            return 'Средняя оценка выбранных ЛЕКТОРОВ одинаковая'
        else:
            return 'Средняя оценка выбранных ЛЕКТОРОВ разная'

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Проверяющий:\nИмя: {self.name}\nФамилия: {self.surname}"


#ВВОД ДАННЫХ

student_1 = Student('Ruoy', 'Eman', 'man')
student_1.courses_in_progress += ['Python', 'SQL']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Evgenyi', 'Gavrilko', 'man')
student_2.courses_in_progress += ['Python', 'SQL']
student_2.finished_courses += ['Введение в программирование']


reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python', 'SQL']

lecturer_1 = Lecturer('Some_1', 'Buddy')
lecturer_1.courses_attached += ['Python', 'SQL']

lecturer_2 = Lecturer('Some_2', 'Buddy')
lecturer_2.courses_attached += ['Python', 'SQL']

#ОБРАЩЕНИЕ К ФУНКЦИЯМ

reviewer_1.rate_hw(student_1, 'Python', 7)                                   #Проверяющий поставил оценку по курсу за дз
reviewer_1.rate_hw(student_1, 'Python', 6)                                   #Проверяющий поставил оценку по курсу за дз
reviewer_1.rate_hw(student_1, 'SQL', 5)                                      #Проверяющий поставил оценку по курсу за дз
student_1.get_average_grade()                                     #Вызов ф-ции Средняя оценка за дз по курсу - студент 1

reviewer_1.rate_hw(student_2, 'Python', 8)                                   #Проверяющий поставил оценку по курсу за дз
reviewer_1.rate_hw(student_2, 'Python', 9)                                   #Проверяющий поставил оценку по курсу за дз
reviewer_1.rate_hw(student_2, 'SQL', 7)                                      #Проверяющий поставил оценку по курсу за дз
reviewer_1.rate_hw(student_2, 'SQL', 8)                                      #Проверяющий поставил оценку по курсу за дз
student_2.get_average_grade()                                     #Вызов ф-ции Средняя оценка за дз по курсу - студент 2

student_1.lecturer_lavel(lecturer_1, 'Python', 7)                                        #Студент курса оценил лектора 1
student_2.lecturer_lavel(lecturer_1, 'Python', 8)                                        #Студент курса оценил лектора 1
lecturer_1.get_average_grade()                                 #Вызов ф-ции Средняя оценка за лекции по курсу - лектор 1

student_1.lecturer_lavel(lecturer_2, 'Python', 7)                                        #Студент курса оценил лектора 2
student_2.lecturer_lavel(lecturer_2, 'Python', 10)                                       #Студент курса оценил лектора 2
lecturer_2.get_average_grade()                                 #Вызов ф-ции Средняя оценка за лекции по курсу - лектор 2



print("_________________________________________________________")
print(reviewer_1)
print("_________________________________________________________")
print(lecturer_1)
print()
print(lecturer_2)
print("_________________________________________________________")
print(student_1)
print()
print(student_2)
print("_________________________________________________________")
print(Student.__eq__(student_1,student_2))                                      #Вызов функции сравнение объектов класса
print(Lecturer.__eq__(lecturer_1,lecturer_2))                                   #Вызов функции сравнение объектов класса


# Не могу организовать добавление объектов класса в список с проверкой на соответствие объекта классу.
# Прищлось добавить объекты в список в ручном режиме.

#class Repository:
    #all_student: list = []

    #def add(self, instance):
        #if isinstance(instance, Student):
            #self.all_student += [instance]

#Repository.add(Repository,Student)
#print(Repository.all_student)

print(f'\nПроверка на наличие объектов в списках')
all_student = []
all_student.append(student_1)
all_student.append(student_2)
print(all_student)

all_lecturer = []
all_lecturer.append(lecturer_1)
all_lecturer.append(lecturer_2)
print(all_lecturer)

print(f'\nСтуденты:')
for i in all_student:
    print(f'Курсы {i.courses_in_progress}, Оценки {i.grades}, Средняя за ДЗ {i.average_grade}') #ПРОВЕРОЧНЫЙ КОД

def calc_student(data_list, course):
    average = []
    for i in data_list:
        for k, v in i.grades.items():
            if k == course:
                average += v
            else:
                return 'Ошибка'
    resalt = sum(average) / len(average)
    return f'Средняя оценка по всем студентам курса {course} - {resalt}'

print("_________________________________________________________")
print(calc_student(all_student, 'Pythn'))

print(f'\nЛекторы:')
for i in all_lecturer:
    print(f'Курсы {i.courses_attached}, Оценки {i.lavel}') #ПРОВЕРОЧНЫЙ КОД

def calc_lecturer(data_list, course):
    average = []
    for i in data_list:
        for k, v in i.lavel.items():
            if k == course:
                average += v
            else:
                return 'Ошибка'
    resalt = sum(average) / len(average)
    return f'Средняя оценка по всем лекторам курса {course} - {resalt}'

print("_________________________________________________________")
print(calc_lecturer(all_lecturer, 'Python'))







