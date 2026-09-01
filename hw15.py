class Student:

    def __init__(self, gender, age, first_name, last_name, group):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.group = group

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return str(self) == str(other)

    def __hash__(self):
        return hash(str(self))


class Group:

    def __init__(self, name):
        self.name = name
        self.students = set()

    def add_student(self, student):
        if len(self.students) >= 10:
            raise Exception('Too many students in the group')
        self.students.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)

        if student is not None:
            self.students.remove(student)

    def find_student(self, last_name):
        for student in self.students:
            if student.last_name == last_name:
                return student

        return None

    def __str__(self):
        result = f'Group: {self.name}\n'

        for student in self.students:
            result += str(student) + '\n'

        return result




st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

gr = Group('PD1')

gr.add_student(st1)
gr.add_student(st2)

print(gr)

assert gr.find_student('Jobs') == st1
assert gr.find_student('Jobs2') is None

gr.delete_student('Taylor')

print(gr)

print('OK')
