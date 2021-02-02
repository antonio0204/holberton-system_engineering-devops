#!/usr/bin/python3
"""Extend your Python script to export data in the Json format."""


def export_to_all_json():
    """what you did in the task #0"""
    url_todo = 'https://jsonplaceholder.typicode.com/todos'
    url_users = 'https://jsonplaceholder.typicode.com/users'

    # does request in url
    to_do = requests.get(url_todo)
    users_todo = requests.get(url_users)
    a_dict = {}

    for user in users_todo.json():
        username = user.get('username')
        a_list = []
        for todo_dict in to_do.json():
            if todo_dict.get('userId') == user.get('id'):
                task_dict = {}
                task_dict['task'] = todo_dict.get('title')
                task_dict.update({'username': username})
                task_dict['completed'] = todo_dict.get('completed')
                a_list.append(task_dict)
        a_dict['{}'.format(user.get('id'))] = a_list

    with open("{}.json".format('todo_all_employees'), 'w', newline='') as fd:
        json.dump(a_dict, fd)


if __name__ == '__main__':
    import json
    import requests
    export_to_all_json()
