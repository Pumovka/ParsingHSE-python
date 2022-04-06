import student_class
import requests
from bs4 import BeautifulSoup as BS
import json
import pandas as pd


list_studs = []
list_a = []
list_marks = [0,0,0,0]

list_links = ["https://www.hse.ru/n/student-ratings/api?unit=122392301&course=1&from=576252978", "https://www.hse.ru/n/student-ratings/api?unit=122392301&course=2&from=576252978", "https://www.hse.ru/n/student-ratings/api?unit=122392301&course=3&from=576252978", "https://www.hse.ru/n/student-ratings/api?unit=122392301&course=4&from=576252978"]





for i in range(len(list_links)):
    responce = requests.get(list_links[i]).text
    responce_json = json.loads(responce)
    course = i+1
    for item in responce_json["data"]: #беру все из объекта data
        stud = student_class.Student(item['title'], course ,item['place'], item["gradeMid"], item['gpa'])
        list_studs.append(stud)




def search_best_course(list): #поиск "успеваемости" по среднему баллу группы
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
        
def best_course(list): #поиск лучшей группы
    mark = list_marks[0]
    for i in range(len(list_marks)):
        if mark < list_marks[i]:
           mark = list_marks[i]
           course = i+1
    return course, mark

def sort_by_title(list):#выбор номера курса для ключа сортировки
    return list.title

def funcSortTitle(list):#сортировка по имени
    try:
        list.sort(key = sort_by_title)
    except TypeError as te:
        print(te)
    student_class.printStuds(list)
pass
