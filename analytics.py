import json
from pprint import pprint

with open('test_data/phodal/github_repos.json') as data_file:
    data = json.load(data_file)

for repo in data:
    pprint(repo['name'])