from pprint import pprint
import requests
import json
import os
# import psutil
from git import Repo

path = r'C:\Users\EK\Desktop\New folder'


def pull():
    repo = Repo(path)
    pull = repo.git.pull('origin', 'main')
    print(pull)


def if_status_change_add_commit_push():
    repo = Repo(path)
    status = repo.git.status()
    print('status', status, '- -' * 30, sep='\n')
    if status.split('\n')[-1] != 'nothing to commit, working tree clean':
        add = repo.git.add('.')
        print('add', add, '- -' * 30, sep='\n')
        for v in status.split('\n'):
            if '	modified:   ' in v:
                print(v.split('	modified:   ')[-1])
                break
        else:
            v = ''
        commit = repo.git.commit('-am', f'auto update {v.strip()}')
        print('commit', commit, '- -' * 30, sep='\n')

        push = repo.git.push('origin', 'main')
        print('push', push, '- -' * 30, sep='\n')


def fetch_repositories(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch repositories: {response.status_code} - {response.reason}")


if __name__ == "__main__":
    repositories = fetch_repositories("hexs")
    for repo in repositories:
        print(f"Name: {repo['name']}, URL: {repo['html_url']}")

    inspection_data = [repo['name'] for repo in repositories if "auto_inspection_data" in repo['name'].lower()]
    pprint(inspection_data)

    for repo in inspection_data:

        repo_url = f"https://github.com/hexs/{repo}.git"
        clone_directory = fr'C:\Users\EK\Desktop\New folder\{repo}'
        os.makedirs(clone_directory, exist_ok=True)
        Repo.clone_from(repo_url, clone_directory)

        print(f"Repository cloned to {clone_directory}")


