from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []


def person_is_seller(name):
    return name[-1] == "m"


def search(name):
    search_queue = deque() # Создание новой очереди
    search_queue += graph[name] # Все соседи добавляются в очередь списка
    searched = []

    while search_queue: # Пока очередь не пуста
        person = search_queue.popleft() # Из очереди извлекается первый человек
        if person_is_seller(person): # Проверяем, является ли этот человек продавцом манго
            print(person + " is a mango seller!")
            #return True
        else:
            search_queue += graph[person] # Нет, не является. Все друзья этого человека добавляются в очередь поиска
            searched.append(person)
        #return False # Если нет в очереди ни одного продавца


search("you")