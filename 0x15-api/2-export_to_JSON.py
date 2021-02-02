#!/usr/bin/python3

''' Extend your Python script to export data in the CSV format.
'''


def export_Json(users_id):

    ''' Get all Employees
    '''

    all_Url = 'http://jsonplaceholder.typicode.com/todos'
    all_User = 'http://jsonplaceholder.typicode.com/users/{}'.format(users_id)

    all_Data = requests.get(all_Url)
    all_Employ = requests.get(all_User)

    name_Employee = all_Employ.json().get('username')
    all_Task, comp_Task = 0, []

    for task in all_Data.json():
        if task.get('userId') == int(users_id):
            comp_Task.append(task)

    with open("{}.json".format(users_id), mode="w") as fd:
        write_file = {users_id: []}
        for obj in comp_Task:
            new_obj = {
                'task': obj.get('title'),
                'completed': obj.get('completed'),
                'username': name_Employee
            }
            write_file[users_id].append(new_obj)
        json.dump(write_file, fd)

if __name__ == '__main__':
    import json
    import requests
    import sys
    if len(sys.argv) == 2:
        export_Json(sys.argv[1])
