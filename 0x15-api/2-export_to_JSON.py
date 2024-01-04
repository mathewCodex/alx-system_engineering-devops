#!/usr/bin/python3
"""Accessing a REST API for todo lists
"""

import json
import requests
import sys


if __name__ == "__main__":
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId

    res = requests.get(url)
    username = res.json().get('username')

    todoUrl = url + "/todos"
    res = requests.get(todoUrl)
    tasks = res.json()

    dictionary = {employeeId: []}
    for t in tasks:
        dictionary[employeeId].append({
            "task": t.get("title"),
            "completed": t.get("completed"),
            "username": username
            })
    with open('{}.json'.format(employeeId), 'w') as filename:
        json.dump(dictionary, filename)
