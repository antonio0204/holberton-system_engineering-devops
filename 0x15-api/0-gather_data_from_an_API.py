#!/usr/bin/python3

''' Development api with https://jsonplaceholder.typicode.com
'''


def get_All(users_id):

    ''' Get all Employees
    '''

    all_Url = 'http://jsonplaceholder.typicode.com/todos'
    all_User = 'http://jsonplaceholder.typicode.com/users/{}'.format(users_id)

    all_Data = requests.get(all_Url)
    all_Employ = requests.get(all_User)

    name_Employee = all_Employ.json().get('name')
    all_Task, comp_Task = 0, []

    for task in all_Data.json():
        if task.get('userId') == int(users_id):
            all_Task += 1
            if task.get('completed') is True:
                comp_Task.append(task)

    print('Employee {} is done with tasks({}/{}):'
          .format(name_Employee, len(comp_Task), all_Task))

    for task in comp_Task:
        print('\t {}'.format(task.get('title')))


if __name__ == '__main__':
    import requests
    import sys
    if len(sys.argv) == 2:
        get_All(sys.argv[1])
