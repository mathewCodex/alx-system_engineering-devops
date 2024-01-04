#!/usr/bin/python3
"""
fexteches employee datas from an api
"""
import re
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            req = requests.get('{}/users/{}'.format(REST_API, id)).json()
            task_req = requests.get('{}/todos'.format(REST_API)).json()
            emp_name = req.get('name')
            tasks = list(filter(lambda x: x.get('userId') == id, task_req))
            comp_task = list(filter(lambda x: x.get('completed'), tasks))
            print(
                    'Employess {} is done with tasks({}/{}):'.format(
                        emp_name,
                        len(comp_task),
                        len(tasks)
                        )
                    )
            if len(comp_task) > 0:
                for task in comp_task:
                    print('\t {}'.format(task.get('title')))
