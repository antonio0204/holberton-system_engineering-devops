#!/usr/bin/python3

''' Extend your Python script to export data in the Json format.
'''


def export_Json_All():

    ''' Get all Json
    '''

    all_Url = 'http://jsonplaceholder.typicode.com/todos'
    all_User = 'http://jsonplaceholder.typicode.com/users'

    all_Data = requests.get(all_Url)
    all_Employ = requests.get(all_User)
    a_dict = {}

    for user in all_Employ.json():
        username = user.get('username')
        a_list = []
        for all_Dict in all_Data.json():
            if all_Dict.get('userId') == user.get('id'):
                task_dict = {}
                task_dict['task'] = all_Dict.get('title')
                task_dict.update({'username': username})
                task_dict['completed'] = all_Dict.get('completed')
                a_list.append(task_dict)
        a_dict['{}'.format(user.get('id'))] = a_list

    with open("{}.json".format('todo_all_employees'), 'w', newline='') as fd:
        json.dump(a_dict, fd)

if __name__ == '__main__':
    import json
    import requests
    export_Json_All()
