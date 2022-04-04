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

printStuds(list)

