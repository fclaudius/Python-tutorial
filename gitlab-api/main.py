import requests

gitlab_url = "https://gitlab.com/api/v4"
url_action = "/users/nanuchi/projects"
response = requests.get(gitlab_url + url_action)
my_projects = response.json()

for project in my_projects:
    print (f"Project Name: {project['name']},\nProject Url: {project['web_url']}\n")

