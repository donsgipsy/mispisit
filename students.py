import json
class Student:
    def __init__(self, id, last_name, first_name, middle_name, dob, address, phone, faculty, course, group, gpa):
        self.id = id
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.dob = dob           
        self.address = address
        self.phone = phone
        self.faculty = faculty   
        self.course = course     
        self.group = group    
        self.gpa = gpa        
    def calculate_scholarship(self):
        if self.gpa >= 4.5:
            return 5000
        elif self.gpa >= 4.0:
            return 4100
        elif self.gpa >= 3.0:
            return 2000
        else:
            return 0
    def to_dict(self):
        return self.__dict__
    @classmethod
    def from_dict(cls, data):
        return cls(**data)
class StudentDatabase:
    def __init__(self):
        self.students = []  
    def add_student(self, student):
        self.students.append(student)
    def get_by_faculty(self, faculty_name):
        print(f"Студенты факультета {faculty_name}")
        found = [s for s in self.students if s.faculty == faculty_name]
        if not found:
            print("Нет студентов")
        else:
            for s in found:
                print(f"{s.last_name} {s.first_name}, Группа: {s.group}, Стипендия: {s.calculate_scholarship()} руб.")
    def get_by_faculty_and_course(self):
        print("Студенты по факультетам и курсам")
        result = {}
        for s in self.students:
            key = f"{s.faculty} - {s.course} курс"
            if key not in result:
                result[key] = []
            result[key].append(s)
        
        for key, students_list in result.items():
            print(f"Группа: {key}")
            for s in students_list:
                print(f"{s.last_name} {s.first_name}")
    def get_born_after_year(self, year):
        print(f"Студенты, родившиеся после {year} год")
        found = [s for s in self.students if int(s.dob.split('-')[0]) > year]
        for s in found:
            print(f"{s.last_name} {s.first_name}, Дата рождения: {s.dob}")
    def get_by_group(self, group_name):
        print(f"\n--- Студенты группы '{group_name}' ---")
        found = [s for s in self.students if s.group == group_name]
        for s in found:
            print(f"{s.last_name} {s.first_name} {s.middle_name}, Средний балл: {s.gpa}")

    def export_to_json(self, filename):
        data = [s.to_dict() for s in self.students]
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Данные сохранены в файл '{filename}'")

    def import_from_json(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
            self.students = [Student.from_dict(d) for d in data]
            print(f"Данные загружены из файла '{filename}'")
        except FileNotFoundError:
            print(f"Файл '{filename}' не найден")

db = StudentDatabase()
db.add_student(Student(1, "Иванов", "Иван", "Иванович", "2005-05-15", "ул. Ленина 1", "+79001112233", "ИТ", 2, "ИТ-21", 4.8))
db.add_student(Student(2, "Петрова", "Анна", "Сергеевна", "2004-11-20", "пр. Мира 5", "+79004445566", "Экономика", 3, "ЭК-31", 3.5))
db.add_student(Student(3, "Сидоров", "Максим", "Алексеевич", "2006-01-10", "ул. Гагарина 10", "+79007778899", "ИТ", 1, "ИТ-11", 4.2))
db.add_student(Student(4, "Смирнова", "Елена", "Дмитриевна", "2003-08-05", "ул. Пушкина 3", "+79000001122", "Экономика", 3, "ЭК-31", 4.9))
db.get_by_faculty("ИТ")       
db.get_by_faculty_and_course()    
db.get_born_after_year(2004)  
db.get_by_group("ЭК-31")     
db.export_to_json("students.json")
new_db = StudentDatabase()
new_db.import_from_json("students.json")
new_db.get_by_faculty("Экономика")