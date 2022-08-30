from random import *
import json

films=[]


def save():
    with open("films.json","w",encoding="utf-8") as fh:
        fh.write(json.dumps(films,ensure_ascii=False))
    print("Наша фильмотека была успешно сохранена в файле films.json")

def load():
    global films
    with open("films.json","r",encoding="utf-8") as fh:
        films=json.load(fh)
    print("Фильмотека была успешно загружена")   

try:
    load()
except:
    films.append("Матрица")
    films.append("Солярис")
    films.append("Властелин колец")
    films.append("Техасская резня бензопилой")
    films.append("Санта Барбара") 


while True:
    command=input("Введите команду ")
    if command=="/start":
        print("Бот-фильмотека начал свою работу")
    elif command=="/stop":
        save()
        print("Бот остановил свою работу. Заходите еще, будем рады!")
        break
    elif command=="/all":
        print("Вот текущий список фильмов")
        print(films)
    elif command =="/add":
        f=input("Введите название фильма ")
        films.append(f)
        print("Фильм был успешно добавлен в коллекцию!")
    elif command=="/help":
        print("здесь какой-то манул")
    elif command=="/delete":
        f=input("Введите название фильма, который надо удалить ")
        '''
        if f in films:
            films.remove(f)
            print("Фильм был успешно удален!")
        else:
            print("Такого фильма нет в фильмотеке!")
        '''
        try:
            films.remove(f)
            print("Фильм был успешно удален!")
        except:
            print("Такого фильма нет в фильмотеке!")
    elif command=="/random":
       # rnd=randint(0,len(films)-1)
       # print("Слепой жребий показал вам фильм -" + films[rnd])
       print("Слепой жребий показал вам фильм -" + choice(films) )
    elif command =="/save":
        save()
    elif command=="/load":
        load()
    else:
        print("Неопознанная команда. Просьба погладить манула через /help")