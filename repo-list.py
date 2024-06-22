import requests

USERNAME = 'am009'

r = requests.get(f"https://api.github.com/users/{USERNAME}/repos?per_page=100&sort=updated")
data = r.json()

for repo in data:
    repo_name = repo['name']
    repo_link = repo['html_url']
    date = repo['updated_at'] #type: str
    date = date[:date.index('T')]
    repo_description = repo['description']
    print(f"| {date} | [{repo_name}]({repo_link}) | {repo_description} |")
