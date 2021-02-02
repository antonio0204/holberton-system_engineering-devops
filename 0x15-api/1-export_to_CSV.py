#!/usr/bin/python3

''' Extend your Python script to export data in the CSV format.
'''


def get_All(users_id):

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

    with open("{}.csv".format(users_id), mode="w", newline='') as fd:
        write_file = csv.writer(fd, quoting=csv.QUOTE_NONNUMERIC)
        for obj in comp_Task:
            row = ["{}".format(users_id), "{}".format(name_Employee),
                   "{}".format(obj.get('completed')),
                   "{}".format(obj.get('title'))]
            write_file.writerow(row)

if __name__ == '__main__':
    import csv
    import requests
    import sys
    if len(sys.argv) == 2:
        get_All(sys.argv[1])
