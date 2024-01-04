#!/usr/bin/python3
"""python script to fetch Rest API for todo lists of employees"""

import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"

    res = requests.get(url)
    Users = res.json()

    users_dict = {}
    for user in Users:
        USER_ID = user.get('id')
        USERNAME = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(USER_ID)
        url = url + '/todos/'
        res = requests.get(url)

        tasks = res.json()
        users_dict[USER_ID] = []
        for t in tasks:
            TASK_COMPLETED_STATUS = t.get('completed')
            TASK_TITLE = t.get('title')
            users_dict[USER_ID].append({
                "task": TASK_TITLE,
                "completed": TASK_COMPLETED_STATUS,
                "username": USERNAME
                })
            """A little Something"""
        with open("todo_all_employees.json", "w") as f:
            json.dump(users_dict, f)
