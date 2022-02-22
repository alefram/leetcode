from collections import deque


# implement a graph
graph = {}
graph["you"] = ["juan", "maria", "freddy"]
graph["maria"] = ["victoria", "miguel"]
graph["juan"] = ["carlos"]
graph["freddy"] = ["teresa", "juan2"]
graph["victoria"] = []
graph["miguel"] = []
graph["carlos"] = []
graph["teresa"] = []
graph["juan2"] = []

def person_is_seller(name):
    return name[-1] == "m"

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []

    while search_queue:
        person = search_queue.popleft()
        
        if not person in searched:
            if person_is_seller(person):
                print(person + "is a mango seller!")
            else:
                search_queue += graph[person]
                searched.append(person)

    return False


if __name__ == "__main__":
    print(search("you"))
