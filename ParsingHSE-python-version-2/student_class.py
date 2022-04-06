

class Student():
    def __init__(self, title, course, place, average, gpa):
        self.title = title
        self.course = course
        self.place = place
        self.average = average
        self.gpa = gpa
        pass
    def __repr__(self):
        return '{title:'+self.title+', course:'+str(self.course)+ ', plase:'+str(self.place)+', average:' + str(self.average)+', gpa:'+str(self.gpa)+'}'
        pass
    def printStudent(self):
        print("ФИО:", self.title, "Курс:", self.course, "Рейтинг:", self.place, "Cредний балл:", self.average, "GPA:", self.gpa)
    pass

def printStuds(list):#создаю функцию для вывода всех студентов из списка 
    for i in range(len(list)): 
        list[i].printStudent()
pass

