#!/usr/bin/python3
"""
    Python script that, for a given employee ID, returns
    information about his/her TODO list progress.
"""
import json
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    usr_url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    tds_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)

    user = requests.get(usr_url).json()
    todo = requests.get(tds_url).json()

<<<<<<< HEAD
    print(json.dumps(todo, indent = 4))
    print(type(user))

    """completed_nb = 0
    total_nb = 0
=======
    number_of_task_done = 0
    total_nuber_task_done = 0
>>>>>>> 8b2b5145ccad3ce8781fb3d2be8ebdaede9f6007
    completed_tasks = []

    for task in todo:
        total_nuber_task_done += 1
        if task.get("completed") is True:
            number_of_task_done += 1
            completed_tasks.append(task.get("title"))

    sentence = "Employee {} is done with tasks({}/{}):"
<<<<<<< HEAD
    print(sentence.format(user.get("name"), completed_nb, total_nb))"""
=======
    print(sentence.format(user.get("name"), number_of_task_done, total_nuber_task_done))
    for task in completed_tasks:
        print("\t {}".format(task))
>>>>>>> 8b2b5145ccad3ce8781fb3d2be8ebdaede9f6007
