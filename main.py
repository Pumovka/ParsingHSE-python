import requests
from bs4 import BeautifulSoup as BS
import json
class Student():
    def __init__(self, title, course, place, average, gpa):
        self.title = title
        self.course = course
        self.place = place
        self.average = average
        self.gpa = gpa
        pass
    def printStudent(self):
        print("ФИО:", self.title, "Курс:", self.course, "Рейтинг:", self.place, "Cредний балл:", self.average, "GPA:", self.gpa)
    pass

list = []
list_a = []
list_marks = [0,0,0,0]
def printStuds(list):#создаю функцию для вывода всех студентов из списка 
    for i in range(len(list)): 
        list[i].printStudent()
pass
#Создаю список ссылок и записываю элементы в лист для создания общего списка
list_links = ["https://www.hse.ru/n/student-ratings/api?unit=122392301&course=1&from=576252978", "https://www.hse.ru/n/student-ratings/api?unit=122392301&course=2&from=576252978", "https://www.hse.ru/n/student-ratings/api?unit=122392301&course=3&from=576252978", "https://www.hse.ru/n/student-ratings/api?unit=122392301&course=4&from=576252978"]

for i in range(len(list_links)):
    responce = requests.get(list_links[i]).text
    responce_json = json.loads(responce)
    course = i+1
    for item in responce_json["data"]: #беру все из объекта data
        stud = Student(item['title'], course ,item['place'], item["gradeMid"], item['gpa'])
        list.append(stud)

# printStuds(list)


def best_course(list): #поиск лучшей группы
    mark = list_marks[0]
    for i in range(len(list_marks)):
        if mark < list_marks[i]:
           mark = list_marks[i]
           course = i+1
    return course, mark



def search_best_course(list):
    
    n = 0
    for course in range(4):
        for i in range(len(list)): 
            if(list[i].course == course + 1):
                list_a.append(list[i])
        for i in range(len(list_a)):
            list_marks[n] = list_marks[n] + list_a[i].average
        list_marks[n] = list_marks[n] / len(list_a)
        n = n + 1
        list_a.clear()

    for i in range(len(list_marks)):
        print(list_marks[i])
    pass
search_best_course(list)


def sort_by_title(list):#выбор номера курса для ключа сортировки
    return list.title

def funcSortTitle(list):#сортировка по имени
    try:
        list.sort(key = sort_by_title)
    except TypeError as te:
        print(te)
    printStuds(list)
pass


print("Курс с наивысшем баллом и балл", best_course(list)) 
funcSortTitle(list)