import requests

def get_id():
    github_id = input("Please enter your GitHub User ID: ")
    return github_id

def get_repo(id):
    response = requests.get('https://api.github.com/users/' + id + '/repos')
    json_obj = response.json()
    repo_names =[]
    for i in range(0,len(json_obj)):
        repo_names.append(json_obj[i]['name'])
    return repo_names

def get_commit(id, repo_name):
    response = requests.get('https://api.github.com/repos/' + id + '/' + repo_name + '/commits')
    json_obj = response.json()
    return len(json_obj)

def display_repo():
    github_id = get_id()
    repo_lst = get_repo(github_id)
    commit_lst = []
    github_lst = []
    for i in range(0, len(repo_lst)):
        commit_lst.append(get_commit(github_id, repo_lst[i]))
    for i in range(0,len(repo_lst)):
        github_lst.append('Repo: ' + repo_lst[i] + ' Number of Commits: ' + str(commit_lst[i]))
    return github_lst