#coding=gbk

import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code:',r.status_code)

response_dict = r.json()
print('Total repositories:',response_dict['total_count'])

#探索有关仓库的信息
repo_dicts = response_dict['items']
print('Repositories returned:',len(repo_dicts))
#研究第一个仓库
repo_dict = repo_dicts[0]
print('\nKeys:',len(repo_dict))
for key in sorted(repo_dict.keys()):
	print(key)

#print(response_dict.keys())
print('\nSelected information about each repository:')
for repo_dict in repo_dicts:
	print('\nname:',repo_dict['name'])
	print('Owner:',repo_dict['owner']['login'])
	print('Stars:',repo_dict['stargazers_count'])
	print('Repository:',repo_dict['html_url'])
	print('Created:',repo_dict['created_at'])
	print('Updated:',repo_dict['updated_at'])
	print('Description:',repo_dict['description'])
